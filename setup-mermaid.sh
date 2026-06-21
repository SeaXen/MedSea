#!/bin/bash
# Setup script: download Mermaid if missing
set -e
DEST="$(dirname "$0")/site/assets/mermaid.min.js"
if [ -f "$DEST" ] && [ -s "$DEST" ]; then
  echo "✓ Mermaid already present: $DEST ($(stat -c%s "$DEST") bytes)"
  exit 0
fi
echo "Downloading Mermaid to $DEST..."
mkdir -p "$(dirname "$DEST")"
wget --timeout=30 -q "https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.min.js" -O "$DEST"
echo "✓ Downloaded: $(stat -c%s "$DEST") bytes"
