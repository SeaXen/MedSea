/* MedSea Exam page logic — depends on /assets/exam-engine.js */
(function () {
  'use strict';

  var $ = function (s, c) { return (c || document).querySelector(s); };
  var $$ = function (s, c) { return Array.from((c || document).querySelectorAll(s)); };
  var MedSea = window.MedSea;

  var SETUP = {
    mode: 'sba',          // 'sba' | 'mcq' | 'both'
    count: 20,
    minutes: 0,
    shuffle: true,
    showAfter: 'end',     // 'end' | 'each'
    chapters: [],         // array of chapter_num
  };

  var DB_DATA = null;
  var CURRENT_EXAM = null;

  /* ---------- tab switching ---------- */
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
    var t = $('#toast');
    t.textContent = msg;
    t.classList.add('show');
    clearTimeout(toastT);
    toastT = setTimeout(function () { t.classList.remove('show'); }, 2200);
  }

  /* ---------- DB load ---------- */
  MedSea.DB.load()
    .then(function (data) {
      DB_DATA = data;
      renderChapterChips(data.chapters);
      updateAvailable();
      $('#hdr-stats').textContent =
        data.totals.chapters + ' chapters · ' +
        (data.totals.mcq + data.totals.sba) + ' questions · ' +
        data.totals.flashcard + ' cards';
    })
    .catch(function (err) {
      console.error(err);
      $('#ch-chips').innerHTML = '<span style="color:var(--bad);font-size:12px;padding:6px;">Failed to load question DB: ' + err.message + '</span>';
    });

  /* ---------- chapter chips ---------- */
  // Clinical = parts 1-2 (chapters 1-15 typically); system-based = parts 3+
  function renderChapterChips(chapters) {
    var html = '';
    chapters.forEach(function (c) {
      html += '<span class="chip" data-ch="' + c.num + '">' +
        '<span class="num">Ch ' + c.num + '</span>' +
        '<span>' + c.name + '</span>' +
        '<span style="font-size:9px;color:var(--text-dim);">·' + (c.mcq_count + c.sba_count) + 'Q</span>' +
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
    $$('#ch-chips .chip').forEach(function (c) { c.classList.add('selected'); });
    updateAvailable();
  });
  $('#ch-none').addEventListener('click', function () {
    SETUP.chapters = [];
    $$('#ch-chips .chip').forEach(function (c) { c.classList.remove('selected'); });
    updateAvailable();
  });
  $('#ch-clinical').addEventListener('click', function () {
    // clinical = chapters 1-15 (parts 1-2)
    SETUP.chapters = DB_DATA.chapters.filter(function (c) { return c.num >= 1 && c.num <= 15; }).map(function (c) { return c.num; });
    refreshChips();
  });
  $('#ch-system').addEventListener('click', function () {
    // system-based = chapters 16+
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
      if (t.dataset.mode !== undefined) SETUP.mode = t.dataset.mode;
      if (t.dataset.shuffle !== undefined) SETUP.shuffle = t.dataset.shuffle === '1';
      if (t.dataset.showafter !== undefined) SETUP.showAfter = t.dataset.showafter;
      updateAvailable();
    });
  });

  $('#q-count').addEventListener('input', function () {
    SETUP.count = parseInt($('#q-count').value, 10) || 1;
    updateAvailable();
  });
  $('#q-time').addEventListener('input', function () {
    SETUP.minutes = parseInt($('#q-time').value, 10) || 0;
  });

  function buildPool() {
    if (!DB_DATA) return [];
    var pool = [];
    if (SETUP.mode === 'mcq' || SETUP.mode === 'both') {
      pool = pool.concat(DB_DATA.mcq.filter(function (q) {
        return SETUP.chapters.length === 0 || SETUP.chapters.indexOf(q.chapter_num) !== -1;
      }));
    }
    if (SETUP.mode === 'sba' || SETUP.mode === 'both') {
      pool = pool.concat(DB_DATA.sba.filter(function (q) {
        return SETUP.chapters.length === 0 || SETUP.chapters.indexOf(q.chapter_num) !== -1;
      }));
    }
    return pool;
  }
  function updateAvailable() {
    if (!DB_DATA) return;
    var pool = buildPool();
    $('#avail-count').textContent = pool.length + ' matching';
    if (pool.length === 0) {
      $('#btn-start').disabled = true;
      $('#setup-summary').textContent = 'No questions match — pick at least one chapter.';
      return;
    }
    $('#btn-start').disabled = false;
    $('#setup-summary').textContent =
      SETUP.chapters.length === 0
        ? 'All chapters · ' + pool.length + ' available'
        : SETUP.chapters.length + ' chapter' + (SETUP.chapters.length === 1 ? '' : 's') + ' · ' + pool.length + ' available';
  }

  /* ---------- start exam ---------- */
  $('#btn-start').addEventListener('click', function () {
    if (!DB_DATA) return;
    var pool = buildPool();
    if (pool.length === 0) { toast('Pick at least one chapter.'); return; }
    var chosen;
    if (SETUP.shuffle) chosen = MedSea.Pool.pick(pool, SETUP.count);
    else chosen = pool.slice(0, SETUP.count);

    var dur = SETUP.minutes > 0 ? SETUP.minutes * 60 : null;
    var chapterLabel = SETUP.chapters.length === 0
      ? 'All chapters'
      : (SETUP.chapters.length <= 3
          ? SETUP.chapters.map(function (n) { return 'Ch ' + n; }).join(', ')
          : SETUP.chapters.length + ' chapters');
    var title = SETUP.mode.toUpperCase() + ' · ' + chapterLabel + ' · ' + chosen.length + 'Q';
    var chaptersUsed = chosen.map(function (q) { return q.chapter_num; })
      .filter(function (v, i, a) { return a.indexOf(v) === i; });

    CURRENT_EXAM = MedSea.Engine.startExam({
      questions: chosen,
      duration_sec: dur,
      title: title,
      chapters: chaptersUsed,
      mode: SETUP.mode,
      question_types: SETUP.mode === 'both' ? ['mcq', 'sba'] : [SETUP.mode],
    });
    CURRENT_EXAM.showAfter = SETUP.showAfter;
    CURRENT_EXAM.onChange(renderRunner);
    renderRunner();
    switchTab('runner');
    CURRENT_EXAM.startTimer(renderRunnerTimer);
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

  /* ---------- runner render ---------- */
  function renderRunnerTimer() {
    if (!CURRENT_EXAM) return;
    var rem = CURRENT_EXAM.remainingSec();
    if (rem == null) { $('#r-timer').textContent = '--:--'; $('#r-timer').className = 'timer'; return; }
    $('#r-timer').textContent = MedSea.Format.fmtTime(rem);
    $('#r-timer').className = 'timer' + (rem < 60 ? ' danger' : rem < 300 ? ' warn' : '');
  }

  function renderRunner() {
    if (!CURRENT_EXAM || CURRENT_EXAM.submitted) {
      if (CURRENT_EXAM && CURRENT_EXAM.submitted) renderResult();
      return;
    }
    var q = CURRENT_EXAM.getCurrent();
    var html = '';
    html += '<div class="question-num">Q ' + (CURRENT_EXAM.idx + 1) + ' · ' +
      q.chapter_name + '</div>';
    html += '<div class="question-meta">From <a href="/' + q.chapter_slug + '/">' +
      'Ch ' + q.chapter_num + ' · ' + q.chapter_name + '</a> · Topic <code>' +
      q.topic_slug + '</code></div>';
    html += '<div class="question-text">' + escape(q.question) + '</div>';
    html += '<div class="options">';
    ['A', 'B', 'C', 'D'].forEach(function (letter) {
      if (!q.options[letter]) return;
      var picked = CURRENT_EXAM.answers[q.id];
      var cls = 'option';
      if (picked === letter) cls += ' selected';
      if (CURRENT_EXAM.submitted) {
        if (letter === q.answer) cls += ' correct';
        else if (picked === letter) cls += ' incorrect';
      }
      html += '<div class="' + cls + '" data-letter="' + letter + '">' +
        '<span class="letter">' + letter + '</span>' +
        '<span class="opt-text">' + escape(q.options[letter]) + '</span>' +
        '</div>';
    });
    html += '</div>';
    $('#r-card').innerHTML = html;
    $$('#r-card .option').forEach(function (opt) {
      opt.addEventListener('click', function () {
        if (CURRENT_EXAM.submitted) return;
        CURRENT_EXAM.setAnswer(q.id, opt.dataset.letter);
        if (CURRENT_EXAM.showAfter === 'each') {
          // auto-submit view of single Q (still allow navigation)
        }
      });
    });

    // top bar
    $('#r-qnum').textContent = (CURRENT_EXAM.idx + 1);
    $('#r-qtotal').textContent = CURRENT_EXAM.total();
    $('#r-ans').textContent = CURRENT_EXAM.answered();
    var pct = Math.round(((CURRENT_EXAM.idx + 1) / CURRENT_EXAM.total()) * 100);
    $('#r-bar').style.width = pct + '%';

    // palette
    var pal = '';
    CURRENT_EXAM.questions.forEach(function (qq, i) {
      var cls = 'qp-item';
      if (CURRENT_EXAM.answers[qq.id]) cls += ' answered';
      if (i === CURRENT_EXAM.idx) cls += ' current';
      if (CURRENT_EXAM.submitted) {
        var b = CURRENT_EXAM.score.breakdown[i];
        if (b.ok) cls += ' correct'; else cls += ' incorrect';
      }
      pal += '<span class="' + cls + '" data-i="' + i + '">' + (i + 1) + '</span>';
    });
    $('#r-palette').innerHTML = pal;
    $$('#r-palette .qp-item').forEach(function (p) {
      p.addEventListener('click', function () { CURRENT_EXAM.goto(parseInt(p.dataset.i, 10)); });
    });
    renderRunnerTimer();
  }

  $('#btn-prev').addEventListener('click', function () { if (CURRENT_EXAM) CURRENT_EXAM.prev(); });
  $('#btn-next').addEventListener('click', function () { if (CURRENT_EXAM) CURRENT_EXAM.next(); });
  $('#btn-quit').addEventListener('click', function () {
    if (!CURRENT_EXAM) return;
    if (!confirm('Quit this exam? Progress will be lost unless you submit first.')) return;
    CURRENT_EXAM = null;
    switchTab('setup');
  });
  $('#btn-submit').addEventListener('click', function () {
    if (!CURRENT_EXAM || CURRENT_EXAM.submitted) return;
    var unanswered = CURRENT_EXAM.total() - CURRENT_EXAM.answered();
    var msg = 'Submit exam?' + (unanswered > 0 ? '\n\n' + unanswered + ' unanswered question' + (unanswered === 1 ? '' : 's') + ' will be marked wrong.' : '');
    if (!confirm(msg)) return;
    CURRENT_EXAM.submit(false);
    renderResult();
    switchTab('result');
  });

  /* ---------- result render ---------- */
  function renderResult() {
    if (!CURRENT_EXAM || !CURRENT_EXAM.score) return;
    var s = CURRENT_EXAM.score;
    var grade = gradeFor(s.accuracy);

    $('#r-hero').innerHTML =
      '<div class="result-score">' + s.correct + ' / ' + s.total + '</div>' +
      '<div class="result-line">' + s.accuracy + '% accuracy</div>' +
      '<div class="result-grade" style="color:' + grade.color + '">' + grade.label + '</div>' +
      '<div class="result-line" style="margin-top:10px;">' + escape(CURRENT_EXAM.cfg.title) + '</div>';

    var stats = [
      { label: 'Correct', value: s.correct, cls: 'good' },
      { label: 'Incorrect', value: s.total - s.correct, cls: 'bad' },
      { label: 'Skipped', value: CURRENT_EXAM.total() - CURRENT_EXAM.answered(), cls: 'warn' },
      { label: 'Time', value: MedSea.Format.fmtTime(Math.floor(s.duration_ms / 1000)), cls: '' },
      { label: 'Per Question', value: MedSea.Format.fmtTime(Math.floor(s.duration_ms / 1000 / s.total)), cls: '' },
    ];
    var statHtml = '';
    stats.forEach(function (st) {
      statHtml += '<div class="stat-card ' + (st.cls || '') + '">' +
        '<div class="label">' + st.label + '</div>' +
        '<div class="value">' + st.value + '</div>' +
        '</div>';
    });
    $('#r-stats').innerHTML = statHtml;

    var rev = '';
    s.breakdown.forEach(function (b, i) {
      var q = b.q;
      var cls = b.ok ? 'ok' : 'bad';
      var ua = b.picked || '—';
      rev += '<div class="review-item ' + cls + '">' +
        '<div class="ri-head">' +
        '<span>Q' + (i + 1) + ' · ' + q.chapter_name + ' · ' + q.topic_slug + '</span>' +
        '<span class="badge">' + (b.ok ? '✓ CORRECT' : '✗ INCORRECT') + '</span>' +
        '</div>' +
        '<div class="ri-q">' + escape(q.question) + '</div>' +
        (ua !== '—'
          ? '<div class="ri-a ' + (b.ok ? 'right' : 'wrong') + '">Your answer: ' + ua + ' — ' + escape(q.options[ua] || '') + '</div>'
          : '<div class="ri-a missed">Not answered</div>') +
        (b.ok ? '' : '<div class="ri-a right">Correct answer: ' + q.answer + ' — ' + escape(q.options[q.answer] || '') + '</div>') +
        '</div>';
    });
    $('#r-review').innerHTML = rev;
  }

  function gradeFor(acc) {
    if (acc >= 90) return { label: 'Outstanding — FCPS / MRCP ready', color: 'var(--good)' };
    if (acc >= 75) return { label: 'Strong — review weak areas', color: 'var(--good)' };
    if (acc >= 60) return { label: 'Pass — needs more revision', color: 'var(--warn)' };
    if (acc >= 40) return { label: 'Below pass mark — back to basics', color: 'var(--warn)' };
    return { label: 'Needs serious revision', color: 'var(--bad)' };
  }

  $('#btn-result-new').addEventListener('click', function () { CURRENT_EXAM = null; switchTab('setup'); });
  $('#btn-result-history').addEventListener('click', function () { switchTab('history'); });

  /* ---------- history render ---------- */
  function renderHistory() {
    var list = MedSea.History.exams();
    if (list.length === 0) {
      $('#hist-list').innerHTML = '<div class="empty-state"><div class="icon">📋</div><p>No exam history yet. Run an exam and your attempts will appear here with chapter-wise analytics.</p></div>';
      return;
    }
    var html = '';
    list.forEach(function (r) {
      var acc = r.total ? Math.round((r.correct / r.total) * 100) : 0;
      var cls = acc >= 75 ? 'good' : acc >= 50 ? '' : 'bad';
      html += '<div class="hist-item">' +
        '<div class="hi-head">' +
        '<span class="hi-title">' + escape(r.title) + '</span>' +
        '<span class="hi-when">' + MedSea.Format.fmtDate(r.finished_at || r.started_at) + '</span>' +
        '</div>' +
        '<div class="hi-meta">' +
        '<span class="stat ' + cls + '"><strong>' + acc + '%</strong> (' + r.correct + '/' + r.total + ')</span>' +
        '<span class="stat">Time <strong>' + MedSea.Format.fmtTime(Math.floor((r.duration_ms || 0) / 1000)) + '</strong></span>' +
        '<span class="stat">Chapters <strong>' + (r.chapters || []).length + '</strong></span>' +
        '<span class="stat">Mode <strong>' + (r.mode || '').toUpperCase() + '</strong></span>' +
        (r.auto_submitted ? '<span class="stat" style="color:var(--warn);"><strong>Auto-submitted</strong></span>' : '') +
        '</div>' +
        '<div class="hi-actions">' +
        '<button class="chip-btn" data-replay="' + r.id + '">Replay Answers</button>' +
        '</div>' +
        '</div>';
    });
    $('#hist-list').innerHTML = html;
    $$('#hist-list [data-replay]').forEach(function (b) {
      b.addEventListener('click', function () { replayExam(b.dataset.replay); });
    });
  }

  function replayExam(rid) {
    var r = MedSea.History.exams().find(function (x) { return x.id === rid; });
    if (!r) return;
    var lookup = {};
    (DB_DATA.mcq.concat(DB_DATA.sba)).forEach(function (q) { lookup[q.id] = q; });
    var questions = (r.breakdown || []).map(function (b) { return lookup[b.id]; }).filter(Boolean);
    if (questions.length === 0) { toast('Could not reconstruct this exam.'); return; }
    CURRENT_EXAM = MedSea.Engine.startExam({
      questions: questions,
      duration_sec: null,
      title: 'Replay · ' + r.title,
      chapters: r.chapters || [],
      mode: r.mode,
      question_types: r.question_types || ['mcq', 'sba'],
    });
    CURRENT_EXAM.showAfter = 'end';
    CURRENT_EXAM.onChange(renderRunner);
    (r.breakdown || []).forEach(function (b) {
      if (b.picked) CURRENT_EXAM.answers[b.id] = b.picked;
    });
    renderRunner();
    switchTab('runner');
  }

  $('#btn-clear-hist').addEventListener('click', function () {
    if (!confirm('Clear all exam history? This cannot be undone.')) return;
    MedSea.History.clear();
    renderHistory();
    toast('History cleared.');
  });

  /* ---------- analytics ---------- */
  function renderAnalytics() {
    var stats = MedSea.History.stats();
    var html = '';
    html += '<div class="analytics-card"><h3>📊 Exam Overview</h3>';
    if (stats.examCount === 0) {
      html += '<div style="font-size:12px;color:var(--text-dim);">No exams taken yet.</div>';
    } else {
      html += '<div class="bm-row"><span class="bm-label">Attempts</span><span class="bm-val"><strong>' + stats.examCount + '</strong></span></div>';
      html += '<div class="bm-row"><span class="bm-label">Questions</span><span class="bm-val"><strong>' + stats.exams.total + '</strong></span></div>';
      html += '<div class="bm-row"><span class="bm-label">Accuracy</span><span class="bm-bar"><span class="bm-fill ' + (stats.exams.accuracy >= 75 ? 'good' : stats.exams.accuracy >= 50 ? 'warn' : 'bad') + '" style="width:' + stats.exams.accuracy + '%;"></span></span><span class="bm-val"><strong>' + stats.exams.accuracy + '%</strong></span></div>';
      html += '<div class="bm-row"><span class="bm-label">Time</span><span class="bm-val"><strong>' + MedSea.Format.fmtTime(Math.floor(stats.exams.time_ms / 1000)) + '</strong></span></div>';
    }
    html += '</div>';

    html += '<div class="analytics-card"><h3>🃏 Flashcard Overview</h3>';
    if (stats.flashCount === 0) {
      html += '<div style="font-size:12px;color:var(--text-dim);">No flashcard sessions yet.</div>';
    } else {
      html += '<div class="bm-row"><span class="bm-label">Sessions</span><span class="bm-val"><strong>' + stats.flashCount + '</strong></span></div>';
      html += '<div class="bm-row"><span class="bm-label">Cards</span><span class="bm-val"><strong>' + stats.cards.total + '</strong></span></div>';
      html += '<div class="bm-row"><span class="bm-label">Retention</span><span class="bm-bar"><span class="bm-fill ' + (stats.cards.retention >= 75 ? 'good' : stats.cards.retention >= 50 ? 'warn' : 'bad') + '" style="width:' + stats.cards.retention + '%;"></span></span><span class="bm-val"><strong>' + stats.cards.retention + '%</strong></span></div>';
    }
    html += '</div>';

    html += '<div class="analytics-card"><h3>⏱ Performance</h3>';
    if (stats.examCount > 0) {
      var avgPerQ = Math.floor(stats.exams.time_ms / 1000 / Math.max(1, stats.exams.total));
      html += '<div class="bm-row"><span class="bm-label">Avg / Q</span><span class="bm-val"><strong>' + MedSea.Format.fmtTime(avgPerQ) + '</strong></span></div>';
    }
    html += '<div class="bm-row"><span class="bm-label">Streak</span><span class="bm-val"><strong>' + computeStreak() + '</strong></span></div>';
    html += '</div>';

    $('#analytics-cards').innerHTML = html;

    // chapter-wise
    var byCh = MedSea.History.byChapter('exam');
    var keys = Object.keys(byCh).map(function (k) { return parseInt(k, 10); }).sort(function (a, b) { return a - b; });
    if (keys.length === 0) {
      $('#ch-bars').innerHTML = '<div style="font-size:12px;color:var(--text-dim);padding:20px;text-align:center;">Take exams across multiple chapters to see your weak areas here.</div>';
    } else {
      var bhtml = '';
      keys.forEach(function (k) {
        var data = byCh[k];
        var name = (DB_DATA.chapters.find(function (c) { return c.num === k; }) || { name: 'Ch ' + k }).name;
        var cls = data.accuracy >= 75 ? 'good' : data.accuracy >= 50 ? 'warn' : 'bad';
        bhtml += '<div class="bm-row">' +
          '<span class="bm-label">Ch ' + k + '</span>' +
          '<span class="bm-bar"><span class="bm-fill ' + cls + '" style="width:' + data.accuracy + '%;"></span></span>' +
          '<span class="bm-val"><strong>' + data.accuracy + '%</strong> · ' + data.correct + '/' + data.total + '</span>' +
          '</div>';
      });
      $('#ch-bars').innerHTML = bhtml;
    }
  }

  function computeStreak() {
    var list = MedSea.History.exams();
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

  /* ---------- helpers ---------- */
  function escape(s) {
    return String(s == null ? '' : s)
      .replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;')
      .replace(/"/g, '&quot;').replace(/'/g, '&#39;');
  }
})();