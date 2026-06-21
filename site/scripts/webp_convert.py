#!/usr/bin/env python3
"""Convert all PNGs in a chapter to WebP using cwebp.
- Keeps PNG files in place (fallback)
- Writes WebP alongside with same basename + .webp
- Reports size savings
"""
import os, sys, subprocess, time

def convert_chapter(chapter_dir, site_root, quality=85):
    chapter_path = os.path.join(site_root, chapter_dir)
    if not os.path.isdir(chapter_path):
        print(f"  ! {chapter_dir}: directory not found")
        return None
    pngs = []
    for root, _, files in os.walk(chapter_path):
        for f in files:
            if f.endswith('.png'):
                pngs.append(os.path.join(root, f))
    if not pngs:
        print(f"  - {chapter_dir}: no PNGs")
        return None
    total_png = sum(os.path.getsize(p) for p in pngs)
    converted = 0
    total_webp = 0
    skipped = 0
    start = time.time()
    for png in pngs:
        webp = png[:-4] + '.webp'
        # Skip if WebP already exists and is newer
        if os.path.exists(webp) and os.path.getmtime(webp) > os.path.getmtime(png):
            total_webp += os.path.getsize(webp)
            skipped += 1
            continue
        # Run cwebp with -quiet to suppress progress
        result = subprocess.run(
            ['cwebp', '-q', str(quality), '-quiet', png, '-o', webp],
            capture_output=True, timeout=60
        )
        if result.returncode == 0 and os.path.exists(webp):
            total_webp += os.path.getsize(webp)
            converted += 1
        else:
            print(f"  ! Failed: {png}: {result.stderr.decode()[:100]}")
    elapsed = time.time() - start
    savings = (1 - total_webp / total_png) * 100 if total_png > 0 else 0
    print(f"  ✓ {chapter_dir}: {converted} converted + {skipped} cached, {total_png/1048576:.1f} MB → {total_webp/1048576:.1f} MB (-{savings:.0f}%) in {elapsed:.1f}s")
    return (total_png, total_webp, converted, skipped)

if __name__ == "__main__":
    site_root = "/mnt/tb/Sea-knowledge/#MedSea/site"
    chapter = sys.argv[1] if len(sys.argv) > 1 else "1-clinical-decision-making"
    convert_chapter(chapter, site_root)
