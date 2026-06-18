#!/usr/bin/env python3
"""Generate MedSea static website.

Scans chapters/, copies all PNG/MD files into site/diseases/, generates HTML pages.
Output: /mnt/tb/Sea-knowledge/#MedSea/site/
"""
import json
import re
import shutil
from pathlib import Path
from datetime import datetime
from urllib.parse import quote

REPO_ROOT = Path("/mnt/tb/Sea-knowledge/#MedSea")
SITE = REPO_ROOT / "site"

# Chapter metadata: (slug, display_name, notion_url, description, accent_color)
CHAPTERS = [
    ("15-nephrology-urology", "Nephrology and Urology",
     "https://app.notion.com/p/SeaHub/Chapter-15-Nephrology-and-Urology-d29e1888740b4d809dd1b0cab7616c05",
     "Renal anatomy, AKI/CKD, glomerular disease, UTI, dialysis.",
     "#06b6d4"),
    ("16-cardiology", "Cardiology",
     "https://app.notion.com/p/SeaHub/Chapter-16-Cardiology-0bfc7d3c798a450fb5c0ac1bf3848da2",
     "ACS, arrhythmias, heart failure, valvular, hypertension, pericardial.",
     "#ef4444"),
    ("17-respiratory-medicine", "Respiratory Medicine",
     "https://app.notion.com/p/SeaHub/Chapter-17-Respiratory-medicine-d4fe7d456ca4481581e806ebe9e177cf",
     "Airway disease, infection, pleural, ILD, respiratory failure, malignancy.",
     "#10b981"),
    ("18-endocrinology", "Endocrinology",
     "https://app.notion.com/p/SeaHub/Chapter-18-Endocrinology-9db6455d6ae840f0ac29129217d6ccef",
     "Pituitary, thyroid, adrenal, parathyroid, reproductive, MEN, NETs.",
     "#a855f7"),
    ("21-gastroenterology", "Gastroenterology",
     "https://app.notion.com/p/SeaHub/Chapter-21-Gastroenterology-bbfd97790eca482eaed8d47428a642b2",
     "Oesophageal, gastric, IBD, colorectal, pancreatic, malabsorption.",
     "#f59e0b"),
]


def find_files(chapter_dir):
    diseases_dir = chapter_dir / "diseases"
    if not diseases_dir.exists():
        return []
    topics = []
    for sub in sorted(diseases_dir.iterdir()):
        if not sub.is_dir():
            continue
        m = re.match(r"^(\d+\.\d+)\.(\d+)-(.+)$", sub.name)
        if not m:
            continue
        hub_num, idx, slug = m.group(1), m.group(2), m.group(3)
        local_prefix = f"{hub_num}.{idx}"
        md_f = sub / "topic.md"
        png_f = sub / "topic.png"
        html_f = sub / "topic.html"
        if not md_f.exists():
            md_f = sub / f"{slug}.md"
        if not png_f.exists():
            png_f = sub / f"{slug}.png"
        if not html_f.exists():
            html_f = sub / f"{slug}.html"
        topics.append({
            "hub_num": hub_num, "local_prefix": local_prefix, "slug": slug,
            "md": md_f if md_f.exists() else None,
            "png": png_f if png_f.exists() else None,
            "html": html_f if html_f.exists() else None,
            "folder": sub.name,
        })
    for f in sorted(diseases_dir.iterdir()):
        if not f.is_file():
            continue
        m = re.match(r"^(\d+\.\d+)\.(\d+)-(.+)\.(md|png|html)$", f.name)
        if not m:
            continue
        hub_num, idx, slug, ext = m.group(1), m.group(2), m.group(3), m.group(4)
        local_prefix = f"{hub_num}.{idx}"
        existing = next((t for t in topics if t["local_prefix"] == local_prefix), None)
        if existing:
            existing[ext] = f
        else:
            topics.append({
                "hub_num": hub_num, "local_prefix": local_prefix, "slug": slug,
                "md": f if ext == "md" else None,
                "png": f if ext == "png" else None,
                "html": f if ext == "html" else None,
                "folder": None,
            })
    return topics


def load_hub_info(chapter_dir):
    manifest_path = chapter_dir / "manifest.json"
    hub_meta = {}
    if manifest_path.exists():
        m = json.loads(manifest_path.read_text())
        for h in m.get("hubs", []):
            hub_meta[h["num"]] = h.get("name", h["num"])
    return hub_meta


PAGE_CSS = """
:root {
  --bg: #0a0e1a;
  --bg-2: #111827;
  --bg-3: #1f2937;
  --border: #2d3748;
  --text: #e5e7eb;
  --text-dim: #9ca3af;
  --accent: #38bdf8;
  --code-bg: #0f172a;
}
* { box-sizing: border-box; margin: 0; padding: 0; }
body {
  background: linear-gradient(135deg, #0a0e1a 0%, #0f1729 100%);
  color: var(--text);
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'SF Pro Text', system-ui, sans-serif;
  line-height: 1.6;
  min-height: 100vh;
}
a { color: var(--accent); text-decoration: none; transition: color 0.15s; }
a:hover { color: #7dd3fc; }
header.site {
  position: sticky; top: 0; z-index: 100;
  background: rgba(10, 14, 26, 0.85);
  backdrop-filter: blur(12px);
  border-bottom: 1px solid var(--border);
  padding: 16px 32px;
  display: flex; justify-content: space-between; align-items: center;
}
header.site h1 {
  font-size: 18px; font-weight: 700; letter-spacing: -0.02em;
  display: flex; align-items: center; gap: 12px;
}
header.site h1 .logo {
  width: 32px; height: 32px;
  background: linear-gradient(135deg, #38bdf8, #a855f7);
  border-radius: 8px; display: inline-flex; align-items: center; justify-content: center;
  font-size: 18px;
}
header.site nav { display: flex; gap: 20px; font-size: 14px; flex-wrap: wrap; }
header.site nav a { color: var(--text-dim); font-weight: 500; }
header.site nav a:hover { color: var(--accent); }
header.site nav a.active { color: var(--accent); }
main { padding: 32px; max-width: 1400px; margin: 0 auto; }
.hero {
  text-align: center; padding: 48px 0 32px;
}
.hero h1 {
  font-size: 56px; font-weight: 800; letter-spacing: -0.04em;
  background: linear-gradient(135deg, #38bdf8 0%, #a855f7 50%, #ec4899 100%);
  -webkit-background-clip: text; background-clip: text; color: transparent;
  margin-bottom: 12px;
}
.hero .subtitle { color: var(--text-dim); font-size: 18px; max-width: 720px; margin: 0 auto; }
.hero .stats {
  display: inline-flex; gap: 32px; margin-top: 24px; padding: 16px 32px;
  background: var(--bg-2); border: 1px solid var(--border); border-radius: 12px;
  font-family: 'JetBrains Mono', 'SF Mono', Menlo, monospace;
}
.hero .stats .stat { text-align: center; }
.hero .stats .stat .num { font-size: 28px; font-weight: 700; color: var(--accent); display: block; }
.hero .stats .stat .label { font-size: 11px; color: var(--text-dim); text-transform: uppercase; letter-spacing: 0.08em; }
.chapters-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(360px, 1fr));
  gap: 20px;
  margin-top: 32px;
}
.chapter-card {
  background: var(--bg-2);
  border: 1px solid var(--border);
  border-radius: 16px;
  padding: 24px;
  transition: all 0.2s ease;
  position: relative; overflow: hidden;
}
.chapter-card::before {
  content: ''; position: absolute; top: 0; left: 0; right: 0; height: 3px;
  background: var(--accent-color, var(--accent));
}
.chapter-card:hover {
  transform: translateY(-2px);
  border-color: var(--accent-color, var(--accent));
  box-shadow: 0 8px 32px rgba(56, 189, 248, 0.1);
}
.chapter-card .ch-num {
  display: inline-block; padding: 4px 10px;
  background: var(--accent-color, var(--accent)); color: #0a0e1a;
  border-radius: 6px; font-size: 11px; font-weight: 700;
  font-family: 'JetBrains Mono', 'SF Mono', Menlo, monospace;
  margin-bottom: 12px;
}
.chapter-card h2 {
  font-size: 22px; font-weight: 700; letter-spacing: -0.02em;
  margin-bottom: 8px;
}
.chapter-card .desc { color: var(--text-dim); font-size: 14px; margin-bottom: 16px; min-height: 40px; }
.chapter-card .ch-stats {
  display: flex; gap: 16px; padding: 12px 0; border-top: 1px solid var(--border);
  font-family: 'JetBrains Mono', 'SF Mono', Menlo, monospace; font-size: 13px;
}
.chapter-card .ch-stats .cs { display: flex; flex-direction: column; }
.chapter-card .ch-stats .num { font-size: 20px; font-weight: 700; color: var(--accent); }
.chapter-card .ch-stats .label { font-size: 10px; color: var(--text-dim); text-transform: uppercase; letter-spacing: 0.06em; }
.chapter-card .ch-actions { display: flex; gap: 8px; margin-top: 16px; flex-wrap: wrap; }
.chapter-card .ch-actions a {
  display: inline-flex; align-items: center; gap: 6px;
  padding: 8px 14px; border-radius: 8px;
  background: var(--bg-3); border: 1px solid var(--border);
  font-size: 13px; font-weight: 500;
}
.chapter-card .ch-actions a:hover { background: var(--bg); }
.chapter-card .ch-actions a.primary {
  background: var(--accent-color, var(--accent));
  color: #0a0e1a; border-color: transparent;
}
.chapter-card .ch-actions a.primary:hover { filter: brightness(1.1); color: #0a0e1a; }
.preview-strip {
  display: flex; gap: 8px; margin-top: 16px;
  height: 80px;
}
.preview-strip .preview {
  flex: 1; border-radius: 6px; overflow: hidden;
  background: var(--bg-3); border: 1px solid var(--border);
}
.preview-strip .preview img {
  width: 100%; height: 100%; object-fit: cover; object-position: top;
}
.crumbs { color: var(--text-dim); font-size: 13px; margin-bottom: 12px; }
.crumbs a { color: var(--text-dim); }
.crumbs a:hover { color: var(--accent); }
.chapter-header { padding: 32px 0; border-bottom: 1px solid var(--border); margin-bottom: 32px; }
.chapter-header h1 { font-size: 40px; font-weight: 800; letter-spacing: -0.03em; margin-bottom: 8px; }
.chapter-header .meta { color: var(--text-dim); font-size: 15px; }
.hub-section {
  margin-bottom: 40px;
  background: var(--bg-2);
  border: 1px solid var(--border);
  border-radius: 12px;
  padding: 24px;
}
.hub-section h2 {
  font-size: 22px; font-weight: 700; margin-bottom: 4px;
  display: flex; align-items: center; gap: 12px;
}
.hub-section h2 .hub-num {
  font-family: 'JetBrains Mono', 'SF Mono', Menlo, monospace;
  font-size: 12px; padding: 4px 8px; background: var(--bg-3); border-radius: 4px;
  color: var(--text-dim);
}
.hub-section .hub-desc { color: var(--text-dim); font-size: 13px; margin-bottom: 16px; }
.topic-grid {
  display: grid; grid-template-columns: repeat(auto-fill, minmax(220px, 1fr));
  gap: 12px;
}
.topic-card {
  background: var(--bg-3);
  border: 1px solid var(--border);
  border-radius: 8px;
  overflow: hidden;
  transition: all 0.15s;
  text-decoration: none !important;
  color: var(--text) !important;
}
.topic-card:hover { border-color: var(--accent); transform: translateY(-1px); }
.topic-card .preview {
  width: 100%; aspect-ratio: 16/9;
  background: linear-gradient(135deg, var(--bg-3) 0%, var(--code-bg) 100%);
  display: flex; align-items: center; justify-content: center;
  overflow: hidden;
}
.topic-card .preview img { width: 100%; height: auto; min-height: 100%; }
.topic-card .no-preview { color: var(--text-dim); font-size: 12px; padding: 12px; text-align: center; }
.topic-card .title {
  padding: 10px 12px;
  font-size: 13px; font-weight: 500;
  border-top: 1px solid var(--border);
  line-height: 1.4;
}
.topic-card .num {
  display: inline-block; font-family: 'JetBrains Mono', 'SF Mono', Menlo, monospace;
  font-size: 10px; color: var(--text-dim); margin-right: 6px;
}
.topic-page { max-width: 1100px; margin: 0 auto; }
.topic-page .topic-header {
  display: flex; justify-content: space-between; align-items: flex-start;
  margin-bottom: 24px; gap: 24px; flex-wrap: wrap;
}
.topic-page .topic-header h1 {
  font-size: 32px; font-weight: 800; letter-spacing: -0.02em;
}
.topic-page .topic-actions { display: flex; gap: 8px; }
.topic-page .topic-actions a {
  padding: 8px 14px; border-radius: 8px;
  background: var(--bg-3); border: 1px solid var(--border);
  font-size: 13px;
}
.topic-page .topic-image {
  background: var(--bg-2); border: 1px solid var(--border); border-radius: 12px;
  padding: 16px; margin-bottom: 24px;
}
.topic-page .topic-image img { width: 100%; height: auto; display: block; border-radius: 6px; }
.topic-page .topic-content {
  background: var(--bg-2); border: 1px solid var(--border); border-radius: 12px;
  padding: 24px;
}
.topic-page .topic-content h2, .topic-page .topic-content h3, .topic-page .topic-content h4 {
  margin-top: 20px; margin-bottom: 10px; font-weight: 700;
}
.topic-page .topic-content h2 { font-size: 22px; border-bottom: 1px solid var(--border); padding-bottom: 6px; }
.topic-page .topic-content h3 { font-size: 18px; color: var(--accent); }
.topic-page .topic-content h4 { font-size: 15px; }
.topic-page .topic-content p { margin-bottom: 12px; color: var(--text); }
.topic-page .topic-content ul, .topic-page .topic-content ol { margin-left: 24px; margin-bottom: 12px; }
.topic-page .topic-content li { margin-bottom: 4px; }
.topic-page .topic-content li:empty { display: none; }
.topic-page .topic-content table {
  border-collapse: collapse; margin: 16px 0; width: 100%; font-size: 13px;
}
.topic-page .topic-content th, .topic-page .topic-content td {
  border: 1px solid var(--border); padding: 8px 10px; text-align: left;
}
.topic-page .topic-content th { background: var(--bg-3); font-weight: 600; }
.topic-page .topic-content code {
  background: var(--code-bg); padding: 2px 6px; border-radius: 4px;
  font-family: 'JetBrains Mono', 'SF Mono', Menlo, monospace; font-size: 0.9em;
}
.topic-page .topic-content blockquote {
  border-left: 3px solid var(--accent); padding: 8px 14px; color: var(--text-dim);
  margin: 12px 0; background: var(--bg-3); border-radius: 0 6px 6px 0;
}
.topic-page .topic-content hr {
  border: none; border-top: 1px solid var(--border); margin: 24px 0;
}
footer {
  margin-top: 64px; padding: 32px;
  border-top: 1px solid var(--border);
  color: var(--text-dim); font-size: 13px;
  text-align: center;
}
footer a { color: var(--text-dim); }
footer a:hover { color: var(--accent); }
@media (max-width: 768px) {
  header.site { flex-direction: column; gap: 8px; align-items: flex-start; }
  .hero h1 { font-size: 36px; }
  .hero .stats { flex-wrap: wrap; gap: 16px; }
}
"""


def page_header(title, active=""):
    nav = ""
    for slug, name, _url, _desc, _color in CHAPTERS:
        is_active = "active" if slug == active else ""
        nav += f'<a href="/{slug}/" class="{is_active}">{name}</a>'
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title} · MedSea</title>
<meta name="description" content="Sea Knowledge medical study library — Davidson's chapters rendered as infographics.">
<style>{PAGE_CSS}</style>
</head>
<body>
<header class="site">
  <h1><span class="logo">⚕</span><a href="/" style="color:inherit">MedSea</a></h1>
  <nav>{nav}</nav>
</header>
<main>
"""


def page_footer():
    return f"""</main>
<footer>
  <p>MedSea · Sea Knowledge Medical Library · <a href="https://github.com/SeaXen/MedSea" target="_blank">github.com/SeaXen/MedSea</a></p>
  <p style="margin-top:8px;opacity:0.6">Generated {datetime.now().strftime("%Y-%m-%d %H:%M UTC")}</p>
</footer>
</body>
</html>
"""


CALLOUT_RE = re.compile(r"<callout[^>]*>(.*?)</callout>", re.DOTALL)
FRONTMATTER_RE = re.compile(r"^---\s*\n.*?\n---\s*\n", re.DOTALL)


def clean_md(text: str) -> str:
    """Strip Obsidian callouts + frontmatter, normalize whitespace."""
    text = CALLOUT_RE.sub(lambda m: "> " + m.group(1).strip().replace("\n", "\n> "), text)
    text = FRONTMATTER_RE.sub("", text)
    text = re.sub(r"<br\s*/?>", "\n", text)
    # Strip the redundant H1 (we render it in the page header)
    text = re.sub(r"^#\s+[^\n]+\n+", "", text, count=1)
    return text


def render_md_to_html(md_text: str) -> str:
    md_text = clean_md(md_text)
    lines = md_text.split("\n")
    out = []
    in_ul = False
    in_ol = False
    in_table = False
    table_rows = []

    def flush_list():
        nonlocal in_ul, in_ol
        if in_ul:
            out.append("</ul>"); in_ul = False
        if in_ol:
            out.append("</ol>"); in_ol = False

    def flush_table():
        nonlocal in_table, table_rows
        if in_table and table_rows:
            out.append('<table>')
            headers = table_rows[0]
            out.append("<tr>" + "".join(f"<th>{inline_md(c)}</th>" for c in headers) + "</tr>")
            for row in table_rows[1:]:
                out.append("<tr>" + "".join(f"<td>{inline_md(c)}</td>" for c in row) + "</tr>")
            out.append("</table>")
        in_table = False
        table_rows = []

    def inline_md(text):
        text = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", text)
        text = re.sub(r"(?<!\*)\*(?!\*)(.+?)(?<!\*)\*(?!\*)", r"<em>\1</em>", text)
        text = re.sub(r"`([^`]+)`", r"<code>\1</code>", text)
        text = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r'<a href="\2">\1</a>', text)
        return text

    for line in lines:
        # HR
        if re.match(r"^\s*---\s*$", line) and not in_table:
            flush_list()
            out.append("<hr>")
            continue
        m = re.match(r"^(#{1,6})\s+(.+)$", line)
        if m:
            flush_list(); flush_table()
            level = len(m.group(1))
            out.append(f"<h{level}>{inline_md(m.group(2))}</h{level}>")
            continue
        if line.strip().startswith("|") and line.strip().endswith("|"):
            flush_list()
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            if not in_table:
                in_table = True; table_rows = [cells]
            else:
                if all(re.match(r"^[-:]+$", c) for c in cells):
                    continue
                table_rows.append(cells)
            continue
        else:
            flush_table()
        m = re.match(r"^\s*[-*]\s+(.*)$", line)
        if m and m.group(1).strip():
            if in_ol:
                out.append("</ol>"); in_ol = False
            if not in_ul:
                out.append("<ul>"); in_ul = True
            out.append(f"<li>{inline_md(m.group(1))}</li>")
            continue
        m = re.match(r"^\s*\d+\.\s+(.*)$", line)
        if m and m.group(1).strip():
            if in_ul:
                out.append("</ul>"); in_ul = False
            if not in_ol:
                out.append("<ol>"); in_ol = True
            out.append(f"<li>{inline_md(m.group(1))}</li>")
            continue
        m = re.match(r"^>\s*(.*)$", line)
        if m:
            flush_list()
            out.append(f"<blockquote>{inline_md(m.group(1))}</blockquote>")
            continue
        if not line.strip():
            flush_list()
            continue
        flush_list()
        out.append(f"<p>{inline_md(line)}</p>")

    flush_list(); flush_table()
    return "\n".join(out)


def chapter_summary(chapter_slug):
    chapter_dir = REPO_ROOT / "chapters" / chapter_slug
    topics = find_files(chapter_dir)
    n_topics = len(topics)
    n_pngs = sum(1 for t in topics if t["png"])
    n_md = sum(1 for t in topics if t["md"])
    hub_meta = load_hub_info(chapter_dir)
    by_hub = {}
    for t in topics:
        by_hub.setdefault(t["hub_num"], []).append(t)
    return {
        "n_topics": n_topics, "n_pngs": n_pngs, "n_md": n_md,
        "n_hubs": len(by_hub), "by_hub": by_hub,
        "hub_names": hub_meta, "topics": topics,
    }


def copy_assets(chapter_slug, info):
    chapter_dir = REPO_ROOT / "chapters" / chapter_slug
    site_chapter = SITE / chapter_slug
    site_chapter.mkdir(parents=True, exist_ok=True)
    copied = 0
    for t in info["topics"]:
        if t["png"]:
            if t["folder"]:
                dest = site_chapter / "diseases" / t["folder"] / "topic.png"
            else:
                dest = site_chapter / "diseases" / f"{t['local_prefix']}-{t['slug']}.png"
            dest.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(t["png"], dest)
            copied += 1
        if t["md"]:
            if t["folder"]:
                dest = site_chapter / "diseases" / t["folder"] / "topic.md"
            else:
                dest = site_chapter / "diseases" / f"{t['local_prefix']}-{t['slug']}.md"
            dest.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(t["md"], dest)
    return copied


def write_index(site_data):
    html = page_header("MedSea · Sea Knowledge Medical Library")
    total_topics = sum(d["n_topics"] for d in site_data.values())
    total_pngs = sum(d["n_pngs"] for d in site_data.values())
    total_hubs = sum(d["n_hubs"] for d in site_data.values())
    html += f"""
<div class="hero">
  <h1>MedSea</h1>
  <p class="subtitle">Sea Knowledge medical study library — Davidson's Principles & Practice of Medicine rendered as searchable infographics. Each topic pairs a 1–3 page visual study guide with rich text content on Notion.</p>
  <div class="stats">
    <div class="stat"><span class="num">{len(CHAPTERS)}</span><span class="label">Chapters</span></div>
    <div class="stat"><span class="num">{total_hubs}</span><span class="label">Hubs</span></div>
    <div class="stat"><span class="num">{total_topics}</span><span class="label">Topics</span></div>
    <div class="stat"><span class="num">{total_pngs}</span><span class="label">Infographics</span></div>
  </div>
</div>

<div class="chapters-grid">
"""
    for ch_slug, ch_name, ch_url, ch_desc, ch_color in CHAPTERS:
        info = site_data[ch_slug]
        if info["n_topics"] == 0:
            continue
        previews = []
        for hub_num in sorted(info["by_hub"].keys()):
            for t in info["by_hub"][hub_num]:
                if t["png"]:
                    if t["folder"]:
                        rel = f"{ch_slug}/diseases/{t['folder']}/topic.png"
                    else:
                        rel = f"{ch_slug}/diseases/{t['local_prefix']}-{t['slug']}.png"
                    previews.append(rel)
                    break
            if len(previews) >= 4:
                break
        preview_html = '<div class="preview-strip">'
        for p in previews[:4]:
            preview_html += f'<div class="preview"><img src="/{p}" alt="preview" loading="lazy"></div>'
        preview_html += "</div>"
        ch_display_num = ch_slug.split("-")[0]
        html += f"""
<article class="chapter-card" style="--accent-color: {ch_color}">
  <span class="ch-num">Ch {ch_display_num}</span>
  <h2>{ch_name}</h2>
  <p class="desc">{ch_desc}</p>
  <div class="ch-stats">
    <div class="cs"><span class="num">{info['n_hubs']}</span><span class="label">Hubs</span></div>
    <div class="cs"><span class="num">{info['n_topics']}</span><span class="label">Topics</span></div>
    <div class="cs"><span class="num">{info['n_pngs']}</span><span class="label">PNGs</span></div>
  </div>
  {preview_html}
  <div class="ch-actions">
    <a href="/{ch_slug}/" class="primary">Browse Topics →</a>
    <a href="{ch_url}" target="_blank">Notion ↗</a>
  </div>
</article>
"""
    html += "</div>"
    html += page_footer()
    (SITE / "index.html").write_text(html)
    print(f"  Wrote index.html ({total_topics} topics across {len(CHAPTERS)} chapters)")


def write_chapter_page(ch_slug, ch_name, ch_url, ch_desc, ch_color, info):
    html = page_header(ch_name, active=ch_slug)
    ch_display_num = ch_slug.split("-")[0]
    html += f"""
<div class="crumbs"><a href="/">Home</a> · <a href="/{ch_slug}/">{ch_name}</a></div>
<div class="chapter-header" style="border-left: 3px solid {ch_color}; padding-left: 24px;">
  <h1>{ch_name}</h1>
  <p class="meta">Chapter {ch_display_num} · Davidson 24th Ed · {info['n_hubs']} hubs · {info['n_topics']} topics · <a href="{ch_url}" target="_blank">View on Notion ↗</a></p>
</div>
"""
    for hub_num in sorted(info["by_hub"].keys()):
        hub_topics = sorted(info["by_hub"][hub_num], key=lambda t: t["local_prefix"])
        hub_name = info["hub_names"].get(hub_num, hub_num)
        html += '<section class="hub-section">\n'
        html += f'  <h2><span class="hub-num">{hub_num}</span> {hub_name}</h2>\n'
        html += f'  <p class="hub-desc">{len(hub_topics)} topic{"s" if len(hub_topics)!=1 else ""}</p>\n'
        html += '  <div class="topic-grid">\n'
        for t in hub_topics:
            title = t["slug"].replace("-", " ").title()
            if t["folder"]:
                png_rel = f"diseases/{t['folder']}/topic.png"
                topic_url = f"diseases/{t['folder']}/"
            else:
                png_rel = f"diseases/{t['local_prefix']}-{t['slug']}.png"
                topic_url = f"diseases/{t['local_prefix']}-{t['slug']}.html"
            png_full = f"/{ch_slug}/{png_rel}"
            img_html = f'<img src="{png_full}" alt="{title}" loading="lazy">' if t["png"] else '<div class="no-preview">No preview</div>'
            html += f'''    <a class="topic-card" href="/{ch_slug}/{topic_url}">
      <div class="preview">{img_html}</div>
      <div class="title"><span class="num">{t["local_prefix"]}</span>{title}</div>
    </a>
'''
        html += '  </div>\n</section>\n'
    html += page_footer()
    out = SITE / ch_slug / "index.html"
    out.write_text(html)
    print(f"  Wrote {ch_slug}/index.html ({len(info['by_hub'])} hubs, {info['n_topics']} topics)")


def write_topic_page(ch_slug, ch_name, ch_color, hub_num, topic):
    slug = topic["slug"]
    title = slug.replace("-", " ").title()
    if topic["folder"]:
        png_rel = f"diseases/{topic['folder']}/topic.png"
        md_path = SITE / ch_slug / "diseases" / topic["folder"] / "topic.md"
        html_path = SITE / ch_slug / "diseases" / topic["folder"] / "index.html"
    else:
        png_rel = f"diseases/{topic['local_prefix']}-{slug}.png"
        md_path = SITE / ch_slug / "diseases" / f"{topic['local_prefix']}-{slug}.md"
        html_path = SITE / ch_slug / "diseases" / f"{topic['local_prefix']}-{slug}.html"

    png_full = f"/{ch_slug}/{png_rel}"
    md_text = md_path.read_text(encoding="utf-8") if md_path.exists() else ""
    md_html = render_md_to_html(md_text) if md_text else "<p><em>No text content available for this topic.</em></p>"
    img_block = f'<img src="{png_full}" alt="{title}">' if (SITE / ch_slug / png_rel).exists() else ""

    html = page_header(title, active=ch_slug)
    html += f"""
<div class="topic-page">
  <div class="crumbs"><a href="/">Home</a> · <a href="/{ch_slug}/">{ch_name}</a> · <span>{hub_num}</span></div>
  <div class="topic-header">
    <div>
      <h1>{title}</h1>
      <p class="meta" style="color:var(--text-dim);margin-top:4px">{hub_num} · {topic['local_prefix']}</p>
    </div>
    <div class="topic-actions">
      <a href="{png_full}" download>Download PNG</a>
    </div>
  </div>
"""
    if img_block:
        html += f'  <div class="topic-image">{img_block}</div>\n'
    html += f'  <div class="topic-content">\n{md_html}\n  </div>\n'
    html += "</div>\n"
    html += page_footer()
    html_path.write_text(html)


def main():
    if SITE.exists():
        shutil.rmtree(SITE)
    SITE.mkdir(parents=True)
    (SITE / "assets").mkdir()

    site_data = {}
    for ch_slug, ch_name, ch_url, ch_desc, ch_color in CHAPTERS:
        print(f"\nProcessing {ch_slug}...")
        info = chapter_summary(ch_slug)
        site_data[ch_slug] = info
        if info["n_topics"] == 0:
            print(f"  No topics found, skipping")
            continue
        n = copy_assets(ch_slug, info)
        print(f"  Copied {n} PNGs to site/{ch_slug}/")
        write_chapter_page(ch_slug, ch_name, ch_url, ch_desc, ch_color, info)
        topic_count = 0
        for hub_num, hub_topics in info["by_hub"].items():
            for t in hub_topics:
                write_topic_page(ch_slug, ch_name, ch_color, hub_num, t)
                topic_count += 1
        print(f"  Wrote {topic_count} topic pages")

    write_index(site_data)

    total_size = sum(p.stat().st_size for p in SITE.rglob("*") if p.is_file())
    print(f"\n✓ Site generated at {SITE}  ({total_size / 1024 / 1024:.1f} MB total)")


if __name__ == "__main__":
    main()
