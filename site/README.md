# MedSea Site

A static website that visualises the Sea Knowledge medical study library — Davidson's Principles & Practice of Medicine chapters rendered as searchable infographics, paired with their rich text on Notion.

## Chapters

| Chapter | Slug | Notion |
|---|---|---|
| 15 Nephrology and Urology | `15-nephrology-urology` | [Open ↗](https://app.notion.com/p/SeaHub/Chapter-15-Nephrology-and-Urology-d29e1888740b4d809dd1b0cab7616c05) |
| 16 Cardiology | `16-cardiology` | [Open ↗](https://app.notion.com/p/SeaHub/Chapter-16-Cardiology-0bfc7d3c798a450fb5c0ac1bf3848da2) |
| 17 Respiratory Medicine | `17-respiratory-medicine` | [Open ↗](https://app.notion.com/p/SeaHub/Chapter-17-Respiratory-medicine-d4fe7d456ca4481581e806ebe9e177cf) |
| 18 Endocrinology | `18-endocrinology` | [Open ↗](https://app.notion.com/p/SeaHub/Chapter-18-Endocrinology-9db6455d6ae840f0ac29129217d6ccef) |
| 21 Gastroenterology | `21-gastroenterology` | [Open ↗](https://app.notion.com/p/SeaHub/Chapter-21-Gastroenterology-bbfd97790eca482eaed8d47428a642b2) |

## Build

```bash
python3 scripts/site/build_site.py
```

Output: `site/` directory with `index.html` + per-chapter pages + per-topic detail pages. PNGs are excluded from git — they're rebuilt from `chapters/*/diseases/` on each build.

## Docker (port 8855)

```bash
docker build -t medsea-site .
docker run -d --name medsea -p 0.0.0.0:8855:8855 --restart unless-stopped medsea-site
```

Open: <http://localhost:8855/> (or `<lan-ip>:8855/`)

## Vercel

`vercel.json` configures the deployment. Vercel serves the `site/` directory automatically.

```bash
vercel deploy --prod
```

## Structure

```
site/
  index.html              # landing page with all 5 chapters
  <chapter-slug>/
    index.html            # chapter page with all hubs
    diseases/
      <topic>/index.html  # topic detail page (PNG + MD content)
```

## Updates

After content changes, rebuild and restart:

```bash
python3 scripts/site/build_site.py
docker build -t medsea-site . && docker stop medsea && docker rm medsea && \
  docker run -d --name medsea -p 0.0.0.0:8855:8855 --restart unless-stopped medsea-site
```
