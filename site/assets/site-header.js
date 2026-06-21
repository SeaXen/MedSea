/* MedSea shared site header — loads on /, /exam/, /flashcards/
   Provides: chapter dropdown, universal topic search, dynamic stats
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
      // Toggle if click was on the drop-btn
      if (e.target.closest('.drop-btn')) dd.classList.toggle('open');
    } else {
      dd.classList.remove('open');
    }
  });

  /* ---------- Search ---------- */
  var idx = null;
  var debounce = null;
  var input = $('#searchInput');
  var results = $('#searchResults');
  var box = $('#searchBox');

  function escHtml(s) {
    return String(s == null ? '' : s)
      .replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;')
      .replace(/"/g, '&quot;').replace(/'/g, '&#39;');
  }
  function highlight(text, q) {
    if (!q) return escHtml(text);
    var i = text.toLowerCase().indexOf(q.toLowerCase());
    if (i < 0) return escHtml(text);
    return escHtml(text.slice(0, i)) + '<mark>' + escHtml(text.slice(i, i + q.length)) + '</mark>' + escHtml(text.slice(i + q.length));
  }
  function loadIdx() {
    if (idx) return Promise.resolve(idx);
    return fetch('/search_index.json', { cache: 'no-cache' })
      .then(function (r) { return r.json(); })
      .then(function (d) { idx = d; return d; });
  }
  function search(q) {
    if (!results) return;
    if (!q || q.length < 2) { box.classList.remove('open'); results.innerHTML = ''; return; }
    loadIdx().then(function (data) {
      var ql = q.toLowerCase();
      var hits = [];
      for (var i = 0; i < data.length; i++) {
        var item = data[i];
        var t = (item.title || '').toLowerCase();
        var h = (item.hub_name || '').toLowerCase();
        var c = (item.chapter_name || '').toLowerCase();
        var score = 0;
        if (t === ql) score = 100;
        else if (t.startsWith(ql)) score = 80;
        else if (t.indexOf(ql) !== -1) score = 60;
        else if (h.indexOf(ql) !== -1) score = 40;
        else if (c.indexOf(ql) !== -1) score = 20;
        if (item.topic && item.topic.startsWith(ql)) score = Math.max(score, 70);
        if (score > 0) hits.push({ item: item, score: score });
      }
      hits.sort(function (a, b) { return b.score - a.score || a.item.title.localeCompare(b.item.title); });
      var top = hits.slice(0, 12);
      if (top.length === 0) {
        results.innerHTML = '<div class="search-empty">No topics match "<strong>' + escHtml(q) + '</strong>"</div>';
      } else {
        results.innerHTML = top.map(function (h) {
          var it = h.item;
          return '<a class="search-hit" href="' + it.url + '?topic=' + encodeURIComponent(it.topic) + '">' +
            '<span class="hit-ch">' + it.chapter_num + '</span>' +
            '<span class="hit-body">' +
              '<span class="hit-title">' + highlight(it.title, q) + '</span>' +
              '<span class="hit-meta">' + highlight(it.chapter_name, q) + ' · ' + highlight(it.hub_name, q) + ' · ' + (it.topic || '') + '</span>' +
            '</span>' +
            '<span class="hit-arrow">→</span>' +
          '</a>';
        }).join('');
        if (hits.length > 12) {
          results.innerHTML += '<div class="search-more">+' + (hits.length - 12) + ' more matches…</div>';
        }
      }
      box.classList.add('open');
    });
  }
  if (input) {
    input.addEventListener('input', function (e) {
      clearTimeout(debounce);
      debounce = setTimeout(function () { search(e.target.value.trim()); }, 150);
    });
    input.addEventListener('focus', function (e) { if (e.target.value.trim().length >= 2) search(e.target.value.trim()); });
    input.addEventListener('blur', function () { setTimeout(function () { box.classList.remove('open'); }, 200); });
    input.addEventListener('keydown', function (e) {
      if (e.key === 'Escape') { box.classList.remove('open'); input.blur(); }
    });
  }

  /* ---------- Populate chapter menu from questions.json (only if menu is empty) ---------- */
  function buildChapterMenu() {
    var dd = $('#chapterDropdown');
    if (!dd) return;
    var menu = $('#chapterMenu') || dd.querySelector('.drop-menu');
    if (!menu) return;
    // If the menu already has hardcoded items (e.g. /index.html), update badges only — don't overwrite
    if (menu.children.length > 0) {
      // Map existing items by chapter num, then enable/update badges based on questions.json
      fetch('/assets/questions.json', { cache: 'no-cache' })
        .then(function (r) { return r.json(); })
        .then(function (d) {
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
        });
      return;
    }
    fetch('/assets/questions.json', { cache: 'no-cache' })
      .then(function (r) { return r.json(); })
      .then(function (d) {
        menu.innerHTML = d.chapters.map(function (c) {
          var num = c.num;
          var slug = c.slug;
          var name = c.name;
          var ready = true;
          var cls = ready ? 'item' : 'item soon';
          var badge = ready ? '●' : '○';
          var href = ready ? ('/' + slug + '/') : '#';
          var onclick = ready ? '' : 'onclick="event.preventDefault();"';
          var topicCount = c.topic_count || 0;
          return '<a class="' + cls + '" ' + onclick + ' href="' + href + '">' +
            '<span class="num">' + num + '</span>' +
            '<span class="name">' + escHtml(name) + ' <span style="color:var(--text-dim);font-size:10px;">·' + topicCount + '</span></span>' +
            '<span class="badge">' + badge + '</span>' +
            '</a>';
        }).join('');
      })
      .catch(function () {});
  }
  buildChapterMenu();

  /* ---------- Dynamic stats (override on all pages for consistency) ---------- */
  function loadStats() {
    fetch('/assets/questions.json', { cache: 'no-cache' })
      .then(function (r) { return r.json(); })
      .then(function (d) {
        var chEl = document.getElementById('stat-chapters');
        var mcqEl = document.getElementById('stat-mcq');
        var flashEl = document.getElementById('stat-flash');
        var hubsEl = document.getElementById('stat-hubs');
        var topicsEl = document.getElementById('stat-topics');
        if (chEl) chEl.textContent = d.totals.chapters;
        if (mcqEl) mcqEl.textContent = (d.totals.mcq + d.totals.sba).toLocaleString();
        if (flashEl) flashEl.textContent = d.totals.flashcard.toLocaleString();
        // On pages that include hubs + topics slots, populate them too
        if (hubsEl) hubsEl.textContent = d.chapters.reduce(function (s, c) { return s + (c.hubs || 0); }, 0);
        if (topicsEl) topicsEl.textContent = d.chapters.reduce(function (s, c) { return s + (c.topic_count || 0); }, 0).toLocaleString();
      })
      .catch(function () {});
  }
  loadStats();

  /* ---------- Active link highlight ---------- */
  var path = location.pathname;
  $$('.ext-links a').forEach(function (a) {
    var href = a.getAttribute('href');
    if (href === '/' && (path === '/' || path === '/index.html')) a.classList.add('active');
    else if (href !== '/' && path.indexOf(href) === 0) a.classList.add('active');
  });
})();