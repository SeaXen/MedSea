#!/usr/bin/env python3
"""Build MedSea backup for chapter 15 (Nephrology & Urology) — mirrors cardiology."""
import json
import shutil
import sys
from pathlib import Path

SRC_SK = Path('/mnt/tb/Sea-knowledge/15. Nephrology and Urology')
SRC_SOURCE = Path('/root/nephro-content')
REPO_ROOT = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).resolve().parent.parent
DEST = REPO_ROOT / 'chapters' / '15-nephrology-urology'

HUBS = [
    ('15.1', 'Renal Anatomy, Physiology, and Investigations',          'renal-anatomy-physiology'),
    ('15.2', 'Acute Kidney Injury and Chronic Kidney Disease',        'aki-ckd'),
    ('15.3', 'Glomerular Diseases',                                    'glomerular-diseases'),
    ('15.4', 'Tubulointerstitial, Cystic, and Inherited Renal Disorders', 'tubulointerstitial-cystic-inherited'),
    ('15.5', 'Urinary Tract Infection, Obstruction, and Urologic Renal Problems', 'uti-urology'),
    ('15.6', 'Dialysis and Renal Replacement Therapy',                  'dialysis-transplant'),
]

stats = {'copied': 0, 'missing_render': 0, 'missing_md': 0}
manifest = {
    'chapter': '15. Nephrology and Urology',
    'total_hubs': len(HUBS),
    'hubs': [],
    'diseases': [],
    'source_root': str(SRC_SK),
}

# Wipe and recreate DEST
if DEST.exists():
    shutil.rmtree(DEST)
(DEST / 'hubs').mkdir(parents=True)
(DEST / 'diseases').mkdir(parents=True)
(DEST / 'source').mkdir(parents=True)

# Copy source .md files (raw, pre-renderer)
if SRC_SOURCE.exists():
    for src_md in sorted(SRC_SOURCE.glob('*.md')):
        shutil.copy2(src_md, DEST / 'source' / src_md.name)

for num, name, rootslug in HUBS:
    hubdir = SRC_SK / f'{num}. {name}'
    if not hubdir.exists():
        print(f'  SKIP hub missing: {num}. {name}')
        continue

    hub_md_src = hubdir / f'{rootslug}.md'
    hub_md_dst = DEST / 'hubs' / f'{num}-{rootslug}.md'
    if hub_md_src.exists():
        shutil.copy2(hub_md_src, hub_md_dst)

    # Find disease topic folders (15.N.M. ...)
    diseases = sorted([d for d in hubdir.iterdir()
                       if d.is_dir() and d.name.startswith(f'{num}.')])
    for disease_dir in diseases:
        slug = disease_dir.name.split(' ', 1)[1] if ' ' in disease_dir.name else disease_dir.name
        md_src = disease_dir / f'{slug}.md'
        png_src = disease_dir / f'{slug}.png'
        if not md_src.exists():
            stats['missing_md'] += 1
            continue

        dest_dir = DEST / 'diseases' / f'{num}-{slug}'
        dest_dir.mkdir(parents=True, exist_ok=True)
        shutil.copy2(md_src, dest_dir / 'topic.md')
        manifest['diseases'].append({
            'hub': f'{num}. {name}',
            'slug': slug,
            'title': ' '.join(w.capitalize() for w in slug.replace('-', ' ').split()),
            'path': str(dest_dir.relative_to(REPO_ROOT)),
        })
        stats['copied'] += 1
        if not png_src.exists():
            stats['missing_render'] += 1

    manifest['hubs'].append({
        'num': num,
        'name': name,
        'slug': rootslug,
        'disease_count': len(diseases),
    })

manifest['total_diseases'] = len(manifest['diseases'])
with open(DEST / 'manifest.json', 'w') as f:
    json.dump(manifest, f, indent=2)

with open(DEST / 'README.md', 'w') as f:
    f.write(f"# Chapter 15: Nephrology and Urology\n\n")
    f.write(f"Auto-generated backup of all rendered topics for Davidson's Nephrology chapter.\n\n")
    f.write(f"## Stats\n")
    f.write(f"- Hubs: {manifest['total_hubs']}\n")
    f.write(f"- Diseases: {manifest['total_diseases']}\n")
    f.write(f"- Copied: {stats['copied']}\n")
    f.write(f"- Missing md: {stats['missing_md']}\n")
    f.write(f"- Missing render (md only): {stats['missing_render']}\n\n")
    f.write(f"## Hubs\n")
    for h in manifest['hubs']:
        f.write(f"- **{h['num']}. {h['name']}** — {h['disease_count']} diseases (slug: `{h['slug']}`)\n")
    f.write(f"\n## Source\n")
    f.write(f"Pre-renderer markdown source in `source/`. Original raw source in `/mnt/tb/Medicine/Nephrology and Urology/`.\n")
    f.write(f"\n## Notion\n")
    f.write(f"Published at: https://app.notion.com/p/searex/Chapter-15-Nephrology-and-urology-710f215344c34692af7584e89e714ff0\n")

print(f'=== Backup stats ===')
print(f"Hubs: {manifest['total_hubs']}")
print(f"Diseases total: {manifest['total_diseases']}")
print(f"  Copied (md): {stats['copied']}")
print(f"  Missing md: {stats['missing_md']}")
print(f"  Missing render (md only): {stats['missing_render']}")
print(f"Source mds copied: {len(list((DEST / 'source').glob('*.md'))) if (DEST / 'source').exists() else 0}")
print(f"Written to: {DEST}")