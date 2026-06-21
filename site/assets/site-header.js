/* MedSea shared site header — loads on /, /exam/, /flashcards/
   Provides: chapter dropdown, universal topic search, dynamic stats.
   Loads ONLY the 5 KB questions-index.json for header data (NOT the
   17 MB questions.json). Heavy question data is lazy-loaded by the
   exam/flashcard apps via /assets/site-db.js.
*/
(function () {
  'use strict';
  var $ = function (s, c) { return (c || document).querySelector(s); };
  var $$ = function (s, c) { return Array.from((c || document).querySelectorAll(s)); };

  /* ---------- Dropdown toggle ---------- */
  document.addEventListener('click', function (e) {
    var dd = $('#chapterDropdown');
    if (!dd) return;
    if (dd.contains(e.target)) {
      if (e.target.closest('.drop-btn')) dd.classList.toggle('open');
    } else {
      dd.classList.remove('open');
    }
  });

  /* ---------- Skip shared search/init if page already self-handles it ----------
     Main /index.html has its own inline search/dropdown JS. Avoid double-binding. */
  if (window.MEDSEA_PAGE_HANDLES_HEADER) {
    return; // exit early — page's own inline JS will do the work
  }

  /* ---------- Search (loads split index: 3KB manifest + 32 chapter files in parallel) ---------- */
  var idx = Object.create(null);  // per-chapter cache map (slug → array)
  var searchManifest = null;
  var debounce = null;
  var input = $('#searchInput');
  var results = $('#searchResults');
  var box = $('#searchBox');

  function escHtml(s) {
    return String(s).replace(/[&<>"']/g, function (c) {
      return ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' })[c];
    });
  }
  function highlight(t, q) {
    if (!q) return escHtml(t);
    var i = t.toLowerCase().indexOf(q.toLowerCase());
    if (i < 0) return escHtml(t);
    return escHtml(t.slice(0, i)) + '<mark>' + escHtml(t.slice(i, i + q.length)) + '</mark>' + escHtml(t.slice(i + q.length));
  }
  function loadIdx() {
    if (idx) return Promise.resolve(idx);
    // Step 1: tiny 3KB manifest pointing to per-chapter files
    return fetch('/assets/search-index.json').then(function (r) { return r.json(); }).then(function (m) {
      searchManifest = m;
      return m;
    });
  }
  // Per-chapter cache map
  function loadChapterIdx(slug, m) {
    if (idx && idx[slug]) return Promise.resolve(idx[slug]);
    if (!idx) idx = Object.create(null);
    var url = (m.files || {})[slug] || ('/assets/search/' + slug + '.json');
    return fetch(url).then(function (r) { return r.json(); }).then(function (arr) {
      idx[slug] = arr;
      return arr;
    }).catch(function () { return []; });
  }
  // Find chapters that match the query by name (no fetches needed)
  function chaptersMatching(q, m) {
    var ql = q.toLowerCase();
    var out = [];
    for (var i = 0; i < m.chapters.length && out.length < 3; i++) {
      var s = m.chapters[i];
      if (s.indexOf(ql) >= 0) out.push(s);
    }
    return out;
  }
  function search(q) {
    if (!q || q.length < 2) { if (box) box.classList.remove('open'); return; }
    loadIdx().then(function (m) {
      // Find candidate chapters (instant, no fetches)
      var slugs = chaptersMatching(q, m);
      if (slugs.length === 0) slugs = m.chapters.slice(0, 5);
      return Promise.all(slugs.map(function (s) { return loadChapterIdx(s, m); })).then(function (arrs) {
        return [].concat.apply([], arrs);
      });
    }).then(function (data) {
      var ql = q.toLowerCase();
      var hits = data.filter(function (it) {
        return (it.title && it.title.toLowerCase().indexOf(ql) >= 0) ||
               (it.chapter_name && it.chapter_name.toLowerCase().indexOf(ql) >= 0) ||
               (it.hub_name && it.hub_name.toLowerCase().indexOf(ql) >= 0) ||
               (it.topic && it.topic.toLowerCase().indexOf(ql) >= 0);
      }).slice(0, 50);
      // If < 3 hits, lazy-load more chapters in background
      if (hits.length < 3) {
        var remaining = searchManifest.chapters.filter(function (s) { return slugs.indexOf(s) < 0; });
        Promise.all(remaining.map(function (s) { return loadChapterIdx(s, searchManifest); })).then(function (arrs) {
          var more = [].concat.apply([], arrs).filter(function (it) {
            return (it.title && it.title.toLowerCase().indexOf(ql) >= 0) ||
                   (it.chapter_name && it.chapter_name.toLowerCase().indexOf(ql) >= 0) ||
                   (it.hub_name && it.hub_name.toLowerCase().indexOf(ql) >= 0) ||
                   (it.topic && it.topic.toLowerCase().indexOf(ql) >= 0);
          });
          if (more.length > hits.length) {
            hits = hits.concat(more).slice(0, 50);
            renderHits();
          }
        });
      }
      function renderHits() {
        if (!results) return;
        if (!hits.length) {
          results.innerHTML = '<div class="search-empty">No topics match "<strong>' + escHtml(q) + '</strong>"</div>';
        } else {
          results.innerHTML = hits.slice(0, 12).map(function (it) {
            return '<a class="search-hit" href="' + it.url + '?topic=' + encodeURIComponent(it.topic) + '">' +
              '<span class="hit-title">' + highlight(it.title || '', q) + '</span>' +
              '<span class="hit-meta">' + escHtml(it.chapter_name || '') + ' · ' + escHtml(it.hub_name || '') + ' · <code>' + escHtml(it.topic || '') + '</code></span>' +
              '</a>';
          }).join('');
          if (hits.length > 12) {
            results.innerHTML += '<div class="search-more">+' + (hits.length - 12) + ' more matches…</div>';
          }
        }
        if (box) box.classList.add('open');
      }
      renderHits();
    }).catch(function () {});
  }
  if (input) {
    input.addEventListener('input', function (e) {
      clearTimeout(debounce);
      debounce = setTimeout(function () { search(e.target.value.trim()); }, 150);
    });
    input.addEventListener('focus', function (e) { if (e.target.value.trim().length >= 2) search(e.target.value.trim()); });
    input.addEventListener('blur', function () { setTimeout(function () { if (box) box.classList.remove('open'); }, 200); });
    input.addEventListener('keydown', function (e) {
      if (e.key === 'Escape') { if (box) box.classList.remove('open'); input.blur(); }
    });
  }

  /* ---------- Chapter menu + stats — load ONLY the 5 KB index ---------- */
  function applyIndex(d) {
    var dd = $('#chapterDropdown');
    if (!dd) return;
    var menu = $('#chapterMenu') || dd.querySelector('.drop-menu');
    if (!menu) return;

    // Stats: lightweight; reads only totals + per-chapter counts
    var chEl = document.getElementById('stat-chapters');
    var mcqEl = document.getElementById('stat-mcq');
    var flashEl = document.getElementById('stat-flash');
    var hubsEl = document.getElementById('stat-hubs');
    var topicsEl = document.getElementById('stat-topics');
    if (chEl) chEl.textContent = d.totals.chapters;
    if (mcqEl) mcqEl.textContent = (d.totals.mcq + d.totals.sba).toLocaleString();
    if (flashEl) flashEl.textContent = d.totals.flashcard.toLocaleString();
    if (hubsEl) hubsEl.textContent = d.chapters.reduce(function (s, c) { return s + (c.hubs || 0); }, 0);
    if (topicsEl) topicsEl.textContent = d.chapters.reduce(function (s, c) { return s + (c.topic_count || 0); }, 0).toLocaleString();

    // Chapter menu: if hardcoded items exist, update badges; else build
    if (menu.children.length > 0) {
      var map = {};
      d.chapters.forEach(function (c) { map[c.num] = c; });
      Array.from(menu.querySelectorAll('.item')).forEach(function (it) {
        var numEl = it.querySelector('.num');
        if (!numEl) return;
        var n = parseInt(numEl.textContent, 10);
        var data = map[n];
        if (data && data.slug) {
          it.classList.remove('soon');
          it.removeAttribute('onclick');
          it.setAttribute('href', '/' + data.slug + '/');
          var badge = it.querySelector('.badge');
          if (badge) badge.textContent = '●';
        }
      });
      return;
    }
    menu.innerHTML = d.chapters.map(function (c) {
      var topicCount = c.topic_count || 0;
      return '<a class="item" href="/' + c.slug + '/">' +
        '<span class="num">' + c.num + '</span>' +
        '<span class="name">' + escHtml(c.name) + ' <span style="color:var(--text-dim);font-size:10px;">·' + topicCount + '</span></span>' +
        '<span class="badge">●</span>' +
        '</a>';
    }).join('');
  }

  if (window.MedSeaDB && window.MedSeaDB.loadIndex) {
    window.MedSeaDB.loadIndex().then(applyIndex).catch(function () {});
  } else {
    // Fallback for pages where site-db.js didn't load
    fetch('/assets/questions-index.json').then(function (r) { return r.json(); }).then(applyIndex).catch(function () {});
  }

  /* ---------- Active link highlight ---------- */
  var path = location.pathname;
  $$('.ext-links a').forEach(function (a) {
    var href = a.getAttribute('href');
    if (href === '/' && (path === '/' || path === '/index.html')) a.classList.add('active');
    else if (href !== '/' && path.indexOf(href) === 0) a.classList.add('active');
  });
})();
