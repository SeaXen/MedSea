#!/bin/bash
# MedSea Restore — pull from GitHub and restore to /mnt/tb/Sea-knowledge/
# Usage: ./restore.sh [--chapter 16] [--target /path/to/dest]
set -euo pipefail

CHAPTER="16"
TARGET="/mnt/tb/Sea-knowledge"

while [[ $# -gt 0 ]]; do
  case $1 in
    --chapter) CHAPTER="$2"; shift 2 ;;
    --target)  TARGET="$2"; shift 2 ;;
    *) echo "Unknown arg: $1"; exit 1 ;;
  esac
done

REPO="/root/MedSea"
CHAPTER_DIR="$REPO/chapters/$CHAPTER-cardiology"

if [ ! -d "$CHAPTER_DIR" ]; then
  echo "Error: chapter dir not found: $CHAPTER_DIR"
  exit 1
fi

DEST="$TARGET/16. Cardiology"
echo "[$(date)] Restoring $CHAPTER_DIR -> $DEST/"
mkdir -p "$DEST"

# Step 1: restore hubs (flat .md files)
if [ -d "$CHAPTER_DIR/hubs" ]; then
  for hub_md in "$CHAPTER_DIR/hubs/"*.md; do
    [ -f "$hub_md" ] || continue
    cp "$hub_md" "$DEST/"
    echo "  hub: $(basename "$hub_md")"
  done
fi

# Step 2: restore diseases into hub-nested structure (uses manifest)
if [ -f "$CHAPTER_DIR/manifest.json" ] && [ -d "$CHAPTER_DIR/diseases" ]; then
  python3 "$REPO/scripts/restore_diseases.py" "$CHAPTER_DIR" "$DEST"
fi

# Step 3: restore source mds to /root/sk-content/
if [ -d "$CHAPTER_DIR/source" ]; then
  mkdir -p /root/sk-content
  cp -n "$CHAPTER_DIR/source/"*.md /root/sk-content/ 2>/dev/null || true
  echo "  source mds: $(ls "$CHAPTER_DIR/source/"*.md 2>/dev/null | wc -l)"
fi

echo "[$(date)] Restore complete"