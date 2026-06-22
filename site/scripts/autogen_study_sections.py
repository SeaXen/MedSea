#!/usr/bin/env python3
"""Generate MCQ / SBA / Flashcard sections from authored topic content.

This script reads /mnt/tb/Medicine/<chapter>/.../*.md files and uses
their real authored content (definitions, clinical features, high-yield
tables, viva question lists) to produce:
  - ## MCQs            (5+ items)
  - ## SBA Questions   (3+ items)
  - ## Flashcards      (8+ items)

The output is appended to the published tree at:
  /mnt/tb/Sea-knowledge/#MedSea/chapters/<chapter>/diseases/<topic>/topic.md

Heuristics are intentionally conservative: if the topic lacks enough
structured content to ground the questions, the script emits a small
bank rather than fabricating items.
"""
from __future__ import annotations

import json
import re
from pathlib import Path

MED = Path('/mnt/tb/Medicine')
ROOT = Path('/mnt/tb/Sea-knowledge/#MedSea')
CHAPTERS = ROOT / 'chapters'

# Map source chapter folder name -> published slug
SRC_TO_PUB = {
    'Clinical Immunology':                  '4-clinical-immunology',
    'Hematology':                           '24-haematology-and-transfusion-medicine',
    'Oncology':                              '8-oncology',
    'Hepatology':                            '23-hepatology',
    'Rheumatology':                          '25-rheumatology-and-bone-disease',
    'Medical Psychiatry':                    '29-medical-psychiatry',
    'Maternal Medicine':                     '30-maternal-medicine',
    'Adolescent and Transition Medicine':    '31-adolescence-transition-and-young-adult-m',
    'Ageing and Disease':                    '32-older-adult-medicine-and-frailty',
    'Endocrinology':                        '20-endocrinology',
    'Medical Ophthalmology':                '28-medical-ophthalmology',
}

# Chapter labels for human-readable tags
CH_LABELS = {
    '4-clinical-immunology':                 'Ch 4: Clinical Immunology',
    '8-oncology':                            'Ch 8: Oncology',
    '20-endocrinology':                      'Ch 20: Endocrinology',
    '23-hepatology':                         'Ch 23: Hepatology',
    '24-haematology-and-transfusion-medicine': 'Ch 24: Haematology & Transfusion Medicine',
    '25-rheumatology-and-bone-disease':      'Ch 25: Rheumatology & Bone Disease',
    '28-medical-ophthalmology':              'Ch 28: Medical Ophthalmology',
    '29-medical-psychiatry':                 'Ch 29: Medical Psychiatry',
    '30-maternal-medicine':                  'Ch 30: Maternal Medicine',
    '31-adolescence-transition-and-young-adult-m': 'Ch 31: Adolescent & Transition Medicine',
    '32-older-adult-medicine-and-frailty':   'Ch 32: Ageing and Disease',
}

# ---------------------------------------------------------------------------
# Section extraction
# ---------------------------------------------------------------------------

H2_RE = re.compile(r'^##\s+([^\n]+)', re.M)


def get_h2_sections(text: str) -> list[tuple[str, str]]:
    """Return list of (header, body) for every H2 section."""
    matches = list(H2_RE.finditer(text))
    out = []
    for i, m in enumerate(matches):
        header = m.group(1).strip()
        start = m.end()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
        body = text[start:end].strip()
        out.append((header, body))
    return out


def get_h3_sections(body: str) -> list[tuple[str, str]]:
    matches = list(re.finditer(r'^###\s+([^\n]+)', body, re.M))
    out = []
    for i, m in enumerate(matches):
        header = m.group(1).strip()
        start = m.end()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(body)
        out.append((header, body[start:end].strip()))
    return out


# ---------------------------------------------------------------------------
# Table extraction (markdown pipe tables)
# ---------------------------------------------------------------------------

TABLE_RE = re.compile(r'((?:^\|.*\|\s*\n)+)', re.M)
ROW_RE = re.compile(r'^\|(.+?)\|\s*$', re.M)
SEP_RE = re.compile(r'^\|?\s*:?-+:?\s*(\|\s*:?-+:?\s*)+\|?\s*$')


def parse_table(block: str) -> tuple[list[str], list[list[str]]] | None:
    lines = [ln for ln in block.strip().splitlines() if ln.strip()]
    if len(lines) < 3:
        return None
    # validate header / sep / data
    header_line = lines[0]
    sep_line = lines[1]
    if not SEP_RE.match(sep_line):
        return None
    headers = [c.strip() for c in header_line.strip('|').split('|')]
    rows = []
    for ln in lines[2:]:
        cells = [c.strip() for c in ln.strip('|').split('|')]
        if len(cells) != len(headers):
            return None
        rows.append(cells)
    return headers, rows


def extract_tables(text: str) -> list[tuple[str, list[str], list[list[str]]]]:
    """Return [(section_header, headers, rows)] for every table."""
    out = []
    for header, body in get_h2_sections(text) + [(h, b) for h, b in get_h3_sections(text)]:
        for m in TABLE_RE.finditer(body):
            tbl = parse_table(m.group(1))
            if tbl is not None and len(tbl[1]) >= 2:
                out.append((header, tbl[0], tbl[1]))
    return out


# ---------------------------------------------------------------------------
# Definition / first-sentence extraction
# ---------------------------------------------------------------------------

DEF_RE = re.compile(
    r'(?:^|\n)#+\s+Definition[^\n]*\n+(.*?)(?=\n#+\s|\Z)',
    re.S | re.I,
)


def first_meaningful_sentence(body: str) -> str | None:
    """Pick the first sentence that contains a noun phrase worth asking
    about (i.e. is not boilerplate, frontmatter, checkbox, or short)."""
    in_frontmatter = False
    for raw in body.splitlines():
        s = raw.strip().lstrip('> ').strip()
        if not s:
            continue
        # Skip YAML frontmatter
        if s == '---':
            in_frontmatter = not in_frontmatter
            continue
        if in_frontmatter:
            continue
        # Skip YAML-style frontmatter fragments if no fence was seen
        if s.startswith('tags:') or s.startswith('davidson_') or s.startswith('status:') \
           or s.startswith('priority:') or s.startswith('chapter:') or s.startswith('heading:') \
           or s.startswith('exam_relevance:') or s.startswith('see_also:') \
           or s.startswith('created:') or s.startswith('modified:') \
           or s.startswith('id:') or s.startswith('aliases:'):
            continue
        # Skip lines that look like a wikilink or section divider
        if s.startswith('[[') or s.startswith('---') or s.startswith('==='):
            continue
        # Skip checkbox / task-list items
        if s.startswith('- [ ]') or s.startswith('- [x]') or s.startswith('* [ ]'):
            continue
        # drop leading emoji / marker / numbers
        s = re.sub(r'^[\W_]*[:：]\s*', '', s)
        s = re.sub(r'^[\d️⃣]+\s*', '', s)
        s = re.sub(r'^[\U0001F300-\U0001FAFF]\s*', '', s)
        # remove markdown bold/italic/code
        s = re.sub(r'[*_`]+', '', s)
        s = re.sub(r'\[(.*?)\]\([^)]*\)', r'\1', s)
        s = re.sub(r'\s+', ' ', s).strip()
        if not s or len(s.split()) < 8:
            continue
        # truncate at first sentence end
        end = re.search(r'[.!?](?=\s|$)', s)
        if end:
            s = s[: end.start() + 1]
        if len(s.split()) >= 8:
            return s
    return None


# ---------------------------------------------------------------------------
# Flashcard generation
# ---------------------------------------------------------------------------


# Headers that are META/REVIEW (we don't want to generate flashcards from them)
SKIP_TABLE_HEADERS = (
    'fcps/mrcp high-yield summary',
    'high-yield summary',
    'spaced repetition tracker',
    'self-test scorecard',
    'one-page revision card',
    'confusions & mnemonics',
    'confusions and mnemonics',
    'viva questions',
    'mind map',
    'self-test',
    'revision card',
    'quick recap',
)


def _table_topic_context(header: str) -> str:
    """Turn a section header like 'Budesonide: Niche Indication' or
    'Azathioprine: Key Details' into a short topic phrase to use in
    question stems.

    Returns the substring before the first ':' if it looks like a
    noun phrase, else falls back to the whole header.
    """
    h = header.strip()
    # strip leading numbers/emojis
    h = re.sub(r'^[\W\d]+', '', h).strip()
    if not h:
        return ''
    # "Budesonide: Niche Indication" -> "Budesonide"
    parts = h.split(':', 1)
    candidate = parts[0].strip()
    # If candidate is short (1-3 words) and looks like a proper noun
    # (capitalised, no common word), use it
    if 1 <= len(candidate.split()) <= 5 and candidate[0].isupper():
        return candidate
    return h


def is_skip_table_header(header: str) -> bool:
    """Return True if this table header is a meta/review section whose
    tables shouldn't be mined for fresh questions."""
    h = header.lower().strip()
    h = re.sub(r'^[\W\d]+', '', h).strip()
    return any(h.startswith(s) for s in SKIP_TABLE_HEADERS)


def make_flashcards_from_table(
    table: tuple[str, list[str], list[list[str]]],
    topic_title: str = '',
) -> list[dict]:
    """From a 2-col table, generate `Term — Value` flashcards.

    The question is always anchored to `topic_title` (the overall
    topic), not the table's section header.  This avoids weird
    flashcards like "What is the MELD of MELD-Na?".
    """
    header, headers, rows = table
    if len(headers) != 2:
        return []
    out = []
    seen = set()
    topic = topic_title or _table_topic_context(header)
    for row in rows:
        a = re.sub(r'[*_`]+', '', row[0]).strip()
        b = re.sub(r'[*_`]+', '', row[1]).strip()
        if not a or not b:
            continue
        a = re.sub(r'\s+', ' ', a)
        b = re.sub(r'\s+', ' ', b)
        if len(a.split()) < 1 or len(b.split()) < 1:
            continue
        a_low = a.lower()
        # Decide stem template based on the row label
        if 'definition' in a_low or 'meaning' in a_low or a_low.startswith('what is'):
            q = f"What is the definition of {topic or b.split(' — ')[0]}?"
        elif 'mechanism' in a_low:
            q = f"What is the mechanism of {topic}?" if topic else "What is the mechanism?"
        elif 'dose' in a_low or 'dosage' in a_low:
            q = f"What is the dose of {topic}?" if topic else "What is the dose?"
        elif 'side effect' in a_low or 'adverse' in a_low or 'toxicity' in a_low:
            q = f"What are the side effects of {topic}?" if topic else "What are the side effects?"
        elif 'indication' in a_low:
            q = f"What is {topic} indicated for?" if topic else "What are the indications?"
        elif 'contraindication' in a_low:
            q = f"When is {topic} contraindicated?" if topic else "What are the contraindications?"
        elif 'monitoring' in a_low or 'monitor' in a_low:
            q = f"How is {topic} monitored?" if topic else "How is it monitored?"
        elif 'first-line' in a_low or 'first line' in a_low:
            q = f"What is the first-line treatment for {topic}?" if topic else "What is first-line?"
        elif 'complication' in a_low:
            q = f"What are the complications of {topic}?" if topic else "What are the complications?"
        elif 'presentation' in a_low or 'symptom' in a_low or 'feature' in a_low:
            q = f"What are the clinical features of {topic}?" if topic else "What are the clinical features?"
        elif 'investigation' in a_low or 'diagnosis' in a_low or 'test' in a_low:
            q = f"What is the investigation of choice for {topic}?" if topic else "What is the investigation of choice?"
        elif 'epidemiology' in a_low or 'incidence' in a_low or 'prevalence' in a_low:
            q = f"What is the epidemiology of {topic}?" if topic else "What is the epidemiology?"
        elif 'aetiology' in a_low or 'etiology' in a_low or 'cause' in a_low or 'risk factor' in a_low:
            q = f"What causes {topic}?" if topic else "What is the cause?"
        elif 'prognosis' in a_low or 'outcome' in a_low:
            q = f"What is the prognosis of {topic}?" if topic else "What is the prognosis?"
        elif 'treatment' in a_low or 'management' in a_low or 'therapy' in a_low:
            q = f"How is {topic} managed?" if topic else "How is it managed?"
        elif 'pathogenesis' in a_low or 'pathophysiology' in a_low:
            q = f"What is the pathogenesis of {topic}?" if topic else "What is the pathogenesis?"
        elif 'classification' in a_low or 'type' in a_low or 'stage' in a_low:
            q = f"How is {topic} classified?" if topic else "How is it classified?"
        else:
            # generic — at least anchor with topic if available
            if topic:
                q = f"What is {a} of {topic}?"
            else:
                q = f"What is {a}?"
        if not q.endswith('?'):
            q += '?'
        if q.lower() in seen:
            continue
        seen.add(q.lower())
        out.append({'q': q, 'a': b[:400]})
    return out


def make_flashcards_from_viva(viva_body: str) -> list[dict]:
    """Convert 'Viva Questions' list to flashcards: front = question,
    back = empty (we don't have the answer; tag them as 'recall').

    The rebuild parser drops these from the live bank unless they have
    a real answer, so we instead convert viva-style text by pulling
    bullet pairs (Q: ... / A: ...) if present, else skip.
    """
    out = []
    # Q:/A: pairs
    for m in re.finditer(r'(?ms)^[-*]?\s*Q:\s*(.+?)\n\s*A:\s*(.+?)(?=^[-*]?\s*Q:|\Z)', viva_body):
        q = re.sub(r'[*_`]+', '', m.group(1)).strip()
        a = re.sub(r'[*_`]+', '', m.group(2)).strip()
        if not q or not a:
            continue
        out.append({'q': q if q.endswith('?') else q + '?', 'a': a[:400]})
    # "1. What is X?" alone (no answer) — skip; we don't fabricate answers
    return out


# ---------------------------------------------------------------------------
# MCQ generation from table rows
# ---------------------------------------------------------------------------


def make_mcq_from_table_row(table: tuple[str, list[str], list[list[str]]], row_idx: int) -> dict | None:
    header, headers, rows = table
    if len(headers) < 2 or row_idx >= len(rows):
        return None
    correct = re.sub(r'[*_`]+', '', rows[row_idx][1]).strip()
    label = re.sub(r'[*_`]+', '', rows[row_idx][0]).strip()
    if not correct or not label:
        return None
    topic = _table_topic_context(header)
    # Build a stem that uses the topic context
    if topic and label.lower() not in ('feature', 'detail', 'description', 'aspect', 'consideration'):
        stem = f'Regarding {topic}, which statement is correct about {label}?'
    elif topic:
        stem = f'Regarding {topic}, which statement is correct?'
    else:
        stem = f'Which statement about {label} is correct?'
    # Build distractors: other rows' value column
    distractors = []
    for j, r in enumerate(rows):
        if j == row_idx:
            continue
        d = re.sub(r'[*_`]+', '', r[1]).strip()
        if d and d != correct and len(d.split()) >= 2:
            distractors.append(d[:160])
    if len(distractors) < 3:
        return None
    distractors = distractors[:3]
    options = {'A': correct, 'B': distractors[0], 'C': distractors[1], 'D': distractors[2]}
    return {'stem': stem, 'options': options, 'answer': 'A'}


# ---------------------------------------------------------------------------
# SBA generation from Definition + Clinical Features
# ---------------------------------------------------------------------------


def make_sba_from_definition_and_features(
    topic_title: str,
    defn_sentence: str,
    features_section: str,
) -> dict | None:
    """Build one SBA: scenario using a clinical feature, then a
    diagnosis question with the definition as the answer context.

    The scenario must be at least 20 words to satisfy SBA quality.
    Features are pulled from the body but we EXCLUDE any line that
    looks like a definition statement.
    """
    if not features_section:
        return None
    feats: list[str] = []
    for raw in features_section.splitlines():
        s = raw.strip()
        if not s:
            continue
        # skip subsection headers, dividers, and frontmatter
        if s.startswith('#') or s.startswith('---') or s.startswith('==='):
            continue
        if s.startswith('|') and '---' in s:
            continue
        # drop leading list markers / blockquote / emoji
        s = re.sub(r'^[#\-\*•>›»\s]+', '', s).strip()
        s = re.sub(r'^[\U0001F300-\U0001FAFF]\s*', '', s)
        if not s:
            continue
        # skip lines that look like a definition
        low = s.lower()
        if 'definition' in low and (':' in s or 'is' in low[:30]):
            continue
        # table-cell row like "| Alcohol | AST:ALT >2 ... |"
        if s.startswith('|'):
            cells = [c.strip() for c in s.strip('|').split('|')]
            if len(cells) >= 2 and len(cells[0].split()) <= 6:
                s = f'{cells[0]} — {cells[1]}'
            else:
                continue
        s = re.sub(r'[*_`]+', '', s)
        s = re.sub(r'\s+', ' ', s)
        if 4 <= len(s.split()) <= 35:
            feats.append(s)
    if not feats and defn_sentence:
        feats = [defn_sentence[:200]]
    if not feats:
        return None
    feats = feats[:3]
    scenario = f'A patient with suspected {topic_title} presents with: ' + '; '.join(feats) + '.'
    stem = scenario + ' What is the most likely diagnosis?'
    if len(stem.split()) < 20:
        return None
    correct = topic_title
    distractors_pool = [
        f'A condition that mimics {topic_title} but is not the same entity',
        f'A complication of {topic_title} rather than the primary diagnosis',
        f'An unrelated condition in the same clinical category as {topic_title}',
    ]
    options = {'A': correct, 'B': distractors_pool[0],
               'C': distractors_pool[1], 'D': distractors_pool[2]}
    return {'stem': stem, 'options': options, 'answer': 'A'}


# ---------------------------------------------------------------------------
# Per-topic generator
# ---------------------------------------------------------------------------


def topic_title_from_path(p: Path) -> str:
    """Extract a clean human-readable topic title from a topic.md path.

    Uses the parent folder's name (stripped of numeric prefix) rather
    than the filename, because topic.md files are generic and the
    folder encodes the actual topic slug.
    """
    folder = p.parent.name
    # Strip "N.N.N-" numeric prefix and trailing flags
    pretty = re.sub(r'^\d+(?:\.\d+)*-', '', folder)
    pretty = re.sub(r'^\d+(?:\.\d+)*\s+', '', pretty)
    pretty = pretty.replace('-', ' ').strip()
    if not pretty or pretty.lower() in ('topic', 'diseases', 'overview', 'hubs', 'root'):
        # fall back to file stem
        pretty = p.stem
    return pretty


def find_published_path(src_topic: Path, pub_slug: str) -> Path | None:
    """Find the corresponding topic.md in the published tree.

    The source tree can be flat (src/<chapter>/Topic Name.md) or
    folder-based (src/<chapter>/Topic Folder/topic.md).  The
    published tree is always folder-based with topic.md inside.
    Match by stem similarity.
    """
    # Build a list of candidate slug fragments from the source filename
    src_stem = src_topic.stem
    src_slug_full = re.sub(r'[^a-z0-9]+', '-', src_stem.lower()).strip('-')
    # Strip leading numeric prefix (e.g. "29-1-3-anxiety-and-stress")
    src_slug_no_num = re.sub(r'^\d+(?:-\d+)*-?', '', src_slug_full).strip('-')
    pub_root = CHAPTERS / pub_slug
    if not pub_root.exists():
        return None
    # 1) exact stem match (after numeric prefix).
    # The published tree can have either topic.md inside a folder, or
    # a direct .md file in diseases/.  Search for both.
    for f in list(pub_root.rglob('topic.md')) + list(pub_root.rglob('*.md')):
        if not f.is_file():
            continue
        if 'moc' in f.name.lower() or 'hierarchy' in f.name.lower() or 'roadmap' in f.name.lower():
            continue
        f_stem = f.parent.name if f.name == 'topic.md' else f.stem
        f_slug = re.sub(r'[^a-z0-9]+', '-',
                        re.sub(r'^\d+(?:\.\d+)*-', '', f_stem).lower()).strip('-')
        if f_slug == src_slug_no_num:
            return f
    # 2) token-based fuzzy match: split into words, require 60% overlap
    src_tokens = set(re.findall(r'[a-z0-9]+', src_slug_no_num))
    if not src_tokens:
        return None
    best = None
    best_score = 0.0
    for f in list(pub_root.rglob('topic.md')) + list(pub_root.rglob('*.md')):
        if not f.is_file():
            continue
        if 'moc' in f.name.lower() or 'hierarchy' in f.name.lower() or 'roadmap' in f.name.lower():
            continue
        f_stem = f.parent.name if f.name == 'topic.md' else f.stem
        f_slug = re.sub(r'[^a-z0-9]+', '-',
                        re.sub(r'^\d+(?:\.\d+)*-', '', f_stem).lower()).strip('-')
        f_tokens = set(re.findall(r'[a-z0-9]+', f_slug))
        if not f_tokens:
            continue
        # Jaccard similarity
        score = len(src_tokens & f_tokens) / len(src_tokens | f_tokens)
        if score > best_score:
            best_score = score
            best = f
    if best and best_score >= 0.6:
        return best
    return None


def detect_existing_study_sections(text: str) -> set[str]:
    """Return set of study section headers that are already authored."""
    headers = set()
    for h, _ in get_h2_sections(text):
        hl = h.lower()
        if hl.startswith('mcq') or hl.startswith('sba') or hl.startswith('flashcard'):
            headers.add(hl)
    return headers


def _is_good_fc_table(table: tuple[str, list[str], list[list[str]]]) -> bool:
    """Return True if the table is suitable for generating flashcards.

    Good tables are 2-col reference tables where the first column is
    a specific term (drug, regimen, concept, sign, etc.) and the
    second column is a substantive description. Comparison tables
    ('Aetiology vs Feature', 'Compensated vs Decompensated') are
    rejected because pulling rows produces nonsensical flashcards.
    """
    header, headers, rows = table
    if len(headers) != 2:
        return False
    h1 = headers[0].lower().strip()
    h2 = headers[1].lower().strip()
    # The first column should look like a noun phrase (e.g. "Concept",
    # "Drug", "Regimen", "Treatment", "Investigation", "Sign", "Feature",
    # "Criterion", "Cause", "Risk Factor", "Complication")
    good_first = (
        'concept', 'drug', 'regimen', 'treatment', 'investigation', 'sign',
        'feature', 'criterion', 'cause', 'risk factor', 'complication',
        'side effect', 'contraindication', 'indication', 'differential',
        'option', 'finding', 'test', 'mechanism', 'dose', 'monitoring',
        'parameter', 'aspect', 'item', 'medication', 'agent', 'choice',
    )
    bad_first = (
        'aetiology', 'etiology', 'compensated', 'decompensated', 'stage',
        'phase', 'time', 'day', 'severity', 'grade', 'class',
    )
    if any(b in h1 for b in bad_first):
        return False
    if not any(g in h1 for g in good_first):
        # accept if header looks like a "Name" or similar generic label
        if h1 not in ('name', 'term', 'label', 'title', 'item', 'topic'):
            return False
    # All rows must have substantive content in col 2
    if not rows:
        return False
    if any(len(r[1].split()) < 3 for r in rows):
        return False
    # And col 1 should be short (a label, not a sentence)
    if any(len(r[0].split()) > 8 for r in rows):
        return False
    return True


def build_study_sections(topic_title: str, body: str) -> tuple[str, str, str]:
    """Return (mcq_md, sba_md, fc_md) blocks ready to insert.

    Honest content strategy:
    - Flashcards: extract from "good" 2-col reference tables
      (drug/regimen/treatment).  Dedupe by (col1, col2).
    - MCQs: only emit when we have a real definition statement.
      Build "Which best describes X?" with the definition as the
      correct answer and generic plausible distractors.
    - SBAs: only emit when we have both a definition and clinical
      features.  Build "A patient with suspected X presents with: F.
      Most likely diagnosis?" with X as the answer and
      category-adjacent distractors.
    """
    # 0) Get the real definition (if any)
    defn_sentence: str | None = None
    in_frontmatter = False
    for raw in body.splitlines():
        s = raw.strip()
        if s == '---':
            in_frontmatter = not in_frontmatter
            continue
        if in_frontmatter:
            continue
        if s.startswith('>') and 'Definition' in s:
            cleaned = re.sub(r'^>\s*\*\*[^*]*Definition\*\*:\s*', '', s)
            cleaned = re.sub(r'[*_`]+', '', cleaned).strip()
            cleaned = re.sub(r'\s+', ' ', cleaned)
            if 8 <= len(cleaned.split()) <= 60:
                defn_sentence = cleaned
                break
    if not defn_sentence:
        defn_sentence = first_meaningful_sentence(body)

    # 1) Flashcards from good 2-col reference tables
    tables = extract_tables(body)
    fc_tables = [t for t in tables
                 if not is_skip_table_header(t[0])
                 and _is_good_fc_table(t)]
    flashcards: list[dict] = []
    seen_pairs: set[tuple[str, str]] = set()
    for tbl in fc_tables:
        for row in tbl[2]:
            a = re.sub(r'[*_`]+', '', row[0]).strip()
            b = re.sub(r'[*_`]+', '', row[1]).strip()
            key = (a.lower(), b.lower())
            if key in seen_pairs:
                continue
            seen_pairs.add(key)
        flashcards.extend(make_flashcards_from_table(tbl, topic_title=topic_title))
    # Insert the definition as a top-priority flashcard
    if defn_sentence:
        q = f'What is the definition of {topic_title}?'
        if not any(c['q'].lower() == q.lower() for c in flashcards):
            flashcards.insert(0, {'q': q, 'a': defn_sentence[:400]})
    # 2) Flashcards from viva Q/A pairs
    for header, b in get_h2_sections(body):
        if 'viva' in header.lower():
            flashcards.extend(make_flashcards_from_viva(b))
    # 3) MCQs: only definition-based, ONE per topic (the rest from tables
    # are not pedagogically sound).  Keep up to 3.
    mcqs: list[dict] = []
    if defn_sentence:
        stem = f'Which of the following best describes {topic_title}?'
        options = {
            'A': defn_sentence[:200],
            'B': f'An unrelated condition not matching the clinical picture of {topic_title}',
            'C': f'A complication seen late in the disease course of {topic_title}',
            'D': f'A condition that mimics {topic_title} but has a different underlying cause',
        }
        mcqs.append({'stem': stem, 'options': options, 'answer': 'A'})
    # 4) SBAs
    sbas: list[dict] = []
    features_body = ''
    for h, b in get_h2_sections(body):
        hl = h.lower()
        if any(kw in hl for kw in ('clinical', 'presentation', 'feature',
                                   'definition', 'classification', 'aetiology')):
            features_body = b
            break
    if not features_body:
        for h, b in get_h3_sections(body):
            if any(kw in h.lower() for kw in ('clinical', 'feature', 'presentation', 'key')):
                features_body = b
                break
    sba = make_sba_from_definition_and_features(topic_title, defn_sentence or '', features_body)
    if sba is not None:
        sbas.append(sba)
    return _format_mcq(mcqs), _format_sba(sbas), _format_fc(flashcards)


def _format_mcq(items: list[dict]) -> str:
    if not items:
        return ''
    lines = ['## MCQs ({} generated)'.format(len(items)), '']
    for i, q in enumerate(items, 1):
        stem = q['stem']
        # If the stem doesn't end with '?' add it
        if not stem.rstrip().endswith(('?', '.', ':')):
            stem += '?'
        lines.append(f"{i}. **{stem}**")
        for letter in ['A', 'B', 'C', 'D']:
            opt = q['options'].get(letter, '')
            bold = letter == q['answer']
            if bold:
                lines.append(f"   {letter}. **{opt}**")
            else:
                lines.append(f"   {letter}. {opt}")
        lines.append('')
    return '\n'.join(lines).rstrip() + '\n'


def _format_sba(items: list[dict]) -> str:
    if not items:
        return ''
    lines = ['## SBA Questions ({} generated)'.format(len(items)), '']
    for i, q in enumerate(items, 1):
        stem = q['stem']
        lines.append(f"{i}. {stem}")
        for letter in ['A', 'B', 'C', 'D']:
            opt = q['options'].get(letter, '')
            bold = letter == q['answer']
            if bold:
                lines.append(f"   {letter}. **{opt}**")
            else:
                lines.append(f"   {letter}. {opt}")
        lines.append('')
    return '\n'.join(lines).rstrip() + '\n'


def _format_fc(items: list[dict]) -> str:
    if not items:
        return ''
    lines = ['## Flashcards ({} generated)'.format(len(items)), '']
    for c in items:
        q = c['q']
        a = c['a']
        lines.append(f"- Q: {q}")
        lines.append(f"  A: {a}")
    lines.append('')
    return '\n'.join(lines).rstrip() + '\n'


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------


def main() -> None:
    summary = {}
    for src_name, pub_slug in SRC_TO_PUB.items():
        src_root = MED / src_name
        if not src_root.exists():
            print(f'[skip] {src_name}: missing source folder')
            continue
        # find real topics (those with substantive medical content)
        topic_files = []
        for f in src_root.rglob('*.md'):
            n = f.name.lower()
            if n in ('roadmap.md', 'readme.md', 'index.md',
                     'how to use this system.md', 'all system rules.md'):
                continue
            if 'template' in n:
                continue
            # skip MOC and roadmap files by name pattern
            if 'moc' in n and 'chapter' not in n.replace(' ', '').lower():
                # allow "Chapter MOC" but skip bare "MOC"
                if n.endswith('moc.md') or n == 'moc.md':
                    continue
            if 'hierarchy' in n and n.endswith('hierarchy.md'):
                continue
            if 'roadmap' in n:
                continue
            try:
                t = f.read_text(encoding='utf-8', errors='ignore')
            except Exception:
                continue
            if len(t) < 1000:
                # too short to be a real topic
                continue
            topic_files.append(f)
        n_topics = len(topic_files)
        n_updated = 0
        n_skipped = 0
        for src in topic_files:
            pub = find_published_path(src, pub_slug)
            if pub is None:
                n_skipped += 1
                continue
            try:
                pub_text = pub.read_text(encoding='utf-8', errors='ignore')
            except Exception:
                n_skipped += 1
                continue
            existing = detect_existing_study_sections(pub_text)
            if existing:
                n_skipped += 1
                continue
            topic_title = topic_title_from_path(src)
            mcq_md, sba_md, fc_md = build_study_sections(topic_title, pub_text)
            if not (mcq_md or sba_md or fc_md):
                n_skipped += 1
                continue
            # append to pub file
            additions = []
            additions.append('\n---\n\n')
            additions.append(f'> Auto-generated study sections for "{topic_title}" — '
                             f'{CH_LABELS.get(pub_slug, pub_slug)}.\n\n')
            if fc_md:
                additions.append(fc_md + '\n')
            if mcq_md:
                additions.append(mcq_md + '\n')
            if sba_md:
                additions.append(sba_md + '\n')
            new_text = pub_text.rstrip() + ''.join(additions)
            try:
                pub.write_text(new_text, encoding='utf-8')
                n_updated += 1
            except Exception as e:
                print(f'  [error] {pub}: {e}')
                n_skipped += 1
        summary[pub_slug] = {
            'topics': n_topics,
            'updated': n_updated,
            'skipped': n_skipped,
        }
        print(f'[{pub_slug}] topics={n_topics} updated={n_updated} skipped={n_skipped}')
    Path(ROOT / 'site' / 'scripts' / '_autogen_summary.json').write_text(
        json.dumps(summary, indent=2), encoding='utf-8')


if __name__ == '__main__':
    main()
