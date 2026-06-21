/* MedSea Service Worker - aggressive caching for fast repeat visits */
const CACHE_VERSION = 'medsea-v3';
const CORE_ASSETS = [
  '/',
  '/index.html',
  '/assets/site-header.css',
  '/assets/site-header.js',
  '/assets/site-db.js',
  '/assets/chapter.css',
  '/assets/chapter.js',
  '/assets/mermaid.min.js',
  '/assets/exam-engine.js',
  '/assets/questions-index.json',
  '/assets/site-header-preview.html',
  '/manifest.json',
];

self.addEventListener('install', (event) => {
  event.waitUntil(
    caches.open(CACHE_VERSION).then((cache) => {
      // Pre-cache core, ignore failures for individual items
      return Promise.allSettled(CORE_ASSETS.map((url) => cache.add(url)));
    }).then(() => self.skipWaiting())
  );
});

self.addEventListener('activate', (event) => {
  event.waitUntil(
    caches.keys().then((keys) => Promise.all(
      keys.filter((k) => k !== CACHE_VERSION).map((k) => caches.delete(k))
    )).then(() => self.clients.claim())
  );
});

self.addEventListener('fetch', (event) => {
  const req = event.request;
  if (req.method !== 'GET') return;
  const url = new URL(req.url);
  // Only handle same-origin
  if (url.origin !== location.origin) return;

  // For navigation requests: network-first, fallback to cache
  if (req.mode === 'navigate') {
    event.respondWith(
      fetch(req).then((res) => {
        const copy = res.clone();
        caches.open(CACHE_VERSION).then((c) => c.put(req, copy));
        return res;
      }).catch(() => caches.match(req).then((r) => r || caches.match('/index.html')))
    );
    return;
  }

  // For CSS/JS/JSON: network-first so hotfixes reach phones immediately
  if (url.pathname.startsWith('/assets/') || url.pathname.endsWith('.css') ||
      url.pathname.endsWith('.js') || url.pathname.endsWith('.json')) {
    event.respondWith(
      fetch(req).then((res) => {
        if (res.ok) {
          const copy = res.clone();
          caches.open(CACHE_VERSION).then((c) => c.put(req, copy));
        }
        return res;
      }).catch(() => caches.match(req))
    );
    return;
  }

  // For images/icons: cache-first
  if (url.pathname.endsWith('.png') || url.pathname.endsWith('.svg') ||
      url.pathname.endsWith('.ico') || url.pathname.endsWith('.webp')) {
    event.respondWith(
      caches.match(req).then((cached) => {
        if (cached) return cached;
        return fetch(req).then((res) => {
          if (res.ok) {
            const copy = res.clone();
            caches.open(CACHE_VERSION).then((c) => c.put(req, copy));
          }
          return res;
        }).catch(() => cached);
      })
    );
    return;
  }
});
