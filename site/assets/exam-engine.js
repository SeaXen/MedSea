/* MedSea shared engine for exam + flashcards + history.
   Loaded by /exam/index.html and /flashcards/index.html.
   Exposes window.MedSea = {DB, Engine, History, Format}.
*/
(function () {
  'use strict';

  /* ---------- formatting helpers ---------- */
  function fmtTime(secs) {
    secs = Math.max(0, Math.floor(secs));
    var m = Math.floor(secs / 60);
    var s = secs % 60;
    return (m < 10 ? '0' : '') + m + ':' + (s < 10 ? '0' : '') + s;
  }
  function fmtDate(iso) {
    try {
      var d = new Date(iso);
      return d.toLocaleString();
    } catch (_) { return iso; }
  }
  function pct(n, d) {
    if (!d) return 0;
    return Math.round((n / d) * 100);
  }

  /* ---------- random helpers (deterministic-ish if needed) ---------- */
  function shuffle(arr) {
    var a = arr.slice();
    for (var i = a.length - 1; i > 0; i--) {
      var j = Math.floor(Math.random() * (i + 1));
      var t = a[i]; a[i] = a[j]; a[j] = t;
    }
    return a;
  }
  function pickWeighted(arr, n) {
    return shuffle(arr).slice(0, Math.min(n, arr.length));
  }

  /* ---------- question pool filtering ---------- */
  function filterPool(pool, filters) {
    var f = filters || {};
    return pool.filter(function (q) {
      if (f.chapters && f.chapters.length && f.chapters.indexOf(q.chapter_num) === -1) return false;
      if (f.excludeChapter && f.excludeChapter === q.chapter_num) return false;
      return true;
    });
  }

  /* ---------- DB loader (cache) ---------- */
  var DB = {
    _data: null,
    _loadPromise: null,
    load: function () {
      if (DB._data) return Promise.resolve(DB._data);
      if (DB._loadPromise) return DB._loadPromise;
      DB._loadPromise = fetch('/assets/questions.json', { cache: 'no-cache' })
        .then(function (r) {
          if (!r.ok) throw new Error('Failed to load questions DB: HTTP ' + r.status);
          return r.json();
        })
        .then(function (j) {
          DB._data = j;
          return j;
        })
        .catch(function (err) {
          DB._loadPromise = null;
          throw err;
        });
      return DB._loadPromise;
    },
    get: function () { return DB._data; }
  };

  /* ---------- history store (localStorage) ---------- */
  var History = {
    KEY: 'medsea_exam_history_v1',
    _list: null,
    _load: function () {
      if (History._list) return History._list;
      try {
        History._list = JSON.parse(localStorage.getItem(History.KEY) || '[]');
      } catch (_) { History._list = []; }
      if (!Array.isArray(History._list)) History._list = [];
      return History._list;
    },
    _save: function () {
      try {
        localStorage.setItem(History.KEY, JSON.stringify(History._list));
      } catch (_) { /* quota */ }
    },
    all: function () {
      var list = History._load().slice();
      list.sort(function (a, b) { return (b.started_at || '').localeCompare(a.started_at || ''); });
      return list;
    },
    exams: function () { return History.all().filter(function (r) { return r.type === 'exam'; }); },
    flashes: function () { return History.all().filter(function (r) { return r.type === 'flashcard'; }); },
    add: function (rec) {
      var list = History._load();
      if (!rec.id) rec.id = 'r_' + Date.now() + '_' + Math.random().toString(36).slice(2, 8);
      list.push(rec);
      History._list = list;
      History._save();
      return rec;
    },
    clear: function () {
      History._list = [];
      try { localStorage.removeItem(History.KEY); } catch (_) {}
    },
    byChapter: function (type) {
      var map = {};
      var list = type ? History.all().filter(function (r) { return r.type === type; }) : History.all();
      list.forEach(function (r) {
        (r.chapters || []).forEach(function (c) {
          if (!map[c]) map[c] = { attempts: 0, correct: 0, total: 0, time_ms: 0 };
          map[c].attempts += 1;
          map[c].total += r.total || 0;
          map[c].correct += r.correct || 0;
          map[c].time_ms += r.duration_ms || 0;
        });
      });
      Object.keys(map).forEach(function (k) {
        map[k].accuracy = map[k].total ? Math.round((map[k].correct / map[k].total) * 100) : 0;
      });
      return map;
    },
    stats: function () {
      var list = History.all();
      var exam = list.filter(function (r) { return r.type === 'exam'; });
      var flash = list.filter(function (r) { return r.type === 'flashcard'; });
      var total = { attempts: 0, correct: 0, total: 0, time_ms: 0 };
      exam.forEach(function (r) {
        total.attempts += 1;
        total.total += r.total || 0;
        total.correct += r.correct || 0;
        total.time_ms += r.duration_ms || 0;
      });
      var cards = { attempts: 0, known: 0, total: 0, time_ms: 0 };
      flash.forEach(function (r) {
        cards.attempts += 1;
        cards.total += r.total || 0;
        cards.known += r.known || 0;
        cards.time_ms += r.duration_ms || 0;
      });
      total.accuracy = total.total ? Math.round((total.correct / total.total) * 100) : 0;
      cards.retention = cards.total ? Math.round((cards.known / cards.total) * 100) : 0;
      return { exams: total, cards: cards, examCount: exam.length, flashCount: flash.length };
    }
  };

  /* ---------- Exam engine ---------- */
  function startExam(cfg) {
    // cfg: { questions: [...], duration_sec: number|null, title: string, chapters: [nums] }
    var state = {
      cfg: cfg,
      idx: 0,
      answers: {}, // qid -> 'A'
      started_at: new Date().toISOString(),
      duration_ms: 0,
      submitted: false,
      score: null,
      // runtime
      _tStart: Date.now(),
      _tEnd: null,
      _tickHandle: null,
      _tickCb: null,
      _onChangeCb: null,
    };
    state.getCurrent = function () { return state.questions[state.idx]; };
    state.total = function () { return state.questions.length; };
    state.answered = function () {
      var c = 0; Object.keys(state.answers).forEach(function (k) { if (state.answers[k]) c++; }); return c;
    };
    state.remainingSec = function () {
      if (state.cfg.duration_sec == null) return null;
      var elapsed = Math.floor((Date.now() - state._tStart) / 1000);
      return Math.max(0, state.cfg.duration_sec - elapsed);
    };
    state.tick = function () {
      if (state._tickCb) state._tickCb(state);
    };
    state.setAnswer = function (qid, ans) {
      state.answers[qid] = ans;
      if (state._onChangeCb) state._onChangeCb(state);
    };
    state.goto = function (i) {
      state.idx = Math.max(0, Math.min(state.questions.length - 1, i));
      if (state._onChangeCb) state._onChangeCb(state);
    };
    state.next = function () { state.goto(state.idx + 1); };
    state.prev = function () { state.goto(state.idx - 1); };
    state.submit = function (auto) {
      if (state.submitted) return state.score;
      state._tEnd = Date.now();
      state.duration_ms = state._tEnd - state._tStart;
      if (state._tickHandle) { clearInterval(state._tickHandle); state._tickHandle = null; }
      var correct = 0;
      var breakdown = state.questions.map(function (q) {
        var ua = state.answers[q.id] || null;
        var ok = ua && ua === q.answer;
        if (ok) correct++;
        return { id: q.id, picked: ua, correct: q.answer, ok: ok, q: q };
      });
      state.score = {
        correct: correct, total: state.questions.length, auto: !!auto,
        breakdown: breakdown, accuracy: state.questions.length ? Math.round((correct / state.questions.length) * 100) : 0,
        duration_ms: state.duration_ms,
      };
      state.submitted = true;
      History.add({
        type: 'exam',
        title: state.cfg.title || 'Exam',
        mode: state.cfg.mode || 'mixed',
        chapters: state.cfg.chapters || [],
        question_types: state.cfg.question_types || ['mcq', 'sba'],
        total: state.questions.length,
        correct: correct,
        duration_sec: state.cfg.duration_sec,
        duration_ms: state.duration_ms,
        started_at: state.started_at,
        finished_at: new Date(state._tEnd).toISOString(),
        auto_submitted: !!auto,
        breakdown: breakdown.map(function (b) { return { id: b.id, picked: b.picked, correct: b.correct, ok: b.ok }; }),
      });
      if (state._onChangeCb) state._onChangeCb(state);
      return state.score;
    };
    state.startTimer = function (cb) {
      state._tickCb = cb;
      if (state._tickHandle) clearInterval(state._tickHandle);
      if (state.cfg.duration_sec != null) {
        state._tickHandle = setInterval(function () {
          if (state.remainingSec() <= 0) {
            state.submit(true);
          }
          state.tick();
        }, 1000);
      }
    };
    state.onChange = function (cb) { state._onChangeCb = cb; };
    state.questions = cfg.questions;
    return state;
  }

  /* ---------- Flashcard engine ---------- */
  function startFlashcards(cfg) {
    // cfg: { cards: [...], duration_sec: number|null, title: string, chapters: [nums] }
    var state = {
      cfg: cfg,
      idx: 0,
      ratings: {}, // qid -> 'known' | 'unknown' | 'skip'
      started_at: new Date().toISOString(),
      duration_ms: 0,
      finished: false,
      _tStart: Date.now(),
      _tEnd: null,
      _tickHandle: null,
      _tickCb: null,
      _onChangeCb: null,
      flipped: false,
    };
    state.total = function () { return state.cards.length; };
    state.known = function () {
      var c = 0; Object.keys(state.ratings).forEach(function (k) { if (state.ratings[k] === 'known') c++; }); return c;
    };
    state.unknown = function () {
      var c = 0; Object.keys(state.ratings).forEach(function (k) { if (state.ratings[k] === 'unknown') c++; }); return c;
    };
    state.rated = function () {
      var c = 0; Object.keys(state.ratings).forEach(function (k) { if (state.ratings[k] !== 'skip') c++; }); return c;
    };
    state.rate = function (qid, rating) {
      state.ratings[qid] = rating;
      if (state._onChangeCb) state._onChangeCb(state);
    };
    state.flip = function () { state.flipped = !state.flipped; if (state._onChangeCb) state._onChangeCb(state); };
    state.goto = function (i) {
      state.idx = Math.max(0, Math.min(state.cards.length - 1, i));
      state.flipped = false;
      if (state._onChangeCb) state._onChangeCb(state);
    };
    state.next = function () { state.goto(state.idx + 1); };
    state.prev = function () { state.goto(state.idx - 1); };
    state.finish = function () {
      state._tEnd = Date.now();
      state.duration_ms = state._tEnd - state._tStart;
      state.finished = true;
      if (state._tickHandle) { clearInterval(state._tickHandle); state._tickHandle = null; }
      var breakdown = state.cards.map(function (c) { return { id: c.id, rating: state.ratings[c.id] || 'skip' }; });
      History.add({
        type: 'flashcard',
        title: state.cfg.title || 'Flashcards',
        chapters: state.cfg.chapters || [],
        total: state.cards.length,
        known: state.known(),
        unknown: state.unknown(),
        duration_sec: state.cfg.duration_sec,
        duration_ms: state.duration_ms,
        started_at: state.started_at,
        finished_at: new Date(state._tEnd).toISOString(),
        breakdown: breakdown,
      });
      if (state._onChangeCb) state._onChangeCb(state);
    };
    state.startTimer = function (cb) {
      state._tickCb = cb;
      if (state._tickHandle) clearInterval(state._tickHandle);
      if (state.cfg.duration_sec != null) {
        state._tickHandle = setInterval(function () {
          if (state.remainingSec() <= 0) state.finish();
          state.tick();
        }, 1000);
      }
    };
    state.onChange = function (cb) { state._onChangeCb = cb; };
    state.remainingSec = function () {
      if (state.cfg.duration_sec == null) return null;
      var elapsed = Math.floor((Date.now() - state._tStart) / 1000);
      return Math.max(0, state.cfg.duration_sec - elapsed);
    };
    state.tick = function () { if (state._tickCb) state._tickCb(state); };
    state.cards = cfg.cards;
    return state;
  }

  /* ---------- Public API ---------- */
  window.MedSea = {
    DB: DB, Engine: { startExam: startExam, startFlashcards: startFlashcards },
    History: History, Format: { fmtTime: fmtTime, fmtDate: fmtDate, pct: pct },
    Pool: { filter: filterPool, shuffle: shuffle, pick: pickWeighted }
  };
})();