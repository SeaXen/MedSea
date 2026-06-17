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

echo "[$(date)] Restoring $CHAPTER_DIR -> $TARGET/16. Cardiology/"
mkdir -p "$TARGET/16. Cardiology"

# Restore hubs
if [ -d "$CHAPTER_DIR/hubs" ]; then
  cp -r "$CHAPTER_DIR/hubs/." "$TARGET/16. Cardiology/"
fi

# Restore diseases (each subfolder has topic.md/html/png)
if [ -d "$CHAPTER_DIR/diseases" ]; then
  cp -r "$CHAPTER_DIR/diseases/." "$TARGET/16. Cardiology/"
fi

# Restore source mds to /root/sk-content/ for future re-rendering
if [ -d "$CHAPTER_DIR/source" ]; then
  mkdir -p /root/sk-content
  cp -n "$CHAPTER_DIR/source/"*.md /root/sk-content/ 2>/dev/null || true
fi

echo "[$(date)] Restore complete"
echo ""
echo "Next steps (if PNG/HTML missing):"
echo "  cd /root/sea-knowledge-infographics"
echo "  python3 render_topic.py --slug <topic> --title <Title> --markdown-file <md> --out-dir <folder>"