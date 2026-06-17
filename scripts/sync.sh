#!/bin/bash
# MedSea Backup — sync /mnt/tb/Sea-knowledge to local MedSea repo
# Run this after editing content in /mnt/tb/Sea-knowledge/
set -euo pipefail

REPO="/root/MedSea"
SRC="/mnt/tb/Sea-knowledge/16. Cardiology"

echo "[$(date)] Starting MedSea backup..."

# Rebuild content
python3 /tmp/build_medsea_backup.py

# Stage and commit changes
cd "$REPO"
git add -A

if git diff --cached --quiet; then
  echo "[$(date)] No changes to commit"
  exit 0
fi

git commit -m "Backup: $(date +%Y-%m-%d_%H%M)

Auto-backup from /mnt/tb/Sea-knowledge/16. Cardiology"

# Push to GitHub
git push origin main 2>&1 || echo "[$(date)] Push failed (will retry next run)"

echo "[$(date)] Backup complete"