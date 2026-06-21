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

  /* ---------- DB loader (lazy + chunked) ----------
     Backed by /assets/site-db.js which splits the old monolithic 17 MB
     questions.json into four files:
       questions-index.json      (5 KB)    - chapter meta + totals
       questions-mcq.json        (~10 MB)  - MCQs
       questions-sba.json        (~800 KB) - SBAs
       questions-flashcard.json  (~5.5 MB) - Flashcards
     This loader fetches ONLY the chunks needed for the current exam mode.
  */
  var DB = {
    _index: null,      // Promise<index> — cached
    _chapters: null,   // array (resolved from index)
    _mcq: null,        // Promise<Array<q>>
    _sba: null,        // Promise<Array<q>>
    _flash: null,      // Promise<Array<card>>
    _loadIndex: function () {
      if (DB._index) return DB._index;
      var src = (window.MedSeaDB && window.MedSeaDB.loadIndex)
        ? window.MedSeaDB.loadIndex()
        : fetch('/assets/questions-index.json').then(function (r) { return r.json(); });
      DB._index = src.then(function (idx) {
        DB._chapters = idx.chapters || [];
        return idx;
      });
      return DB._index;
    },
    /** Fetch the question chunks needed for a given mode.
        mode: 'mcq' | 'sba' | 'mixed' | 'flashcard' */
    _loadChunks: function (mode) {
      var need = [];
      if (mode === 'mcq' || mode === 'mixed') need.push('mcq');
      if (mode === 'sba' || mode === 'mixed') need.push('sba');
      if (mode === 'flashcard') need.push('flashcard');
      var src = (window.MedSeaDB && window.MedSeaDB.loadChunks)
        ? window.MedSeaDB.loadChunks(need)
        : Promise.all(need.map(function (k) {
            return fetch('/assets/questions-' + k + '.json').then(function (r) { return r.json(); }).then(function (d) {
              var o = {}; o[k] = d; return o;
            });
          })).then(function (arr) {
            return arr.reduce(function (acc, o) { Object.keys(o).forEach(function (k) { acc[k] = o[k]; }); return acc; }, {});
          });
      var p = src.then(function (chunks) {
        if (chunks.mcq !== undefined) DB._mcq = Promise.resolve(chunks.mcq);
        if (chunks.sba !== undefined) DB._sba = Promise.resolve(chunks.sba);
        if (chunks.flashcard !== undefined) DB._flash = Promise.resolve(chunks.flashcard);
        return chunks;
      });
      // Reuse cached promises if already loaded
      if (mode === 'mcq' && DB._mcq) return DB._mcq.then(function (mcq) { return { mcq: mcq }; });
      if (mode === 'sba' && DB._sba) return DB._sba.then(function (sba) { return { sba: sba }; });
      if (mode === 'flashcard' && DB._flash) return DB._flash.then(function (flashcard) { return { flashcard: flashcard }; });
      return p;
    },
    /** Public: warm the cache for a mode without returning data. */
    prefetch: function (mode) {
      DB._loadIndex(); // index needed everywhere
      if (window.MedSeaDB && window.MedSeaDB.prefetch) {
        if (mode === 'mcq' || mode === 'mixed') window.MedSeaDB.prefetch('mcq');
        if (mode === 'sba' || mode === 'mixed') window.MedSeaDB.prefetch('sba');
        if (mode === 'flashcard') window.MedSeaDB.prefetch('flashcard');
      } else {
        DB._loadChunks(mode).catch(function () {});
      }
    },
    /** Public: load everything for a mode. Returns Promise<{chapters, mcq?, sba?, flashcard?}> */
    load: function (mode) {
      return Promise.all([DB._loadIndex(), DB._loadChunks(mode || 'mixed')]).then(function (parts) {
        var idx = parts[0], chunks = parts[1];
        return {
          chapters: idx.chapters,
          totals: idx.totals,
          mcq: chunks.mcq || DB._cached(DB._mcq) || [],
          sba: chunks.sba || DB._cached(DB._sba) || [],
          flashcard: chunks.flashcard || DB._cached(DB._flash) || [],
        };
      });
    },
    _cached: function (p) {
      if (!p) return null;
      var v = null, done = false;
      p.then(function (x) { v = x; done = true; });
      return done ? v : null;
    },
    /** Public: sync getter (only valid after load() resolved) */
    get: function () {
      return {
        chapters: DB._chapters || [],
        get mcq() { return DB._cached(DB._mcq) || []; },
        get sba() { return DB._cached(DB._sba) || []; },
        get flashcard() { return DB._cached(DB._flash) || []; }
      };
    },
    /** Public: get just the flashcards array (for flashcards app) */
    flashcards: function () {
      if (DB._flash) return DB._flash;
      return DB._loadChunks('flashcard').then(function (c) { return c.flashcard || []; });
    }
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