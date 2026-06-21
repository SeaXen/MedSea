/* =====================================================================
   MedSea Chapter Page - shared script
   - Universal topic search (search_index.json)
   - Topic manifest loading + sidebar nav + topic render
   - Mermaid init + dynamic re-render
   - Dropdown close on outside click
   ===================================================================== */

(function () {
  'use strict';

  const CHAPTER = window.CHAPTER || {};
  const CHAPTER_SLUG = CHAPTER.slug || '';
  const CHAPTER_NAME = CHAPTER.name || CHAPTER_SLUG;
  const MANIFEST_URL = CHAPTER.manifest_url || ('/' + CHAPTER_SLUG + '/topics.json');

  let MANIFEST = null;
  let CURRENT_TOPIC = null;

  // ============================================================
  // 1. Universal topic search
  // ============================================================
  let searchIdx = null;
  let searchDebounce = null;

  function escHtml(s) {
    return String(s).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
  }

  function highlight(text, q) {
    if (!q) return escHtml(text);
    const i = text.toLowerCase().indexOf(q.toLowerCase());
    if (i < 0) return escHtml(text);
    return escHtml(text.slice(0, i)) + '<mark>' + escHtml(text.slice(i, i + q.length)) + '</mark>' + escHtml(text.slice(i + q.length));
  }

  function loadSearchIdx() {
    if (searchIdx) return Promise.resolve(searchIdx);
    return fetch('/search_index.json').then(function (r) { return r.json(); }).then(function (d) {
      searchIdx = d;
      return d;
    });
  }

  function doSearch(q) {
    loadSearchIdx().then(function (data) {
      const ql = q.toLowerCase();
      const hits = [];
      for (let i = 0; i < data.length && hits.length < 20; i++) {
        const t = data[i];
        const title = (t.title || '').toLowerCase();
        const hub = (t.hub_name || '').toLowerCase();
        const chapter = (t.chapter_name || '').toLowerCase();
        let score = 0;
        if (title.startsWith(ql)) score = 100;
        else if (title.includes(ql)) score = 60;
        else if (hub.includes(ql)) score = 30;
        else if (chapter.includes(ql)) score = 10;
        if (score > 0) hits.push({ t: t, s: score });
      }
      hits.sort(function (a, b) { return b.s - a.s; });
      const results = document.getElementById('searchResults');
      if (!results) return;
      if (hits.length === 0) {
        results.innerHTML = '<div class="search-empty">No matches</div>';
        return;
      }
      results.innerHTML = hits.map(function (h) {
        return '<a class="search-hit" href="/' + escHtml(h.t.chapter_slug) + '/?topic=' + encodeURIComponent(h.t.local_prefix) + '">' +
          '<div class="hit-title">' + highlight(h.t.title || '', q) + '</div>' +
          '<div class="hit-meta">' + escHtml(h.t.chapter_name || '') + ' · ' + escHtml(h.t.hub_name || '') + ' · <code>' + escHtml(h.t.local_prefix) + '</code></div>' +
          '</a>';
      }).join('');
    });
  }

  function initSearch() {
    const input = document.getElementById('searchInput');
    const results = document.getElementById('searchResults');
    if (!input || !results) return;
    input.addEventListener('input', function (e) {
      const q = e.target.value.trim();
      clearTimeout(searchDebounce);
      if (q.length < 2) { results.innerHTML = ''; return; }
      searchDebounce = setTimeout(function () { doSearch(q); }, 150);
    });
    // Close results when clicking outside
    document.addEventListener('click', function (e) {
      const box = document.getElementById('searchBox');
      if (box && !box.contains(e.target)) results.innerHTML = '';
    });
  }

  // ============================================================
  // 2. Topic manifest loading + sidebar nav + topic render
  // ============================================================
  async function loadManifest() {
    try {
      const res = await fetch(MANIFEST_URL);
      MANIFEST = await res.json();
      const params = new URLSearchParams(location.search);
      let t = params.get('topic');
      if (t) {
        const found = MANIFEST.topics.find(function (x) {
          return x.local_prefix === t || x.local_prefix === t.split('-')[0];
        });
        if (found) showTopic(found.local_prefix);
      }
    } catch (e) {
      console.error('Failed to load topics.json', e);
    }
  }

  function navigateTopic(dir) {
    if (!MANIFEST || !CURRENT_TOPIC) return;
    const i = MANIFEST.topics.findIndex(function (x) { return x.local_prefix === CURRENT_TOPIC.local_prefix; });
    const ni = i + dir;
    if (ni < 0 || ni >= MANIFEST.topics.length) return;
    showTopic(MANIFEST.topics[ni].local_prefix);
  }

  function toggleTopicImage(btn) {
    btn.classList.toggle('collapsed');
    const wrap = btn.nextElementSibling;
    if (wrap) {
      wrap.classList.toggle('collapsed');
      const span = btn.querySelector('span:last-child');
      if (span) span.textContent = wrap.classList.contains('collapsed') ? 'click to expand' : 'click to collapse';
    }
  }

  function showTopic(localPrefix) {
    const t = MANIFEST.topics.find(function (x) { return x.local_prefix === localPrefix; });
    if (!t) return;
    CURRENT_TOPIC = t;
    document.querySelectorAll('.topic-item').forEach(function (el) { el.classList.remove('active'); });
    const activeEl = document.querySelector('.topic-item[data-topic="' + localPrefix + '"]');
    if (activeEl) {
      activeEl.classList.add('active');
      activeEl.scrollIntoView({ block: 'nearest', behavior: 'smooth' });
    }
    const url = new URL(location.href);
    url.searchParams.set('topic', localPrefix);
    history.replaceState(null, '', url);
    const container = document.getElementById('topicContainer');
    container.className = 'topic-detail';
    const imgHtml = t.png ? (
      '<div class="topic-image-toggle collapsed" onclick="window.medseaToggleImage(this)">' +
        '<span><span class="toggle-icon">▼</span> &nbsp;Show infographic image</span>' +
        '<span style="font-size:12px;color:var(--text-dim)">click to expand</span>' +
      '</div>' +
      '<div class="topic-image-wrap collapsed">' +
        '<div class="topic-image"><img src="/' + CHAPTER_SLUG + '/' + t.png + '" alt="' + escHtml(t.title) + '" loading="lazy" decoding="async"></div>' +
      '</div>'
    ) : '';
    container.innerHTML =
      '<div class="crumbs"><a href="/">Home</a> · <a href="/' + CHAPTER_SLUG + '/">' + escHtml(CHAPTER_NAME) + '</a> · <span>' + escHtml(t.hub_num) + ' · ' + escHtml(t.hub_name) + '</span></div>' +
      '<div class="topic-header">' +
        '<div>' +
          '<h1>' + escHtml(t.title) + '</h1>' +
          '<p class="meta">' + escHtml(t.hub_num) + ' · ' + escHtml(t.local_prefix) + ' · ' + escHtml(t.slug) + '</p>' +
        '</div>' +
        '<div class="topic-actions">' +
          (t.png ? '<a href="/' + CHAPTER_SLUG + '/' + t.png + '" download>Download PNG</a>' : '') +
          (t.md ? '<a href="/' + CHAPTER_SLUG + '/' + t.md + '" download>Download MD</a>' : '') +
          '<button onclick="window.medseaNav(-1)">← Prev</button>' +
          '<button onclick="window.medseaNav(1)">Next →</button>' +
        '</div>' +
      '</div>' +
      '<div class="topic-content">' + t.html + '</div>' +
      imgHtml;
    if (typeof window.renderMermaidIn === 'function') {
      setTimeout(function () { window.renderMermaidIn(container); }, 50);
    }
    container.scrollTop = 0;
    const main = document.querySelector('.chapter-main');
    if (main) main.scrollTop = 0;
  }

  function initChapter() {
    if (!CHAPTER_SLUG) return;
    // Wire up topic-item clicks
    document.querySelectorAll('.topic-item').forEach(function (el) {
      el.addEventListener('click', function (e) {
        e.preventDefault();
        const t = el.dataset.topic;
        if (t) showTopic(t);
      });
    });
    // Expose helpers for inline onclick
    window.medseaNav = navigateTopic;
    window.medseaToggleImage = toggleTopicImage;
    // Kick off manifest load
    if (document.readyState === 'loading') {
      document.addEventListener('DOMContentLoaded', loadManifest);
    } else {
      loadManifest();
    }
  }

  // ============================================================
  // 3. Mermaid init + dynamic re-render
  // ============================================================
  function initMermaid() {
    if (typeof mermaid === 'undefined') return;
    mermaid.initialize({
      startOnLoad: true,
      theme: 'base',
      themeVariables: {
        primaryColor: '#1f2937',
        primaryTextColor: '#e5e7eb',
        primaryBorderColor: '#38bdf8',
        lineColor: '#9ca3af',
        secondaryColor: '#111827',
        tertiaryColor: '#0f172a',
        fontFamily: 'system-ui, -apple-system, sans-serif'
      },
      flowchart: { useMaxWidth: true, htmlLabels: true, curve: 'basis' },
      mindmap: { useMaxWidth: true },
      securityLevel: 'loose'
    });
  }

  window.renderMermaidIn = function (container) {
    if (typeof mermaid === 'undefined') return;
    const blocks = (container || document).querySelectorAll('pre.mermaid:not([data-rendered])');
    blocks.forEach(function (block, i) {
      block.setAttribute('data-rendered', 'true');
      const id = 'mm-' + Date.now() + '-' + i;
      try {
        mermaid.render(id, block.textContent).then(function (result) {
          const wrapper = document.createElement('div');
          wrapper.className = 'mermaid-diagram';
          wrapper.innerHTML = result.svg;
          block.replaceWith(wrapper);
        }).catch(function (err) {
          console.warn('mermaid render failed:', err);
          block.style.color = '#f87171';
        });
      } catch (e) {
        console.warn('mermaid error:', e);
      }
    });
  };

  function initMermaidAfter() {
    document.addEventListener('DOMContentLoaded', function () {
      setTimeout(function () { window.renderMermaidIn(document); }, 100);
    });
  }

  // ============================================================
  // 4. Dropdown close on outside click
  // ============================================================
  function initDropdown() {
    document.addEventListener('click', function (e) {
      const dd = document.getElementById('chapterDropdown');
      if (dd && !dd.contains(e.target)) dd.classList.remove('open');
    });
  }

  // ============================================================
  // 5. Service worker registration
  // ============================================================
  function initSW() {
    if ('serviceWorker' in navigator && location.protocol !== 'file:') {
      window.addEventListener('load', function () {
        navigator.serviceWorker.register('/sw.js').catch(function (e) { /* silent */ });
      });
    }
  }

  // ============================================================
  // Boot
  // ============================================================
  function boot() {
    initSearch();
    initChapter();
    initDropdown();
    initSW();
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', boot);
  } else {
    boot();
  }

  // Mermaid depends on external script - init when ready
  if (typeof mermaid !== 'undefined') {
    initMermaid();
  } else {
    document.addEventListener('DOMContentLoaded', function () {
      // Wait a tick for mermaid script to load
      if (typeof mermaid !== 'undefined') {
        initMermaid();
        initMermaidAfter();
      } else {
        // Poll briefly for mermaid
        let tries = 0;
        const it = setInterval(function () {
          if (typeof mermaid !== 'undefined') {
            initMermaid();
            initMermaidAfter();
            clearInterval(it);
          } else if (++tries > 20) { clearInterval(it); }
        }, 100);
      }
    });
  }
})();
