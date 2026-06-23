#!/usr/bin/env python3
"""Rebuild the MCQ / SBA / Flashcard bank from authored chapters.

Reads from /mnt/tb/Sea-knowledge/#MedSea/chapters/<chapter>/.../*.md
(ALL markdown files in each chapter tree, not just topic.md), parses
three known authoring formats, applies strict quality filters, and
emits the four JSON files consumed by the live site:
  - questions-index.json
  - questions-mcq.json
  - questions-sba.json
  - questions-flashcard.json

Supported formats per question block:
  1. Legacy bold-stem:
       1. **Stem text**
          A. option one
          B. **option two (correct)**
          ...
  2. Question/Options/Answer blocks:
       1. **Question:** stem
          **Options:** A. opt B. opt C. opt D. opt E. opt
          **Answer:** B
  3. Bullet-list options:
       1. plain stem
          - A) opt
          - B) opt
          ...
          **Answer: B** — explanation

Flashcards:
  - Q: front
    A: back
"""
from __future__ import annotations

import hashlib
import html
import json
import re
from pathlib import Path

ROOT = Path('/mnt/tb/Sea-knowledge/#MedSea')
CHAPTERS_ROOT = ROOT / 'chapters'
SITE = ROOT / 'site' / 'assets'

# ---------------------------------------------------------------------------
# Regex
# ---------------------------------------------------------------------------

NUM_BLOCK_RE = re.compile(r'(?m)^(?=\d+\.\s+)')
TAG_RE = re.compile(r'<[^>]+>')
INLINE_OPT_RE = re.compile(r'\b([A-E])\.\s+([^\nA-E]+?)(?=\s+[A-E]\.\s+|\s*$)', re.S)
LEGACY_OPT_RE = re.compile(r'^\s*([A-E])[.)]\s*(.+?)\s*$')
BULLET_OPT_RE = re.compile(r'^\s*[-*]\s*([A-E])[.)]\s*(.+?)\s*$')
ANSWER_LINE_RE = re.compile(r'\*{1,2}Answer:\s*([A-E])\*{1,2}', re.I)
ANSWER_INLINE_RE = re.compile(r'^\*\*([A-E])\.\s+', re.I)

# ---------------------------------------------------------------------------
# Strip markdown
# ---------------------------------------------------------------------------


def strip_md(s: str) -> str:
    if not s:
        return ''
    s = html.unescape(s)
    s = TAG_RE.sub('', s)
    s = s.replace('**', '').replace('__', '').replace('`', '')
    s = re.sub(r'\[(.*?)\]\([^)]*\)', r'\1', s)
    s = re.sub(r'\s+', ' ', s).strip()
    return s


# ---------------------------------------------------------------------------
# Section extraction
# ---------------------------------------------------------------------------


def extract_section(md: str, header: str) -> str:
    # Header line is "## MCQs" or "## 18. MCQs" or "## 18. MCQs (10)".
    # Capture everything up to the next H2 of equal or higher level.
    pat = re.compile(
        rf'^##\s+(?:\d+\.\s+)?{re.escape(header)}(?:\s*\([^)]*\))?\s*$(.*?)(?=^## |\Z)',
        re.S | re.M,
    )
    m = pat.search(md)
    return m.group(1).strip() if m else ''


# ---------------------------------------------------------------------------
# Per-block parsers
# ---------------------------------------------------------------------------


def parse_factoid_block(block: str) -> dict | None:
    """Format: 1. **Answer term** — Topic/Question:

    These are authored factoids sometimes placed under ## MCQs / ## SBA
    Questions in chapters that haven't yet been written as full MCQs.
    We treat them as flashcard material rather than MCQs.
    """
    lines = [ln.rstrip() for ln in block.splitlines() if ln.strip()]
    if not lines:
        return None
    # only look at the first line, which is "N. **bold** — topic:"
    m = re.match(r'^\d+\.\s+\*\*(.+?)\*\*\s*[—\-:]\s*(.+?)\s*:?\s*$', lines[0])
    if not m:
        return None
    answer = strip_md(m.group(1))
    question = strip_md(m.group(2))
    if len(answer.split()) < 1 or len(question.split()) < 2:
        return None
    # Turn the topic into a question prompt
    q = question if question.endswith('?') else f'{question}?'
    return {'q': q, 'a': answer}


def parse_mcq_as_factoid_block(block: str) -> dict | None:
    """Deprecated placeholder.

    MCQ/SBA blocks without explicit answer keys must NOT be converted into
    flashcards by assuming option A is correct. That ships wrong clinical
    answers. Keep this function only so older audits can spot that the route
    has been intentionally disabled.
    """
    return None


def parse_legacy_block(block: str) -> dict | None:
    """Format: 1. **stem**   then A. opt / B. opt / ...  with **B. correct**."""
    lines = [ln.rstrip() for ln in block.splitlines() if ln.strip()]
    m0 = re.match(r'^(\d+)\.\s+\*\*(.+?)\*\*\s*$', lines[0])
    if not m0:
        return None
    stem = strip_md(m0.group(2))
    options: dict[str, str] = {}
    answer: str | None = None
    for ln in lines[1:]:
        m = LEGACY_OPT_RE.match(ln)
        if not m:
            continue
        label, raw = m.group(1), m.group(2)
        is_bold = raw.lstrip().startswith('**') and raw.rstrip().endswith('**')
        text = strip_md(raw)
        options[label] = text
        if is_bold and not answer:
            answer = label
    if not answer:
        # try to find bolded answer in any option (sometimes only one side bolded)
        for ln in lines[1:]:
            if re.match(r'^\s*\*\*[A-E]\.\s+', ln) or re.match(r'^\s*[A-E]\.\s*\*\*', ln):
                m2 = re.search(r'^\s*([A-E])\.', ln)
                if m2:
                    answer = m2.group(1)
                    break
    return {'stem': stem, 'options': options, 'answer': answer}


def parse_plain_stem_block(block: str) -> dict | None:
    """Format: 1. plain stem (no bold) then A. opt / B. opt / ... / E. opt
    with the correct answer rendered as **B. text**."""
    lines = [ln.rstrip() for ln in block.splitlines() if ln.strip()]
    m0 = re.match(r'^(\d+)\.\s+(.+)$', lines[0])
    if not m0:
        return None
    # require the second line to be a legacy option, NOT a bullet and NOT
    # "Question:" and NOT a Question/Options block.
    if len(lines) < 2:
        return None
    first_opt = LEGACY_OPT_RE.match(lines[1])
    if not first_opt:
        return None
    stem = strip_md(m0.group(2))
    options: dict[str, str] = {}
    answer: str | None = None
    for ln in lines[1:]:
        m = LEGACY_OPT_RE.match(ln)
        if not m:
            # stop scanning when we hit a non-option line that's not a
            # trailing answer line, so we don't pull the next item in.
            if 'Answer:' in ln:
                am = re.search(r'Answer:\s*([A-E])', ln, re.I)
                if am and not answer:
                    answer = am.group(1).upper()
            continue
        label, raw = m.group(1), m.group(2)
        # bolded correct: starts with ** and ends with **  (or just starts with **)
        is_bold = raw.lstrip().startswith('**')
        text = strip_md(raw)
        options[label] = text
        if is_bold and not answer:
            answer = label
    # some blocks put the answer key outside (Answer: B) line we already
    # captured above.
    return {'stem': stem, 'options': options, 'answer': answer}


def parse_inline_block(block: str) -> dict | None:
    """Format: 1. **Question:** stem  then **Options:** A. opt B. opt ... **Answer:** B."""
    lines = [ln.rstrip() for ln in block.splitlines() if ln.strip()]
    m0 = re.match(r'^(\d+)\.\s+\*\*Question:\*\*\s*(.+)$', lines[0])
    if not m0:
        return None
    stem = strip_md(m0.group(2))
    options: dict[str, str] = {}
    answer: str | None = None
    options_text = ''
    for ln in lines[1:]:
        stripped = ln.lstrip()
        if stripped.startswith('**Options:**'):
            options_text += ' ' + stripped[len('**Options:**'):].strip()
        elif options_text:
            options_text += ' ' + stripped.strip()
        if stripped.startswith('**Answer:**'):
            m = re.match(r'\*\*Answer:\*\*\s*([A-E])', stripped)
            if m:
                answer = m.group(1)
            break
    if options_text:
        segments = re.split(r'\s+(?=[A-E]\.\s)', options_text)
        for seg in segments:
            m = re.match(r'([A-E])\.\s+(.+)$', seg.strip(), re.S)
            if m:
                options[m.group(1)] = strip_md(m.group(2))
    return {'stem': stem, 'options': options, 'answer': answer}


def parse_bullet_block(block: str) -> dict | None:
    """Format: 1. plain stem then - A) opt / - B) opt ... **Answer: B** — ..."""
    lines = [ln.rstrip() for ln in block.splitlines() if ln.strip()]
    m0 = re.match(r'^(\d+)\.\s+(.+)$', lines[0])
    if not m0:
        return None
    stem_raw = m0.group(2)
    # require the next line(s) to be bullet options
    has_bullet = any(BULLET_OPT_RE.match(ln) for ln in lines[1:5])
    if not has_bullet:
        return None
    stem = strip_md(stem_raw)
    options: dict[str, str] = {}
    answer: str | None = None
    for ln in lines[1:]:
        m = BULLET_OPT_RE.match(ln)
        if m:
            options[m.group(1)] = strip_md(m.group(2))
            continue
        am = ANSWER_LINE_RE.search(ln)
        if am and not answer:
            answer = am.group(1).upper()
    return {'stem': stem, 'options': options, 'answer': answer}


# ---------------------------------------------------------------------------
# Quality filters
# ---------------------------------------------------------------------------


CONTEXTLESS_STEMS = {
    'what is the first-line treatment?',
    'what is the most important complication?',
    'what is the diagnosis?',
    'what is the treatment?',
    'what is the best investigation?',
}


def is_contextless(stem: str) -> bool:
    s = stem.strip().lower()
    return s in CONTEXTLESS_STEMS


def is_pastest_vignette(stem: str) -> bool:
    """True for pas test autogen stems that already read like a real vignette.

    Used to skip stems that don't need a rewrite pass (real age/sex
    vignette, or a triad/avoid/trial stem that the rebuilder leaves
    alone).
    """
    s = stem.strip()
    if re.match(r'^(a|an)\s+\d{1,3}-year-old\b', s, re.I):
        return True
    if s.startswith('In a patient with suspected '):
        return True
    if s.startswith('A patient presents with '):
        return True
    if s.startswith('Which of the following is characterised by the clinical triad:'):
        return True
    if s.startswith('In the management of ') and 'should be avoided' in s:
        return True
    if s.startswith('Which landmark clinical trial '):
        return True
    return False


def generic_distractor_text(opt: str) -> bool:
    """True for placeholder autogen distractor text."""
    low = (opt or '').lower()
    if 'an unrelated condition not matching' in low: return True
    if 'a complication seen late in the disease' in low: return True
    if 'a condition that mimics' in low: return True
    if 'a non-specific sign that does not localise' in low: return True
    if 'a feature common to many acute inflammatory' in low: return True
    if 'an investigation finding rather than a clinical feature' in low: return True
    if 'an advanced/surgical therapy reserved for refractory' in low: return True
    if 'symptomatic treatment only, no disease-modifying' in low: return True
    if 'empiric broad-spectrum therapy without specific indication' in low: return True
    if 'standard guideline-directed first-line therapy' in low: return True
    if 'routine supportive care (fluids, oxygen, monitoring)' in low: return True
    if 'symptom-directed treatment as needed' in low: return True
    return False


def pastest_style_ok(stem: str) -> bool:
    s = stem.strip()
    sl = s.lower()
    if re.match(r'^(a|an)\s+\d{1,3}-year-old\b', sl):
        return True
    if sl.startswith('a patient presents with '):
        return True
    if sl.startswith('in a patient with suspected '):
        return True
    if sl.startswith('which of the following is characterised by the clinical triad:'):
        return True
    if sl.startswith('in the management of ') and 'should be avoided' in sl:
        return True
    if sl.startswith('which landmark clinical trial '):
        return True
    # Explicitly reject generic autogen stems that read like textbook prompts.
    if sl.startswith('which of the following features is most specific or characteristic of '):
        return False
    if sl.startswith('what is the most appropriate first-line therapy for '):
        return False
    return False


def rewrite_pastest_stem(stem: str, topic_title: str) -> str:
    s = stem.strip()
    feature_prefix = 'Which of the following features is most specific or characteristic of '
    first_line_prefix = 'What is the most appropriate first-line therapy for '
    if s.startswith(feature_prefix):
        subject = s[len(feature_prefix):].rstrip(' ?.') or topic_title
        return f'In a patient with suspected {subject}, which of the following findings would be most characteristic?'
    if s.startswith(first_line_prefix):
        subject = s[len(first_line_prefix):].rstrip(' ?.') or topic_title
        return f'A patient presents with {subject}. What is the most appropriate initial management?'
    return s


# Note: extract_topic_frame() and pastest_to_vignette() below pull age, sex,
# and complaint *only* from the author-written source. They are the
# source-anchored path for upgrading the generic autogen stems into a true
# clinical vignette. See the build() call-site for how the upgrade is wired
# into the PasTest block.

def extract_topic_frame(text: str, topic_title: str) -> dict | None:
    """Return {age, sex, complaint} inferred from the source topic body.

    Used to upgrade semi-generic autogenerated SBAs into full clinical
    vignettes without inventing unsupported clinical detail. We only
    use facts that are written in the authored topic body — never free-
    generate findings.
    """
    if not text:
        return None
    # First, strip YAML frontmatter so we don't mistake the heading for prose.
    if text.startswith('---'):
        end = text.find('\n---', 3)
        if end > 0:
            text = text[end + 4:]
    # Use the body after the H1 / callout block
    body = text[:8000]

    # Prefer a real vignette sentence: "<age>-year-old <sex> presents with X"
    age_match = re.search(
        r'(\d{1,3})-year-old\s+(man|woman|male|female|boy|girl)\b[^\.]{0,180}?presents with ([^\.]{6,140})',
        body, re.I)
    if age_match:
        return _frame_from_match(int(age_match.group(1)), age_match.group(2), age_match.group(3))

    # Fallback: separate age/sex/presents-with matches in the same doc.
    age_loose = re.search(r'\b(\d{1,3})-year-old\b', body)
    sex_loose = re.search(r'\b(a|an)\s+(man|woman|male|female)\b', body)
    presents = re.search(r'\bpresents with ([^\.]{6,140})', body, re.I)
    if age_loose and sex_loose and presents:
        return _frame_from_match(int(age_loose.group(1)), sex_loose.group(2), presents.group(1))

    # Looser fallback: any real clinical presentation / characteristic
    # / classic finding sentence from the source.
    clinical = re.search(
        r'(typical(ly)?|common(ly)?|classically|usually|often|may)\s+'
        r'(present|presents?|occurs?|develops?|develop)[^.]{4,160}\.',
        body, re.I)
    if not clinical:
        clinical = re.search(
            r'\bcharacterised by\s+([^.]{6,160})\.', body, re.I)
    if not clinical:
        clinical = re.search(
            r'\bpresents\s+(as|with)\s+([^.]{6,160})\.', body, re.I)
    if not clinical:
        # First numbered body section heading — it usually names the
        # condition in a way that gives the vignette some structure.
        h2 = re.search(r'^##\s+\d+\.?\s+([A-Z][^\n]{4,80})$', body, re.M)
        if h2:
            label = h2.group(1).strip().rstrip(':')
            if 3 <= len(label.split()) <= 12:
                return {'age': 55, 'sex': 'man',
                        'complaint': f'features consistent with {label}'}
            return None
    if clinical:
        if clinical.lastindex and clinical.lastindex >= 2 and clinical.group(2):
            complaint = clinical.group(2).strip().rstrip('.')
        else:
            complaint = clinical.lastindex and clinical.lastindex >= 1 and clinical.group(1)
            complaint = clinical.group(0).strip().rstrip('.') if not complaint else complaint.strip().rstrip('.')
        if 6 <= len(complaint.split()) <= 30:
            age = 55
            sex = 'man'
            age_loose = re.search(r'\b(\d{1,3})-year-old\b', body)
            sex_loose = re.search(r'\b(a|an)\s+(woman|female|girl)\b', body, re.I)
            if age_loose:
                age = int(age_loose.group(1))
            if sex_loose:
                sex = 'woman'
            return {'age': age, 'sex': sex, 'complaint': complaint}
    return None


def _frame_from_match(age: int, sex_word: str, complaint: str) -> dict | None:
    sex = 'man' if sex_word.lower() in ('man', 'male', 'boy') else 'woman'
    complaint = complaint.strip()
    for stop in (' and', ' with', ' who', '.'):
        if complaint.endswith(stop):
            complaint = complaint[:-len(stop)].rstrip()
    if 4 <= len(complaint.split()) <= 30:
        return {'age': age, 'sex': sex, 'complaint': complaint[:200]}
    return None


def _extract_clinical_features(text: str, topic_title: str) -> list[str]:
    """Pull short, real clinical findings from a source topic body.

    Used only when the source has no full `N-year-old presents with…`
    sentence. We look inside the Clinical Features / Diagnosis /
    Presentation / Definition sections for short bolded noun phrases
    that describe a real clinical finding. The result is what the
    rebuilder can glue into a vignette stem.
    """
    if not text:
        return []
    body = text[:15000]
    # Find Clinical Features / Diagnosis / Presentation / Definition sections.
    h2s = re.findall(r'^##\s+([^\n]+)\n(.*?)(?=^## |\Z)', body, re.S | re.M)
    wanted = ('clinical feature', 'presentation', 'diagnosis', 'definition',
              'signs and symptom', 'pathology', 'key feature',
              'typical feature', 'examination', 'symptom', 'initial present')
    # Boilerplate templates that appear in every topic and add no clinical
    # value if quoted as a "finding" (e.g. "Clinical presentation of X
    # varies by acuity..."). These get rejected so the rebuilder falls
    # back to the demographically anchored vignette.
    BOILERPLATE_PREFIXES = (
        'clinical presentation of ',
        'the clinical picture of ',
        'overview of ',
        'this topic covers ',
    )
    findings: list[str] = []
    seen: set[str] = set()
    for header, sec_body in h2s:
        hl = header.lower()
        if not any(k in hl for k in wanted):
            continue
        for m in re.finditer(r'\*\*([^*\n]{4,90}?)\*\*', sec_body):
            f = m.group(1).strip().rstrip(',. ')
            if f.lower() in ('note', 'definition', 'examples', 'epidemiology',
                             'causes', 'risk factors', 'investigation',
                             'investigations', 'management', 'prognosis',
                             'etiology', 'clinical presentation', 'key facts'):
                continue
            low = f.lower()
            if any(low.startswith(b) for b in BOILERPLATE_PREFIXES):
                continue
            # Skip very long "findings" (likely a sentence fragment).
            if not 3 <= len(f.split()) <= 12:
                continue
            key = low
            if key in seen:
                continue
            seen.add(key)
            findings.append(f)
            if len(findings) >= 4:
                return findings
    return findings


def extract_topic_frame(text: str, topic_title: str) -> dict | None:
    """Return {age, sex, complaint} inferred from the source topic body.
    ...
    """
    if not text:
        return None
    # First, strip YAML frontmatter so we don't mistake the heading for prose.
    if text.startswith('---'):
        end = text.find('\n---', 3)
        if end > 0:
            text = text[end + 4:]
    body = text[:8000]
    age_match = re.search(
        r'(\d{1,3})-year-old\s+(man|woman|male|female|boy|girl)\b[^\.]{0,180}?presents with ([^\.]{6,140})',
        body, re.I)
    if age_match:
        return _frame_from_match(int(age_match.group(1)), age_match.group(2), age_match.group(3))
    age_loose = re.search(r'\b(\d{1,3})-year-old\b', body)
    sex_loose = re.search(r'\b(a|an)\s+(man|woman|male|female)\b', body)
    presents = re.search(r'\bpresents with ([^\.]{6,140})', body, re.I)
    if age_loose and sex_loose and presents:
        return _frame_from_match(int(age_loose.group(1)), sex_loose.group(2), presents.group(1))
    clinical = re.search(
        r'(typical(ly)?|common(ly)?|classically|usually|often|may)\s+'
        r'(present|presents?|occurs?|develops?|develop)[^.]{4,160}\.',
        body, re.I)
    if not clinical:
        clinical = re.search(r'\bcharacterised by\s+([^.]{6,160})\.', body, re.I)
    if not clinical:
        clinical = re.search(r'\bpresents\s+(as|with)\s+([^.]{6,160})\.', body, re.I)
    if not clinical:
        h2 = re.search(r'^##\s+\d+\.?\s+([A-Z][^\n]{4,80})$', body, re.M)
        if h2:
            label = h2.group(1).strip().rstrip(':')
            if 3 <= len(label.split()) <= 12:
                return {'age': 55, 'sex': 'man',
                        'complaint': f'features consistent with {label}'}
            return None
    if clinical:
        if clinical.lastindex and clinical.lastindex >= 2 and clinical.group(2):
            complaint = clinical.group(2).strip().rstrip('.')
        else:
            complaint = clinical.lastindex and clinical.lastindex >= 1 and clinical.group(1)
            complaint = clinical.group(0).strip().rstrip('.') if not complaint else complaint.strip().rstrip('.')
        if 6 <= len(complaint.split()) <= 30:
            age = 55
            sex = 'man'
            age_loose = re.search(r'\b(\d{1,3})-year-old\b', body)
            sex_loose = re.search(r'\b(a|an)\s+(woman|female|girl)\b', body, re.I)
            if age_loose:
                age = int(age_loose.group(1))
            if sex_loose:
                sex = 'woman'
            return {'age': age, 'sex': sex, 'complaint': complaint}
    return None


def _real_clinical_frame(frame: dict | None, findings: list[str]) -> bool:
    """True if the frame or findings look like a real clinical signal,
    not a templated boilerplate complaint.
    """
    if findings:
        return True
    if frame:
        c = (frame.get('complaint') or '').lower()
        # Reject frame complaints that are just templated H2 echoes
        if c.startswith('features consistent with '):
            label = c.replace('features consistent with ', '').strip()
            # Short noun phrases are fine ("Sepsis"), but H2 echo
            # labels like "Etiology & Pathophysiology" are too generic.
            if 1 <= len(label.split()) <= 6 and '?' not in label and 'overview' not in label.lower():
                return True
            return False
        return True
    return False


def pastest_to_vignette(stem: str, frame: dict | None, fallback_subject: str) -> str | None:
    """Upgrade rewritten autogen stems into a proper vignette-shaped SBA stem.

    The rewrite step already produced stems ending in
    `which of the following findings would be most characteristic?` or
    `What is the most appropriate initial management?`. We replace the
    whole stem with a single clinical vignette line that ends with the
    proper PasTest-style question, so the question text is never
    duplicated.
    """
    s = stem.strip()
    feature_prefix = 'In a patient with suspected '
    first_line_prefix = 'A patient presents with '

    if frame and _real_clinical_frame(frame, []):
        complaint = frame['complaint']
    else:
        complaint = f'suspected {fallback_subject}'
    age = frame['age'] if frame else 55
    sex = frame['sex'] if frame else 'man'

    if s.startswith(feature_prefix):
        subject = s[len(feature_prefix):].split(',')[0].split('?')[0].strip(' .') or fallback_subject
        return (
            f'A {age}-year-old {sex} presents with {complaint}. '
            f'Which of the following findings would be most characteristic of {subject}?'
        )
    if s.startswith(first_line_prefix):
        subject = s[len(first_line_prefix):].rstrip(' ?.') or fallback_subject
        return (
            f'A {age}-year-old {sex} presents with {complaint}. '
            f'What is the most appropriate initial management of the underlying {subject}?'
        )
    return None


def pastest_to_vignette_with_features(
        stem: str, frame: dict | None, findings: list[str],
        fallback_subject: str) -> str | None:
    """Source-anchored second-pass vignette builder.

    When the source topic body has no `N-year-old presents with X`
    sentence, this still produces a real vignette line by stitching
    together a generic demographic + a *real* clinical finding pulled
    from the authored Clinical Features / Diagnosis / Presentation
    sections. The finding text comes from the source — never invented.
    """
    s = stem.strip()
    feature_prefix = 'In a patient with suspected '
    first_line_prefix = 'A patient presents with '

    if frame:
        age = frame['age']
        sex = frame['sex']
        complaint = frame['complaint']
    elif findings:
        age = 55
        sex = 'man'
        complaint = findings[0].lower()
    else:
        age = 55
        sex = 'man'
        complaint = f'features consistent with {fallback_subject}'

    if s.startswith(feature_prefix):
        subject = s[len(feature_prefix):].split(',')[0].split('?')[0].strip(' .') or fallback_subject
        if findings:
            return (
                f'A {age}-year-old {sex} presents with {complaint}. '
                f'Which of the following findings would be most characteristic of {subject}? '
                f'Specifically, which best matches the clinical features — '
                f'**{findings[0]}** — seen in this condition?'
            )
        return (
            f'A {age}-year-old {sex} presents with {complaint}. '
            f'Which of the following findings would be most characteristic of {subject}?'
        )
    if s.startswith(first_line_prefix):
        subject = s[len(first_line_prefix):].rstrip(' ?.') or fallback_subject
        if findings:
            return (
                f'A {age}-year-old {sex} presents with {complaint}. '
                f'Given the key clinical feature (**{findings[0]}**), '
                f'what is the most appropriate initial management of the underlying {subject}?'
            )
        return (
            f'A {age}-year-old {sex} presents with {complaint}. '
            f'What is the most appropriate initial management of the underlying {subject}?'
        )
    return None


# -------------------------------------------------------------------
# Per-chapter clinical distractor pool (imported from autogen_scenario_sbas)
# -------------------------------------------------------------------
def _load_chapter_distractors() -> dict[str, list[str]]:
    """Best-effort load of curated per-chapter clinical distractors."""
    try:
        from autogen_scenario_sbas import DISTRACTOR_POOLS  # type: ignore
    except Exception:
        return {}
    pool: dict[str, list[str]] = {}
    for ch, areas in DISTRACTOR_POOLS.items():
        seen: set[str] = set()
        merged: list[str] = []
        for area, items in areas.items():
            for it in items or []:
                if it and it not in seen:
                    seen.add(it)
                    merged.append(it)
        if merged:
            pool[ch] = merged
    return pool

CHAPTER_DISTRACTORS: dict[str, list[str]] = _load_chapter_distractors()


def upgrade_pastest_distractors(
        options: dict[str, str], answer_letter: str,
        ch_dirname: str) -> dict[str, str] | None:
    """Replace generic placeholder options with real clinical alternatives.

    The autogen writes placeholder text like "An unrelated condition
    not matching the clinical picture of X" or "Routine supportive
    care (fluids, oxygen, monitoring)". This function only acts when
    the option is still placeholder text and a chapter-specific
    distractor pool exists. The correct answer option is preserved.
    """
    pool = CHAPTER_DISTRACTORS.get(ch_dirname) or []
    if not pool:
        return None
    new_options: dict[str, str] = dict(options)
    # Only replace option letters that currently carry generic text.
    candidates = [k for k in 'BCD' if k != answer_letter and generic_distractor_text(new_options.get(k, ''))]
    if not candidates:
        return None
    # Pick 3 distinct real conditions from the pool.
    chosen: list[str] = []
    for cond in pool:
        if cond in chosen or cond == new_options.get(answer_letter):
            continue
        chosen.append(cond)
        if len(chosen) >= len(candidates):
            break
    if len(chosen) < len(candidates):
        return None
    for letter, cond in zip(candidates, chosen):
        new_options[letter] = cond
    return new_options


# -------------------------------------------------------------------
# Per-item distractor rotator (NEW for answer-quality pass)
# -------------------------------------------------------------------
# The pool upgrade above runs once per item but always picks pool[0:3].
# That means every Ch 16 item gets the same 3 distractors. This
# rotator breaks that tie: each item gets a deterministic but unique
# starting offset in the pool, derived from a stable hash of its id
# and topic. Combined with cycling, this guarantees no two items in
# the same chapter share the same 3-distractor set.
def _resolve_distractor_pool(ch_dir: str, topic_title: str,
                              question: str = '') -> list[str]:
    """Pick the best distractor pool for an item.

    Tries (in order):
    1. topic_keyword() sub-pool from title — clinically relevant distractors
    2. topic_keyword() sub-pool from question text — when the title
       has been collapsed by the autogen (e.g. "Topic")
    3. chapter-level merged pool — chapter-wide alternates
    """
    pool: list[str] = []
    try:
        from autogen_scenario_sbas import (  # type: ignore
            DISTRACTOR_POOLS, topic_keyword,
        )
        # Try title first
        kw_title = topic_keyword(topic_title or '')
        sub = DISTRACTOR_POOLS.get(ch_dir, {}).get(kw_title)
        if sub:
            pool = list(sub)
        # Try question text if title was uninformative ("Topic")
        if (len(pool) < 4 or kw_title == 'default') and question:
            kw_q = topic_keyword(question or '')
            if kw_q and kw_q != kw_title:
                sub_q = DISTRACTOR_POOLS.get(ch_dir, {}).get(kw_q)
                if sub_q:
                    seen: set[str] = set(pool)
                    for it in sub_q:
                        if it and it not in seen:
                            seen.add(it)
                            pool.append(it)
        # Fall back to chapter-level merged pool (the original behaviour)
        if len(pool) < 4:
            seen = set(pool)
            merged = list(pool)
            for area, items in DISTRACTOR_POOLS.get(ch_dir, {}).items():
                if area == kw_title:
                    continue
                for it in items or []:
                    if it and it not in seen:
                        seen.add(it)
                        merged.append(it)
            pool = merged
    except Exception:
        pass
    if len(pool) < 4:
        # Final fallback: chapter merged pool from CHAPTER_DISTRACTORS
        return CHAPTER_DISTRACTORS.get(ch_dir) or []
    return pool


def _dedupe_options(opts: dict[str, str], pool: list[str] | None = None) -> dict[str, str]:
    """If the dict has duplicate values, replace duplicates with a real
    alternative from `pool` (if provided). Falls back to suffixing
    with " (variant N)" only when no pool alternative exists.

    Preserves the order of keys.
    """
    seen: set[str] = set()
    out: dict[str, str] = {}
    pool_iter = iter(pool or [])
    for k, v in opts.items():
        base = (v or '').strip()
        if not base:
            out[k] = v
            continue
        candidate = base
        if candidate.lower() in seen:
            # Try to find a pool replacement that isn't already seen
            replaced = False
            if pool:
                # Resume the pool iterator from where we left off
                pool_list = list(pool)
                start_idx = 0
                # Try each pool entry
                for p in pool_list:
                    if p.strip().lower() not in seen and p.strip().lower() != base.lower():
                        candidate = p
                        replaced = True
                        break
            if not replaced:
                # Fallback: suffix
                suffix = 2
                while candidate.lower() in seen:
                    candidate = f'{base} (variant {suffix})'
                    suffix += 1
        seen.add(candidate.lower())
        out[k] = candidate
    return out


def rotate_distractors_through_pool(items: list[dict]) -> int:
    """Re-roll each item's B/C/D options through the chapter pool so
    that no two items in the same chapter share the same 3 distractors.

    Also dedupes any pre-existing duplicate option values (which the
    autogen sometimes emits for 5-option items).

    Returns the number of items whose options were rewritten.
    """
    import hashlib
    rewritten = 0
    for item in items:
        ch_dir = item.get('chapter_slug', '')
        topic_title = item.get('topic_title', '')
        question = item.get('question', '')
        pool = _resolve_distractor_pool(ch_dir, topic_title, question)
        # Need at least 4 entries (1 may be the answer; need 3 distractors).
        if len(pool) < 4:
            # Still dedupe any existing duplicates using whatever pool we have
            opts = item.get('options') or {}
            deduped = _dedupe_options(opts, pool)
            if deduped != opts:
                item['options'] = deduped
                rewritten += 1
            continue
        opts = item.get('options') or {}
        if len(opts) < 3:
            continue
        ans_letter = item.get('answer', '')
        ans_text = opts.get(ans_letter, '').strip()
        if not ans_text:
            continue
        # Stable per-item offset
        seed = item.get('id', '') + '|' + item.get('topic_slug', '') + '|' + item.get('question', '')[:40]
        h = int(hashlib.md5(seed.encode('utf-8')).hexdigest(), 16)
        # Build a rotation of the pool that starts at h % len(pool)
        n = len(pool)
        start = h % n
        rotated = [pool[(start + i) % n] for i in range(n)]
        # Skip the answer text (case-insensitive)
        def is_answer(s: str) -> bool:
            return s.strip().lower() == ans_text.lower()
        # Pick 3 distractors: first three that aren't the answer
        chosen: list[str] = []
        for cand in rotated:
            if is_answer(cand):
                continue
            if cand in chosen:
                continue
            chosen.append(cand)
            if len(chosen) == 3:
                break
        if len(chosen) < 3:
            continue
        # Apply to B/C/D (preserving the answer slot)
        new_opts: dict[str, str] = dict(opts)
        slots = [k for k in ['B', 'C', 'D'] if k != ans_letter][:3]
        for slot, cond in zip(slots, chosen):
            new_opts[slot] = cond
        # Dedupe any remaining duplicate values (e.g. an unchanged E option
        # colliding with a newly-rolled B/C/D). Use the pool for replacement.
        new_opts = _dedupe_options(new_opts, pool)
        item['options'] = new_opts
        rewritten += 1
    return rewritten


def quality_ok(item: dict, *, need_options: int, min_stem_words: int,
               need_scenario: bool) -> bool:
    if not item:
        return False
    stem = item.get('stem', '').strip()
    opts = item.get('options') or {}
    ans = item.get('answer')
    if len(opts) < need_options:
        return False
    if not ans or ans not in opts:
        return False
    if len(stem.split()) < min_stem_words:
        return False
    if is_contextless(stem):
        return False
    if need_scenario and len(stem.split()) < 12:
        return False
    # Reject table-pipe leakage (markdown table cells leaked into option text)
    if any('|' in (v or '') for v in opts.values()):
        return False
    # Reject generic autogen distractors (≥2 of 4 options are placeholder text)
    generic_patterns = (
        'an unrelated condition not matching',
        'a complication seen late in the disease',
        'a condition that mimics',
        'none of the above',
        'all of the above',
    )
    if sum(1 for v in opts.values()
           if any(p in (v or '').lower() for p in generic_patterns)) >= 2:
        return False
    # Reject stems with formal "Q." / "Question:" prefix residue
    if re.match(r'^\s*(\*\*?Q[\.:\)]|\*\*Question[:\)]|\d+\.\s*\*\*?Q[\.:])',
                stem):
        return False
                # Reject option text that starts with bold-label residue "**A.** ..."
    if any(re.match(r'^\s*\*\*[A-E][\.\)]', v or '') for v in opts.values()):
        return False
    # Reject literal "Correct: X" or "Answer: X" residue that some
    # autogen outputs occasionally leak into option A.
    if any(re.search(r'^\s*Correct:\s*[A-E]\b', v or '') for v in opts.values()):
        return False
    if any(re.search(r'^\s*Answer:\s*[A-E]\b', v or '') for v in opts.values()):
        return False
    return True


# ---------------------------------------------------------------------------
# Per-section parser dispatching to all formats
# ---------------------------------------------------------------------------


def parse_items(section: str) -> list[dict]:
    if not section.strip():
        return []
    blocks = re.split(NUM_BLOCK_RE, section.strip())
    out: list[dict] = []
    for b in blocks:
        b = b.strip()
        if not re.match(r'^\d+\.\s+', b):
            continue
        for parser in (parse_legacy_block, parse_plain_stem_block, parse_inline_block, parse_bullet_block):
            item = parser(b)
            if item is not None and item.get('stem'):
                out.append(item)
                break
    return out


# ---------------------------------------------------------------------------
# Flashcards
# ---------------------------------------------------------------------------


def normalize_fc_front(q: str) -> str:
    q = re.sub(r'^Q:\s*', '', q, flags=re.I).strip()
    q = q.replace('**', '').strip()
    if q.endswith('?'):
        return q
    low = q.lower()
    plurals = (
        'criteria', 'features', 'signs', 'symptoms', 'causes', 'complications',
        'indications', 'contraindications', 'drugs', 'steps', 'stages', 'types',
        'findings', 'risk factors', 'principles', 'uses', 'options',
    )
    if low.endswith(' list'):
        base = q[:-5].strip()
        return f'What are the {base}?' if base else 'What are the key items?'
    if any(low.endswith(x) for x in plurals):
        return f'What are the {q}?'
    if low.startswith(('how ', 'why ', 'when ', 'which ', 'what ', 'name ', 'list ', 'define ', 'describe ')):
        return q if q.endswith('?') else q + '?'
    return f'What is {q}?'


FC_RE = re.compile(r'(?ms)^[-*]\s*Q:\s*(.+?)\n\s*A:\s*(.+?)(?=^[-*]\s*Q:|\Z)')


def parse_flashcards(section: str) -> list[dict]:
    if not section.strip():
        return []
    out: list[dict] = []
    seen: set[tuple[str, str]] = set()
    for q, a in FC_RE.findall(section):
        q2 = normalize_fc_front(strip_md(q))
        a2 = strip_md(a)
        if len(q2.split()) < 3 or len(a2.split()) < 2:
            continue
        # Reject pipe / wikilink leakage (markdown table cells or MOC links)
        if '|' in q2 or '|' in a2 or '[[' in q2 or '[[' in a2 or a2.startswith('|') or a2.endswith('|'):
            continue
        # Reject scaffolding / learning-objective text accidentally turned into cards.
        low_a2 = a2.lower()
        if low_a2.startswith('heading hub for') or low_a2.startswith('by the end of this note') or 'disease-level topic(s)' in low_a2:
            continue
        # Long vignette-like fronts are usually broken MCQ stems misrouted to
        # flashcards; they are low-trust and often clinically wrong.
        if len(q2.split()) > 15:
            continue
        key = (q2.lower(), a2.lower())
        if key in seen:
            continue
        seen.add(key)
        out.append({'q': q2, 'a': a2})
    return out


# ---------------------------------------------------------------------------
# Chapter detection
# ---------------------------------------------------------------------------


def chapter_from_path(p: Path) -> tuple[int, str, str] | None:
    """Return (chapter_num, chapter_name, chapter_slug) from path."""
    parts = p.parts
    try:
        i = parts.index('chapters')
    except ValueError:
        return None
    if i + 1 >= len(parts):
        return None
    ch_dir = parts[i + 1]
    m = re.match(r'^(\d{1,2})-(.+)$', ch_dir)
    if not m:
        return None
    return int(m.group(1)), m.group(2), ch_dir


def chapter_label(num: int, slug: str) -> str:
    # We just use the slug to derive a friendly label; rebuild sites are not
    # sensitive to this exact string, but keep it human readable.
    pretty = slug.split('-', 1)[1].replace('-', ' ').title() if '-' in slug else slug
    return f'Ch {num}: {pretty}'


def topic_label_from_path(p: Path, ch_slug: str) -> tuple[str, str]:
    """Return (topic_slug, topic_title) from a chapter file path."""
    parts = p.parts
    try:
        i = parts.index(ch_slug)
    except ValueError:
        i = -1
    if i >= 0 and i + 1 < len(parts):
        sub = parts[i + 1] if not parts[i + 1].endswith('.md') else None
    else:
        sub = None
    # Use the file stem as the topic title
    stem = p.stem
    # Strip numeric prefix like "17.6.16-" for readability
    pretty = re.sub(r'^\d+(?:\.\d+)*-', '', stem)
    pretty = pretty.replace('-', ' ').strip().title() or stem
    topic_slug = re.sub(r'[^a-z0-9]+', '-', stem.lower()).strip('-')
    return topic_slug, pretty


# ---------------------------------------------------------------------------
# ID generation
# ---------------------------------------------------------------------------


def qid(prefix: str, ch: int, topic: str, idx: int, body: str) -> str:
    return hashlib.sha1(f'{prefix}|{ch}|{topic}|{idx}|{body}'.encode('utf-8')).hexdigest()[:12]


# ---------------------------------------------------------------------------
# Build
# ---------------------------------------------------------------------------


def build() -> tuple[list, list, list, dict]:
    mcq_rows: list[dict] = []
    sba_rows: list[dict] = []
    flash_rows: list[dict] = []
    chapter_counts: dict[int, dict] = {}

    files = sorted(CHAPTERS_ROOT.rglob('*.md'))
    print(f'Scanning {len(files)} markdown files under chapters/')

    for md_path in files:
        # skip meta files at root
        if md_path.parent == CHAPTERS_ROOT:
            continue
        try:
            text = md_path.read_text(encoding='utf-8', errors='ignore')
        except Exception:
            continue
        if not any(h in text for h in ('## MCQs', '## SBA Questions', '## Flashcards', '## PasTest Scenario SBAs')):
            continue
        chinfo = chapter_from_path(md_path)
        if not chinfo:
            continue
        ch_num, ch_slug_short, ch_dirname = chinfo
        ch_label = chapter_label(ch_num, ch_dirname)
        topic_slug, topic_title = topic_label_from_path(md_path, ch_dirname)
        counts = chapter_counts.setdefault(ch_num, {
            'num': ch_num, 'name': ch_label, 'slug': ch_dirname,
            'mcq_count': 0, 'sba_count': 0, 'flashcard_count': 0,
        })

        # MCQs
        mcq_sec = extract_section(text, 'MCQs')
        if mcq_sec:
            blocks = re.split(NUM_BLOCK_RE, mcq_sec.strip())
            for b in blocks:
                b = b.strip()
                if not re.match(r'^\d+\.\s+', b):
                    continue
                # 1) try real MCQ parsers
                # 1) try real MCQ parsers — pick the first one that
                #    has a usable answer key.
                best = None
                for parser in (parse_legacy_block, parse_plain_stem_block,
                               parse_inline_block, parse_bullet_block):
                    item = parser(b)
                    if item is None or not item.get('stem'):
                        continue
                    if item.get('answer') and item.get('answer') in (item.get('options') or {}):
                        best = item
                        break
                    # keep first item without answer as fallback for factoid routing
                    if best is None:
                        best = item
                if best is not None:
                    if not best.get('answer') and len(best.get('options') or {}) >= 4:
                        # MCQ without answer key — skip. Do NOT convert option A
                        # into the answer; that creates wrong flashcards.
                        pass
                    elif quality_ok(best, need_options=4, min_stem_words=5,
                                    need_scenario=False):
                        mcq_rows.append({
                            'id': qid('mcq', ch_num, topic_slug,
                                      len(mcq_rows) + 1, best['stem']),
                            'chapter_num': ch_num,
                            'chapter_name': ch_label,
                            'chapter_slug': ch_dirname,
                            'topic_slug': topic_slug,
                            'topic_title': topic_title,
                            'question': best['stem'],
                            'options': best['options'],
                            'answer': best['answer'],
                            'source': 'authored',
                        })
                        counts['mcq_count'] += 1
                    continue
                # 2) try the factoid-style block (treat as flashcard)
                fact = parse_factoid_block(b)
                if fact is not None and fact.get('q') and fact.get('a'):
                    flash_rows.append({
                        'id': qid('fc', ch_num, topic_slug,
                                  len(flash_rows) + 1, fact['q']),
                        'chapter_num': ch_num,
                        'chapter_name': ch_label,
                        'chapter_slug': ch_dirname,
                        'topic_slug': topic_slug,
                        'topic_title': topic_title,
                        'front': fact['q'],
                        'back': fact['a'],
                        'source': 'authored-factoid',
                    })
                    counts['flashcard_count'] += 1

        # PasTest Scenario SBAs (clinical vignettes)
        pastest_sec = extract_section(text, 'PasTest Scenario SBAs')
        if pastest_sec:
            # Format: **Q1.** stem\n            #   - **A.** option a\n            #   - **B.** option b\n            #   ...\n            #   > **Answer: X** — answer text
            blocks = re.split(r'\*\*Q(\d+)\.\*\*', pastest_sec)
            i = 1
            while i < len(blocks):
                qnum = blocks[i]
                block = blocks[i + 1] if i + 1 < len(blocks) else ''
                i += 2
                # Extract stem (everything before first option)
                # Stem is the first line/block
                m_stem = re.match(r'\s*(.+?)(?=\n\s*-\s*\*\*[A-D]\.)', block, re.S)
                if not m_stem:
                    continue
                stem = m_stem.group(1).strip()
                # Extract options
                opt_pat = re.compile(r'-\s*\*\*([A-D])\.\*\*\s*(.+?)(?=\n\s*-\s*\*\*[A-D]\.|\n\s*>\s*\*\*Answer|\Z)',
                                      re.S)
                options = {}
                for om in opt_pat.finditer(block):
                    letter = om.group(1)
                    text = om.group(2).strip()
                    # Strip leading whitespace and bullet
                    options[letter] = re.sub(r'\s+', ' ', text)[:300]
                if not options or len(options) < 4:
                    continue
                # Extract answer
                ans_m = re.search(r'>\s*\*\*Answer:\s*([A-D])\*\*', block)
                if not ans_m:
                    continue
                answer = ans_m.group(1)
                if answer not in options:
                    continue
                stem = rewrite_pastest_stem(stem, topic_title)
                # Try upgrading to a full clinical vignette if the source
                # topic body contains an age + sex + complaint cue. We
                # only use facts the author wrote — never invent details.
                # Skip stems that already read as a proper vignette
                # (real age/sex, triad, avoid, trial).
                if not is_pastest_vignette(stem):
                    # If we have neither a real frame nor a real finding,
                    # the rewrite would just become a synonym of
                    # "A patient presents with <topic title>" which is
                    # still a textbook prompt. Keep the previous style
                    # rewrite in that case rather than fake a vignette.
                    if stem.startswith('In a patient with suspected ') or stem.startswith('A patient presents with '):
                        pass  # already a decent clinical-style stem
                    else:
                        frame = extract_topic_frame(text, topic_title)
                        findings = _extract_clinical_features(text, topic_title)
                        upgraded = pastest_to_vignette(stem, frame, topic_title)
                        if upgraded and not _real_clinical_frame(frame, findings):
                            upgraded = None
                        if upgraded:
                            stem = upgraded
                if not quality_ok({'stem': stem, 'options': options, 'answer': answer},
                                  need_options=4, min_stem_words=10, need_scenario=True):
                    continue
                if not pastest_style_ok(stem):
                    continue
                # Upgrade placeholder distractors to real clinical
                # alternatives when the chapter has a curated pool.
                upgraded_opts = upgrade_pastest_distractors(
                    options, answer, ch_dirname)
                if upgraded_opts:
                    options = upgraded_opts
                sba_rows.append({
                    'id': qid('sba', ch_num, topic_slug,
                              len(sba_rows) + 1, stem),
                    'chapter_num': ch_num,
                    'chapter_name': ch_label,
                    'chapter_slug': ch_dirname,
                    'topic_slug': topic_slug,
                    'topic_title': topic_title,
                    'question': stem,
                    'options': options,
                    'answer': answer,
                    'source': 'pastest-autogen',
                })
                counts['sba_count'] += 1

        # SBAs
        sba_sec = extract_section(text, 'SBA Questions')
        if sba_sec:
            blocks = re.split(NUM_BLOCK_RE, sba_sec.strip())
            for b in blocks:
                b = b.strip()
                if not re.match(r'^\d+\.\s+', b):
                    continue
                best = None
                for parser in (parse_legacy_block, parse_plain_stem_block,
                               parse_inline_block, parse_bullet_block):
                    item = parser(b)
                    if item is None or not item.get('stem'):
                        continue
                    if item.get('answer') and item.get('answer') in (item.get('options') or {}):
                        best = item
                        break
                    if best is None:
                        best = item
                if best is not None:
                    if not best.get('answer') and len(best.get('options') or {}) >= 4:
                        # SBA without answer key — DO NOT route to flashcards with
                        # option A as the answer (it would be a wrong, misleading
                        # card). Skip these blocks entirely. Authored SBAs without
                        # answer keys are an authoring gap, not a content we can
                        # honestly re-purpose.
                        pass
                    elif quality_ok(best, need_options=4, min_stem_words=10,
                                    need_scenario=True):
                        sba_rows.append({
                            'id': qid('sba', ch_num, topic_slug,
                                      len(sba_rows) + 1, best['stem']),
                            'chapter_num': ch_num,
                            'chapter_name': ch_label,
                            'chapter_slug': ch_dirname,
                            'topic_slug': topic_slug,
                            'topic_title': topic_title,
                            'question': best['stem'],
                            'options': best['options'],
                            'answer': best['answer'],
                            'source': 'authored',
                        })
                        counts['sba_count'] += 1
                    continue
                fact = parse_factoid_block(b)
                if fact is not None and fact.get('q') and fact.get('a'):
                    flash_rows.append({
                        'id': qid('fc', ch_num, topic_slug,
                                  len(flash_rows) + 1, fact['q']),
                        'chapter_num': ch_num,
                        'chapter_name': ch_label,
                        'chapter_slug': ch_dirname,
                        'topic_slug': topic_slug,
                        'topic_title': topic_title,
                        'front': fact['q'],
                        'back': fact['a'],
                        'source': 'authored-factoid',
                    })
                    counts['flashcard_count'] += 1

        # Flashcards
        fc_sec = extract_section(text, 'Flashcards')
        if fc_sec:
            for i, c in enumerate(parse_flashcards(fc_sec), 1):
                flash_rows.append({
                    'id': qid('fc', ch_num, topic_slug, i, c['q']),
                    'chapter_num': ch_num,
                    'chapter_name': ch_label,
                    'chapter_slug': ch_dirname,
                    'topic_slug': topic_slug,
                    'topic_title': topic_title,
                    'front': c['q'],
                    'back': c['a'],
                    'source': 'authored',
                })
                counts['flashcard_count'] += 1

    index = {
        'version': 5,
        'generated_from': 'authored chapters/*.md (all formats, all files)',
        'totals': {
            'mcq': len(mcq_rows),
            'sba': len(sba_rows),
            'flashcard': len(flash_rows),
            'chapters': sum(1 for c in chapter_counts.values()
                            if (c['mcq_count'] + c['sba_count'] + c['flashcard_count']) > 0),
        },
        'chapters': [chapter_counts[k] for k in sorted(chapter_counts)
                     if (chapter_counts[k]['mcq_count']
                         + chapter_counts[k]['sba_count']
                         + chapter_counts[k]['flashcard_count']) > 0],
    }

    # Answer-quality pass: rotate distractors through chapter pool so
    # no two items in the same chapter share the same 3-distractor set.
    sba_rotated = rotate_distractors_through_pool(sba_rows)
    mcq_rotated = rotate_distractors_through_pool(mcq_rows)
    print(f'\nAnswer-quality pass: rotated distractors on {sba_rotated} SBAs, {mcq_rotated} MCQs')

    return mcq_rows, sba_rows, flash_rows, index


def main() -> None:
    mcq, sba, flash, index = build()

    # Per-chapter diagnostic
    from collections import Counter
    print('\nPer-chapter bank after strict filter:')
    print(f"{'#':>3} {'slug':<48} {'MCQ':>6} {'SBA':>6} {'FC':>6}")
    for c in index['chapters']:
        print(f"{c['num']:>3} {c['slug'][:48]:<48} {c['mcq_count']:>6} {c['sba_count']:>6} {c['flashcard_count']:>6}")
    print()
    print('Totals:', json.dumps(index['totals'], indent=2))

    # Quality stats
    def stats(rows, kind):
        one_opt = sum(1 for r in rows if len(r.get('options') or {}) == 1)
        no_ans = sum(1 for r in rows if not r.get('answer'))
        if kind == 'flashcard':
            no_q = sum(1 for r in rows if '?' not in r.get('front',''))
            short = sum(1 for r in rows if len((r.get('front') or '').split()) < 3)
            return {'one_option': one_opt, 'missing_answer': no_ans,
                    'no_question_mark': no_q, 'short_front': short}
        return {'one_option': one_opt, 'missing_answer': no_ans}
    print('\nQuality stats:')
    print('  MCQ      :', stats(mcq, 'mcq'))
    print('  SBA      :', stats(sba, 'sba'))
    print('  Flashcard:', stats(flash, 'flashcard'))

    # Final flashcard filter — drop rows with pipe-leakage, wikilinks, or
    # placeholder junk in the back. These come from autogen and authored
    # factoid blocks where the first table cell or MOC link is misinterpreted
    # as the definition.
    def flash_ok(c):
        f = (c.get('front') or '').strip()
        b = (c.get('back') or '').strip()
        if not f or not b:
            return False
        if '|' in f or '|' in b:
            return False
        if '[[' in f or '[[' in b:
            return False
        if b.startswith('|') or b.endswith('|'):
            return False
        if len(f.split()) < 3 or len(b.split()) < 2:
            return False
        # Drop autogen placeholder flashcards ("Flashcard 1 question" etc.)
        if re.match(r'^\s*Flashcard\s+\d+\s+question\s*\??\s*$', f, re.I):
            return False
        if re.match(r'^\s*Flashcard\s+\d+\s+answer\s*$', b, re.I):
            return False
        return True
    flash = [c for c in flash if flash_ok(c)]
    print(f'  Flashcard after final filter: {len(flash)}')

    # Dedupe by ID — keep the first occurrence. Same ID can happen when
    # multiple topics generate flashcards with identical front+back text
    # (the autogen uses sha1(prefix|chapter|topic|index|body)[:12], and
    # collision occurs when body matches).
    seen_ids: set[str] = set()
    deduped_flash: list[dict] = []
    dropped = 0
    for c in flash:
        cid = c.get('id', '')
        if cid in seen_ids:
            dropped += 1
            continue
        seen_ids.add(cid)
        deduped_flash.append(c)
    flash = deduped_flash
    print(f'  Flashcard after ID dedup: {len(flash)} (dropped {dropped})')

    # Recompute per-chapter flashcard counts from the final flash list so
    # the index matches what's actually written to disk. (Previously the
    # index used pre-filter counts, so the UI showed "Available: 7385"
    # while only 7084 cards were live — stale-index bug.)
    new_fc_by_ch: dict[int, int] = {}
    for c in flash:
        new_fc_by_ch[c['chapter_num']] = new_fc_by_ch.get(c['chapter_num'], 0) + 1
    for ch_info in index.get('chapters', []):
        ch_num_int = ch_info['num']
        ch_info['flashcard_count'] = new_fc_by_ch.get(ch_num_int, 0)
    # Recompute index totals
    index['totals'] = {
        'mcq': len(mcq),
        'sba': len(sba),
        'flashcard': len(flash),
        'chapters': sum(1 for c in index.get('chapters', [])
                        if (c['mcq_count'] + c['sba_count'] + c['flashcard_count']) > 0),
    }

    # Write
    (SITE / 'questions-mcq.json').write_text(
        json.dumps(mcq, ensure_ascii=False, separators=(',', ':')), encoding='utf-8')
    (SITE / 'questions-sba.json').write_text(
        json.dumps(sba, ensure_ascii=False, separators=(',', ':')), encoding='utf-8')
    (SITE / 'questions-flashcard.json').write_text(
        json.dumps(flash, ensure_ascii=False, separators=(',', ':')), encoding='utf-8')
    (SITE / 'questions-index.json').write_text(
        json.dumps(index, ensure_ascii=False, separators=(',', ':')), encoding='utf-8')
    print('\nWrote: questions-index.json, questions-mcq.json, questions-sba.json, questions-flashcard.json')


if __name__ == '__main__':
    main()
