#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import html
import importlib.util
import json
import re
from pathlib import Path

ROOT = Path('/mnt/tb/Sea-knowledge/#MedSea')
SITE = ROOT / 'site' / 'assets'
BUILD_SITE = ROOT / 'scripts' / 'site' / 'build_site.py'

spec = importlib.util.spec_from_file_location('build_site_mod', BUILD_SITE)
assert spec and spec.loader, f'Unable to load {BUILD_SITE}'
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)


OPT_RE = re.compile(r'^\s*([A-E])\.\s*(.+?)\s*$')
NUM_BLOCK_RE = re.compile(r'(?m)^(?=\d+\.\s+)')
MD_BOLD_RE = re.compile(r'\*\*(.+?)\*\*')
TAG_RE = re.compile(r'<[^>]+>')


def strip_md(s: str) -> str:
    if not s:
        return ''
    s = html.unescape(s)
    s = TAG_RE.sub('', s)
    s = s.replace('**', '').replace('__', '').replace('`', '')
    s = re.sub(r'\[(.*?)\]\([^)]*\)', r'\1', s)
    s = re.sub(r'\s+', ' ', s).strip()
    return s


def slug_title(slug: str) -> str:
    return slug.replace('-', ' ').title()


def extract_section(md: str, wanted_prefixes: list[str]) -> str:
    lines = md.splitlines()
    capture = False
    buf: list[str] = []
    wanted = [w.lower() for w in wanted_prefixes]
    for line in lines:
        if line.startswith('## '):
            name = line[3:].strip().lower()
            if capture:
                break
            if any(name.startswith(w) for w in wanted):
                capture = True
                continue
        elif capture and line.startswith('#'):
            break
        if capture:
            buf.append(line)
    return '\n'.join(buf).strip()


def extract_answer_keys(md: str) -> tuple[dict[int, str], dict[int, str]]:
    mcq_keys: dict[int, str] = {}
    sba_keys: dict[int, str] = {}
    section = extract_section(md, ['Answer Key with Explanations', 'Answers', 'Answer Key'])
    if not section:
        return mcq_keys, sba_keys
    current = None
    for raw in section.splitlines():
        line = raw.strip()
        if not line:
            continue
        low = line.lower()
        if low.startswith('### mcq'):
            current = 'mcq'
            continue
        if low.startswith('### sba'):
            current = 'sba'
            continue
        m = re.match(r'^(\d+)\.\s*\**([A-E])\**\s*[—-]', line)
        if m and current:
            n = int(m.group(1))
            ans = m.group(2)
            if current == 'mcq':
                mcq_keys[n] = ans
            else:
                sba_keys[n] = ans
    return mcq_keys, sba_keys


def normalize_mcq_stem(stem: str) -> str:
    stem = re.sub(r'^Q:\s*', '', stem, flags=re.I).strip()
    return stem


def is_contextless_mcq(stem: str) -> bool:
    s = stem.strip().lower()
    bad = {
        'what is the first-line treatment?',
        'what is the most important complication?',
        'what is the diagnosis?',
        'what is the treatment?',
        'what is the best investigation?',
    }
    return s in bad


def parse_mcqs(section: str, answer_keys: dict[int, str]) -> list[dict]:
    out: list[dict] = []
    if not section.strip():
        return out
    blocks = re.split(NUM_BLOCK_RE, section.strip())
    for block in blocks:
        block = block.strip()
        if not re.match(r'^\d+\.\s+', block):
            continue
        lines = [ln.rstrip() for ln in block.splitlines() if ln.strip()]
        m0 = re.match(r'^(\d+)\.\s+(.*)$', lines[0])
        if not m0:
            continue
        qnum = int(m0.group(1))
        stem = normalize_mcq_stem(strip_md(m0.group(2)))
        options: dict[str, str] = {}
        answer = answer_keys.get(qnum, '')
        for ln in lines[1:]:
            m = OPT_RE.match(ln)
            if m:
                label = m.group(1)
                text = strip_md(m.group(2))
                options[label] = text
                # bolded correct option pattern inside question block
                if '**' in ln and not answer:
                    answer = label
                continue
            if 'Answer:' in ln and not answer:
                am = re.search(r'Answer:\s*([A-E])', ln, re.I)
                if am:
                    answer = am.group(1).upper()
        if len(options) < 4:
            continue
        if answer not in options:
            continue
        if len(stem.split()) < 5:
            continue
        if is_contextless_mcq(stem):
            continue
        out.append({'qnum': qnum, 'stem': stem, 'options': options, 'answer': answer})
    return out


def parse_sbas(section: str, answer_keys: dict[int, str]) -> list[dict]:
    out: list[dict] = []
    if not section.strip():
        return out
    blocks = re.split(NUM_BLOCK_RE, section.strip())
    for block in blocks:
        block = block.strip()
        if not re.match(r'^\d+\.\s+', block):
            continue
        lines = [ln.rstrip() for ln in block.splitlines() if ln.strip()]
        m0 = re.match(r'^(\d+)\.\s+(.*)$', lines[0])
        if not m0:
            continue
        qnum = int(m0.group(1))
        stem = strip_md(m0.group(2))
        options: dict[str, str] = {}
        answer = answer_keys.get(qnum, '')
        for ln in lines[1:]:
            m = OPT_RE.match(ln)
            if m:
                label = m.group(1)
                text = strip_md(m.group(2))
                options[label] = text
                if '**' in ln and not answer:
                    answer = label
                continue
            if 'Answer:' in ln and not answer:
                am = re.search(r'Answer:\s*([A-E])', ln, re.I)
                if am:
                    answer = am.group(1).upper()
        if len(options) < 4:
            continue
        if answer not in options:
            continue
        # SBA should be an actual scenario/question, not a stub
        if len(stem.split()) < 10:
            continue
        out.append({'qnum': qnum, 'stem': stem, 'options': options, 'answer': answer})
    return out


def normalize_flash_front(q: str) -> str:
    q = re.sub(r'^Q:\s*', '', q, flags=re.I).strip()
    q = q.replace('**', '').strip()
    if q.endswith('?'):
        return q
    low = q.lower()
    plural_markers = (
        'criteria', 'features', 'signs', 'symptoms', 'causes', 'complications',
        'indications', 'contraindications', 'drugs', 'steps', 'stages', 'types',
        'findings', 'risk factors', 'principles', 'uses', 'options'
    )
    if low.endswith(' list'):
        base = q[:-5].strip()
        return f'What are the {base}?' if base else 'What are the key items?'
    if any(low.endswith(x) for x in plural_markers):
        return f'What are the {q}?'
    if low.startswith(('how ', 'why ', 'when ', 'which ', 'what ', 'name ', 'list ', 'define ', 'describe ')):
        return q if q.endswith('?') else q + '?'
    return f'What is {q}?'


def parse_flashcards(section: str) -> list[dict]:
    out: list[dict] = []
    if not section.strip():
        return out
    patterns = [
        re.compile(r'(?ms)^[-*]\s*Q:\s*(.+?)\n\s*A:\s*(.+?)(?=^[-*]\s*Q:|\Z)'),
        re.compile(r'(?ms)^\*\*Q:\s*(.+?)\*\*\s*\nA:\s*(.+?)(?=^\*\*Q:|\Z)'),
    ]
    seen = set()
    for pat in patterns:
        for q, a in pat.findall(section.strip()):
            q2 = normalize_flash_front(strip_md(q))
            a2 = strip_md(a)
            if len(q2.split()) < 3 or len(a2.split()) < 2:
                continue
            key = (q2.lower(), a2.lower())
            if key in seen:
                continue
            seen.add(key)
            out.append({'q': q2, 'a': a2})
    return out


def qid(prefix: str, ch: int, topic_slug: str, idx: int, stem: str) -> str:
    return hashlib.sha1(f'{prefix}|{ch}|{topic_slug}|{idx}|{stem}'.encode('utf-8')).hexdigest()[:12]


def build() -> tuple[list, list, list, dict]:
    mcq_rows = []
    sba_rows = []
    flash_rows = []
    chapter_counts: dict[int, dict] = {}

    for ch_slug, (ch_name, _url, _color) in mod.BUILT_CHAPTERS.items():
        chapter_dir = ROOT / 'chapters' / ch_slug
        if not chapter_dir.exists():
            continue
        for t in mod.find_files(chapter_dir):
            md_path = t.get('md')
            if not md_path or not Path(md_path).exists():
                continue
            md = Path(md_path).read_text(encoding='utf-8', errors='ignore')
            mcq_keys, sba_keys = extract_answer_keys(md)
            mcqs = parse_mcqs(extract_section(md, ['MCQs']), mcq_keys)
            sbas = parse_sbas(extract_section(md, ['SBA Questions', 'SBAs']), sba_keys)
            fcs = parse_flashcards(extract_section(md, ['Flashcards']))
            if not (mcqs or sbas or fcs):
                continue

            ch_num = int(ch_slug.split('-', 1)[0])
            ch_clean = ch_name.replace('Medicine & ', '').replace('Clinical ', 'Clinical ')
            topic_slug = t['slug']
            topic_title = slug_title(topic_slug)
            counts = chapter_counts.setdefault(ch_num, {
                'num': ch_num, 'name': ch_name, 'slug': ch_slug,
                'mcq_count': 0, 'sba_count': 0, 'flashcard_count': 0,
            })

            for i, q in enumerate(mcqs, 1):
                row = {
                    'id': qid('mcq', ch_num, topic_slug, i, q['stem']),
                    'chapter_num': ch_num,
                    'chapter_name': ch_name,
                    'chapter_slug': ch_slug,
                    'topic_slug': topic_slug,
                    'topic_title': topic_title,
                    'question': q['stem'],
                    'options': q['options'],
                    'answer': q['answer'],
                    'source': 'authored',
                }
                mcq_rows.append(row)
                counts['mcq_count'] += 1

            for i, q in enumerate(sbas, 1):
                row = {
                    'id': qid('sba', ch_num, topic_slug, i, q['stem']),
                    'chapter_num': ch_num,
                    'chapter_name': ch_name,
                    'chapter_slug': ch_slug,
                    'topic_slug': topic_slug,
                    'topic_title': topic_title,
                    'question': q['stem'],
                    'options': q['options'],
                    'answer': q['answer'],
                    'source': 'authored',
                }
                sba_rows.append(row)
                counts['sba_count'] += 1

            for i, c in enumerate(fcs, 1):
                row = {
                    'id': qid('fc', ch_num, topic_slug, i, c['q']),
                    'chapter_num': ch_num,
                    'chapter_name': ch_name,
                    'chapter_slug': ch_slug,
                    'topic_slug': topic_slug,
                    'topic_title': topic_title,
                    'front': c['q'],
                    'back': c['a'],
                    'source': 'authored',
                }
                flash_rows.append(row)
                counts['flashcard_count'] += 1

    index = {
        'version': 4,
        'generated_from': 'authored topic.md sections only',
        'totals': {
            'mcq': len(mcq_rows),
            'sba': len(sba_rows),
            'flashcard': len(flash_rows),
            'chapters': len(chapter_counts),
        },
        'chapters': [chapter_counts[k] for k in sorted(chapter_counts)],
    }
    return mcq_rows, sba_rows, flash_rows, index


def main() -> None:
    mcq, sba, flash, index = build()
    (SITE / 'questions-mcq.json').write_text(json.dumps(mcq, ensure_ascii=False, separators=(',', ':')), encoding='utf-8')
    (SITE / 'questions-sba.json').write_text(json.dumps(sba, ensure_ascii=False, separators=(',', ':')), encoding='utf-8')
    (SITE / 'questions-flashcard.json').write_text(json.dumps(flash, ensure_ascii=False, separators=(',', ':')), encoding='utf-8')
    (SITE / 'questions-index.json').write_text(json.dumps(index, ensure_ascii=False, separators=(',', ':')), encoding='utf-8')
    print(json.dumps(index['totals'], indent=2))


if __name__ == '__main__':
    main()
