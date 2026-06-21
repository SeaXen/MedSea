/* MedSea Flashcards page logic — depends on /assets/exam-engine.js */
(function () {
  'use strict';

  var $ = function (s, c) { return (c || document).querySelector(s); };
  var $$ = function (s, c) { return Array.from((c || document).querySelectorAll(s)); };
  var MedSea = window.MedSea;

  var SETUP = {
    order: 'random',
    count: 20,
    minutes: 0,
    mode: 'flip',         // 'flip' = flip+rate; 'quick' = show both at once
    autoFlipSec: 5,
    chapters: [],
  };

  var DB_DATA = null;
  var CURRENT = null;
  var AUTOFLIP_HANDLE = null;

  /* ---------- tabs ---------- */
  $$('.tabs .tab').forEach(function (t) {
    t.addEventListener('click', function () {
      $$('.tabs .tab').forEach(function (x) { x.classList.remove('active'); });
      t.classList.add('active');
      var name = t.dataset.tab;
      $$('.panel').forEach(function (p) { p.classList.remove('active'); });
      $('#panel-' + name).classList.add('active');
      if (name === 'history') renderHistory();
      if (name === 'analytics') renderAnalytics();
    });
  });

  /* ---------- toast ---------- */
  var toastT;
  function toast(msg) {
    var t = $('#toast'); t.textContent = msg; t.classList.add('show');
    clearTimeout(toastT);
    toastT = setTimeout(function () { t.classList.remove('show'); }, 2200);
  }

  /* ---------- DB load ---------- */
  MedSea.DB.load()
    .then(function (data) {
      DB_DATA = data;
      renderChapterChips(data.chapters);
      updateAvailable();
    })
    .catch(function (err) {
      console.error(err);
      $('#ch-chips').innerHTML = '<span style="color:var(--bad);font-size:12px;padding:6px;">Failed to load DB: ' + err.message + '</span>';
    });

  /* ---------- chapters ---------- */
  function renderChapterChips(chapters) {
    var html = '';
    chapters.forEach(function (c) {
      html += '<span class="chip" data-ch="' + c.num + '">' +
        '<span class="num">Ch ' + c.num + '</span>' +
        '<span>' + c.name + '</span>' +
        '<span style="font-size:9px;color:var(--text-dim);">·' + c.flashcard_count + ' cards</span>' +
        '</span>';
    });
    $('#ch-chips').innerHTML = html;
    $$('#ch-chips .chip').forEach(function (chip) {
      chip.addEventListener('click', function () {
        chip.classList.toggle('selected');
        var n = parseInt(chip.dataset.ch, 10);
        var i = SETUP.chapters.indexOf(n);
        if (i === -1) SETUP.chapters.push(n); else SETUP.chapters.splice(i, 1);
        updateAvailable();
      });
    });
  }
  $('#ch-all').addEventListener('click', function () {
    SETUP.chapters = DB_DATA.chapters.map(function (c) { return c.num; });
    refreshChips();
  });
  $('#ch-none').addEventListener('click', function () {
    SETUP.chapters = []; refreshChips();
  });
  $('#ch-clinical').addEventListener('click', function () {
    SETUP.chapters = DB_DATA.chapters.filter(function (c) { return c.num >= 1 && c.num <= 15; }).map(function (c) { return c.num; });
    refreshChips();
  });
  $('#ch-system').addEventListener('click', function () {
    SETUP.chapters = DB_DATA.chapters.filter(function (c) { return c.num >= 16; }).map(function (c) { return c.num; });
    refreshChips();
  });
  function refreshChips() {
    $$('#ch-chips .chip').forEach(function (c) {
      var n = parseInt(c.dataset.ch, 10);
      if (SETUP.chapters.indexOf(n) !== -1) c.classList.add('selected');
      else c.classList.remove('selected');
    });
    updateAvailable();
  }

  /* ---------- toggles ---------- */
  $$('.toggle-row .toggle').forEach(function (t) {
    t.addEventListener('click', function () {
      var siblings = t.parentNode.querySelectorAll('.toggle');
      siblings.forEach(function (x) { x.classList.remove('active'); });
      t.classList.add('active');
      if (t.dataset.order !== undefined) SETUP.order = t.dataset.order;
      if (t.dataset.mode !== undefined) SETUP.mode = t.dataset.mode;
      if (t.dataset.autoflip !== undefined) {
        SETUP.autoFlipSec = parseInt(t.dataset.autoflip, 10);
      }
    });
  });

  $('#c-count').addEventListener('input', function () { SETUP.count = parseInt($('#c-count').value, 10) || 1; });
  $('#c-time').addEventListener('input', function () { SETUP.minutes = parseInt($('#c-time').value, 10) || 0; });

  function buildPool() {
    if (!DB_DATA) return [];
    return DB_DATA.flashcard.filter(function (q) {
      return SETUP.chapters.length === 0 || SETUP.chapters.indexOf(q.chapter_num) !== -1;
    });
  }
  function updateAvailable() {
    if (!DB_DATA) return;
    var pool = buildPool();
    $('#avail-count').textContent = pool.length + ' matching';
    if (pool.length === 0) {
      $('#btn-start').disabled = true;
      $('#setup-summary').textContent = 'No flashcards — pick at least one chapter.';
      return;
    }
    $('#btn-start').disabled = false;
    $('#setup-summary').textContent =
      SETUP.chapters.length === 0
        ? 'All chapters · ' + pool.length + ' cards available'
        : SETUP.chapters.length + ' chapter' + (SETUP.chapters.length === 1 ? '' : 's') + ' · ' + pool.length + ' cards available';
  }

  /* ---------- start ---------- */
  $('#btn-start').addEventListener('click', function () {
    if (!DB_DATA) return;
    var pool = buildPool();
    if (pool.length === 0) { toast('Pick at least one chapter.'); return; }
    var chosen;
    if (SETUP.order === 'random') chosen = MedSea.Pool.pick(pool, SETUP.count);
    else chosen = pool.slice(0, SETUP.count);

    var dur = SETUP.minutes > 0 ? SETUP.minutes * 60 : null;
    var chapterLabel = SETUP.chapters.length === 0
      ? 'All chapters'
      : (SETUP.chapters.length <= 3
          ? SETUP.chapters.map(function (n) { return 'Ch ' + n; }).join(', ')
          : SETUP.chapters.length + ' chapters');
    var title = SETUP.order === 'random' ? 'Random' : 'Sequential' + ' · ' + chapterLabel + ' · ' + chosen.length + ' cards';
    var chaptersUsed = chosen.map(function (q) { return q.chapter_num; })
      .filter(function (v, i, a) { return a.indexOf(v) === i; });

    CURRENT = MedSea.Engine.startFlashcards({
      cards: chosen,
      duration_sec: dur,
      title: title,
      chapters: chaptersUsed,
    });
    CURRENT.onChange(renderRunner);
    renderRunner();
    switchTab('runner');
    CURRENT.startTimer(renderRunnerTimer);
    if (SETUP.autoFlipSec > 0 && SETUP.mode === 'flip') startAutoFlip();
  });

  function switchTab(name) {
    $$('.tabs .tab').forEach(function (x) {
      x.classList.toggle('active', x.dataset.tab === name);
    });
    $$('.panel').forEach(function (p) { p.classList.remove('active'); });
    $('#panel-' + name).classList.add('active');
    if (name === 'history') renderHistory();
    if (name === 'analytics') renderAnalytics();
  }

  /* ---------- render ---------- */
  function renderRunnerTimer() {
    if (!CURRENT) return;
    var rem = CURRENT.remainingSec();
    if (rem == null) { $('#r-timer').textContent = '--:--'; $('#r-timer').className = 'timer'; return; }
    $('#r-timer').textContent = MedSea.Format.fmtTime(rem);
    $('#r-timer').className = 'timer' + (rem < 60 ? ' danger' : rem < 300 ? ' warn' : '');
  }

  function startAutoFlip() {
    if (AUTOFLIP_HANDLE) clearTimeout(AUTOFLIP_HANDLE);
    if (SETUP.mode !== 'flip') return;
    AUTOFLIP_HANDLE = setTimeout(function () {
      if (!CURRENT || CURRENT.finished) return;
      if (!CURRENT.flipped) {
        CURRENT.flip();
      }
    }, SETUP.autoFlipSec * 1000);
  }

  function renderRunner() {
    if (!CURRENT) return;
    if (CURRENT.finished) { renderResult(); return; }
    var c = CURRENT.cards[CURRENT.idx];
    $('#c-meta-q').textContent = 'Ch ' + c.chapter_num + ' · ' + c.chapter_name;
    $('#c-meta-a').textContent = 'Ch ' + c.chapter_num + ' · ' + c.chapter_name;
    $('#c-q').textContent = c.front;
    $('#c-a').textContent = c.back;
    $('#c-source').innerHTML = '<a href="/' + c.chapter_slug + '/">Ch ' + c.chapter_num + ' · ' + escape(c.chapter_name) + '</a> · Topic <code>' + escape(c.topic_slug) + '</code>';
    if (SETUP.mode === 'quick') {
      $('#card-flip').classList.add('flipped');
    } else {
      $('#card-flip').classList.toggle('flipped', CURRENT.flipped);
    }

    // bar
    var pct = Math.round(((CURRENT.idx + 1) / CURRENT.total()) * 100);
    $('#r-bar').style.width = pct + '%';
    $('#r-cnum').textContent = CURRENT.idx + 1;
    $('#r-ctotal').textContent = CURRENT.total();
    $('#r-known').textContent = CURRENT.known();
    $('#r-hard').textContent = countHard();

    function countHard() {
      var c = 0;
      Object.keys(CURRENT.ratings).forEach(function (k) { if (CURRENT.ratings[k] === 'hard') c++; });
      return c;
    }

    // palette
    var pal = '';
    CURRENT.cards.forEach(function (cc, i) {
      var cls = 'cp-item';
      var r = CURRENT.ratings[cc.id];
      if (r === 'known') cls += ' known';
      else if (r === 'unknown') cls += ' unknown';
      else if (r === 'hard') cls += ' hard';
      if (i === CURRENT.idx) cls += ' current';
      pal += '<span class="' + cls + '" data-i="' + i + '">' + (i + 1) + '</span>';
    });
    $('#r-palette').innerHTML = pal;
    $$('#r-palette .cp-item').forEach(function (p) {
      p.addEventListener('click', function () { CURRENT.goto(parseInt(p.dataset.i, 10)); });
    });
    renderRunnerTimer();
  }

  /* rate buttons */
  $$('.rate-btn').forEach(function (b) {
    b.addEventListener('click', function () { rateAndNext(b.dataset.rate); });
  });
  function rateAndNext(rating) {
    if (!CURRENT || CURRENT.finished) return;
    var c = CURRENT.cards[CURRENT.idx];
    CURRENT.rate(c.id, rating);
    if (CURRENT.idx < CURRENT.total() - 1) CURRENT.next();
    else {
      if (confirm('You\'ve reached the last card. Finish session?')) {
        CURRENT.finish();
        renderResult();
        switchTab('result');
      } else {
        renderRunner();
      }
      return;
    }
    if (AUTOFLIP_HANDLE) { clearTimeout(AUTOFLIP_HANDLE); AUTOFLIP_HANDLE = null; }
    startAutoFlip();
  }

  $('#btn-prev').addEventListener('click', function () { if (CURRENT) CURRENT.prev(); });
  $('#btn-next').addEventListener('click', function () {
    if (!CURRENT || CURRENT.finished) return;
    CURRENT.rate(CURRENT.cards[CURRENT.idx].id, 'skip');
    if (CURRENT.idx < CURRENT.total() - 1) CURRENT.next();
  });
  $('#btn-quit').addEventListener('click', function () {
    if (!CURRENT) return;
    if (!confirm('Quit this flashcard session?')) return;
    CURRENT = null;
    if (AUTOFLIP_HANDLE) clearTimeout(AUTOFLIP_HANDLE);
    switchTab('setup');
  });
  $('#btn-finish').addEventListener('click', function () {
    if (!CURRENT || CURRENT.finished) return;
    if (!confirm('Finish this session now? Unrated cards count as skipped.')) return;
    CURRENT.finish();
    renderResult();
    switchTab('result');
  });

  $('#card-flip').addEventListener('click', function () {
    if (!CURRENT || SETUP.mode === 'quick') return;
    CURRENT.flip();
  });

  /* keyboard */
  document.addEventListener('keydown', function (e) {
    if (!$('#panel-runner').classList.contains('active')) return;
    if (!CURRENT) return;
    if (e.target.tagName === 'INPUT') return;
    if (e.code === 'Space') { e.preventDefault(); CURRENT.flip(); }
    else if (e.key === '1') rateAndNext('unknown');
    else if (e.key === '2') rateAndNext('hard');
    else if (e.key === '3') rateAndNext('known');
    else if (e.key === 'ArrowRight') {
      if (CURRENT.idx < CURRENT.total() - 1) CURRENT.next();
    }
    else if (e.key === 'ArrowLeft') {
      if (CURRENT.idx > 0) CURRENT.prev();
    }
  });

  /* ---------- result ---------- */
  function renderResult() {
    if (!CURRENT) return;
    var known = CURRENT.known(), unknown = CURRENT.unknown(), hard = countHard();
    var rated = known + unknown + hard;
    var total = CURRENT.total();
    var acc = rated ? Math.round((known / rated) * 100) : 0;
    var grade = gradeFor(acc);

    $('#r-hero').innerHTML =
      '<div class="result-score">' + acc + '%</div>' +
      '<div class="result-line">Retention across ' + rated + ' rated cards</div>' +
      '<div class="result-grade" style="color:' + grade.color + '">' + grade.label + '</div>' +
      '<div class="result-line" style="margin-top:10px;">' + escape(CURRENT.cfg.title) + '</div>';

    var stats = [
      { label: 'Known', value: known, cls: 'good' },
      { label: 'Hard', value: hard, cls: 'warn' },
      { label: 'Again', value: unknown, cls: 'bad' },
      { label: 'Skipped', value: total - rated, cls: 'warn' },
      { label: 'Total', value: total, cls: '' },
      { label: 'Time', value: MedSea.Format.fmtTime(Math.floor(CURRENT.duration_ms / 1000)), cls: '' },
    ];
    var sh = '';
    stats.forEach(function (st) {
      sh += '<div class="stat-card ' + (st.cls || '') + '"><div class="label">' + st.label + '</div><div class="value">' + st.value + '</div></div>';
    });
    $('#r-stats').innerHTML = sh;

    // weak cards
    var weak = [];
    CURRENT.cards.forEach(function (c) {
      var r = CURRENT.ratings[c.id];
      if (r === 'unknown' || r === 'hard') {
        weak.push({ card: c, rating: r });
      }
    });
    if (weak.length === 0) {
      $('#weak-cards').innerHTML = '<div style="font-size:12px;color:var(--text-dim);padding:8px;">No weak cards — great session!</div>';
    } else {
      var wh = '';
      weak.slice(0, 50).forEach(function (w) {
        var badge = w.rating === 'unknown' ? '✗ AGAIN' : '⚠ HARD';
        var cls = w.rating === 'unknown' ? 'bad' : 'warn';
        wh += '<div class="review-item ' + cls + '" style="background:var(--bg-2);border:1px solid var(--border);border-left:3px solid var(--' + cls + ');padding:10px 12px;border-radius:8px;margin-bottom:6px;">' +
          '<div style="font-size:11px;color:var(--text-dim);font-family:\'JetBrains Mono\',monospace;margin-bottom:4px;">Ch ' + w.card.chapter_num + ' · ' + escape(w.card.chapter_name) + ' · <span class="badge" style="background:rgba(239,68,68,0.18);color:var(--bad);padding:1px 6px;border-radius:3px;font-size:10px;font-weight:700;">' + badge + '</span></div>' +
          '<div style="font-size:13px;font-weight:500;margin-bottom:4px;">' + escape(w.card.front) + '</div>' +
          '<div style="font-size:12px;color:var(--text-dim);">' + escape(w.card.back) + '</div>' +
          '</div>';
      });
      if (weak.length > 50) wh += '<div style="text-align:center;font-size:11px;color:var(--text-dim);padding:6px;">…and ' + (weak.length - 50) + ' more</div>';
      $('#weak-cards').innerHTML = wh;
    }
  }

  function countHard() {
    var c = 0;
    Object.keys(CURRENT.ratings).forEach(function (k) { if (CURRENT.ratings[k] === 'hard') c++; });
    return c;
  }
  function gradeFor(acc) {
    if (acc >= 90) return { label: 'Outstanding retention', color: 'var(--good)' };
    if (acc >= 75) return { label: 'Solid — review the weak cards', color: 'var(--good)' };
    if (acc >= 60) return { label: 'OK — needs more practice', color: 'var(--warn)' };
    if (acc >= 40) return { label: 'Below target — repeat session', color: 'var(--warn)' };
    return { label: 'Needs serious revision', color: 'var(--bad)' };
  }

  $('#btn-result-new').addEventListener('click', function () { CURRENT = null; switchTab('setup'); });
  $('#btn-result-history').addEventListener('click', function () { switchTab('history'); });

  /* ---------- history ---------- */
  function renderHistory() {
    var list = MedSea.History.flashes();
    if (list.length === 0) {
      $('#hist-list').innerHTML = '<div class="empty-state"><div class="icon">🃏</div><p>No flashcard sessions yet. Start one above and your history will appear here.</p></div>';
      return;
    }
    var html = '';
    list.forEach(function (r) {
      var rated = (r.known || 0) + (r.unknown || 0) + (function () {
        // no hard in saved? count skip
        var skipCount = (r.breakdown || []).filter(function (b) { return b.rating === 'hard'; }).length;
        return skipCount;
      })();
      var acc = rated ? Math.round((r.known / rated) * 100) : 0;
      var cls = acc >= 75 ? 'good' : acc >= 50 ? '' : 'bad';
      html += '<div class="hist-item">' +
        '<div class="hi-head">' +
        '<span class="hi-title">' + escape(r.title) + '</span>' +
        '<span class="hi-when">' + MedSea.Format.fmtDate(r.finished_at || r.started_at) + '</span>' +
        '</div>' +
        '<div class="hi-meta">' +
        '<span class="stat ' + cls + '"><strong>' + acc + '%</strong> retention</span>' +
        '<span class="stat">Got it <strong>' + (r.known || 0) + '</strong></span>' +
        '<span class="stat">Again <strong>' + (r.unknown || 0) + '</strong></span>' +
        '<span class="stat">Time <strong>' + MedSea.Format.fmtTime(Math.floor((r.duration_ms || 0) / 1000)) + '</strong></span>' +
        '<span class="stat">Chapters <strong>' + (r.chapters || []).length + '</strong></span>' +
        '</div>' +
        '</div>';
    });
    $('#hist-list').innerHTML = html;
  }

  $('#btn-clear-hist').addEventListener('click', function () {
    if (!confirm('Clear all flashcard history?')) return;
    MedSea.History.clear();
    renderHistory();
    toast('History cleared.');
  });

  /* ---------- analytics ---------- */
  function renderAnalytics() {
    var stats = MedSea.History.stats();
    var html = '';

    html += '<div class="analytics-card"><h3>🃏 Flashcard Overview</h3>';
    if (stats.flashCount === 0) html += '<div style="font-size:12px;color:var(--text-dim);">No sessions yet.</div>';
    else {
      html += '<div class="bm-row"><span class="bm-label">Sessions</span><span class="bm-val"><strong>' + stats.flashCount + '</strong></span></div>';
      html += '<div class="bm-row"><span class="bm-label">Cards</span><span class="bm-val"><strong>' + stats.cards.total + '</strong></span></div>';
      html += '<div class="bm-row"><span class="bm-label">Retention</span><span class="bm-bar"><span class="bm-fill ' + (stats.cards.retention >= 75 ? 'good' : stats.cards.retention >= 50 ? 'warn' : 'bad') + '" style="width:' + stats.cards.retention + '%;"></span></span><span class="bm-val"><strong>' + stats.cards.retention + '%</strong></span></div>';
      html += '<div class="bm-row"><span class="bm-label">Time</span><span class="bm-val"><strong>' + MedSea.Format.fmtTime(Math.floor(stats.cards.time_ms / 1000)) + '</strong></span></div>';
    }
    html += '</div>';

    html += '<div class="analytics-card"><h3>📊 Exam Cross-ref</h3>';
    if (stats.examCount === 0) html += '<div style="font-size:12px;color:var(--text-dim);">No exams taken yet.</div>';
    else {
      html += '<div class="bm-row"><span class="bm-label">Attempts</span><span class="bm-val"><strong>' + stats.examCount + '</strong></span></div>';
      html += '<div class="bm-row"><span class="bm-label">Accuracy</span><span class="bm-bar"><span class="bm-fill ' + (stats.exams.accuracy >= 75 ? 'good' : stats.exams.accuracy >= 50 ? 'warn' : 'bad') + '" style="width:' + stats.exams.accuracy + '%;"></span></span><span class="bm-val"><strong>' + stats.exams.accuracy + '%</strong></span></div>';
    }
    html += '</div>';

    html += '<div class="analytics-card"><h3>🔥 Streak</h3><div class="bm-row"><span class="bm-label">Days</span><span class="bm-val"><strong>' + computeStreak() + '</strong></span></div></div>';

    $('#analytics-cards').innerHTML = html;

    // chapter retention from flashcard history
    var list = MedSea.History.flashes();
    var map = {};
    list.forEach(function (r) {
      (r.chapters || []).forEach(function (c) {
        if (!map[c]) map[c] = { known: 0, total: 0 };
        var bKnown = (r.breakdown || []).filter(function (b) { return b.rating === 'known'; }).length;
        var bRated = (r.breakdown || []).filter(function (b) { return b.rating !== 'skip'; }).length;
        map[c].known += bKnown;
        map[c].total += bRated;
      });
    });
    var keys = Object.keys(map).map(function (k) { return parseInt(k, 10); }).sort(function (a, b) { return a - b; });
    if (keys.length === 0) {
      $('#ch-bars').innerHTML = '<div style="font-size:12px;color:var(--text-dim);padding:20px;text-align:center;">Complete flashcard sessions to see chapter-wise retention.</div>';
    } else {
      var bh = '';
      keys.forEach(function (k) {
        var data = map[k];
        var acc = data.total ? Math.round((data.known / data.total) * 100) : 0;
        var name = (DB_DATA.chapters.find(function (c) { return c.num === k; }) || { name: 'Ch ' + k }).name;
        var cls = acc >= 75 ? 'good' : acc >= 50 ? 'warn' : 'bad';
        bh += '<div class="bm-row"><span class="bm-label">Ch ' + k + '</span><span class="bm-bar"><span class="bm-fill ' + cls + '" style="width:' + acc + '%;"></span></span><span class="bm-val"><strong>' + acc + '%</strong> · ' + data.known + '/' + data.total + '</span></div>';
      });
      $('#ch-bars').innerHTML = bh;
    }
  }

  function computeStreak() {
    var list = MedSea.History.flashes();
    if (list.length === 0) return '0';
    var today = new Date(); today.setHours(0, 0, 0, 0);
    var streak = 0;
    for (var i = 0; i < 365; i++) {
      var day = new Date(today); day.setDate(today.getDate() - i);
      var has = list.some(function (r) {
        var d = new Date(r.started_at);
        return d.getFullYear() === day.getFullYear() &&
               d.getMonth() === day.getMonth() &&
               d.getDate() === day.getDate();
      });
      if (has) streak++; else if (i > 0) break;
    }
    return streak + (streak === 1 ? ' day' : ' days');
  }

  function escape(s) {
    return String(s == null ? '' : s)
      .replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;')
      .replace(/"/g, '&quot;').replace(/'/g, '&#39;');
  }
})();