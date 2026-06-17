#!/usr/bin/env python3
"""Build MedSea backup for Nephrology & Urology (chapter 15).
Reuses cardiology chapter's structure under chapters/15-nephrology/."""
import json
import shutil
import sys
from pathlib import Path

SRC_SK = Path("/mnt/tb/Sea-knowledge/15. Nephrology and Urology")
SRC_SOURCE = Path("/mnt/tb/Medicine/Nephrology and Urology")
REPO_ROOT = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).resolve().parent.parent
DEST = REPO_ROOT / "chapters" / "15-nephrology-urology"

HUBS = [
    ("15.1", "Renal Anatomy, Physiology, and Investigations", "anatomy-physiology-investigations"),
    ("15.2", "Acute Kidney Injury and Chronic Kidney Disease", "aki-and-ckd"),
    ("15.3", "Glomerular Diseases", "glomerular-diseases"),
    ("15.4", "Tubulointerstitial, Cystic, and Inherited Renal Disorders", "tubulointerstitial-cystic-inherited"),
    ("15.5", "Urinary Tract Infection, Obstruction, and Urologic Renal Problems", "urinary-tract-uti-urology"),
    ("15.6", "Dialysis and Renal Replacement Therapy", "dialysis-and-transplant"),
]

# Load manifest from canonical topics file
with open("/root/nephro_topics.json") as f:
    canonical = json.load(f)

manifest = {
    "chapter": "15. Nephrology and Urology",
    "davidson_chapter": "Chapter 15: Nephrology and urology",
    "total_hubs": len(HUBS),
    "total_diseases": len(canonical),
    "hubs": [{"num": n, "name": name, "slug": slug, "disease_count": sum(1 for c in canonical if c["hub"] == slug)} for n, name, slug in HUBS],
    "diseases": []
}

stats = {"copied": 0, "missing_render": 0, "missing_md": 0, "md_only": 0}

# Reset destination
if DEST.exists():
    shutil.rmtree(DEST)
DEST.mkdir(parents=True)
(DEST / "hubs").mkdir()
(DEST / "diseases").mkdir()
(DEST / "source").mkdir()

# Per-hub local counter
hub_counters = {}
for x in canonical:
    hub_counters[x["hub"]] = hub_counters.get(x["hub"], 0) + 1
    local_idx = hub_counters[x["hub"]]

    hub_num, hub_name, hub_slug = next((n, nm, sl) for n, nm, sl in HUBS if sl == x["hub"])
    folder_name = f"{hub_num}.{local_idx}-{x['slug']}"
    dest = DEST / "diseases" / folder_name
    dest.mkdir(parents=True, exist_ok=True)

    # Find source disease folder in /mnt/tb/Sea-knowledge
    src_disease = None
    for hub_dir in SRC_SK.iterdir():
        if not hub_dir.is_dir() or not hub_dir.name.startswith(hub_num + "."):
            continue
        for d in hub_dir.iterdir():
            if d.is_dir() and d.name.endswith(f". {x['slug']}"):
                src_disease = d
                break
        if src_disease: break

    md_src = None
    md_html = None
    md_png = None
    if src_disease:
        md_src = src_disease / f"{x['slug']}.md"
        md_html = src_disease / f"{x['slug']}.html"
        md_png = src_disease / f"{x['slug']}.png"

    for f in [md_src, md_html, md_png]:
        if f and f.exists():
            shutil.copy2(f, dest / f.name)

    has_md = md_src and md_src.exists()
    has_png = md_png and md_png.exists()

    if not has_md:
        stats["missing_md"] += 1
    if has_md and not has_png:
        stats["md_only"] += 1
    if not has_png:
        stats["missing_render"] += 1

    if has_md:
        stats["copied"] += 1

    manifest["diseases"].append({
        "idx": x["idx"],
        "slug": x["slug"],
        "title": x["title"],
        "parent_slug": hub_slug,
        "parent_name": hub_name,
        "folder_name": folder_name,
        "has_md": has_md,
        "has_html": md_html.exists() if md_html else False,
        "has_png": has_png,
    })

# Copy source mds
for f in SRC_SOURCE.glob("*.md"):
    shutil.copy2(f, DEST / "source" / f.name)

# Write manifest
with open(DEST / "manifest.json", "w") as f:
    json.dump(manifest, f, indent=2)

# Write per-hub markdown files
for hub_num, hub_name, hub_slug in HUBS:
    hub_md = DEST / "hubs" / f"{hub_num}-{hub_slug}.md"
    hub_diseases = [d for d in manifest["diseases"] if d["parent_slug"] == hub_slug]
    with open(hub_md, "w") as f:
        f.write(f"---\n")
        f.write(f"hub: {hub_num}\n")
        f.write(f"name: {hub_name}\n")
        f.write(f"davidson_chapter: Chapter 15: Nephrology and urology\n")
        f.write(f"---\n\n")
        f.write(f"# {hub_num}. {hub_name}\n\n")
        f.write(f"Sea Knowledge disease-level notes for **{hub_name}** ({len(hub_diseases)} topics).\n\n")
        f.write("## Topics\n\n")
        for d in sorted(hub_diseases, key=lambda x: x["idx"]):
            status = "✅" if d["has_png"] else ("📝" if d["has_md"] else "❌")
            f.write(f"- {status} [{d['title']}](../diseases/{d['folder_name']}/{d['slug']}.md)\n")
    print(f"  Wrote {hub_md.name}")

# Write chapter README
with open(DEST / "README.md", "w") as f:
    f.write(f"# {manifest['chapter']}\n\n")
    f.write(f"Davidson 24e — Chapter 15: Nephrology and urology\n\n")
    f.write(f"## Status\n\n")
    f.write(f"- Total hubs: {manifest['total_hubs']}\n")
    f.write(f"- Total diseases: {manifest['total_diseases']}\n")
    f.write(f"- With full PNG+HTML+MD: {sum(1 for d in manifest['diseases'] if d['has_png'])}\n")
    f.write(f"- MD-only: {stats['md_only']}\n")
    f.write(f"- Missing MD: {stats['missing_md']}\n\n")
    f.write(f"## Hubs\n\n")
    for h in manifest['hubs']:
        f.write(f"- **{h['num']}** {h['name']} — {h['disease_count']} topics\n")

print(f"\n=== Backup complete ===")
print(f"Stats: {stats}")
print(f"Destination: {DEST}")