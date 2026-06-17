#!/usr/bin/env python3
"""Helper for restore.sh — restore diseases from backup into hub-nested structure."""
import json
import shutil
import sys
from pathlib import Path

def main():
    chapter_dir = Path(sys.argv[1])
    dest_root = Path(sys.argv[2])

    manifest = json.loads((chapter_dir / 'manifest.json').read_text())
    diseases_src = chapter_dir / 'diseases'

    hubs = {h['slug']: (h['num'], h['name']) for h in manifest['hubs']}

    restored = 0
    for d in manifest['diseases']:
        folder = d['folder']
        src = chapter_dir / folder
        if not src.exists():
            print(f'  missing in backup: {folder}')
            continue
        hub_info = hubs.get(d['parent_slug'])
        if not hub_info:
            print(f'  unknown hub for {folder}: {d["parent_slug"]}')
            continue
        hub_num, hub_name = hub_info
        hub_dir = dest_root / f'{hub_num}. {hub_name}'
        hub_dir.mkdir(parents=True, exist_ok=True)
        clean_topic = d['topic'].lower().replace(' ', '-').replace('/', '-').replace('—', '-').replace('(', '').replace(')', '').replace(',', '').replace("'", '').replace('`', '')
        while '--' in clean_topic:
            clean_topic = clean_topic.replace('--', '-')
        clean_topic = clean_topic.strip('-')[:80]
        target_dir = hub_dir / f'{d["subnum"]}. {clean_topic}'
        target_dir.mkdir(parents=True, exist_ok=True)
        for f in src.iterdir():
            target = target_dir / f.name
            if target.exists():
                target.unlink()
            shutil.copy2(f, target)
        restored += 1
    print(f'  diseases restored: {restored}')

if __name__ == '__main__':
    main()