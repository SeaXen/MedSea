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
        "https://medsea.notion.site/Chapter-19-Clinical-biochemistry-and-metabolic-medicine-184c380212d94c48a17cd879d941e6a3",
        "#06b6d4",
    ),
    "21-diabetes-mellitus": (
        "Diabetes Mellitus",
        "https://medsea.notion.site/Chapter-21-Diabetes-mellitus-e6939ea1fa3d417684fa442a673efdb5",
        "#dc2626",
    ),
    "23-hepatology": (
        "Hepatology",
        "https://medsea.notion.site/Chapter-23-Hepatology-b916d8dadff6444ab8431495bf91c539",
        "#a16207",
    ),
    "24-haematology-and-transfusion-medicine": (
        "Haematology & Transfusion Medicine",
        "https://medsea.notion.site/Chapter-24-Haematology-and-transfusion-medicine-3b59159ad1ab47f0bd3e1fb51a9bca44",
        "#be123c",
    ),
    "25-rheumatology-and-bone-disease": (
        "Rheumatology & Bone Disease",
        "https://medsea.notion.site/Chapter-25-Rheumatology-and-bone-disease-fbf3e71640a44890849068e40a85a5a9",
        "#7c2d12",
    ),
    "26-dermatology": (
        "Dermatology",
        "https://medsea.notion.site/Chapter-26-Dermatology-02211b2a0d9f42f4844a043a7c5edde0",
        "#ec4899",
    ),
    "27-neurology-and-stroke-medicine": (
        "Neurology & Stroke Medicine",
        "https://medsea.notion.site/Chapter-27-Neurology-and-stroke-medicine-c76acd09ed434a7885ffa0dd59cecb03",
        "#8b5cf6",
    ),
    "28-medical-ophthalmology": (
        "Medical Ophthalmology",
        "https://medsea.notion.site/Chapter-28-Medical-ophthalmology-ff44045a4cab42f2be7e4b35d4dd606a",
        "#0ea5e9",
    ),
    "29-medical-psychiatry": (
        "Medical Psychiatry",
        "https://medsea.notion.site/Chapter-29-Medical-psychiatry-9d121dc4548f4f489db76e48579a34e9",
        "#6366f1",
    ),
    "30-maternal-medicine": (
        "Maternal Medicine",
        "https://medsea.notion.site/Chapter-30-Maternal-medicine-4091353758324bbb9c6a5307754989f5",
        "#d946ef",
    ),
    "31-adolescence-transition-and-young-adult-m": (
        "Adolescence Transition & Young Adult Medicine",
        "https://medsea.notion.site/Chapter-31-Adolescence-transition-and-young-adult-medicine-7a36823752104013a5a37adc48747b5d",
        "#f97316",
    ),
    "32-older-adult-medicine-and-frailty": (
        "Older Adult Medicine & Frailty",
        "https://medsea.notion.site/Chapter-32-Older-adult-medicine-and-frailty-ed39c5f1c1714a779458a32c3e8f7a2c",
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
  padding: 8px 24px;
  display: flex; align-items: center;
  flex-wrap: nowrap;
  min-height: 48px;
}
header.site .header-inner {
  display: grid;
  grid-template-columns: 1fr auto 1fr;
  align-items: center;
  gap: 16px;
  max-width: 1600px; width: 100%;
  margin: 0 auto;
}
header.site .header-left { display: flex; align-items: center; gap: 16px; justify-self: start; }
header.site .header-right { display: flex; align-items: center; gap: 12px; justify-self: end; }
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

/* ===== Universal search ===== */
header.site .search-box {
  position: relative;
  flex: 1 1 auto;
  max-width: 480px;
  margin: 0 auto;
}
header.site .search-box input {
  width: 100%;
  padding: 6px 12px 6px 32px;
  font-size: 12px;
  font-family: inherit;
  background: var(--bg-3) url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 16 16' fill='%2394a3b8'><path d='M11.5 11.5 14 14M7 12a5 5 0 1 1 0-10 5 5 0 0 1 0 10z' stroke='%2394a3b8' stroke-width='1.4' fill='none' stroke-linecap='round'/></svg>") no-repeat 9px center;
  background-size: 14px 14px;
  border: 1px solid var(--border-2);
  border-radius: 7px;
  color: var(--text);
  outline: none;
  transition: border-color 0.15s, box-shadow 0.15s;
}
header.site .search-box input:focus {
  border-color: var(--accent);
  box-shadow: 0 0 0 2px rgba(56, 189, 248, 0.18);
}
header.site .search-box input::placeholder { color: var(--text-dim); }
header.site .search-box .search-results {
  position: fixed;
  left: 16px;
  right: 16px;
  top: 56px;
  max-width: 520px;
  margin: 0 auto;
  background: var(--bg-2);
  border: 1px solid var(--border-2);
  border-radius: 9px;
  box-shadow: 0 16px 48px rgba(0,0,0,0.5);
  max-height: calc(100vh - 72px);
  overflow-y: auto;
  z-index: 999;
  display: none;
}
header.site .search-box.open .search-results { display: block; }
header.site .search-box .search-hit {
  display: flex;
  align-items: center;
  gap: 10px;
  padding: 8px 12px;
  text-decoration: none !important;
  color: var(--text) !important;
  border-bottom: 1px solid var(--border);
  transition: background 0.1s;
}
header.site .search-box .search-hit:last-child { border-bottom: none; }
header.site .search-box .search-hit:hover,
header.site .search-box .search-hit.active {
  background: var(--bg-3);
}
header.site .search-box .search-hit .hit-ch {
  flex-shrink: 0;
  min-width: 30px;
  padding: 2px 5px;
  background: var(--bg-3);
  border: 1px solid var(--border);
  border-radius: 4px;
  font-size: 9px;
  text-align: center;
  color: var(--accent);
  font-weight: 600;
}
header.site .search-box .search-hit .hit-body {
  flex: 1;
  min-width: 0;
  display: flex;
  flex-direction: column;
  gap: 2px;
}
header.site .search-box .search-hit .hit-title {
  font-size: 13px;
  font-weight: 500;
  color: var(--text);
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}
header.site .search-box .search-hit .hit-title mark,
header.site .search-box .search-hit .hit-meta mark {
  background: rgba(56, 189, 248, 0.25);
  color: var(--accent);
  padding: 0 1px;
  border-radius: 2px;
}
header.site .search-box .search-hit .hit-meta {
  font-size: 10px;
  color: var(--text-dim);
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}
header.site .search-box .search-hit .hit-arrow {
  color: var(--text-dim);
  font-size: 14px;
  flex-shrink: 0;
}
header.site .search-box .search-empty,
header.site .search-box .search-more {
  padding: 14px;
  text-align: center;
  color: var(--text-dim);
  font-size: 12px;
}
header.site .search-box .search-empty strong { color: var(--accent); }
@media (max-width: 720px) {
  /* Tablet: tighten search */
  header.site .search-box { max-width: 180px; margin: 0 6px; }
  header.site .search-box input { font-size: 11px; }
}

/* ===========================================================
   MOBILE-ONLY LAYOUT — completely separate from desktop.
   Desktop elements (header-left/right, .search-box in header)
   are hidden here. A dedicated .mobile-bar is shown instead.
   This block MUST NOT contain desktop styles.
   =========================================================== */

/* Mobile bar is hidden on desktop */
.mobile-bar { display: none; }

/* Mobile bar wrapper */
.mobile-bar {
  width: 100%;
  background: var(--bg-2);
  border-bottom: 1px solid var(--border);
  padding: 10px 12px;
  display: none;
  flex-direction: column;
  gap: 8px;
  position: sticky;
  top: 0;
  z-index: 200;
}

.mobile-bar .row {
  display: flex;
  align-items: center;
  gap: 8px;
  width: 100%;
}

.mobile-bar .row.top {
  justify-content: space-between;
}

.mobile-bar .logo-mini {
  display: flex;
  align-items: center;
  gap: 8px;
  font-weight: 700;
  font-size: 16px;
  color: var(--text);
}
.mobile-bar .logo-mini .logo {
  color: var(--accent);
  font-size: 20px;
}

.mobile-bar .stats-mini {
  display: flex;
  gap: 6px;
  font-size: 10px;
  color: var(--text-dim);
}
.mobile-bar .stats-mini .stat {
  background: var(--bg-3);
  padding: 3px 7px;
  border-radius: 10px;
  white-space: nowrap;
}
.mobile-bar .stats-mini .stat .num {
  color: var(--accent);
  font-weight: 700;
  margin-right: 3px;
}

.mobile-bar .menu-btn,
.mobile-bar .github-btn {
  background: var(--bg-3);
  border: 1px solid var(--border);
  color: var(--text);
  padding: 8px 10px;
  border-radius: 8px;
  font-size: 13px;
  cursor: pointer;
  display: flex;
  align-items: center;
  gap: 4px;
  text-decoration: none;
  white-space: nowrap;
}
.mobile-bar .menu-btn:hover,
.mobile-bar .github-btn:hover {
  background: var(--bg-4);
  color: var(--accent);
}

.mobile-bar .current-ch-label {
  font-size: 12px;
  color: var(--accent);
  font-weight: 600;
}

.mobile-bar .search-row .search-box-m {
  position: relative;
  flex: 1;
}
.mobile-bar .search-row input {
  width: 100%;
  background: var(--bg-3);
  border: 1px solid var(--border);
  color: var(--text);
  padding: 9px 12px 9px 32px;
  border-radius: 8px;
  font-size: 13px;
  outline: none;
  box-sizing: border-box;
}
.mobile-bar .search-row input:focus {
  border-color: var(--accent);
}
.mobile-bar .search-row .search-icon {
  position: absolute;
  left: 10px;
  top: 50%;
  transform: translateY(-50%);
  color: var(--text-dim);
  font-size: 13px;
  pointer-events: none;
}
.mobile-bar .search-row .search-results {
  position: absolute;
  top: 100%;
  left: 0;
  right: 0;
  margin-top: 4px;
  background: var(--bg-2);
  border: 1px solid var(--border);
  border-radius: 8px;
  max-height: 60vh;
  overflow-y: auto;
  display: none;
  z-index: 300;
  box-shadow: 0 4px 12px rgba(0,0,0,0.4);
}
.mobile-bar .search-row .search-results.open {
  display: block;
}
.mobile-bar .search-row .result-item {
  padding: 10px 12px;
  border-bottom: 1px solid var(--border);
  cursor: pointer;
  font-size: 13px;
  display: flex;
  flex-direction: column;
  gap: 2px;
}
.mobile-bar .search-row .result-item:hover,
.mobile-bar .search-row .result-item.active {
  background: var(--bg-3);
}
.mobile-bar .search-row .result-item:last-child {
  border-bottom: none;
}
.mobile-bar .search-row .result-item .badge {
  display: inline-block;
  background: var(--accent);
  color: #fff;
  padding: 1px 6px;
  border-radius: 4px;
  font-size: 9px;
  font-weight: 700;
  align-self: flex-start;
}
.mobile-bar .search-row .result-item .crumb {
  color: var(--text-dim);
  font-size: 10px;
}
.mobile-bar .search-row .result-item mark {
  background: var(--accent);
  color: #fff;
  padding: 0 2px;
  border-radius: 2px;
}

/* Mobile chapter menu drawer */
.mobile-menu {
  display: none;
  position: fixed;
  inset: 0;
  background: rgba(0,0,0,0.6);
  z-index: 400;
}
.mobile-menu.open { display: block; }
.mobile-menu .panel {
  position: absolute;
  top: 0;
  right: 0;
  bottom: 0;
  width: 280px;
  max-width: 85vw;
  background: var(--bg-2);
  border-left: 1px solid var(--border);
  padding: 16px 12px;
  overflow-y: auto;
  box-shadow: -4px 0 16px rgba(0,0,0,0.5);
}
.mobile-menu .panel h3 {
  margin: 0 0 12px;
  color: var(--text);
  font-size: 14px;
  text-transform: uppercase;
  letter-spacing: 0.08em;
  color: var(--text-dim);
}
.mobile-menu .panel a {
  display: flex;
  align-items: center;
  gap: 8px;
  padding: 10px 12px;
  color: var(--text);
  text-decoration: none;
  border-radius: 6px;
  font-size: 13px;
  border: 1px solid transparent;
}
.mobile-menu .panel a:hover,
.mobile-menu .panel a.active {
  background: var(--bg-3);
  border-color: var(--accent);
  color: var(--accent);
}
.mobile-menu .panel a.soon {
  opacity: 0.5;
  cursor: default;
}
.mobile-menu .panel a .num {
  color: var(--accent);
  font-weight: 700;
  min-width: 28px;
  flex-shrink: 0;
}
.mobile-menu .panel a .name {
  flex: 1;
}
.mobile-menu .panel a .badge {
  color: var(--accent);
  font-size: 10px;
}
.mobile-menu .close-btn {
  position: absolute;
  top: 8px;
  right: 8px;
  background: var(--bg-3);
  border: 1px solid var(--border);
  color: var(--text);
  width: 32px;
  height: 32px;
  border-radius: 6px;
  cursor: pointer;
  font-size: 16px;
}

/* Mobile chapter page: stacked layout */
/* ===== Chapter page layout (DESKTOP: sidebar + main) ===== */
.chapter-page {
  display: grid;
  grid-template-columns: 320px 1fr;
  gap: 0;
  min-height: calc(100vh - 65px);
}

/* Desktop sidebar: hub/topic navigation */
.chapter-sidebar {
  background: var(--bg-2);
  border-right: 1px solid var(--border);
  padding: 20px 16px;
  overflow-y: auto;
  max-height: calc(100vh - 65px);
  position: sticky;
  top: 65px;
}
.chapter-sidebar .search {
  width: 100%;
  padding: 8px 12px;
  background: var(--bg-3);
  border: 1px solid var(--border);
  border-radius: 8px;
  color: var(--text);
  font-size: 13px;
  font-family: inherit;
  margin-bottom: 12px;
}
.chapter-sidebar .search:focus {
  outline: none;
  border-color: var(--accent);
}
.chapter-sidebar .hub-group {
  margin-bottom: 14px;
}
.chapter-sidebar .hub-group h3 {
  font-size: 11px;
  color: var(--accent);
  text-transform: uppercase;
  letter-spacing: 0.08em;
  padding: 6px 8px;
  margin: 0 0 4px;
  font-weight: 700;
  background: rgba(56, 189, 248, 0.06);
  border-left: 2px solid var(--accent);
  border-radius: 0 4px 4px 0;
}
.chapter-sidebar .topic-item {
  display: block;
  padding: 5px 10px 5px 22px;
  border-radius: 4px;
  color: var(--text);
  font-size: 12.5px;
  font-weight: 500;
  cursor: pointer;
  transition: all 0.1s;
  border: 1px solid transparent;
  text-decoration: none !important;
  position: relative;
  line-height: 1.35;
}
.chapter-sidebar .topic-item:hover {
  background: var(--bg-3);
  color: #fff;
}
.chapter-sidebar .topic-item.active {
  background: rgba(56, 189, 248, 0.15);
  color: var(--accent);
  font-weight: 600;
  border-color: rgba(56, 189, 248, 0.3);
}
.chapter-sidebar .topic-item .num {
  font-family: 'JetBrains Mono', 'SF Mono', Menlo, monospace;
  font-size: 10px;
  margin-right: 6px;
  color: var(--text-dim);
  font-weight: 400;
}
.chapter-sidebar .topic-item.active .num {
  color: var(--accent);
  font-weight: 600;
}
.chapter-sidebar .no-results {
  color: var(--text-dim);
  font-size: 12px;
  padding: 12px 8px;
  text-align: center;
  display: none;
}
.chapter-sidebar .no-results.show {
  display: block;
}

/* Desktop main: clicked topic content */
.chapter-main {
  padding: 16px 24px;
  overflow-x: hidden;
}
.chapter-main .chapter-header {
  padding: 8px 0 10px;
  border-bottom: 1px solid var(--border);
  margin-bottom: 16px;
  border-left: 3px solid var(--accent-color, var(--accent));
  padding-left: 14px;
  display: flex;
  align-items: baseline;
  gap: 12px;
  flex-wrap: wrap;
}
.chapter-main .chapter-header h1 {
  font-size: 22px;
  font-weight: 800;
  letter-spacing: -0.02em;
  margin-bottom: 0;
  line-height: 1.2;
}
.chapter-main .chapter-header .meta {
  color: var(--text-dim);
  font-size: 12px;
  font-family: 'JetBrains Mono', 'SF Mono', Menlo, monospace;
  display: inline-flex;
  align-items: center;
  gap: 10px;
  flex-wrap: wrap;
}
.chapter-main .chapter-header .meta a {
  color: var(--accent);
  text-decoration: none;
}
.chapter-main .chapter-header .meta a:hover {
  text-decoration: underline;
}
.chapter-main .placeholder {
  text-align: center;
  padding: 60px 20px;
  color: var(--text-dim);
}
.chapter-main .placeholder .icon {
  font-size: 48px;
  margin-bottom: 12px;
  opacity: 0.5;
}

/* Topic detail (rendered in main pane) */
.topic-detail .crumbs {
  color: var(--text-dim);
  font-size: 12px;
  margin-bottom: 12px;
  font-family: 'JetBrains Mono', 'SF Mono', Menlo, monospace;
}
.topic-detail .crumbs a {
  color: var(--text-dim);
}
.topic-detail .crumbs a:hover {
  color: var(--accent);
}
.topic-detail .topic-header {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  margin-bottom: 20px;
  gap: 20px;
  flex-wrap: wrap;
}
.topic-detail .topic-header h1 {
  font-size: 32px;
  font-weight: 800;
  letter-spacing: -0.02em;
}
.topic-detail .topic-header .meta {
  color: var(--text-dim);
  font-size: 13px;
  margin-top: 4px;
}
.topic-detail .topic-actions {
  display: flex;
  gap: 6px;
}
.topic-detail .topic-actions a,
.topic-detail .topic-actions button {
  padding: 6px 12px;
  border-radius: 6px;
  background: var(--bg-3);
  border: 1px solid var(--border);
  color: var(--text);
  font-size: 12px;
  font-family: inherit;
  cursor: pointer;
  text-decoration: none;
}
.topic-detail .topic-actions a:hover,
.topic-detail .topic-actions button:hover {
  background: var(--bg);
  border-color: var(--accent);
  color: var(--accent);
}
.topic-detail .topic-image {
  background: var(--bg-2);
  border: 1px solid var(--border);
  border-radius: 12px;
  padding: 16px;
  margin-bottom: 20px;
}
.topic-detail .topic-image img {
  width: 100%;
  height: auto;
  display: block;
  border-radius: 6px;
}
.topic-detail .topic-image-toggle {
  display: flex;
  align-items: center;
  justify-content: space-between;
  background: var(--bg-3);
  border: 1px solid var(--border);
  border-radius: 10px;
  padding: 10px 16px;
  margin-bottom: 16px;
  cursor: pointer;
  color: var(--text-dim);
  font-size: 14px;
  font-weight: 600;
  transition: all 0.15s ease;
}
.topic-detail .topic-image-toggle:hover {
  background: var(--bg-2);
  border-color: var(--accent);
  color: var(--accent);
}
.topic-detail .topic-image-toggle .toggle-icon {
  font-size: 16px;
  transition: transform 0.2s ease;
}
.topic-detail .topic-image-toggle.collapsed .toggle-icon {
  transform: rotate(-90deg);
}
.topic-detail .topic-image-wrap {
  overflow: hidden;
}
.topic-detail .topic-image-wrap.collapsed {
  display: none;
}
.topic-detail .topic-content {
  background: var(--bg-2);
  border: 1px solid var(--border);
  border-radius: 12px;
  padding: 24px;
}
.topic-detail .topic-content h2,
.topic-detail .topic-content h3,
.topic-detail .topic-content h4 {
  margin-top: 20px;
  margin-bottom: 10px;
  font-weight: 700;
}
.topic-detail .topic-content h2 {
  font-size: 22px;
  border-bottom: 1px solid var(--border);
  padding-bottom: 6px;
}
.topic-detail .topic-content h3 {
  font-size: 18px;
  color: var(--accent);
}
.topic-detail .topic-content h4 {
  font-size: 15px;
}
.topic-detail .topic-content p {
  margin-bottom: 12px;
  color: var(--text);
}
.topic-detail .topic-content ul,
.topic-detail .topic-content ol {
  margin-left: 24px;
  margin-bottom: 12px;
}
.topic-detail .topic-content li {
  margin-bottom: 4px;
}
.topic-detail .topic-content li:empty {
  display: none;
}
.topic-detail .topic-content table {
  border-collapse: collapse;
  margin: 16px 0;
  width: 100%;
  font-size: 13px;
}
.topic-detail .topic-content th,
.topic-detail .topic-content td {
  border: 1px solid var(--border);
  padding: 8px 10px;
  text-align: left;
}
.topic-detail .topic-content th {
  background: var(--bg-3);
  font-weight: 600;
}
.topic-detail .topic-content code {
  background: var(--code-bg);
  padding: 2px 6px;
  border-radius: 4px;
  font-family: 'JetBrains Mono', 'SF Mono', Menlo, monospace;
  font-size: 0.9em;
}
.topic-detail .topic-content blockquote {
  border-left: 3px solid var(--accent);
  padding: 8px 14px;
  color: var(--text-dim);
  margin: 12px 0;
  background: var(--bg-3);
  border-radius: 0 6px 6px 0;
}
.topic-detail .topic-content hr {
  border: none;
  border-top: 1px solid var(--border);
  margin: 24px 0;
}

/* ===== Layout visibility ===== */
.d-only { display: block; }
.chapter-mobile { display: none; }

/* On mobile: hide desktop sidebar+main, show mobile accordion */
@media (max-width: 900px) {
  .d-only { display: none !important; }
  .chapter-mobile { display: block !important; }
  .chapter-page { display: block !important; grid-template-columns: 1fr !important; min-height: auto !important; }
}

.chapter-header {
  padding: 12px 0 16px;
  border-bottom: 1px solid var(--border);
  margin-bottom: 16px;
  border-left: 3px solid var(--accent-color, var(--accent));
  padding-left: 14px;
}
.chapter-page > .chapter-header h1 {
  font-size: 26px;
  font-weight: 800;
  letter-spacing: -0.02em;
  margin: 0 0 6px;
  line-height: 1.2;
  color: var(--text);
}
.chapter-page > .chapter-header .meta {
  color: var(--text-dim);
  font-size: 12px;
  font-family: 'JetBrains Mono', 'SF Mono', Menlo, monospace;
}
.chapter-page > .chapter-header .meta a {
  color: var(--accent);
  text-decoration: none;
}
.chapter-page > .chapter-header .meta a:hover {
  text-decoration: underline;
}

.chapter-toolbar {
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
  align-items: center;
  margin-bottom: 16px;
  padding: 10px 12px;
  background: var(--bg-2);
  border: 1px solid var(--border);
  border-radius: 10px;
  position: sticky;
  top: 64px;
  z-index: 50;
  backdrop-filter: blur(10px);
}
.chapter-toolbar .search {
  flex: 1;
  min-width: 200px;
  background: var(--bg-3);
  border: 1px solid var(--border);
  color: var(--text);
  padding: 9px 12px;
  border-radius: 7px;
  font-size: 13px;
  outline: none;
  box-sizing: border-box;
}
.chapter-toolbar .search:focus {
  border-color: var(--accent);
  box-shadow: 0 0 0 2px rgba(56, 189, 248, 0.18);
}
.chapter-toolbar .toolbar-actions {
  display: flex;
  gap: 6px;
}
.chapter-toolbar .btn-acc {
  background: var(--bg-3);
  border: 1px solid var(--border);
  color: var(--text);
  padding: 7px 12px;
  border-radius: 7px;
  font-size: 12px;
  cursor: pointer;
  white-space: nowrap;
  transition: all 0.15s;
}
.chapter-toolbar .btn-acc:hover {
  background: var(--bg-4);
  color: var(--accent);
  border-color: var(--accent);
}
.chapter-toolbar .no-results {
  flex-basis: 100%;
  color: var(--text-dim);
  font-size: 12px;
  text-align: center;
  padding: 6px;
  display: none;
}
.chapter-toolbar .no-results.show {
  display: block;
}

/* Hub accordion */
.hub-accordion {
  display: flex;
  flex-direction: column;
  gap: 8px;
}
.hub-acc {
  background: var(--bg-2);
  border: 1px solid var(--border);
  border-radius: 10px;
  overflow: hidden;
  transition: border-color 0.15s;
}
.hub-acc[open] {
  border-color: var(--accent-color, var(--accent));
  box-shadow: 0 2px 12px rgba(0, 0, 0, 0.2);
}
.hub-summary {
  list-style: none;
  cursor: pointer;
  padding: 14px 16px;
  display: flex;
  align-items: center;
  gap: 12px;
  user-select: none;
  transition: background 0.15s;
  background: var(--bg-2);
}
.hub-summary:hover {
  background: var(--bg-3);
}
.hub-summary::-webkit-details-marker {
  display: none;
}
.hub-arrow {
  color: var(--accent);
  font-size: 14px;
  transition: transform 0.2s;
  display: inline-block;
  width: 14px;
}
.hub-acc[open] > .hub-summary .hub-arrow {
  transform: rotate(90deg);
}
.hub-num {
  font-family: 'JetBrains Mono', 'SF Mono', Menlo, monospace;
  font-size: 11px;
  color: var(--accent);
  background: rgba(56, 189, 248, 0.1);
  border: 1px solid rgba(56, 189, 248, 0.25);
  padding: 2px 6px;
  border-radius: 4px;
  font-weight: 600;
  margin-right: 8px;
}
.hub-label {
  flex: 1;
  font-size: 14px;
  font-weight: 600;
  color: var(--text);
}
.hub-count {
  font-family: 'JetBrains Mono', 'SF Mono', Menlo, monospace;
  font-size: 11px;
  color: var(--text-dim);
  background: var(--bg-3);
  padding: 3px 8px;
  border-radius: 10px;
  font-weight: 600;
}

.hub-body {
  padding: 4px 12px 12px;
  display: flex;
  flex-direction: column;
  gap: 4px;
  background: var(--bg);
  border-top: 1px solid var(--border);
}

/* Topic accordion */
.topic-acc {
  background: var(--bg-2);
  border: 1px solid transparent;
  border-radius: 8px;
  margin-left: 14px;
  transition: all 0.15s;
  position: relative;
}
.topic-acc::before {
  content: '';
  position: absolute;
  left: -10px;
  top: 24px;
  width: 8px;
  height: 1px;
  background: var(--border);
}
.topic-acc:hover {
  background: var(--bg-3);
  border-color: var(--border);
}
.topic-acc[open] {
  background: var(--bg-3);
  border-color: var(--accent-color, var(--accent));
  box-shadow: 0 1px 8px rgba(0, 0, 0, 0.15);
}
.topic-summary {
  list-style: none;
  cursor: pointer;
  padding: 10px 14px;
  display: flex;
  align-items: center;
  gap: 10px;
  user-select: none;
  border-radius: 8px;
}
.topic-summary::-webkit-details-marker {
  display: none;
}
.topic-arrow {
  color: var(--text-dim);
  font-size: 12px;
  transition: transform 0.2s;
  display: inline-block;
  width: 12px;
}
.topic-acc[open] > .topic-summary .topic-arrow {
  transform: rotate(90deg);
  color: var(--accent);
}
.topic-num {
  font-family: 'JetBrains Mono', 'SF Mono', Menlo, monospace;
  font-size: 10px;
  color: var(--text-dim);
  background: var(--bg-3);
  border: 1px solid var(--border);
  padding: 2px 6px;
  border-radius: 4px;
  font-weight: 600;
  flex-shrink: 0;
  min-width: 48px;
  text-align: center;
}
.topic-acc[open] > .topic-summary .topic-num {
  color: var(--accent);
  border-color: var(--accent);
  background: rgba(56, 189, 248, 0.08);
}
.topic-title {
  flex: 1;
  font-size: 13px;
  font-weight: 500;
  color: var(--text);
  line-height: 1.35;
}

.topic-body {
  padding: 12px 16px 18px;
  border-top: 1px solid var(--border);
  background: var(--bg);
  margin-top: 6px;
  border-radius: 0 0 8px 8px;
}
.topic-content {
  font-size: 14px;
  line-height: 1.65;
  color: var(--text);
}
.topic-content h1 { font-size: 22px; margin: 16px 0 10px; color: var(--accent); }
.topic-content h2 { font-size: 18px; margin: 16px 0 8px; color: var(--accent); border-left: 3px solid var(--accent); padding-left: 10px; }
.topic-content h3 { font-size: 15px; margin: 14px 0 6px; color: var(--text); }
.topic-content p { margin: 8px 0; }
.topic-content ul, .topic-content ol { margin: 8px 0; padding-left: 24px; }
.topic-content li { margin: 4px 0; }
.topic-content pre {
  background: var(--bg-3);
  border: 1px solid var(--border);
  padding: 10px 12px;
  border-radius: 6px;
  overflow-x: auto;
  font-size: 12px;
}
.topic-content code {
  background: var(--bg-3);
  padding: 1px 5px;
  border-radius: 3px;
  font-size: 12px;
}
.topic-content pre code {
  background: transparent;
  padding: 0;
}
.topic-content table {
  border-collapse: collapse;
  margin: 10px 0;
  font-size: 13px;
  width: 100%;
}
.topic-content th, .topic-content td {
  border: 1px solid var(--border);
  padding: 6px 10px;
  text-align: left;
}
.topic-content th {
  background: var(--bg-3);
  font-weight: 600;
}
.topic-content blockquote {
  border-left: 3px solid var(--accent);
  padding: 8px 14px;
  margin: 10px 0;
  background: var(--bg-2);
  border-radius: 0 6px 6px 0;
  color: var(--text-dim);
}
.topic-content img {
  max-width: 100%;
  border-radius: 6px;
}

/* Topic image toggle (collapsible) */
.topic-image-toggle {
  margin-top: 12px;
  padding: 10px 12px;
  background: var(--bg-2);
  border: 1px solid var(--border);
  border-radius: 8px;
  cursor: pointer;
  display: flex;
  justify-content: space-between;
  align-items: center;
  font-size: 13px;
  color: var(--accent);
  transition: background 0.15s;
}
.topic-image-toggle:hover {
  background: var(--bg-3);
}
.topic-image-toggle .toggle-icon {
  display: inline-block;
  transition: transform 0.2s;
}
.topic-image-toggle:not(.collapsed) .toggle-icon {
  transform: rotate(180deg);
}
.topic-image-wrap {
  margin-top: 8px;
  overflow: hidden;
  max-height: 5000px;
  transition: max-height 0.4s ease;
}
.topic-image-wrap.collapsed {
  max-height: 0;
  margin-top: 0;
}
.topic-image {
  background: var(--bg-2);
  border: 1px solid var(--border);
  border-radius: 8px;
  padding: 8px;
}
.topic-image img {
  width: 100%;
  height: auto;
  display: block;
  border-radius: 4px;
}

/* Old legacy classes (kept for backward compat with existing topics.json users) */
.chapter-sidebar {
  position: sticky;
  top: 80px;
  max-height: calc(100vh - 100px);
  overflow-y: auto;
  background: var(--bg-2);
  border: 1px solid var(--border);
  border-radius: 10px;
  padding: 14px;
}

@media (max-width: 900px) {
  /* On mobile: hide desktop elements, show mobile bar */
  header.site { display: none; }
  .mobile-bar { display: flex; }

  /* Single column chapter page */
  .chapter-page { padding: 12px 12px 60px; }

  /* Accordion: tighter on mobile */
  .hub-summary { padding: 12px 14px; }
  .hub-label { font-size: 13px; }
  .topic-acc { margin-left: 8px; }
  .topic-summary { padding: 9px 12px; }
  .topic-title { font-size: 12px; }
  .topic-num { font-size: 9px; min-width: 42px; }
  .topic-body { padding: 10px 12px 14px; }
  .topic-content { font-size: 13px; line-height: 1.55; }
  .topic-content h1 { font-size: 18px; }
  .topic-content h2 { font-size: 16px; }
  .topic-content h3 { font-size: 14px; }
  .topic-content pre { font-size: 11px; padding: 8px 10px; }
  .chapter-toolbar { position: static; }
  .chapter-toolbar .search { font-size: 12px; padding: 8px 10px; }
  .chapter-toolbar .btn-acc { font-size: 11px; padding: 6px 10px; }

  /* Compact 2-col grid */
  .chapters-grid { grid-template-columns: repeat(2, 1fr); gap: 8px; }
  .ch-card { padding: 12px 6px; border-radius: 8px; }
  .ch-card .ch-num { font-size: 20px; }
  .ch-card .ch-title { font-size: 11px; line-height: 1.3; }
  .ch-card .ch-meta { font-size: 9px; }

  /* Index page header */
  .index-hero h1 { font-size: 26px; }
  .index-hero p { font-size: 14px; }
  .index-stats { gap: 16px; flex-wrap: wrap; }
  .stat-pill { font-size: 12px; padding: 6px 12px; }

  /* Topic page */
  .topic-page { padding: 12px; }
  .topic-page h1 { font-size: 22px; }
  .topic-page h2 { font-size: 18px; }
  .topic-page h3 { font-size: 15px; }
  .topic-page pre { font-size: 11px; padding: 10px; }
  .topic-page table { font-size: 12px; }

  /* Back-to-top button */
  .back-top { bottom: 12px; right: 12px; padding: 8px 12px; font-size: 12px; }
}

@media (max-width: 380px) {
  /* Tiny phones: 2-col stays but tighter */
  .chapters-grid { grid-template-columns: repeat(2, 1fr); gap: 6px; }
  .ch-card { padding: 10px 4px; }
  .ch-card .ch-num { font-size: 18px; }
  .ch-card .ch-title { font-size: 10px; }
  .mobile-bar .stats-mini { display: none; }
}

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
main {
  padding: 28px 24px 64px;
  max-width: 1640px;
  margin: 0 auto;
}
.chapters-grid {
  display: grid;
  grid-template-columns: repeat(5, 1fr);
  gap: 12px;
  margin-top: 8px;
}
@media (max-width: 1500px) { .chapters-grid { grid-template-columns: repeat(4, 1fr); } }
@media (max-width: 1200px) { .chapters-grid { grid-template-columns: repeat(3, 1fr); } }
@media (max-width: 850px)  { .chapters-grid { grid-template-columns: repeat(2, 1fr); } }
@media (max-width: 550px)  { .chapters-grid { grid-template-columns: repeat(2, 1fr); } }
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
  align-items: center; justify-content: flex-start;
  text-align: center;
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
  align-self: center;
}
.chapter-card h2 {
  font-size: 15px; font-weight: 700; letter-spacing: -0.01em;
  margin-bottom: 10px; line-height: 1.25;
  flex: 1; text-align: center;
}
.chapter-card .ch-stats {
  display: flex; gap: 12px; padding: 8px 0; border-top: 1px solid var(--border);
  font-family: 'JetBrains Mono', 'SF Mono', Menlo, monospace; font-size: 12px;
  justify-content: center;
}
.chapter-card .ch-stats .cs { display: flex; flex-direction: column; align-items: center; }
.chapter-card .ch-stats .num { font-size: 16px; font-weight: 700; color: var(--accent); line-height: 1; text-align: center; }
.chapter-card .ch-stats .label { font-size: 9px; color: var(--text-dim); text-transform: uppercase; letter-spacing: 0.06em; margin-top: 2px; text-align: center; }
.chapter-card .ch-links {
  display: flex; gap: 12px; margin-top: 8px;
  font-size: 11px; justify-content: center;
}
.chapter-card .ch-link-primary {
  color: var(--accent); font-weight: 600; text-decoration: none !important;
}
.chapter-card .ch-link-secondary {
  color: var(--text-dim); text-decoration: none !important;
}
.chapter-card .ch-link-primary:hover { color: #7dd3fc; }
.chapter-card .ch-link-secondary:hover { color: var(--accent); }

/* ===== Chapter accordion SPA (replaces old sidebar+main layout) ===== */

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

/* ===== Mermaid mindmap & flowchart (rendered as styled HTML) ===== */
.topic-detail .topic-content .mindmap {
  background: linear-gradient(135deg, #fff8e7 0%, #fdf3e0 100%);
  border: 1px solid #c9a96e;
  border-radius: 6px; padding: 10px 12px 12px; margin: 12px 0;
  text-align: center; overflow-x: auto;
}
.topic-detail .topic-content .mm-root {
  display: inline-block;
  font-size: 14px; font-weight: 800; color: #8b3a3a;
  background: #fff; border: 2px solid #8b3a3a; border-radius: 14px;
  padding: 4px 16px; margin: 0 auto 8px; letter-spacing: 0.3px;
}
.topic-detail .topic-content .mm-branches {
  display: flex; flex-wrap: wrap; gap: 8px; justify-content: center;
  align-items: flex-start; margin-top: 6px;
}
.topic-detail .topic-content .mm-branch {
  background: #fff; border: 1px solid #5a7a5a; border-radius: 6px;
  padding: 6px 8px 8px; min-width: 120px; flex: 1 1 auto; max-width: 240px;
}
.topic-detail .topic-content .mm-l1 {
  font-size: 12px; font-weight: 800; color: #8b3a3a;
  text-align: center; border-bottom: 1px solid #d4a574;
  padding-bottom: 4px; margin-bottom: 5px; letter-spacing: 0.3px;
}
.topic-detail .topic-content .mm-l2 {
  font-size: 11px; color: #1f2937; padding: 2px 0;
  border-left: 2px solid #5a7a5a; padding-left: 6px; margin: 2px 0;
  text-align: left;
}
.topic-detail .topic-content .mm-l3, .topic-detail .topic-content .mm-deep {
  font-size: 10px; color: #4b5563; padding-left: 10px; line-height: 1.3;
  text-align: left;
}
.topic-detail .topic-content .flowchart {
  background: linear-gradient(135deg, #f5f0e2 0%, #ece1c8 100%);
  border: 1px solid #b8a878; border-radius: 6px;
  padding: 10px 10px 12px; margin: 12px 0; text-align: center;
  overflow-x: auto;
}
.topic-detail .topic-content .fc-title {
  font-size: 10px; font-weight: 800; color: #6b5d3f;
  letter-spacing: 1.2px; text-transform: uppercase; margin-bottom: 6px;
}
.topic-detail .topic-content .fc-level {
  display: flex; flex-wrap: wrap; gap: 6px; justify-content: center;
  align-items: center; margin: 4px 0;
}
.topic-detail .topic-content .fc-node {
  background: #fff; border: 1.5px solid #8b3a3a; color: #1f2937;
  border-radius: 5px; padding: 4px 10px;
  font-size: 11px; font-weight: 700; display: inline-block;
  letter-spacing: 0.2px; line-height: 1.3; max-width: 200px;
  text-align: center;
}
.topic-detail .topic-content .fc-arrows {
  color: #8b3a3a; font-size: 14px; font-weight: 700;
  margin: 2px 0; letter-spacing: 4px;
}
.topic-detail .topic-content .codeblock {
  background: var(--code-bg); border: 1px solid var(--border);
  border-radius: 6px; padding: 12px 14px; margin: 10px 0;
  overflow-x: auto;
}
.topic-detail .topic-content .codeblock code {
  background: transparent; padding: 0; font-size: 12px;
  color: var(--text); font-family: 'JetBrains Mono', 'SF Mono', Menlo, monospace;
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
    ch_display = ''
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
  <div class="header-inner">
    <div class="header-left">
      <div class="logo-wrap">
        <span class="logo">⚕</span>
        <a href="/">MedSea</a>
      </div>
      <div class="stats">{stats_html}</div>
    </div>
    <div class="search-box" id="searchBox">
      <input type="text" id="searchInput" placeholder="Search 2,957 topics…" autocomplete="off" spellcheck="false">
      <div class="search-results" id="searchResults"></div>
    </div>
    <div class="header-right">
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
    </div>
  </div>
</header>
<!-- MOBILE-ONLY BAR — hidden on desktop via CSS, shown via @media (max-width: 900px) -->
<div class="mobile-bar">
  <div class="row top">
    <div class="logo-mini">
      <span class="logo">⚕</span>
      <a href="/">MedSea</a>
    </div>
    <button class="menu-btn" type="button" onclick="document.getElementById('mobileMenu').classList.add('open')">☰ Chapters</button>
  </div>
  <div class="row search-row">
    <div class="search-box-m" id="searchBoxMobile">
      <span class="search-icon">🔍</span>
      <input type="text" id="searchInputMobile" placeholder="Search topics…" autocomplete="off" spellcheck="false">
      <div class="search-results" id="searchResultsMobile"></div>
    </div>
  </div>
  <div class="row" style="justify-content: space-between; font-size: 11px; color: var(--text-dim);">
    {('<span class="current-ch-label">'+ch_display+'</span>') if current_ch_slug else '<span></span>'}
    <a class="github-btn" href="https://github.com/SeaXen/MedSea" target="_blank">GitHub ↗</a>
  </div>
</div>

<!-- MOBILE-ONLY CHAPTER MENU DRAWER -->
<div class="mobile-menu" id="mobileMenu" onclick="if(event.target===this) this.classList.remove('open')">
  <div class="panel">
    <button class="close-btn" type="button" onclick="document.getElementById('mobileMenu').classList.remove('open')">✕</button>
    <h3>Chapters</h3>
    {''.join(dropdown_items)}
  </div>
</div>
<script>
// ===== Universal topic search =====
(function() {{
  let idx = null;
  let debounce = null;
  const input = document.getElementById('searchInput');
  const results = document.getElementById('searchResults');
  const box = document.getElementById('searchBox');

  function loadIdx() {{
    if (idx) return Promise.resolve(idx);
    return fetch('/search_index.json').then(r => r.json()).then(d => {{ idx = d; return d; }});
  }}

  function escHtml(s) {{
    return s.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
  }}

  function highlight(text, q) {{
    if (!q) return escHtml(text);
    const i = text.toLowerCase().indexOf(q.toLowerCase());
    if (i < 0) return escHtml(text);
    return escHtml(text.slice(0, i)) + '<mark>' + escHtml(text.slice(i, i + q.length)) + '</mark>' + escHtml(text.slice(i + q.length));
  }}

  function search(q) {{
    loadIdx().then(data => {{
      const ql = q.toLowerCase();
      const hits = [];
      // Score: title-prefix > title-contains > hub > chapter
      for (const item of data) {{
        const t = item.title.toLowerCase();
        const h = item.hub_name.toLowerCase();
        const c = item.chapter_name.toLowerCase();
        let score = 0;
        if (t === ql) score = 100;
        else if (t.startsWith(ql)) score = 80;
        else if (t.includes(ql)) score = 60;
        else if (h.includes(ql)) score = 40;
        else if (c.includes(ql)) score = 20;
        if (item.topic && item.topic.startsWith(ql)) score = Math.max(score, 70);
        if (score > 0) hits.push({{ item, score }});
      }}
      hits.sort((a, b) => b.score - a.score || a.item.title.localeCompare(b.item.title));
      const top = hits.slice(0, 20);
      if (top.length === 0) {{
        results.innerHTML = '<div class="search-empty">No topics match "<strong>' + escHtml(q) + '</strong>"</div>';
      }} else {{
        results.innerHTML = top.map(h => {{
          const it = h.item;
          return '<a class="search-hit" href="' + it.url + '?topic=' + encodeURIComponent(it.topic) + '">' +
            '<span class="hit-ch">' + it.chapter_num + '</span>' +
            '<span class="hit-body">' +
              '<span class="hit-title">' + highlight(it.title, q) + '</span>' +
              '<span class="hit-meta">' + highlight(it.chapter_name, q) + ' · ' + highlight(it.hub_name, q) + ' · ' + it.topic + '</span>' +
            '</span>' +
            '<span class="hit-arrow">→</span>' +
          '</a>';
        }}).join('');
        if (hits.length > 20) {{
          results.innerHTML += '<div class="search-more">+' + (hits.length - 20) + ' more matches…</div>';
        }}
      }}
      box.classList.add('open');
    }}).catch(err => {{
      results.innerHTML = '<div class="search-empty">Search index unavailable.</div>';
      box.classList.add('open');
    }});
  }}

  input.addEventListener('input', function(e) {{
    clearTimeout(debounce);
    const q = e.target.value.trim();
    if (q.length < 2) {{
      results.innerHTML = '';
      box.classList.remove('open');
      return;
    }}
    debounce = setTimeout(() => search(q), 120);
  }});

  input.addEventListener('focus', function(e) {{
    if (e.target.value.trim().length >= 2) box.classList.add('open');
  }});

  // Close on outside click
  document.addEventListener('click', function(e) {{
    if (!box.contains(e.target)) box.classList.remove('open');
  }});

  // Close on Escape
  input.addEventListener('keydown', function(e) {{
    if (e.key === 'Escape') {{
      input.value = '';
      results.innerHTML = '';
      box.classList.remove('open');
      input.blur();
    }}
  }});

  // Keyboard nav: ArrowDown/Up, Enter
  let activeIdx = -1;
  input.addEventListener('keydown', function(e) {{
    const hits = results.querySelectorAll('.search-hit');
    if (e.key === 'ArrowDown') {{
      e.preventDefault();
      activeIdx = Math.min(activeIdx + 1, hits.length - 1);
      hits.forEach((h, i) => h.classList.toggle('active', i === activeIdx));
      if (hits[activeIdx]) hits[activeIdx].scrollIntoView({{ block: 'nearest' }});
    }} else if (e.key === 'ArrowUp') {{
      e.preventDefault();
      activeIdx = Math.max(activeIdx - 1, 0);
      hits.forEach((h, i) => h.classList.toggle('active', i === activeIdx));
      if (hits[activeIdx]) hits[activeIdx].scrollIntoView({{ block: 'nearest' }});
    }} else if (e.key === 'Enter' && activeIdx >= 0 && hits[activeIdx]) {{
      e.preventDefault();
      hits[activeIdx].click();
    }}
  }});
}})();

// ===== Mobile search (separate code, doesn't touch desktop) =====
(function() {{
  const input = document.getElementById('searchInputMobile');
  const results = document.getElementById('searchResultsMobile');
  const box = document.getElementById('searchBoxMobile');
  if (!input) return;

  let sharedIdx = null;
  let debounce = null;
  let activeIdx = -1;
  let hits = [];

  function loadIdx() {{
    if (sharedIdx) return Promise.resolve(sharedIdx);
    return fetch('/search_index.json').then(r => r.json()).then(d => {{ sharedIdx = d; return d; }});
  }}

  function escHtml(s) {{
    return s.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
  }}

  function highlight(text, q) {{
    if (!q) return escHtml(text);
    const i = text.toLowerCase().indexOf(q.toLowerCase());
    if (i < 0) return escHtml(text);
    return escHtml(text.slice(0, i)) + '<mark>' + escHtml(text.slice(i, i + q.length)) + '</mark>' + escHtml(text.slice(i + q.length));
  }}

  function search(q) {{
    loadIdx().then(data => {{
      const ql = q.toLowerCase();
      hits = [];
      for (const item of data) {{
        const t = item.title.toLowerCase();
        const h = item.hub_name.toLowerCase();
        const c = item.chapter_name.toLowerCase();
        let score = 0;
        if (t === ql) score = 100;
        else if (t.startsWith(ql)) score = 80;
        else if (t.includes(ql)) score = 60;
        else if (h.includes(ql)) score = 40;
        else if (c.includes(ql)) score = 20;
        if (item.topic && item.topic.startsWith(ql)) score = Math.max(score, 70);
        if (score > 0) hits.push({{ item, score }});
      }}
      hits.sort((a, b) => b.score - a.score || a.item.title.localeCompare(b.item.title));
      const top = hits.slice(0, 30);
      activeIdx = -1;
      if (top.length === 0) {{
        results.innerHTML = '<div class="result-item" style="cursor:default;color:var(--text-dim);">No topics match "<strong style="color:var(--accent)">' + escHtml(q) + '</strong>"</div>';
      }} else {{
        results.innerHTML = top.map(h => {{
          const it = h.item;
          return '<a class="result-item" href="' + it.url + '?topic=' + encodeURIComponent(it.topic) + '">' +
            '<span class="badge">Ch ' + it.chapter_num + '</span>' +
            '<span>' + highlight(it.title, q) + '</span>' +
            '<span class="crumb">' + highlight(it.chapter_name, q) + ' · ' + it.topic + '</span>' +
          '</a>';
        }}).join('');
      }}
      results.classList.add('open');
    }}).catch(err => {{
      results.innerHTML = '<div class="result-item" style="cursor:default;color:var(--text-dim);">Search index unavailable.</div>';
      results.classList.add('open');
    }});
  }}

  input.addEventListener('input', function(e) {{
    clearTimeout(debounce);
    const q = e.target.value.trim();
    if (q.length < 2) {{
      results.classList.remove('open');
      results.innerHTML = '';
      return;
    }}
    debounce = setTimeout(() => search(q), 150);
  }});

  input.addEventListener('focus', function() {{
    if (input.value.trim().length >= 2) results.classList.add('open');
  }});

  document.addEventListener('click', function(e) {{
    if (!box.contains(e.target)) {{
      results.classList.remove('open');
    }}
  }});

  input.addEventListener('keydown', function(e) {{
    const items = results.querySelectorAll('.result-item');
    if (e.key === 'ArrowDown') {{
      e.preventDefault();
      activeIdx = Math.min(activeIdx + 1, items.length - 1);
      items.forEach((it, i) => it.classList.toggle('active', i === activeIdx));
      if (items[activeIdx]) items[activeIdx].scrollIntoView({{ block: 'nearest' }});
    }} else if (e.key === 'ArrowUp') {{
      e.preventDefault();
      activeIdx = Math.max(activeIdx - 1, 0);
      items.forEach((it, i) => it.classList.toggle('active', i === activeIdx));
      if (items[activeIdx]) items[activeIdx].scrollIntoView({{ block: 'nearest' }});
    }} else if (e.key === 'Enter' && activeIdx >= 0 && items[activeIdx]) {{
      e.preventDefault();
      items[activeIdx].click();
    }} else if (e.key === 'Escape') {{
      results.classList.remove('open');
      input.blur();
    }}
  }});
}})();
</script>
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


# ----- Mermaid mindmap/flowchart helpers (ported from render_topic.py) -----

def _esc(s: str) -> str:
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def _extract_label(lbl: str) -> str:
    """Extract clean text from a Mermaid node label like '[X]', '{{X}}', '{X}'.
    Handles malformed hexagons like '{{X} Y}' (mismatched braces) by extracting the
    content between the first pair of balanced braces."""
    if not lbl:
        return lbl
    # Try cleanest outer wrappers first
    for opener, closer in [("{{", "}}"), ("[[", "]]"), ("[(", ")]"),
                           ("{", "}"), ("[", "]"), ("(", ")")]:
        if lbl.startswith(opener) and lbl.endswith(closer):
            inner = lbl[len(opener):-len(closer)]
            return _extract_label(inner)  # recurse in case of nested
    # Malformed: count braces
    if lbl.count("{") >= 1 and lbl.count("}") >= 1:
        m = re.search(r"\{([^{}]*)\}", lbl)
        if m:
            return m.group(1).strip()
    # Fallback: strip first and last char if they're brackets
    if lbl and lbl[0] in "[({<" and lbl[-1] in "])}>":
        return lbl[1:-1].strip()
    return lbl.strip()


def render_mindmap_md(text: str) -> str:
    """Convert mermaid mindmap to a styled tree (matches PNG infographic layout)."""
    lines = [l for l in text.split("\n") if l.strip()]
    items = []
    for line in lines:
        if line.strip().lower().startswith("mindmap"):
            continue
        stripped = line.lstrip()
        raw_indent = len(line) - len(stripped)
        indent = raw_indent // 2
        # Treat first non-mindmap line as root regardless of indent
        if "((" in stripped:
            m = re.search(r"\(\((.+?)\)\)", stripped)
            text_v = m.group(1) if m else stripped
        else:
            text_v = stripped
        items.append((indent, text_v))
    if not items:
        return ""
    # First item is always the root; rebadge others by depth from first
    html = ['<div class="mindmap">']
    html.append(f'<div class="mm-root">{_esc(items[0][1])}</div>')
    html.append('<div class="mm-branches">')
    current_branch = None
    # Compute relative depth (treat first item's indent as 0 for branch structure)
    root_indent = items[0][0]
    for indent, text_v in items[1:]:
        rel = max(1, indent - root_indent)
        if rel == 1:
            if current_branch is not None:
                html.append('</div>')
            html.append('<div class="mm-branch">')
            html.append(f'<div class="mm-node mm-l1">{_esc(text_v)}</div>')
            current_branch = rel
        elif rel == 2:
            html.append(f'<div class="mm-node mm-l2">{_esc(text_v)}</div>')
        elif rel == 3:
            html.append(f'<div class="mm-node mm-l3">– {_esc(text_v)}</div>')
        else:
            html.append(f'<div class="mm-node mm-deep">– {_esc(text_v)}</div>')
    if current_branch is not None:
        html.append('</div>')
    html.append('</div>')
    html.append('</div>')
    return "\n".join(html)


def render_flowchart_md(text: str) -> str:
    """Convert mermaid flowchart/graph to a styled diagram."""
    from collections import deque
    # Pre-process: join multi-line edge labels and node labels
    # Strategy: walk lines, accumulate until we find a complete edge (with proper closure)
    raw_lines = text.split("\n")
    lines = []
    buf = []
    for ln in raw_lines:
        s = ln.strip()
        if not s or s.lower().startswith(("flowchart", "graph")):
            if buf:
                lines.append(" ".join(buf))
                buf = []
            if s:
                lines.append(s)
            continue
        # If line has `-->`, we have an edge. If buf non-empty, this is continuation
        buf.append(s)
        # Check if the line ends with a node closure: `]`, `}`, `)` or a node id at end
        # Heuristic: if the line ends with a closing bracket or has a complete right side
        # The "end of edge" is when we see a closing bracket on the right of `-->` (with optional edge label)
        # Simpler: check if there's an unbalanced bracket
        combined = " ".join(buf)
        # Count brackets
        sq_open = combined.count("[") - combined.count("]")
        curly_open = combined.count("{") - combined.count("}")
        paren_open = combined.count("(") - combined.count(")")
        pipe_open = combined.count("|") - combined.count("|") if combined.count("|") % 2 == 0 else 1
        if sq_open == 0 and curly_open == 0 and paren_open == 0 and pipe_open == 0:
            lines.append(combined)
            buf = []
    if buf:
        lines.append(" ".join(buf))

    direction = "TD"
    nodes = {}
    edges = []
    for line in lines:
        s = line.strip()
        if s.lower().startswith("flowchart") or s.lower().startswith("graph"):
            parts = s.split()
            if len(parts) > 1:
                direction = parts[1].upper()
            continue
        # Edge line: capture src, dst, and any labels/edge text up to end of line
        s_stripped = s.rstrip()
        # Try to find a ` --> ` or ` --- ` separator
        arrow_m = re.search(r"\s*(?:-->|---|--[->o]+)\s*", s_stripped)
        if arrow_m:
            left = s_stripped[:arrow_m.start()].strip()
            right_with_label = s_stripped[arrow_m.end():].strip()
            # Edge label like |text|
            edge_label = None
            edge_lbl_m = re.match(r"^\|([^|]*)\|\s*", right_with_label)
            if edge_lbl_m:
                edge_label = edge_lbl_m.group(1)
                right_with_label = right_with_label[edge_lbl_m.end():]
            # Parse left and right as `<id><label?>` where label is any non-space chars
            def parse_node(text):
                m = re.match(r"^([A-Za-z0-9_]+)(.*)$", text)
                if not m:
                    return None, None
                return m.group(1), m.group(2)
            from_id, from_label_raw = parse_node(left)
            to_id, to_label_raw = parse_node(right_with_label)
            from_label = from_label_raw.strip() if from_label_raw else None
            to_label = to_label_raw.strip() if to_label_raw else None
            # Skip edges with missing endpoints (e.g., multi-line labels)
            if not from_id or not to_id:
                continue
            # Process labels
            for ref, lbl in [(from_id, from_label), (to_id, to_label)]:
                if lbl:
                    inner = _extract_label(lbl)
                    nodes[ref] = inner.strip() if inner else ref
                else:
                    nodes.setdefault(ref, ref)
            edges.append((from_id, to_id, edge_label or ""))
            continue
        # Fallback: try original node_m pattern
        node_m = re.match(r"^([A-Za-z0-9_]+)\s*(\[\[.+?\]\]|\[\(.+?\)\]|\{\{.*?\}\}|\[[^\]]+\]|\([^)]+\)|\{[^}]+\}|>[^<]+<)$", s)
        if node_m:
            nid, nlabel = node_m.groups()
            inner = _extract_label(nlabel)
            nodes[nid] = inner.strip() if inner else nid
    if not nodes:
        return f'<pre class="codeblock"><code>{_esc(text)}</code></pre>'

    adj = {nid: [] for nid in nodes}
    for f, t, lbl in edges:
        adj.setdefault(f, []).append((t, lbl))
        adj.setdefault(t, [])
    incoming = {nid: 0 for nid in nodes}
    for f, t, _ in edges:
        incoming[t] = incoming.get(t, 0) + 1
    roots = [nid for nid, cnt in incoming.items() if cnt == 0]
    if not roots:
        roots = [next(iter(nodes))]

    levels = {}
    queue = deque()
    for r in roots:
        levels[r] = 0
        queue.append(r)
    while queue:
        nid = queue.popleft()
        for t, _ in adj.get(nid, []):
            if t not in levels:
                levels[t] = levels[nid] + 1
                queue.append(t)
    max_level = max(levels.values()) if levels else 0
    by_level = {}
    for nid, lv in levels.items():
        by_level.setdefault(lv, []).append(nid)

    html = [f'<div class="flowchart" data-dir="{direction}">']
    html.append('<div class="fc-title">⬇ Clinical Pathway</div>')
    for lv in range(max_level + 1):
        level_nodes = by_level.get(lv, [])
        html.append('<div class="fc-level">')
        for nid in level_nodes:
            label = nodes.get(nid, nid) or nid
            if not isinstance(label, str):
                label = str(label)
            html.append(f'<div class="fc-node" data-id="{nid}">{_esc(label)}</div>')
        html.append('</div>')
        if lv < max_level:
            html.append('<div class="fc-arrows">↓</div>')
    html.append('</div>')
    return "\n".join(html)


def _synthesize_mindmap_from_headings(md_text: str) -> str:
    """If MD has no mermaid/mindmap/flowchart block, build a mindmap from H1/H2/H3.

    Returns empty string if no usable structure is found.
    """
    headings = []  # (level, text)
    for line in md_text.split("\n"):
        m = re.match(r"^(#{1,6})\s+(.+?)\s*$", line)
        if m:
            level = len(m.group(1))
            text = m.group(2).strip()
            # Strip markdown emphasis and emoji-only decorations
            text = re.sub(r"\*\*(.+?)\*\*", r"\1", text)
            text = re.sub(r"\*(.+?)\*", r"\1", text)
            text = re.sub(r"`(.+?)`", r"\1", text)
            # Cap heading length
            if len(text) > 80:
                text = text[:77] + "..."
            headings.append((level, text))
    if len(headings) < 2:
        return ""
    # Build mermaid mindmap text. Root is the first H1; H2/H3 become branches.
    root = ""
    items = []  # (level, text)
    for lvl, txt in headings[:40]:  # cap to first 40
        if lvl == 1 and not root:
            root = txt
            continue
        # Only include H2/H3 for branches
        if lvl in (2, 3):
            items.append((lvl, txt))
    if not root and items:
        root = items.pop(0)[1]
    if not root:
        return ""
    # Build mermaid text
    lines = ["mindmap", f"  root(({root}))"]
    for lvl, txt in items[:30]:  # cap branches
        indent = "    " if lvl == 2 else "      "
        lines.append(f"{indent}{txt}")
    body = "\n".join(lines)
    return render_mindmap_md(body)


def render_md_to_html(md_text: str) -> str:
    md_text = clean_md(md_text)
    lines = md_text.split("\n")
    out = []
    in_ul = False
    in_ol = False
    in_table = False
    in_code = False
    code_buf = []
    code_kind = None  # 'mindmap', 'flowchart', 'graph', 'code', None
    code_fence_open = None
    table_rows = []
    found_mermaid = False  # Track whether any mermaid block was rendered

    def flush_list():
        nonlocal in_ul, in_ol
        if in_ul:
            out.append("</ul>"); in_ul = False
        if in_ol:
            out.append("</ol>"); in_ol = False

    def flush_code():
        nonlocal in_code, code_buf, code_kind, code_fence_open, found_mermaid
        if not in_code:
            return
        body = "\n".join(code_buf)
        if code_kind in ("mindmap",):
            rendered = render_mindmap_md(body)
            found_mermaid = True
        elif code_kind in ("flowchart", "graph"):
            rendered = render_flowchart_md(body)
            found_mermaid = True
        else:
            rendered = f'<pre class="codeblock"><code>{_esc(body)}</code></pre>'
        out.append(rendered)
        in_code = False
        code_buf = []
        code_kind = None
        code_fence_open = None

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
        # Code fence detection (must run before other rules)
        fence_m = re.match(r"^(\s*)(```+|~~~+)(.*)$", line)
        if fence_m:
            indent, fence, rest = fence_m.groups()
            if not in_code:
                # Opening fence — determine kind
                in_code = True
                code_buf = []
                code_fence_open = fence[:3]
                rest_s = rest.strip().lower()
                if rest_s in ("mermaid", ""):
                    # Defer kind decision to first content line
                    code_kind = None
                elif rest_s.startswith("mermaid") or rest_s.startswith("mindmap") or rest_s.startswith("flowchart") or rest_s.startswith("graph"):
                    # Same-line declaration
                    if rest_s.startswith("mindmap") or "mindmap" in rest_s:
                        code_kind = "mindmap"
                    elif rest_s.startswith("flowchart") or rest_s.startswith("graph") or "flowchart" in rest_s or "graph" in rest_s:
                        code_kind = "flowchart"
                    else:
                        code_kind = None
                else:
                    code_kind = "code"
                continue
            else:
                # Closing fence
                if code_fence_open and fence.startswith(code_fence_open):
                    flush_code()
                else:
                    code_buf.append(line)
                continue
        if in_code:
            code_buf.append(line)
            # Detect kind from first content line
            if code_kind is None and line.strip():
                first = line.strip().lower()
                if first.startswith("mindmap"):
                    code_kind = "mindmap"
                elif first.startswith("flowchart") or first.startswith("graph "):
                    code_kind = "flowchart"
                else:
                    code_kind = "code"
            continue

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

    flush_list(); flush_table(); flush_code()

    # If no explicit mermaid/mindmap/flowchart block was rendered, synthesize
    # a mindmap from the MD's heading structure so every topic gets a visual.
    if not found_mermaid:
        synth = _synthesize_mindmap_from_headings(md_text)
        if synth:
            out.append('<h2>Topic Overview</h2>')
            out.append(synth)

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
    """Build chapter SPA with desktop sidebar+main AND mobile-only accordion.

    Desktop (default):
      <div class="chapter-page">
        <aside class="chapter-sidebar">  # hub/topic nav + search
        <section class="chapter-main">   # clicked topic content (loaded via JS)
      </div>

    Mobile (≤900px):
      Sidebar+main hidden, accordion tree with all topics inline (no fetch).
    """
    ch_display_num = ch_slug.split("-")[0]
    stats = [
        (info["n_hubs"], "Hubs"),
        (info["n_topics"], "Topics"),
        (info["n_pngs"], "PNGs"),
    ]
    html = page_header(f"{ch_name} · MedSea", current_ch_slug=ch_slug, stats=stats)

    # ---- First pass: render topic HTML, build manifest + sidebar + accordion ----
    topics_for_manifest = []
    rendered_topics = {}  # local_prefix -> (md_html, png_rel, t_data)
    sidebar_html = ""
    accordion_html = ""

    for hub_num in sorted(info["by_hub"].keys()):
        hub_topics = sorted(info["by_hub"][hub_num], key=lambda t: t["local_prefix"])
        hub_name = info["hub_names"].get(hub_num, hub_num)
        # Sidebar hub group
        sidebar_html += f'<div class="hub-group" data-hub="{hub_num}">\n'
        sidebar_html += f'  <h3>{hub_num} · {hub_name}</h3>\n'
        # Accordion hub group
        n_topics = len(hub_topics)
        accordion_html += f'<details class="hub-acc" data-hub="{hub_num}">\n'
        accordion_html += f'  <summary class="hub-summary">\n'
        accordion_html += f'    <span class="hub-arrow">▸</span>\n'
        accordion_html += f'    <span class="hub-label"><span class="hub-num">{hub_num}</span> {hub_name}</span>\n'
        accordion_html += f'    <span class="hub-count">{n_topics}</span>\n'
        accordion_html += f'  </summary>\n'
        accordion_html += f'  <div class="hub-body">\n'
        for t in hub_topics:
            title = t["slug"].replace("-", " ").title()
            if t["folder"]:
                png_rel = f"diseases/{t['folder']}/topic.png"
                md_rel = f"diseases/{t['folder']}/topic.md"
            else:
                png_rel = f"diseases/{t['local_prefix']}-{t['slug']}.png"
                md_rel = f"diseases/{t['local_prefix']}-{t['slug']}.md"
            png_exists = (SITE / ch_slug / png_rel).exists()
            md_exists = (SITE / ch_slug / md_rel).exists()
            t_data = {
                "local_prefix": t["local_prefix"],
                "hub_num": hub_num,
                "hub_name": hub_name,
                "slug": t["slug"],
                "title": title,
                "png": png_rel if png_exists else None,
                "md": md_rel if md_exists else None,
            }
            topics_for_manifest.append(t_data)
            md_text = (SITE / ch_slug / md_rel).read_text(encoding="utf-8") if md_exists else ""
            md_html = render_md_to_html(md_text) if md_text else "<p><em>No text content available for this topic.</em></p>"
            rendered_topics[t["local_prefix"]] = (md_html, png_rel if png_exists else None, t_data)
            # Sidebar link (desktop navigation)
            sidebar_html += f'  <a class="topic-item" data-topic="{t["local_prefix"]}" data-hub="{hub_num}" href="?topic={t["local_prefix"]}"><span class="num">{t["local_prefix"]}</span>{title}</a>\n'
            # Accordion topic (mobile inline)
            img_html = ""
            if png_exists:
                img_html = f'''
    <div class="topic-image-toggle collapsed" onclick="toggleTopicImage(this)">
      <span><span class="toggle-icon">▼</span> &nbsp;Show infographic image</span>
      <span style="font-size:11px;color:var(--text-dim)">click to expand</span>
    </div>
    <div class="topic-image-wrap collapsed">
      <div class="topic-image"><img src="/{ch_slug}/{png_rel}" alt="{title}" loading="lazy"></div>
    </div>'''
            accordion_html += f'    <details class="topic-acc" data-topic="{t["local_prefix"]}" data-hub="{hub_num}">\n'
            accordion_html += f'      <summary class="topic-summary">\n'
            accordion_html += f'        <span class="topic-arrow">▸</span>\n'
            accordion_html += f'        <span class="topic-num">{t["local_prefix"]}</span>\n'
            accordion_html += f'        <span class="topic-title">{title}</span>\n'
            accordion_html += f'      </summary>\n'
            accordion_html += f'      <div class="topic-body">\n'
            accordion_html += f'        <div class="topic-content">{md_html}</div>\n'
            accordion_html += f'        {img_html}\n'
            accordion_html += f'      </div>\n'
            accordion_html += f'    </details>\n'
        sidebar_html += '</div>\n'
        accordion_html += f'  </div>\n'
        accordion_html += f'</details>\n'

    # Build topics.json manifest with pre-rendered HTML for instant desktop loading
    manifest = {
        "chapter": ch_slug,
        "chapter_name": ch_name,
        "notion_url": ch_url,
        "accent_color": ch_color,
        "topics": [],
    }
    for t in topics_for_manifest:
        md_html, _, _ = rendered_topics[t["local_prefix"]]
        manifest["topics"].append({**t, "html": md_html})
    (SITE / ch_slug / "topics.json").write_text(json.dumps(manifest, ensure_ascii=False))

    # Build the page: BOTH layouts in same HTML
    html += f"""
<div class="chapter-page" style="--accent-color: {ch_color}">
  <!-- DESKTOP: sidebar + main (hidden on mobile via CSS) -->
  <aside class="chapter-sidebar d-only">
    <input type="text" class="search" id="topicSearch" placeholder="Search topics…">
    <div class="no-results" id="noResults">No matching topics</div>
    {sidebar_html}
  </aside>
  <section class="chapter-main d-only">
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

  <!-- MOBILE: accordion tree (hidden on desktop via CSS) -->
  <div class="chapter-mobile m-only">
    <div class="chapter-toolbar">
      <input type="text" class="search" id="topicSearchMobile" placeholder="🔍 Search topics…">
      <div class="toolbar-actions">
        <button class="btn-acc" onclick="expandAllMobile()">Expand all</button>
        <button class="btn-acc" onclick="collapseAllMobile()">Collapse all</button>
      </div>
      <div class="no-results" id="noResultsMobile">No matching topics</div>
    </div>
    <div class="hub-accordion" id="hubAccordionMobile">
      {accordion_html}
    </div>
  </div>
</div>
<script>
const CHAPTER_SLUG = "{ch_slug}";
const MANIFEST_URL = "/{ch_slug}/topics.json";
let MANIFEST = null;
let CURRENT_TOPIC = null;

// ---- Desktop: load topics.json + sidebar nav + topic render ----
async function loadManifest() {{
  try {{
    const res = await fetch(MANIFEST_URL);
    MANIFEST = await res.json();
    const params = new URLSearchParams(location.search);
    const t = params.get("topic");
    if (t) showTopic(t);
  }} catch(e) {{
    console.error("Failed to load topics.json", e);
  }}
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
  if (wrap) {{
    wrap.classList.toggle("collapsed");
    const span = btn.querySelector("span:last-child");
    if (span) span.textContent = wrap.classList.contains("collapsed") ? "click to expand" : "click to collapse";
  }}
}}

function showTopic(localPrefix) {{
  const t = MANIFEST.topics.find(x => x.local_prefix === localPrefix);
  if (!t) return;
  CURRENT_TOPIC = t;
  document.querySelectorAll(".topic-item").forEach(el => el.classList.remove("active"));
  const activeEl = document.querySelector(`.topic-item[data-topic="${{localPrefix}}"]`);
  if (activeEl) {{
    activeEl.classList.add("active");
    activeEl.scrollIntoView({{ block: "nearest", behavior: "smooth" }});
  }}
  const url = new URL(location.href);
  url.searchParams.set("topic", localPrefix);
  history.replaceState(null, "", url);
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

document.getElementById("topicSearch").addEventListener("input", function(e) {{
  const q = e.target.value.toLowerCase();
  let visible = 0;
  document.querySelectorAll(".topic-item").forEach(el => {{
    const text = el.textContent.toLowerCase();
    const show = !q || text.includes(q);
    el.style.display = show ? "" : "none";
    if (show) visible++;
  }});
  document.querySelectorAll(".hub-group").forEach(g => {{
    const anyVisible = Array.from(g.querySelectorAll(".topic-item")).some(el => el.style.display !== "none");
    g.style.display = anyVisible ? "" : "none";
  }});
  document.getElementById("noResults").classList.toggle("show", visible === 0);
}});

loadManifest();

// ---- Mobile: accordion expand/collapse + search ----
function expandAllMobile() {{
  document.querySelectorAll("#hubAccordionMobile details").forEach(d => d.open = true);
}}
function collapseAllMobile() {{
  document.querySelectorAll("#hubAccordionMobile details").forEach(d => d.open = false);
  const p = new URL(location.href);
  p.searchParams.delete("topic");
  p.searchParams.delete("expand");
  history.replaceState(null, "", p);
}}
document.getElementById("topicSearchMobile").addEventListener("input", function(e) {{
  const q = e.target.value.trim().toLowerCase();
  let visible = 0;
  document.querySelectorAll("#hubAccordionMobile .topic-acc").forEach(el => {{
    const text = el.textContent.toLowerCase();
    const show = !q || text.includes(q);
    el.style.display = show ? "" : "none";
    if (show) {{
      visible++;
      if (q) {{
        el.open = true;
        const hub = el.closest(".hub-acc");
        if (hub) hub.open = true;
      }}
    }}
  }});
  document.querySelectorAll("#hubAccordionMobile .hub-acc").forEach(g => {{
    const anyVisible = Array.from(g.querySelectorAll(".topic-acc")).some(el => el.style.display !== "none");
    g.style.display = anyVisible ? "" : "none";
    if (!q) g.open = false;
  }});
  document.getElementById("noResultsMobile").classList.toggle("show", visible === 0);
}});

// On mobile: open topic from URL ?topic=...
(function() {{
  if (window.innerWidth > 900) return;
  const params = new URLSearchParams(location.search);
  const t = params.get("topic");
  if (t) {{
    const el = document.querySelector(`#hubAccordionMobile .topic-acc[data-topic="${{t}}"]`);
    if (el) {{
      el.open = true;
      const hub = el.closest(".hub-acc");
      if (hub) hub.open = true;
      setTimeout(() => el.scrollIntoView({{ block: "start", behavior: "smooth" }}), 100);
    }}
  }} else if (params.get("expand") === "all") {{
    document.querySelectorAll("#hubAccordionMobile details").forEach(d => d.open = true);
  }}
}})();
</script>
"""
    html += page_footer()
    out = SITE / ch_slug / "index.html"
    out.write_text(html)
    print(f"  Wrote {ch_slug}/index.html (desktop sidebar+main + mobile accordion, {len(info['by_hub'])} hubs, {info['n_topics']} topics)")


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
    write_search_index(site_data)

    total_size = sum(p.stat().st_size for p in SITE.rglob("*") if p.is_file())
    print(f"\n✓ Site generated at {SITE}  ({total_size / 1024 / 1024:.1f} MB total)")


def write_search_index(site_data):
    """Build a flat search index across all 2957 topics for the header search box."""
    items = []
    for ch_slug, (ch_name, _ch_url, _ch_color) in BUILT_CHAPTERS.items():
        info = site_data.get(ch_slug)
        if not info or info["n_topics"] == 0:
            continue
        ch_num = ch_slug.split("-")[0]
        for hub_num in sorted(info["by_hub"].keys()):
            hub_topics = sorted(info["by_hub"][hub_num], key=lambda t: t["local_prefix"])
            hub_name = info["hub_names"].get(hub_num, hub_num)
            for t in hub_topics:
                title = t["slug"].replace("-", " ").title()
                items.append({
                    "chapter_num": ch_num,
                    "chapter_name": ch_name,
                    "chapter_slug": ch_slug,
                    "hub_num": hub_num,
                    "hub_name": hub_name,
                    "topic": t["local_prefix"],
                    "title": title,
                    "url": f"/{ch_slug}/",
                })
    (SITE / "search_index.json").write_text(
        json.dumps(items, ensure_ascii=False, separators=(",", ":"))
    )
    print(f"  Wrote search_index.json ({len(items)} topics)")


if __name__ == "__main__":
    main()
