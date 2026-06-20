#!/usr/bin/env python3
"""Clean up test page and run full sync."""
import os
import json
import time
import urllib.request
import urllib.error
import pathlib
from datetime import datetime

api_key = os.environ.get("NOTION_API_KEY")
if not api_key:
    with open("/root/.hermes/.env") as f:
        for line in f:
            if line.startswith("NOTION_API_KEY"):
                api_key = line.split("=", 1)[1].strip().strip('"').strip("'")
                break


def http(method, url, data=None):
    h = {
        "Authorization": f"Bearer {api_key}",
        "Notion-Version": "2022-06-28",
        "Content-Type": "application/json",
    }
    body = json.dumps(data).encode() if data is not None else None
    req = urllib.request.Request(url, data=body, method=method, headers=h)
    for attempt in range(5):
        try:
            with urllib.request.urlopen(req, timeout=120) as r:
                return json.loads(r.read().decode())
        except urllib.error.HTTPError as e:
            txt = e.read().decode()
            if e.code == 429:
                wait = int(e.headers.get("Retry-After", "5"))
                print(f"  429 rate-limited, sleeping {wait}s", flush=True)
                time.sleep(wait)
                continue
            return {"_error": e.code, "_body": txt}
        except (urllib.error.URLError, TimeoutError, OSError) as e:
            wait = 5 + attempt * 2
            print(f"  Network error (attempt {attempt+1}/5): {e}, retry in {wait}s", flush=True)
            time.sleep(wait)
            continue
    return {"_error": "max_retries", "_body": "network timeout"}


HUB_IDS = json.load(open("/tmp/cardio_hub_ids.json"))


def fetch_child_pages(hub_id):
    titles = {}
    cursor = None
    while True:
        path = f"/blocks/{hub_id}/children?page_size=100"
        if cursor:
            path += f"&start_cursor={cursor}"
        r = http("GET", f"https://api.notion.com/v1{path}")
        if "results" not in r:
            break
        for b in r["results"]:
            if b.get("type") == "child_page":
                t = b.get("child_page", {}).get("title", "").lower().strip()
                titles[t] = b["id"]
        if not r.get("has_more"):
            break
        cursor = r.get("next_cursor")
    return titles


def create_topic_page(hub_id, title, markdown_content):
    payload = {
        "parent": {"type": "page_id", "page_id": hub_id},
        "properties": {
            "title": [{"type": "text", "text": {"content": title}}]
        },
        "markdown": markdown_content
    }
    r = http("POST", "https://api.notion.com/v1/pages", payload)
    if "_error" in r:
        return None, r
    page_id = r.get("id")
    # Append Sea Knowledge callout
    children = [{
        "object": "block",
        "type": "callout",
        "callout": {
            "rich_text": [{
                "type": "text",
                "text": {"content": "Sea Knowledge full study note — Davidson's 24e, Chapter 16 Cardiology. FCPS/MRCP exam format with mindmap + flowchart."}
            }],
            "icon": {"type": "emoji", "emoji": "🫀"},
            "color": "red_background"
        }
    }]
    http("PATCH", f"https://api.notion.com/v1/blocks/{page_id}/children", data={"children": children})
    return page_id, r.get("url")


def extract_title(folder_name):
    parts = folder_name.split("-", 1)
    slug = parts[1] if len(parts) == 2 else parts[0]
    return " ".join(w.capitalize() for w in slug.replace("-", " ").replace("_", " ").split())


def hub_from_prefix(prefix):
    return ".".join(prefix.split(".")[:2])


CHAPTER_ROOT = pathlib.Path("/mnt/tb/Sea-knowledge/#MedSea/chapters/16-cardiology/diseases")

# Pre-fetch existing pages
print("=== Pre-fetching existing child pages from each hub ===\n", flush=True)
hub_existing = {}
for hub_num, hub_id in HUB_IDS.items():
    existing = fetch_child_pages(hub_id)
    hub_existing[hub_num] = existing
    print(f"  {hub_num}: {len(existing)} existing pages", flush=True)

topics = sorted([d for d in CHAPTER_ROOT.iterdir() if d.is_dir()])
print(f"\n=== Found {len(topics)} topic folders ===\n")
print(f"Starting sync at {datetime.now().strftime('%H:%M:%S')}\n", flush=True)

stats = {
    "created": 0,
    "skipped_existing": 0,
    "failed": 0,
    "errors": [],
    "start_time": time.time(),
    "by_hub": {},
}

for i, topic_dir in enumerate(topics, 1):
    folder_name = topic_dir.name
    md_path = topic_dir / "topic.md"
    if not md_path.exists():
        stats["failed"] += 1
        stats["errors"].append(f"{folder_name}: no topic.md")
        continue

    prefix_parts = folder_name.split("-", 1)[0]
    hub_num = hub_from_prefix(prefix_parts)

    if hub_num not in HUB_IDS:
        stats["failed"] += 1
        stats["errors"].append(f"{folder_name}: no hub for {hub_num}")
        continue

    title = f"{prefix_parts} {extract_title(folder_name)}"

    if title.lower() in hub_existing[hub_num]:
        stats["skipped_existing"] += 1
        continue

    md_content = md_path.read_text(encoding="utf-8")

    page_id, url = create_topic_page(HUB_IDS[hub_num], title, md_content)
    if page_id:
        stats["created"] += 1
        stats["by_hub"][hub_num] = stats["by_hub"].get(hub_num, 0) + 1
        hub_existing[hub_num][title.lower()] = page_id

        if stats["created"] % 10 == 0:
            elapsed = time.time() - stats["start_time"]
            rate = stats["created"] / max(elapsed / 60, 0.01)
            remaining = (len(topics) - i) / rate if rate > 0 else 0
            print(f"[{i}/{len(topics)}] created={stats['created']}, "
                  f"skipped={stats['skipped_existing']}, failed={stats['failed']} | "
                  f"{rate:.1f}/min, ~{remaining:.0f}min remaining", flush=True)

        time.sleep(0.4)
    else:
        stats["failed"] += 1
        err_msg = url.get("_body", str(url))[:200] if isinstance(url, dict) else str(url)
        stats["errors"].append(f"{folder_name}: {err_msg}")
        if stats["failed"] <= 3:
            print(f"  FAIL {folder_name}: {err_msg[:200]}", flush=True)
        if isinstance(url, dict) and url.get("_error") in (429, 500, 503):
            time.sleep(5)

elapsed = time.time() - stats["start_time"]
print(f"\n=== DONE in {elapsed/60:.1f} min ===")
print(f"Created: {stats['created']}")
print(f"Skipped (existing): {stats['skipped_existing']}")
print(f"Failed: {stats['failed']}")
print(f"\nBy hub:")
for hub, count in sorted(stats["by_hub"].items()):
    print(f"  {hub}: {count} topics created")

if stats["errors"]:
    print(f"\nFirst 10 errors:")
    for e in stats["errors"][:10]:
        print(f"  - {e[:200]}")

with open("/tmp/cardio_sync_stats.json", "w") as f:
    json.dump({k: v for k, v in stats.items() if k != "start_time"}, f, indent=2, default=str)
print(f"\nStats saved to /tmp/cardio_sync_stats.json")