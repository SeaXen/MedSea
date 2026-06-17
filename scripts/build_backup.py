#!/usr/bin/env python3
"""Build MedSea backup from /mnt/tb/Sea-knowledge + /root/sk-content.
Output: <repo>/chapters/16-cardiology/
"""
import json
import shutil
import sys
from pathlib import Path

SRC_SK = Path('/mnt/tb/Sea-knowledge/16. Cardiology')
SRC_SOURCE = Path('/root/sk-content')
REPO_ROOT = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).resolve().parent.parent
DEST = REPO_ROOT / 'chapters' / '16-cardiology'

# Hubs in order
HUBS = [
    ('16.1',  'Acute Coronary Syndromes',                   'acute-coronary-syndromes'),
    ('16.2',  'Adult Congenital Heart Disease',             'adult-congenital-heart-disease'),
    ('16.3',  'Arrhythmias',                                'arrhythmias'),
    ('16.4',  'Cardiac Devices and Electrophysiology',      'cardiac-devices-ep'),
    ('16.5',  'Cardiac Disease in Special Populations',      'special-populations'),
    ('16.6',  'Cardiac Emergencies and Critical Care',      'cardiac-emergencies'),
    ('16.7',  'Cardiac Investigations',                     'cardiac-investigations'),
    ('16.8',  'Cardiomyopathies',                           'cardiomyopathies'),
    ('16.9',  'Chronic Coronary Syndromes',                 'chronic-coronary-syndromes'),
    ('16.10', 'Diseases of the Aorta',                      'aortic-diseases'),
    ('16.11', 'Heart Failure',                              'heart-failure'),
    ('16.12', 'Hypertension and CV Risk',                   'hypertension-cv-risk'),
    ('16.13', 'Infective Endocarditis',                     'infective-endocarditis'),
    ('16.14', 'Pericardial Diseases',                       'pericardial-diseases'),
    ('16.15', 'Pulmonary Hypertension',                     'pulmonary-hypertension'),
    ('16.16', 'Systemic Diseases and Cardiac Involvement',  'systemic-cardiac'),
    ('16.17', 'Valvular Heart Disease',                     'valvular-heart-disease'),
]

# Load canonical list for manifest
with open('/root/sea-knowledge-infographics/all_disease_topics.json') as f:
    canonical = json.load(f)

# Build manifest entries
manifest = {
    'chapter': '16. Cardiology',
    'total_hubs': len(HUBS),
    'total_diseases': len(canonical),
    'hubs': [],
    'diseases': []
}

# Track stats
stats = {'copied': 0, 'missing_render': 0, 'missing_md': 0}

for num, name, rootslug in HUBS:
    hubdir = SRC_SK / f'{num}. {name}'
    if not hubdir.exists():
        print(f'  SKIP hub missing: {num}. {name}')
        continue

    # Copy hub md (if exists) into hubs/
    hub_md_src = hubdir / f'{rootslug}.md'
    if hub_md_src.exists():
        shutil.copy2(hub_md_src, DEST / 'hubs' / f'{rootslug}.md')
    manifest['hubs'].append({
        'num': num,
        'name': name,
        'slug': rootslug,
        'has_local_md': hub_md_src.exists(),
    })

# Process each canonical disease
for d in canonical:
    parent_slug = d['parent_slug']

    # Find the hub display number by matching parent_slug to HUBS
    hub_info = next(((num, name) for num, name, rs in HUBS if rs == parent_slug), None)
    if not hub_info:
        continue
    num, hub_name = hub_info
    slug = d['slug']
    topic = d['topic']

    # Find disease folder in /mnt/tb/Sea-knowledge
    src_folder = None
    hub_path = SRC_SK / f"{num}. {hub_name}"
    if not hub_path.exists():
        continue

    # The disease folder name format: "16.N.<local-M>. <clean-topic-name>"
    # Local counter is per-hub starting at 1. We need to find local M by counting.
    local_counter = 1
    hub_diseases = [dd for dd in canonical if dd['parent_slug'] == parent_slug]
    for local_idx, dd in enumerate(hub_diseases, start=1):
        if dd['idx'] == d['idx']:
            local_counter = local_idx
            break
    expected_prefix = f"{num}.{local_counter}."
    for candidate in hub_path.iterdir():
        if candidate.is_dir() and candidate.name.startswith(expected_prefix):
            src_folder = candidate
            break

    subnum = f"{num}.{d['idx']}"

    # Use simplified disease folder name: 16.N.M-<topic-slug>
    topic_slug = topic.lower().replace(' ', '-').replace('/', '-').replace('—', '-').replace('(', '').replace(')', '').replace(',', '').replace("'", '').replace('`', '')
    while '--' in topic_slug:
        topic_slug = topic_slug.replace('--', '-')
    topic_slug = topic_slug.strip('-')[:80]  # truncate

    disease_dest = DEST / 'diseases' / f"{subnum}-{topic_slug}"

    has_md = False
    has_html = False
    has_png = False

    if src_folder and src_folder.exists():
        disease_dest.mkdir(parents=True, exist_ok=True)
        for f in src_folder.iterdir():
            if f.suffix == '.md' and not f.name.startswith('-'):
                shutil.copy2(f, disease_dest / 'topic.md')
                has_md = True
            elif f.suffix == '.html':
                shutil.copy2(f, disease_dest / 'topic.html')
                has_html = True
            elif f.suffix == '.png':
                shutil.copy2(f, disease_dest / 'topic.png')
                has_png = True

    if has_md:
        stats['copied'] += 1
    else:
        stats['missing_md'] += 1
    if has_md and not (has_html and has_png):
        stats['missing_render'] += 1

    manifest['diseases'].append({
        'idx': d['idx'],
        'subnum': subnum,
        'hub_num': num,
        'parent_slug': parent_slug,
        'topic': topic,
        'slug': slug,
        'folder': f"diseases/{subnum}-{topic_slug}",
        'has_md': has_md,
        'has_html': has_html,
        'has_png': has_png,
    })

# Copy source markdown into source/
source_count = 0
for src_md in SRC_SOURCE.glob('*.md'):
    shutil.copy2(src_md, DEST / 'source' / src_md.name)
    source_count += 1

# Save manifest
with open(DEST / 'manifest.json', 'w') as f:
    json.dump(manifest, f, indent=2)

print(f'\n=== Backup stats ===')
print(f'Hubs: {len(manifest["hubs"])}')
print(f'Diseases total: {len(manifest["diseases"])}')
print(f'  Copied (md): {stats["copied"]}')
print(f'  Missing md: {stats["missing_md"]}')
print(f'  Missing render (md only): {stats["missing_render"]}')
print(f'Source mds copied: {source_count}')