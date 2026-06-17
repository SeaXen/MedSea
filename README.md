# MedSea

Medical study knowledge backup repo — Sea Knowledge infographic pipeline.

## Purpose

Safe backup of `/mnt/tb/Sea-knowledge/` content on GitHub so it can be
restored if local files are accidentally deleted or corrupted.

This repo mirrors the Sea Knowledge style study notes:
- 330 disease-level cardiology topics with markdown + HTML + PNG renders
- 17 hub pages (one per major cardiology section)
- Raw markdown source for re-rendering if needed

## Structure

```
MedSea/
├── README.md                       # this file
├── .gitignore                      # excludes transient files
├── scripts/
│   ├── sync.sh                     # rebuild + commit + push backup
│   └── restore.sh                  # pull from GitHub, restore to /mnt/tb/Sea-knowledge/
└── chapters/
    └── 16-cardiology/              # Davidson 24th Edition Chapter 16
        ├── manifest.json           # canonical list of all 330 topics + render status
        ├── README.md               # chapter status + known gaps
        ├── hubs/                   # 17 hub-level .md files
        ├── diseases/               # 330 disease folders
        │   └── 16.N.M-<topic-slug>/
        │       ├── topic.md        # markdown source
        │       ├── topic.html      # rendered HTML (Sea Knowledge style)
        │       └── topic.png       # A4 portrait PNG
        └── source/                 # raw markdown (358 files including duplicates)
```

## Quick start

### Backup current content

```bash
/root/MedSea/scripts/sync.sh
```

This rebuilds the chapters/, commits changes, and pushes to GitHub.

### Restore from backup

```bash
/root/MedSea/scripts/restore.sh
```

This pulls the latest commit from GitHub and copies files back to
`/mnt/tb/Sea-knowledge/16. Cardiology/`. Source mds are restored to
`/root/sk-content/`.

### Re-render a missing PNG/HTML

If a disease folder has only `topic.md` (chromium render failed), you can
re-render manually:

```bash
python3 /root/sea-knowledge-infographics/render_topic.py \
  --slug <topic-slug> \
  --title "<Display Title>" \
  --markdown-file /path/to/topic.md \
  --out-dir /path/to/disease/folder
```

Then run `/root/MedSea/scripts/sync.sh` to back up the new render.

## Known gaps (Chapter 16)

2 of 330 disease folders are missing PNG/HTML renders because chromium
hangs on those markdown files (`adhf-management` and `cross-link-...` in
the cardiac emergencies hub). Markdown is present; PNG/HTML can be
regenerated with a different renderer if needed (e.g. weasyprint).

## Auto-backup

A cron job runs `/root/MedSea/scripts/sync.sh` periodically. Check
`/root/.hermes/cron/jobs.json` for the schedule.

## License

Personal study notes — Dr. Sagar (SeaXen). Not for redistribution.