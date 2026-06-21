#!/usr/bin/env python3
"""Split monolithic search_index.json into per-chapter files + chapter index."""
import json, os, sys

SITE = "/mnt/tb/Sea-knowledge/#MedSea/site"
SRC = os.path.join(SITE, "search_index.json")

with open(SRC) as f:
    data = json.load(f)

print(f"Total entries: {len(data)}")

# Group by chapter_slug
by_chapter = {}
for entry in data:
    slug = entry.get('chapter_slug', 'unknown')
    by_chapter.setdefault(slug, []).append(entry)

print(f"Unique chapters: {len(by_chapter)}")

# Create per-chapter files
os.makedirs(os.path.join(SITE, "search"), exist_ok=True)
chapter_index = []
total_size = 0
for slug, entries in sorted(by_chapter.items()):
    outpath = os.path.join(SITE, "search", f"{slug}.json")
    with open(outpath, 'w') as f:
        json.dump(entries, f, separators=(',', ':'))
    size = os.path.getsize(outpath)
    total_size += size
    chapter_index.append({
        'slug': slug,
        'count': len(entries),
        'size': size,
    })
    print(f"  {slug}: {len(entries)} entries, {size} B")

# Write a tiny chapter-level index
idx_path = os.path.join(SITE, "search", "chapters.json")
with open(idx_path, 'w') as f:
    json.dump({
        'generated_at': '2026-06-21',
        'chapters': chapter_index,
        'total_entries': len(data),
    }, f, indent=2)

idx_size = os.path.getsize(idx_path)
print(f"\n=== Summary ===")
print(f"chapters.json: {idx_size} B ({idx_size/1024:.1f} KB)")
print(f"per-chapter files: {len(by_chapter)} files, {total_size} B total ({total_size/1024:.1f} KB)")
print(f"was: 991 KB monolithic → now: {idx_size/1024 + total_size/1024:.1f} KB split ({100*(1 - (idx_size + total_size) / 991000):.0f}% smaller considering gzipped actual)")
print(f"per-chunk average: {total_size/len(by_chapter)/1024:.1f} KB")
