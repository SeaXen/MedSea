#!/usr/bin/env python3
"""Generate MedSea static website.

Scans chapters/, copies all PNG/MD files into site/diseases/, generates HTML pages.

Design:
- Sticky header with logo + stats bar + chapter dropdown + Notion link
- No hero text — chapter grid is the main content
- Chapter page = SPA with sidebar (left = topic list) | main (right = topic content)
- Topic content is pre-rendered HTML loaded via fetch() from topics.json manifest
"""
import json
import re
import shutil
from pathlib import Path
from datetime import datetime
from urllib.parse import quote

REPO_ROOT = Path("/mnt/tb/Sea-knowledge/#MedSea")
SITE = REPO_ROOT / "site"

# Full Davidson 25th Edition chapter list (32 chapters)
DAVIDSON_25TH = [
    (1,  "Clinical decision-making",                "1-clinical-decision-making"),
    (2,  "Clinical therapeutics and good prescribing", "2-clinical-therapeutics"),
    (3,  "Clinical genetics",                       "3-clinical-genetics"),
    (4,  "Clinical immunology",                     "4-clinical-immunology"),
    (5,  "Nutritional factors in disease",          "5-nutritional-factors"),
    (6,  "Population health and epidemiology",      "6-population-health"),
    (7,  "Principles of infection",                 "7-principles-of-infection"),
    (8,  "Oncology",                                "8-oncology"),
    (9,  "Palliative and supportive care",          "9-palliative-care"),
    (10, "Acute medicine and critical illness",     "10-acute-medicine"),
    (11, "Poisoning",                               "11-poisoning"),
    (12, "Envenomation",                            "12-envenomation"),
    (13, "Medicine in austere environments",        "13-austere-medicine"),
    (14, "Infectious disease",                      "14-infectious-disease"),
    (15, "Sexually transmitted infections",         "15-sexually-transmitted-infections"),
    (16, "Cardiology",                              "16-cardiology"),
    (17, "Respiratory medicine",                    "17-respiratory-medicine"),
    (18, "Nephrology and urology",                  "18-nephrology-urology"),
    (19, "Clinical biochemistry and metabolic medicine", None),
    (20, "Endocrinology",                           "20-endocrinology"),
    (21, "Diabetes mellitus",                       None),
    (22, "Gastroenterology",                        "22-gastroenterology"),
    (23, "Hepatology",                              None),
    (24, "Haematology and transfusion medicine",    None),
    (25, "Rheumatology and bone disease",           None),
    (26, "Dermatology",                             None),
    (27, "Neurology and stroke medicine",           None),
    (28, "Medical ophthalmology",                   None),
    (29, "Medical psychiatry",                      None),
    (30, "Maternal medicine",                       None),
    (31, "Adolescence, transition and young adult medicine", None),
    (32, "Older adult medicine and frailty",        None),
]

# Built chapters with metadata: (slug, display_name, notion_url, accent_color)
BUILT_CHAPTERS = {
    "1-clinical-decision-making": (
        "Clinical Decision-Making",
        "https://medsea.notion.site/Chapter-1-Clinical-decision-making-8e5cd1ec34904d69aa7fb21ab056a508",
        "#64748b",
    ),
    "2-clinical-therapeutics": (
        "Clinical Therapeutics & Prescribing",
        "https://medsea.notion.site/Chapter-2-Clinical-therapeutics-and-good-prescribing-5ec47a8c567148fc91af45d63691e6e6",
        "#0ea5e9",
    ),
    "3-clinical-genetics": (
        "Clinical Genetics",
        "https://medsea.notion.site/Chapter-3-Clinical-genetics-0b1c71bf18984f99ab97018154d0ad71",
        "#84cc16",
    ),
    "4-clinical-immunology": (
        "Clinical Immunology",
        "https://medsea.notion.site/Chapter-4-Clinical-immunology-0b4e940adc464a56b120b1e4ba682c63",
        "#f97316",
    ),
    "5-nutritional-factors": (
        "Nutritional Factors in Disease",
        "https://medsea.notion.site/Chapter-5-Nutritional-factors-in-disease-20ae0f805c75401983af5d981bccbe72",
        "#eab308",
    ),
    "6-population-health": (
        "Population Health & Epidemiology",
        "https://medsea.notion.site/Chapter-6-Population-health-and-epidemiology-83035ef3c78d462b816a3d8ad0b0e653",
        "#14b8a6",
    ),
    "7-principles-of-infection": (
        "Principles of Infection",
        "https://medsea.notion.site/Chapter-7-Principles-of-infection-6469084f1ff046798f4f4bab9f1d0802",
        "#dc2626",
    ),
    "8-oncology": (
        "Oncology",
        "https://medsea.notion.site/Chapter-8-Oncology-8d4228ea84974d4db2e7f62a746f39d1",
        "#7c3aed",
    ),
    "9-palliative-care": (
        "Palliative & Supportive Care",
        "https://medsea.notion.site/Chapter-9-Palliative-and-supportive-care-c65289d8222748e3a809cb07e2b70f66",
        "#be185d",
    ),
    "10-acute-medicine": (
        "Acute Medicine",
        "https://medsea.notion.site/Chapter-10-Acute-Medicine-and-Critical-Illness-3835588e846f81a1bd40fbd5d564fd2e",
        "#f43f5e",
    ),
    "11-poisoning": (
        "Poisoning",
        "https://medsea.notion.site/Chapter-11-Poisoning-abc75846ef544efcb3b78f00134f50b2",
        "#84cc16",
    ),
    "12-envenomation": (
        "Envenomation",
        "https://medsea.notion.site/Chapter-12-Envenomation-fce508f973a64d58b48ad1e2d186e39d",
        "#22c55e",
    ),
    "13-austere-medicine": (
        "Austere Medicine",
        "https://medsea.notion.site/Chapter-13-Medicine-in-austere-environments-b9b201cbbecc4eaab3c4b6c958c8ac11",
        "#0d9488",
    ),
    "14-infectious-disease": (
        "Infectious Disease",
        "https://medsea.notion.site/Chapter-14-Infectious-disease-eb9d6efbe3bb4ccc8302396a8edc57cf",
        "#0891b2",
    ),
    "15-sexually-transmitted-infections": (
        "Sexually Transmitted Infections",
        "https://medsea.notion.site/Chapter-15-Sexually-transmitted-infections-19c59a0895cd4ea4bee4e69d90ce37c8",
        "#7c3aed",
    ),
    "16-cardiology": (
        "Cardiology",
        "https://medsea.notion.site/Chapter-16-Cardiology-8baa010d9cc94c48826136417d383973",
        "#ef4444",
    ),
    "17-respiratory-medicine": (
        "Respiratory Medicine",
        "https://medsea.notion.site/Chapter-17-Respiratory-medicine-d4fe7d456ca4481581e806ebe9e177cf",
        "#10b981",
    ),
    "18-nephrology-urology": (
        "Nephrology & Urology",
        "https://medsea.notion.site/Chapter-18-Nephrology-and-urology-710f215344c34692af7584e89e714ff0",
        "#06b6d4",
    ),
    "20-endocrinology": (
        "Endocrinology",
        "https://medsea.notion.site/Chapter-20-Endocrinology-9db6455d6ae840f0ac29129217d6ccef",
        "#a855f7",
    ),
    "22-gastroenterology": (
        "Gastroenterology",
        "https://medsea.notion.site/Chapter-22-Gastroenterology-bbfd97790eca482eaed8d47428a642b2",
        "#f59e0b",
    ),
    "19-clinical-biochemistry-and-metabolic-medi": (
        "Clinical Biochemistry & Metabolic Medicine",
        "https://medsea.notion.site/",
        "#06b6d4",
    ),
    "21-diabetes-mellitus": (
        "Diabetes Mellitus",
        "https://medsea.notion.site/",
        "#dc2626",
    ),
    "23-hepatology": (
        "Hepatology",
        "https://medsea.notion.site/",
        "#a16207",
    ),
    "24-haematology-and-transfusion-medicine": (
        "Haematology & Transfusion Medicine",
        "https://medsea.notion.site/",
        "#be123c",
    ),
    "25-rheumatology-and-bone-disease": (
        "Rheumatology & Bone Disease",
        "https://medsea.notion.site/",
        "#7c2d12",
    ),
    "26-dermatology": (
        "Dermatology",
        "https://medsea.notion.site/",
        "#ec4899",
    ),
    "27-neurology-and-stroke-medicine": (
        "Neurology & Stroke Medicine",
        "https://medsea.notion.site/",
        "#8b5cf6",
    ),
    "28-medical-ophthalmology": (
        "Medical Ophthalmology",
        "https://medsea.notion.site/",
        "#0ea5e9",
    ),
    "29-medical-psychiatry": (
        "Medical Psychiatry",
        "https://medsea.notion.site/",
        "#6366f1",
    ),
    "30-maternal-medicine": (
        "Maternal Medicine",
        "https://medsea.notion.site/",
        "#d946ef",
    ),
    "31-adolescence-transition-and-young-adult-m": (
        "Adolescence Transition & Young Adult Medicine",
        "https://medsea.notion.site/",
        "#f97316",
    ),
    "32-older-adult-medicine-and-frailty": (
        "Older Adult Medicine & Frailty",
        "https://medsea.notion.site/",
        "#64748b",
    ),
}


# ------------------------ File scanning ------------------------

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
        if not md_f.exists():
            md_f = sub / f"{slug}.md"
        if not png_f.exists():
            png_f = sub / f"{slug}.png"
        topics.append({
            "hub_num": hub_num, "local_prefix": local_prefix, "slug": slug,
            "md": md_f if md_f.exists() else None,
            "png": png_f if png_f.exists() else None,
            "folder": sub.name,
        })
    for f in sorted(diseases_dir.iterdir()):
        if not f.is_file():
            continue
        m = re.match(r"^(\d+\.\d+)\.(\d+)-(.+)\.(md|png)$", f.name)
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


# ------------------------ HTML rendering ------------------------

PAGE_CSS = """
:root {
  --bg: #0a0e1a;
  --bg-2: #111827;
  --bg-3: #1f2937;
  --bg-4: #0f172a;
  --border: #2d3748;
  --border-2: #374151;
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

/* ===== Header (sticky) ===== */
header.site {
  position: sticky; top: 0; z-index: 100;
  background: rgba(10, 14, 26, 0.94);
  backdrop-filter: blur(12px);
  -webkit-backdrop-filter: blur(12px);
  border-bottom: 1px solid var(--border);
  padding: 8px 16px;
  display: flex; align-items: center; gap: 12px;
  flex-wrap: nowrap;
  min-height: 48px;
}
header.site .logo-wrap {
  display: flex; align-items: center; gap: 8px;
  font-size: 15px; font-weight: 700; letter-spacing: -0.02em;
  white-space: nowrap;
  flex-shrink: 0;
}
header.site .logo {
  width: 26px; height: 26px;
  background: linear-gradient(135deg, #38bdf8, #a855f7);
  border-radius: 7px; display: inline-flex; align-items: center; justify-content: center;
  font-size: 14px;
}
header.site .logo-wrap a { color: inherit; }

/* ===== Stats bar in header ===== */
header.site .stats {
  display: flex; gap: 3px; align-items: center;
  font-family: 'JetBrains Mono', 'SF Mono', Menlo, monospace;
  font-size: 11px;
  flex-shrink: 0;
}
header.site .stats .stat {
  display: inline-flex; align-items: baseline; gap: 4px;
  padding: 3px 8px; border-radius: 5px;
  background: rgba(56, 189, 248, 0.08);
  border: 1px solid rgba(56, 189, 248, 0.15);
}
header.site .stats .stat .num { font-size: 12px; font-weight: 700; color: var(--accent); }
header.site .stats .stat .label { color: var(--text-dim); font-size: 9px; text-transform: uppercase; letter-spacing: 0.05em; }

/* ===== Chapter dropdown ===== */
header.site .chapter-dropdown {
  position: relative;
  margin-left: auto;
  flex-shrink: 0;
}
header.site .chapter-dropdown .drop-btn {
  padding: 6px 12px; border-radius: 7px;
  background: var(--bg-3); border: 1px solid var(--border-2);
  color: var(--text); font-size: 12px; font-weight: 500;
  cursor: pointer; display: inline-flex; align-items: center; gap: 6px;
  font-family: inherit;
}
header.site .chapter-dropdown .drop-btn:hover { background: var(--bg-2); border-color: var(--accent); }
header.site .chapter-dropdown .drop-btn .arrow { font-size: 9px; opacity: 0.7; }
header.site .chapter-dropdown .drop-btn .current-ch { color: var(--accent); font-weight: 600; }
/* Full-height dropdown showing all 32 chapters in a 2-col grid */
header.site .chapter-dropdown .drop-menu {
  position: fixed; right: 16px; top: 56px;
  width: 640px; max-height: calc(100vh - 72px); overflow-y: auto;
  background: var(--bg-2); border: 1px solid var(--border-2);
  border-radius: 10px;
  box-shadow: 0 20px 50px rgba(0,0,0,0.6);
  padding: 8px;
  display: none;
  z-index: 200;
  column-count: 2;
  column-gap: 6px;
}
header.site .chapter-dropdown .drop-menu .item { break-inside: avoid; }
header.site .chapter-dropdown.open .drop-menu { display: block; }
header.site .chapter-dropdown .drop-menu .item {
  display: flex; align-items: center; gap: 8px;
  padding: 6px 8px; border-radius: 5px;
  color: var(--text); font-size: 12px;
  cursor: pointer; transition: background 0.1s;
  text-decoration: none !important;
}
header.site .chapter-dropdown .drop-menu .item:hover { background: var(--bg-3); }
header.site .chapter-dropdown .drop-menu .item.active { background: rgba(56, 189, 248, 0.15); }
header.site .chapter-dropdown .drop-menu .item .num {
  display: inline-block; min-width: 24px; padding: 1px 4px;
  background: var(--bg-3); border: 1px solid var(--border);
  border-radius: 3px; font-family: 'JetBrains Mono', 'SF Mono', Menlo, monospace;
  font-size: 9px; text-align: center; color: var(--text-dim);
  flex-shrink: 0;
}
header.site .chapter-dropdown .drop-menu .item .name {
  flex: 1; overflow: hidden; text-overflow: ellipsis; white-space: nowrap;
}
header.site .chapter-dropdown .drop-menu .item.active .num { background: var(--accent); color: #0a0e1a; border-color: transparent; }
/* Strong visual distinction: LIVE = accent green, SOON = dim grey + lock icon */
header.site .chapter-dropdown .drop-menu .item.soon { color: var(--text-dim); cursor: not-allowed; opacity: 0.5; }
header.site .chapter-dropdown .drop-menu .item.soon .num { opacity: 0.7; }
header.site .chapter-dropdown .drop-menu .item .badge {
  margin-left: auto; font-size: 8px; padding: 1px 5px;
  background: var(--bg-3); border-radius: 8px;
  color: var(--accent); text-transform: uppercase; letter-spacing: 0.04em;
  font-weight: 700;
  flex-shrink: 0;
}
header.site .chapter-dropdown .drop-menu .item.soon .badge {
  background: transparent; border: 1px solid var(--border);
  color: var(--text-dim); font-weight: 500;
}
header.site .chapter-dropdown .drop-menu .item:not(.soon) .badge {
  background: rgba(16, 185, 129, 0.15);
  color: #10b981;
}

header.site .ext-links { display: flex; gap: 6px; flex-shrink: 0; }
header.site .ext-links a {
  padding: 5px 10px; border-radius: 6px;
  background: var(--bg-3); border: 1px solid var(--border);
  color: var(--text-dim); font-size: 11px;
  text-decoration: none;
}
header.site .ext-links a:hover { color: var(--accent); border-color: var(--accent); }

/* ===== Landing page main ===== */
main { padding: 24px 20px; max-width: 1600px; margin: 0 auto; }
.chapters-grid {
  display: grid;
  grid-template-columns: repeat(5, 1fr);
  gap: 14px;
  margin-top: 8px;
}
@media (max-width: 1400px) { .chapters-grid { grid-template-columns: repeat(4, 1fr); } }
@media (max-width: 1100px) { .chapters-grid { grid-template-columns: repeat(3, 1fr); } }
@media (max-width: 800px)  { .chapters-grid { grid-template-columns: repeat(2, 1fr); } }
@media (max-width: 500px)  { .chapters-grid { grid-template-columns: 1fr; } }
.section-title {
  font-size: 13px; color: var(--text-dim);
  text-transform: uppercase; letter-spacing: 0.12em;
  margin-bottom: 14px; font-weight: 600;
}
.chapter-card {
  background: var(--bg-2);
  border: 1px solid var(--border);
  border-radius: 12px;
  padding: 16px 16px 14px;
  transition: all 0.18s ease;
  position: relative; overflow: hidden;
  text-decoration: none !important; color: inherit !important;
  display: flex; flex-direction: column;
  cursor: pointer; min-height: 150px;
}
.chapter-card::before {
  content: ''; position: absolute; top: 0; left: 0; right: 0; height: 3px;
  background: var(--accent-color, var(--accent));
}
.chapter-card:hover {
  transform: translateY(-2px);
  border-color: var(--accent-color, var(--accent));
  box-shadow: 0 6px 24px rgba(56, 189, 248, 0.08);
}
.chapter-card .ch-num {
  display: inline-block; padding: 2px 8px;
  background: var(--accent-color, var(--accent)); color: #0a0e1a;
  border-radius: 4px; font-size: 10px; font-weight: 700;
  font-family: 'JetBrains Mono', 'SF Mono', Menlo, monospace;
  margin-bottom: 8px;
  align-self: flex-start;
}
.chapter-card h2 {
  font-size: 15px; font-weight: 700; letter-spacing: -0.01em;
  margin-bottom: 10px; line-height: 1.25;
  flex: 1;
}
.chapter-card .ch-stats {
  display: flex; gap: 12px; padding: 8px 0; border-top: 1px solid var(--border);
  font-family: 'JetBrains Mono', 'SF Mono', Menlo, monospace; font-size: 12px;
}
.chapter-card .ch-stats .cs { display: flex; flex-direction: column; }
.chapter-card .ch-stats .num { font-size: 16px; font-weight: 700; color: var(--accent); line-height: 1; }
.chapter-card .ch-stats .label { font-size: 9px; color: var(--text-dim); text-transform: uppercase; letter-spacing: 0.06em; margin-top: 2px; }
.chapter-card .ch-links {
  display: flex; gap: 12px; margin-top: 8px;
  font-size: 11px;
}
.chapter-card .ch-link-primary {
  color: var(--accent); font-weight: 600; text-decoration: none !important;
}
.chapter-card .ch-link-secondary {
  color: var(--text-dim); text-decoration: none !important;
}
.chapter-card .ch-link-primary:hover { color: #7dd3fc; }
.chapter-card .ch-link-secondary:hover { color: var(--accent); }

/* ===== Chapter page (SPA: sidebar + main) ===== */
.chapter-page {
  display: grid;
  grid-template-columns: 320px 1fr;
  gap: 0;
  min-height: calc(100vh - 65px);
}
.chapter-sidebar {
  background: var(--bg-2);
  border-right: 1px solid var(--border);
  padding: 20px 16px;
  overflow-y: auto;
  max-height: calc(100vh - 65px);
  position: sticky; top: 65px;
}
.chapter-sidebar .search {
  width: 100%; padding: 8px 12px;
  background: var(--bg-3); border: 1px solid var(--border);
  border-radius: 8px; color: var(--text); font-size: 13px;
  font-family: inherit;
  margin-bottom: 12px;
}
.chapter-sidebar .search:focus { outline: none; border-color: var(--accent); }
.chapter-sidebar .hub-group { margin-bottom: 14px; }
.chapter-sidebar .hub-group h3 {
  font-size: 11px; color: var(--accent);
  text-transform: uppercase; letter-spacing: 0.08em;
  padding: 6px 8px; margin: 0 0 4px;
  font-weight: 700;
  background: rgba(56, 189, 248, 0.06);
  border-left: 2px solid var(--accent);
  border-radius: 0 4px 4px 0;
}
.chapter-sidebar .topic-item {
  display: block; padding: 5px 10px 5px 22px;
  border-radius: 4px;
  color: var(--text); font-size: 12.5px; font-weight: 500;
  cursor: pointer; transition: all 0.1s;
  border: 1px solid transparent;
  text-decoration: none !important;
  position: relative;
  line-height: 1.35;
}
.chapter-sidebar .topic-item:hover { background: var(--bg-3); color: #fff; }
.chapter-sidebar .topic-item.active {
  background: rgba(56, 189, 248, 0.15);
  color: var(--accent);
  font-weight: 600;
  border-color: rgba(56, 189, 248, 0.3);
}
.chapter-sidebar .topic-item .num {
  font-family: 'JetBrains Mono', 'SF Mono', Menlo, monospace;
  font-size: 10px; margin-right: 6px;
  color: var(--text-dim);
  font-weight: 400;
}
.chapter-sidebar .topic-item.active .num { color: var(--accent); font-weight: 600; }
.chapter-sidebar .no-results {
  color: var(--text-dim); font-size: 12px;
  padding: 12px 8px; text-align: center;
  display: none;
}
.chapter-sidebar .no-results.show { display: block; }

.chapter-main {
  padding: 16px 24px;
  overflow-x: hidden;
}
.chapter-main .chapter-header {
  padding: 8px 0 10px; border-bottom: 1px solid var(--border); margin-bottom: 16px;
  border-left: 3px solid var(--accent-color, var(--accent));
  padding-left: 14px;
  display: flex; align-items: baseline; gap: 12px; flex-wrap: wrap;
}
.chapter-main .chapter-header h1 {
  font-size: 22px; font-weight: 800; letter-spacing: -0.02em; margin-bottom: 0;
  line-height: 1.2;
}
.chapter-main .chapter-header .meta {
  color: var(--text-dim); font-size: 12px;
  font-family: 'JetBrains Mono', 'SF Mono', Menlo, monospace;
  display: inline-flex; align-items: center; gap: 10px; flex-wrap: wrap;
}
.chapter-main .chapter-header .meta a { color: var(--accent); text-decoration: none; }
.chapter-main .chapter-header .meta a:hover { text-decoration: underline; }

.chapter-main .placeholder {
  text-align: center; padding: 60px 20px;
  color: var(--text-dim);
}
.chapter-main .placeholder .icon { font-size: 48px; margin-bottom: 12px; opacity: 0.5; }

/* ===== Topic content (main pane) ===== */
.topic-detail .crumbs {
  color: var(--text-dim); font-size: 12px; margin-bottom: 12px;
  font-family: 'JetBrains Mono', 'SF Mono', Menlo, monospace;
}
.topic-detail .crumbs a { color: var(--text-dim); }
.topic-detail .crumbs a:hover { color: var(--accent); }
.topic-detail .topic-header {
  display: flex; justify-content: space-between; align-items: flex-start;
  margin-bottom: 20px; gap: 20px; flex-wrap: wrap;
}
.topic-detail .topic-header h1 {
  font-size: 32px; font-weight: 800; letter-spacing: -0.02em;
}
.topic-detail .topic-header .meta { color: var(--text-dim); font-size: 13px; margin-top: 4px; }
.topic-detail .topic-actions { display: flex; gap: 6px; }
.topic-detail .topic-actions a, .topic-detail .topic-actions button {
  padding: 6px 12px; border-radius: 6px;
  background: var(--bg-3); border: 1px solid var(--border);
  color: var(--text); font-size: 12px;
  font-family: inherit; cursor: pointer;
  text-decoration: none;
}
.topic-detail .topic-actions a:hover, .topic-detail .topic-actions button:hover {
  background: var(--bg); border-color: var(--accent); color: var(--accent);
}
.topic-detail .topic-image {
  background: var(--bg-2); border: 1px solid var(--border); border-radius: 12px;
  padding: 16px; margin-bottom: 20px;
}
.topic-detail .topic-image img { width: 100%; height: auto; display: block; border-radius: 6px; }
.topic-detail .topic-image-toggle {
  display: flex; align-items: center; justify-content: space-between;
  background: var(--bg-3); border: 1px solid var(--border); border-radius: 10px;
  padding: 10px 16px; margin-bottom: 16px; cursor: pointer;
  color: var(--text-dim); font-size: 14px; font-weight: 600;
  transition: all 0.15s ease;
}
.topic-detail .topic-image-toggle:hover {
  background: var(--bg-2); border-color: var(--accent); color: var(--accent);
}
.topic-detail .topic-image-toggle .toggle-icon {
  font-size: 16px; transition: transform 0.2s ease;
}
.topic-detail .topic-image-toggle.collapsed .toggle-icon {
  transform: rotate(-90deg);
}
.topic-detail .topic-image-wrap { overflow: hidden; }
.topic-detail .topic-image-wrap.collapsed { display: none; }
.topic-detail .topic-content {
  background: var(--bg-2); border: 1px solid var(--border); border-radius: 12px;
  padding: 24px;
}
.topic-detail .topic-content h2, .topic-detail .topic-content h3, .topic-detail .topic-content h4 {
  margin-top: 20px; margin-bottom: 10px; font-weight: 700;
}
.topic-detail .topic-content h2 { font-size: 22px; border-bottom: 1px solid var(--border); padding-bottom: 6px; }
.topic-detail .topic-content h3 { font-size: 18px; color: var(--accent); }
.topic-detail .topic-content h4 { font-size: 15px; }
.topic-detail .topic-content p { margin-bottom: 12px; color: var(--text); }
.topic-detail .topic-content ul, .topic-detail .topic-content ol { margin-left: 24px; margin-bottom: 12px; }
.topic-detail .topic-content li { margin-bottom: 4px; }
.topic-detail .topic-content li:empty { display: none; }
.topic-detail .topic-content table {
  border-collapse: collapse; margin: 16px 0; width: 100%; font-size: 13px;
}
.topic-detail .topic-content th, .topic-detail .topic-content td {
  border: 1px solid var(--border); padding: 8px 10px; text-align: left;
}
.topic-detail .topic-content th { background: var(--bg-3); font-weight: 600; }
.topic-detail .topic-content code {
  background: var(--code-bg); padding: 2px 6px; border-radius: 4px;
  font-family: 'JetBrains Mono', 'SF Mono', Menlo, monospace; font-size: 0.9em;
}
.topic-detail .topic-content blockquote {
  border-left: 3px solid var(--accent); padding: 8px 14px; color: var(--text-dim);
  margin: 12px 0; background: var(--bg-3); border-radius: 0 6px 6px 0;
}
.topic-detail .topic-content hr {
  border: none; border-top: 1px solid var(--border); margin: 24px 0;
}

/* ===== Old chapter header (kept for legacy chapter pages) ===== */
.chapter-header.legacy { padding: 32px 0; border-bottom: 1px solid var(--border); margin-bottom: 32px; }
.chapter-header.legacy h1 { font-size: 40px; font-weight: 800; letter-spacing: -0.03em; margin-bottom: 8px; }
.chapter-header.legacy .meta { color: var(--text-dim); font-size: 15px; }
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

footer {
  margin-top: 64px; padding: 32px;
  border-top: 1px solid var(--border);
  color: var(--text-dim); font-size: 13px;
  text-align: center;
}
footer a { color: var(--text-dim); }
footer a:hover { color: var(--accent); }

@media (max-width: 900px) {
  header.site { gap: 12px; }
  header.site .stats { order: 3; width: 100%; justify-content: flex-start; }
  header.site .chapter-dropdown { margin-left: 0; }
  .chapter-page { grid-template-columns: 1fr; }
  .chapter-sidebar { position: static; max-height: 400px; }
  .chapters-grid { grid-template-columns: 1fr; }
}
"""


def chapter_dropdown_html(current_ch_slug=None, current_dav_num=None):
    """Build the 32-chapter dropdown HTML — shows Davidson 25th Ed numbering."""
    items = []
    for dav_num, name, built_slug in DAVIDSON_25TH:
        # Show the canonical Davidson chapter number, not the MedSea slug prefix
        display_num = str(dav_num)
        is_live = built_slug and built_slug in BUILT_CHAPTERS
        if is_live:
            href = f"/{built_slug}/"
            # Prefer the user-facing chapter name from BUILT_CHAPTERS for live items
            display_name = BUILT_CHAPTERS[built_slug][0]
            badge = '<span class="badge">●</span>'
            active = "active" if built_slug == current_ch_slug else ""
            onclick = ""
            cls = f"item {active}".strip()
        else:
            href = "#"
            display_name = name
            badge = '<span class="badge">○</span>'
            active = ""
            onclick = " onclick=\"event.preventDefault();\""
            cls = "item soon"
        items.append(
            f'<a class="{cls}"{onclick} href="{href}">'
            f'<span class="num">{display_num}</span>'
            f'<span class="name">{display_name}</span>'
            f'{badge}</a>'
        )
    return items


def page_header(title, current_ch_slug=None, stats=None):
    dropdown_items = chapter_dropdown_html(current_ch_slug=current_ch_slug)
    # Stats pill bar
    if stats is None:
        stats = []
    stats_html = ""
    for num, label in stats:
        stats_html += f'<span class="stat"><span class="num">{num}</span><span class="label">{label}</span></span>'

    # Find current chapter display
    if current_ch_slug and current_ch_slug in BUILT_CHAPTERS:
        ch_display = BUILT_CHAPTERS[current_ch_slug][0]
        btn_label = f'<span class="current-ch">{ch_display}</span> <span class="arrow">▾</span>'
    else:
        btn_label = '<span>Chapters</span> <span class="arrow">▾</span>'

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
  <div class="logo-wrap">
    <span class="logo">⚕</span>
    <a href="/">MedSea</a>
  </div>
  <div class="stats">{stats_html}</div>
  <div class="chapter-dropdown" id="chapterDropdown">
    <button class="drop-btn" type="button" onclick="document.getElementById('chapterDropdown').classList.toggle('open')">
      {btn_label}
    </button>
    <div class="drop-menu">
      {''.join(dropdown_items)}
    </div>
  </div>
  <div class="ext-links">
    <a href="https://github.com/SeaXen/MedSea" target="_blank">GitHub ↗</a>
  </div>
</header>
<main>
"""


def page_footer():
    return f"""</main>
<footer>
  <p>MedSea · Sea Knowledge Medical Library · <a href="https://github.com/SeaXen/MedSea" target="_blank">github.com/SeaXen/MedSea</a></p>
  <p style="margin-top:8px;opacity:0.6">Generated {datetime.now().strftime("%Y-%m-%d %H:%M UTC")} · Davidson 25th Ed</p>
</footer>
<script>
// Close dropdown when clicking outside
document.addEventListener('click', function(e) {{
  const dd = document.getElementById('chapterDropdown');
  if (dd && !dd.contains(e.target)) dd.classList.remove('open');
}});
</script>
</body>
</html>
"""


# ------------------------ Markdown rendering ------------------------

CALLOUT_RE = re.compile(r"<callout[^>]*>(.*?)</callout>", re.DOTALL)
FRONTMATTER_RE = re.compile(r"^---\s*\n.*?\n---\s*\n", re.DOTALL)


def clean_md(text: str) -> str:
    text = CALLOUT_RE.sub(lambda m: "> " + m.group(1).strip().replace("\n", "\n> "), text)
    text = FRONTMATTER_RE.sub("", text)
    text = re.sub(r"<br\s*/?>", "\n", text)
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


# ------------------------ Chapter data + asset copy ------------------------

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


# ------------------------ Page writers ------------------------

def write_index(site_data):
    # Compute global stats
    total_topics = sum(d["n_topics"] for d in site_data.values())
    total_pngs = sum(d["n_pngs"] for d in site_data.values())
    total_hubs = sum(d["n_hubs"] for d in site_data.values())
    n_built = sum(1 for d in site_data.values() if d["n_topics"] > 0)

    stats = [
        (n_built, "Chapters"),
        (total_hubs, "Hubs"),
        (total_topics, "Topics"),
        (total_pngs, "PNGs"),
        (32, "Total (25th)"),
    ]
    html = page_header("MedSea · Sea Knowledge Medical Library", stats=stats)
    html += '<div class="section-title">Built Chapters · Davidson 25th Edition</div>\n'
    html += '<div class="chapters-grid">\n'

    for ch_slug, (ch_name, ch_url, ch_color) in BUILT_CHAPTERS.items():
        info = site_data.get(ch_slug)
        if not info or info["n_topics"] == 0:
            continue
        ch_display_num = ch_slug.split("-")[0]
        html += f"""
<article class="chapter-card" style="--accent-color: {ch_color}" onclick="location.href='/{ch_slug}/'" role="button" tabindex="0">
  <span class="ch-num">Ch {ch_display_num}</span>
  <h2>{ch_name}</h2>
  <div class="ch-stats">
    <div class="cs"><span class="num">{info['n_hubs']}</span><span class="label">Hubs</span></div>
    <div class="cs"><span class="num">{info['n_topics']}</span><span class="label">Topics</span></div>
  </div>
  <div class="ch-links">
    <a href="/{ch_slug}/" class="ch-link-primary">Browse →</a>
    <a href="{ch_url}" target="_blank" onclick="event.stopPropagation()" class="ch-link-secondary">Notion ↗</a>
  </div>
</article>
"""
    html += "</div>"
    html += page_footer()
    (SITE / "index.html").write_text(html)
    print(f"  Wrote index.html ({total_topics} topics across {n_built} chapters)")


def write_chapter_spa(ch_slug, ch_name, ch_url, ch_color, info):
    """Build chapter SPA with sidebar (topics) | main (topic content)."""
    ch_display_num = ch_slug.split("-")[0]
    stats = [
        (info["n_hubs"], "Hubs"),
        (info["n_topics"], "Topics"),
        (info["n_pngs"], "PNGs"),
    ]
    html = page_header(f"{ch_name} · MedSea", current_ch_slug=ch_slug, stats=stats)

    # Build sidebar items grouped by hub
    sidebar_html = ""
    topics_for_manifest = []  # for topics.json

    for hub_num in sorted(info["by_hub"].keys()):
        hub_topics = sorted(info["by_hub"][hub_num], key=lambda t: t["local_prefix"])
        hub_name = info["hub_names"].get(hub_num, hub_num)
        sidebar_html += f'<div class="hub-group" data-hub="{hub_num}">\n'
        sidebar_html += f'  <h3>{hub_num} · {hub_name}</h3>\n'
        for t in hub_topics:
            title = t["slug"].replace("-", " ").title()
            if t["folder"]:
                png_rel = f"diseases/{t['folder']}/topic.png"
                md_rel = f"diseases/{t['folder']}/topic.md"
            else:
                png_rel = f"diseases/{t['local_prefix']}-{t['slug']}.png"
                md_rel = f"diseases/{t['local_prefix']}-{t['slug']}.md"
            sidebar_html += f'  <a class="topic-item" data-topic="{t["local_prefix"]}" data-hub="{hub_num}" href="?topic={t["local_prefix"]}"><span class="num">{t["local_prefix"]}</span>{title}</a>\n'
            topics_for_manifest.append({
                "local_prefix": t["local_prefix"],
                "hub_num": hub_num,
                "hub_name": hub_name,
                "slug": t["slug"],
                "title": title,
                "png": png_rel if (SITE / ch_slug / png_rel).exists() else None,
                "md": md_rel if (SITE / ch_slug / md_rel).exists() else None,
            })
        sidebar_html += '</div>\n'

    # Pre-render all topic HTML and embed in topics.json for instant loading
    manifest = {
        "chapter": ch_slug,
        "chapter_name": ch_name,
        "notion_url": ch_url,
        "accent_color": ch_color,
        "topics": [],
    }
    for t in topics_for_manifest:
        md_text = ""
        if t["md"]:
            md_path = SITE / ch_slug / t["md"]
            if md_path.exists():
                md_text = md_path.read_text(encoding="utf-8")
        md_html = render_md_to_html(md_text) if md_text else "<p><em>No text content available for this topic.</em></p>"
        manifest["topics"].append({**t, "html": md_html})

    (SITE / ch_slug / "topics.json").write_text(json.dumps(manifest, ensure_ascii=False))

    # Build the page
    html += f"""
<div class="chapter-page" style="--accent-color: {ch_color}">
  <aside class="chapter-sidebar">
    <input type="text" class="search" id="topicSearch" placeholder="Search topics…">
    <div class="no-results" id="noResults">No matching topics</div>
    {sidebar_html}
  </aside>
  <section class="chapter-main">
    <div class="chapter-header">
      <h1>{ch_name}</h1>
      <div class="meta">Davidson Ch {ch_display_num} · {info['n_hubs']} hubs · {info['n_topics']} topics · <a href="{ch_url}" target="_blank">Notion ↗</a></div>
    </div>
    <div id="topicContainer" class="topic-detail-placeholder">
      <div class="placeholder">
        <div class="icon">📖</div>
        <p>Select a topic from the sidebar to view its content.</p>
        <p style="font-size:12px; margin-top:8px;">Or pick a chapter from the header dropdown.</p>
      </div>
    </div>
  </section>
</div>
<script>
const CHAPTER_SLUG = "{ch_slug}";
const MANIFEST_URL = "/{ch_slug}/topics.json";
let MANIFEST = null;
let CURRENT_TOPIC = null;

async function loadManifest() {{
  const res = await fetch(MANIFEST_URL);
  MANIFEST = await res.json();
  // Activate topic from URL hash
  const params = new URLSearchParams(location.search);
  const t = params.get("topic");
  if (t) showTopic(t);
}}

function navigateTopic(dir) {{
  if (!MANIFEST || !CURRENT_TOPIC) return;
  const i = MANIFEST.topics.findIndex(x => x.local_prefix === CURRENT_TOPIC.local_prefix);
  const ni = i + dir;
  if (ni < 0 || ni >= MANIFEST.topics.length) return;
  showTopic(MANIFEST.topics[ni].local_prefix);
}}

function toggleTopicImage(btn) {{
  btn.classList.toggle("collapsed");
  const wrap = btn.nextElementSibling;
  if (wrap) wrap.classList.toggle("collapsed");
  if (wrap && !wrap.classList.contains("collapsed")) {{
    btn.querySelector("span:last-child").textContent = "click to collapse";
  }} else {{
    btn.querySelector("span:last-child").textContent = "click to expand";
  }}
}}

function showTopic(localPrefix) {{
  const t = MANIFEST.topics.find(x => x.local_prefix === localPrefix);
  if (!t) return;
  CURRENT_TOPIC = t;
  // Update active in sidebar
  document.querySelectorAll(".topic-item").forEach(el => el.classList.remove("active"));
  const activeEl = document.querySelector(`.topic-item[data-topic="${{localPrefix}}"]`);
  if (activeEl) {{
    activeEl.classList.add("active");
    // Scroll into view
    activeEl.scrollIntoView({{ block: "nearest", behavior: "smooth" }});
  }}
  // Update URL
  const url = new URL(location.href);
  url.searchParams.set("topic", localPrefix);
  history.replaceState(null, "", url);
  // Render content
  const container = document.getElementById("topicContainer");
  container.className = "topic-detail";
  const imgHtml = t.png ? `
    <div class="topic-image-toggle collapsed" onclick="toggleTopicImage(this)">
      <span><span class="toggle-icon">▼</span> &nbsp;Show infographic image</span>
      <span style="font-size:12px;color:var(--text-dim)">click to expand</span>
    </div>
    <div class="topic-image-wrap collapsed">
      <div class="topic-image"><img src="/{ch_slug}/${{t.png}}" alt="${{t.title}}"></div>
    </div>` : "";
  container.innerHTML = `
    <div class="crumbs"><a href="/">Home</a> · <a href="/{ch_slug}/">{ch_name}</a> · <span>${{t.hub_num}} · ${{t.hub_name}}</span></div>
    <div class="topic-header">
      <div>
        <h1>${{t.title}}</h1>
        <p class="meta">${{t.hub_num}} · ${{t.local_prefix}} · ${{t.slug}}</p>
      </div>
      <div class="topic-actions">
        ${{t.png ? `<a href="/{ch_slug}/${{t.png}}" download>Download PNG</a>` : ""}}
        ${{t.md ? `<a href="/{ch_slug}/${{t.md}}" download>Download MD</a>` : ""}}
        <button onclick="navigateTopic(-1)">← Prev</button>
        <button onclick="navigateTopic(1)">Next →</button>
      </div>
    </div>
    <div class="topic-content">${{t.html}}</div>
    ${{imgHtml}}
  `;
}}

// Sidebar search filter
document.getElementById("topicSearch").addEventListener("input", function(e) {{
  const q = e.target.value.toLowerCase();
  let visible = 0;
  document.querySelectorAll(".topic-item").forEach(el => {{
    const text = el.textContent.toLowerCase();
    const show = !q || text.includes(q);
    el.style.display = show ? "" : "none";
    if (show) visible++;
  }});
  // Hide empty hub groups
  document.querySelectorAll(".hub-group").forEach(g => {{
    const anyVisible = Array.from(g.querySelectorAll(".topic-item")).some(el => el.style.display !== "none");
    g.style.display = anyVisible ? "" : "none";
  }});
  document.getElementById("noResults").classList.toggle("show", visible === 0);
}});

loadManifest();
</script>
"""
    html += page_footer()
    out = SITE / ch_slug / "index.html"
    out.write_text(html)
    print(f"  Wrote {ch_slug}/index.html (SPA, {len(info['by_hub'])} hubs, {info['n_topics']} topics)")


# ------------------------ Main ------------------------

_README_MD = """# MedSea Static Site

Auto-generated by `scripts/site/build_site.py`.

**Live:** Docker (port 8855) · Vercel (via `vercel.json`)

## Structure

- `index.html` — landing page (no hero, chapter grid)
- `<chapter-slug>/index.html` — chapter SPA (sidebar + main)
- `<chapter-slug>/topics.json` — manifest of all topics in that chapter
- `<chapter-slug>/diseases/<topic-folder-or-file>/` — topic PNGs + MDs

## Build

```bash
python3 scripts/site/build_site.py
```

## Deploy

**Docker (port 8855):**
```bash
docker build -t medsea-site .
docker run -d --name medsea --restart unless-stopped -p 0.0.0.0:8855:8855 medsea-site
```

**Vercel:**
```bash
vercel deploy --prod
```

## Chapters (14 live of 32)

| Ch | Slug | Topics | Live |
|---|---|---|---|
| 1  | 1-clinical-decision-making | 6 | ✅ |
| 2  | 2-clinical-therapeutics | 71 | ✅ |
| 3  | 3-clinical-genetics | 6 | ✅ |
| 4  | 4-clinical-immunology | 2 | ✅ |
| 5  | 5-nutritional-factors | 35 | ✅ |
| 6  | 6-population-health | 27 | ✅ |
| 7  | 7-principles-of-infection | 26 | ✅ |
| 8  | 8-oncology | 119 | ✅ |
| 9  | 9-palliative-care | 51 | ✅ |
| 15 | 15-nephrology-urology | 49 | ✅ |
| 16 | 16-cardiology | 330 | ✅ |
| 17 | 17-respiratory-medicine | 149 | ✅ |
| 18 | 18-endocrinology | 87 | ✅ |
| 21 | 21-gastroenterology | 147 | ✅ |

Source: [github.com/SeaXen/MedSea](https://github.com/SeaXen/MedSea)
"""


def main():
    if SITE.exists():
        shutil.rmtree(SITE)
    SITE.mkdir(parents=True)
    (SITE / "assets").mkdir()
    # Re-create README.md (was just deleted by rmtree)
    (SITE / "README.md").write_text(_README_MD)

    site_data = {}
    for ch_slug in BUILT_CHAPTERS.keys():
        print(f"\nProcessing {ch_slug}...")
        info = chapter_summary(ch_slug)
        site_data[ch_slug] = info
        if info["n_topics"] == 0:
            print(f"  No topics found, skipping")
            continue
        n = copy_assets(ch_slug, info)
        print(f"  Copied {n} PNGs to site/{ch_slug}/")
        ch_name, ch_url, ch_color = BUILT_CHAPTERS[ch_slug]
        write_chapter_spa(ch_slug, ch_name, ch_url, ch_color, info)

    write_index(site_data)

    total_size = sum(p.stat().st_size for p in SITE.rglob("*") if p.is_file())
    print(f"\n✓ Site generated at {SITE}  ({total_size / 1024 / 1024:.1f} MB total)")


if __name__ == "__main__":
    main()
