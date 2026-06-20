#!/usr/bin/env python3
from __future__ import annotations

import html
import importlib.util
import re
from pathlib import Path

ROOT = Path('/mnt/tb/Sea-knowledge/#MedSea')
SITE = ROOT / 'site'
BUILD_SITE = ROOT / 'scripts/site/build_site.py'

spec = importlib.util.spec_from_file_location('build_site_mod', BUILD_SITE)
assert spec and spec.loader, f'Unable to load {BUILD_SITE}'
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)


def esc(s: str) -> str:
    return html.escape(s or '', quote=True)


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


def parse_mcqs(section: str) -> list[dict]:
    out = []
    blocks = re.split(r'(?m)^(?=\d+\.\s+)', section.strip())
    for block in blocks:
        block = block.strip()
        if not re.match(r'^\d+\.\s+', block):
            continue
        lines = [ln.rstrip() for ln in block.splitlines() if ln.strip()]
        stem = re.sub(r'^\d+\.\s+', '', lines[0]).strip()
        options = []
        answer = ''
        for ln in lines[1:]:
            if re.match(r'^\s*[A-Z]\)', ln):
                options.append(ln.strip())
            elif 'Answer:' in ln:
                answer = re.sub(r'^\*\*Answer:\s*', '', ln).replace('**', '').strip()
        out.append({'stem': stem, 'options': options, 'answer': answer})
    return out


def parse_sbas(section: str) -> list[dict]:
    out = []
    for ln in section.splitlines():
        ln = ln.strip()
        m = re.match(r'^(\d+)\.\s+(.*?)\s*\|\s*(.+)$', ln)
        if m:
            out.append({'stem': m.group(2).strip(), 'answer': m.group(3).strip()})
    return out


def parse_flashcards(section: str) -> list[dict]:
    out = []
    pat = re.compile(r'(?ms)^\*\*Q:\s*(.+?)\*\*\s*\nA:\s*(.+?)(?=^\*\*Q:|\Z)')
    for q, a in pat.findall(section.strip()):
        out.append({'q': q.strip(), 'a': a.strip()})
    return out


def collect_data() -> list[dict]:
    chapters = []
    for ch_slug, (ch_name, _url, _color) in mod.BUILT_CHAPTERS.items():
        chapter_dir = ROOT / 'chapters' / ch_slug
        if not chapter_dir.exists():
            continue
        topics = mod.find_files(chapter_dir)
        topic_items = []
        for t in topics:
            md_path = t.get('md')
            if not md_path or not Path(md_path).exists():
                continue
            md = Path(md_path).read_text(encoding='utf-8', errors='ignore')
            mcqs = parse_mcqs(extract_section(md, ['MCQs']))
            sbas = parse_sbas(extract_section(md, ['SBA Questions', 'SBAs']))
            flashcards = parse_flashcards(extract_section(md, ['Flashcards']))
            if not (mcqs or sbas or flashcards):
                continue
            topic_title = t['slug'].replace('-', ' ').title()
            topic_items.append({
                'topic': t['local_prefix'],
                'title': topic_title,
                'href': f"/{ch_slug}/?topic={t['local_prefix']}",
                'mcqs': mcqs,
                'sbas': sbas,
                'flashcards': flashcards,
            })
        chapters.append({
            'slug': ch_slug,
            'name': ch_name,
            'topics': topic_items,
            'mcq_count': sum(len(x['mcqs']) for x in topic_items),
            'sba_count': sum(len(x['sbas']) for x in topic_items),
            'flashcard_count': sum(len(x['flashcards']) for x in topic_items),
        })
    return [c for c in chapters if c['topics']]


TOOLS_CSS = """
<style>
.tools-hero{background:var(--bg-2);border:1px solid var(--border);border-radius:14px;padding:18px 18px 14px;margin-bottom:16px}
.tools-hero h1{font-size:28px;margin:0 0 8px}
.tools-hero p{color:var(--text-dim);margin:0}
.tools-filter{display:flex;gap:10px;flex-wrap:wrap;align-items:center;margin:16px 0 18px}
.tools-filter input{flex:1;min-width:240px;background:var(--bg-3);border:1px solid var(--border);color:var(--text);padding:10px 12px;border-radius:8px;font-size:14px;outline:none}
.tools-filter input:focus{border-color:var(--accent);box-shadow:0 0 0 2px rgba(56,189,248,.18)}
.tools-filter .meta{color:var(--text-dim);font-size:12px}
.chapter-tool{background:var(--bg-2);border:1px solid var(--border);border-radius:12px;margin-bottom:12px;overflow:hidden}
.chapter-tool summary{cursor:pointer;list-style:none;padding:14px 16px;display:flex;gap:12px;align-items:center;background:var(--bg-2)}
.chapter-tool summary::-webkit-details-marker{display:none}
.chapter-tool summary:hover{background:var(--bg-3)}
.chapter-tool .arrow{color:var(--accent);width:14px;display:inline-block}
.chapter-tool[open] .arrow{transform:rotate(90deg)}
.chapter-tool .title{flex:1;font-weight:700}
.chapter-tool .counts{display:flex;gap:8px;flex-wrap:wrap}
.chapter-tool .counts span,.tool-chip{background:var(--bg-3);border:1px solid var(--border);border-radius:999px;padding:3px 8px;font-size:11px;color:var(--text-dim)}
.topic-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(300px,1fr));gap:12px;padding:0 12px 12px}
.topic-tool{background:var(--bg);border:1px solid var(--border);border-radius:10px;padding:12px}
.topic-tool h3{font-size:15px;line-height:1.35;margin:0 0 8px}
.topic-tool h3 a{color:var(--text);text-decoration:none}
.topic-tool h3 a:hover{color:var(--accent)}
.topic-tool .chips{display:flex;gap:6px;flex-wrap:wrap;margin-bottom:10px}
.preview-block{background:var(--bg-3);border:1px solid var(--border);border-radius:8px;padding:10px;margin-top:8px}
.preview-block .label{font-size:11px;color:var(--accent);text-transform:uppercase;letter-spacing:.08em;margin-bottom:6px}
.preview-block ol{margin:0;padding-left:18px}
.preview-block li{margin:4px 0}
.preview-block p{margin:0;color:var(--text-dim)}
.flash-card{background:var(--bg-3);border:1px solid var(--border);border-radius:8px;padding:10px;margin-top:8px}
.flash-card .q{font-weight:700;margin-bottom:6px}
.flash-card .a{color:var(--text-dim)}
.topic-tool.hidden,.chapter-tool.hidden{display:none!important}
@media (max-width:900px){.tools-hero h1{font-size:22px}.topic-grid{grid-template-columns:1fr;padding:0 8px 8px}.chapter-tool summary{padding:12px}.tools-filter{margin:12px 0 14px}.tools-filter input{min-width:0;width:100%}}
</style>
"""


FILTER_JS = """
<script>
(function(){
  const input = document.getElementById('toolFilter');
  if(!input) return;
  input.addEventListener('input', function(){
    const q = input.value.trim().toLowerCase();
    document.querySelectorAll('.topic-tool').forEach(card => {
      const hit = !q || (card.dataset.search || '').includes(q);
      card.classList.toggle('hidden', !hit);
    });
    document.querySelectorAll('.chapter-tool').forEach(ch => {
      const visibleTopics = ch.querySelectorAll('.topic-tool:not(.hidden)').length;
      ch.classList.toggle('hidden', visibleTopics === 0 && !!q);
    });
  });
})();
</script>
"""


def chapter_summary_line(ch: dict, kind: str) -> str:
    if kind == 'exam':
        return f"<span>{ch['mcq_count']} MCQs</span><span>{ch['sba_count']} SBAs</span><span>{len(ch['topics'])} topics</span>"
    return f"<span>{ch['flashcard_count']} flashcards</span><span>{len(ch['topics'])} topics</span>"


def render_exam_page(chapters: list[dict]) -> str:
    topic_count = sum(len(c['topics']) for c in chapters)
    mcq_count = sum(c['mcq_count'] for c in chapters)
    sba_count = sum(c['sba_count'] for c in chapters)
    stats = [(len(chapters), 'Chapters'), (topic_count, 'Topics'), (mcq_count, 'MCQs'), (sba_count, 'SBAs')]
    html_out = [mod.page_header('Exam Bank', stats=stats), TOOLS_CSS]
    html_out.append('<section class="tools-hero"><h1>Exam Bank</h1><p>All chapter exam material in one place. Browse by chapter, preview the first MCQ/SBA, then open the full topic note.</p></section>')
    html_out.append(f'<div class="tools-filter"><input id="toolFilter" type="text" placeholder="Filter chapter or topic…"><div class="meta">{len(chapters)} chapters · {topic_count} topics · {mcq_count} MCQs · {sba_count} SBAs</div></div>')
    for ch in chapters:
        html_out.append(f'<details class="chapter-tool" data-search="{esc((ch["name"] + " " + ch["slug"]).lower())}"><summary><span class="arrow">▸</span><span class="title">{esc(ch["name"])}</span><span class="counts">{chapter_summary_line(ch, "exam")}</span></summary><div class="topic-grid">')
        for topic in ch['topics']:
            search_text = f"{ch['name']} {topic['topic']} {topic['title']}".lower()
            html_out.append(f'<article class="topic-tool" data-search="{esc(search_text)}"><h3><a href="{esc(topic["href"])}">{esc(topic["topic"])} · {esc(topic["title"])} ↗</a></h3><div class="chips"><span class="tool-chip">{len(topic["mcqs"])} MCQs</span><span class="tool-chip">{len(topic["sbas"])} SBAs</span><span class="tool-chip">{len(topic["flashcards"])} flashcards</span></div>')
            if topic['mcqs']:
                first = topic['mcqs'][0]
                html_out.append(f'<div class="preview-block"><div class="label">MCQ preview</div><p>{esc(first["stem"])}</p><ol>' + ''.join(f'<li>{esc(opt)}</li>' for opt in first['options'][:4]) + '</ol></div>')
            if topic['sbas']:
                first_sba = topic['sbas'][0]
                html_out.append(f'<div class="preview-block"><div class="label">SBA preview</div><p>{esc(first_sba["stem"])}</p><p style="margin-top:6px"><strong>Key:</strong> {esc(first_sba["answer"])}</p></div>')
            html_out.append('</article>')
        html_out.append('</div></details>')
    html_out.append(FILTER_JS)
    html_out.append(mod.page_footer())
    return ''.join(html_out)


def render_flashcards_page(chapters: list[dict]) -> str:
    topic_count = sum(len(c['topics']) for c in chapters)
    flash_count = sum(c['flashcard_count'] for c in chapters)
    stats = [(len(chapters), 'Chapters'), (topic_count, 'Topics'), (flash_count, 'Cards')]
    html_out = [mod.page_header('Flashcards', stats=stats), TOOLS_CSS]
    html_out.append('<section class="tools-hero"><h1>Flashcards</h1><p>All chapter flashcards in one place. Browse by chapter, scan rapid recall cards, then open the full topic note when needed.</p></section>')
    html_out.append(f'<div class="tools-filter"><input id="toolFilter" type="text" placeholder="Filter chapter or topic…"><div class="meta">{len(chapters)} chapters · {topic_count} topics · {flash_count} flashcards</div></div>')
    for ch in chapters:
        html_out.append(f'<details class="chapter-tool" data-search="{esc((ch["name"] + " " + ch["slug"]).lower())}"><summary><span class="arrow">▸</span><span class="title">{esc(ch["name"])}</span><span class="counts">{chapter_summary_line(ch, "flash")}</span></summary><div class="topic-grid">')
        for topic in ch['topics']:
            if not topic['flashcards']:
                continue
            search_text = f"{ch['name']} {topic['topic']} {topic['title']}".lower()
            html_out.append(f'<article class="topic-tool" data-search="{esc(search_text)}"><h3><a href="{esc(topic["href"])}">{esc(topic["topic"])} · {esc(topic["title"])} ↗</a></h3><div class="chips"><span class="tool-chip">{len(topic["flashcards"])} flashcards</span><span class="tool-chip">{len(topic["mcqs"])} MCQs</span><span class="tool-chip">{len(topic["sbas"])} SBAs</span></div>')
            for card in topic['flashcards'][:4]:
                html_out.append(f'<div class="flash-card"><div class="q">Q: {esc(card["q"])}</div><div class="a">A: {esc(card["a"])}</div></div>')
            if len(topic['flashcards']) > 4:
                html_out.append(f'<div class="preview-block"><p>+ {len(topic["flashcards"]) - 4} more flashcards in the full topic note.</p></div>')
            html_out.append('</article>')
        html_out.append('</div></details>')
    html_out.append(FILTER_JS)
    html_out.append(mod.page_footer())
    return ''.join(html_out)


def main() -> None:
    chapters = collect_data()
    (SITE / 'exam').mkdir(parents=True, exist_ok=True)
    (SITE / 'flashcards').mkdir(parents=True, exist_ok=True)
    (SITE / 'exam' / 'index.html').write_text(render_exam_page(chapters), encoding='utf-8')
    (SITE / 'flashcards' / 'index.html').write_text(render_flashcards_page(chapters), encoding='utf-8')
    print(f'wrote exam page for {len(chapters)} chapters')
    print(f'wrote flashcards page for {len(chapters)} chapters')


if __name__ == '__main__':
    main()
