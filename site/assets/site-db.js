/* MedSea shared site database loader.
   Replaces multiple ad-hoc fetches of /assets/questions.json with a single
   lazy, chunked loader. Exposes window.MedSeaDB.

   Files on disk (split by content type for fast first paint):
     /assets/questions-index.json       ~5 KB   — chapters meta + totals (always loaded)
     /assets/questions-mcq.json         ~10 MB  — MCQs only
     /assets/questions-sba.json         ~0.8 MB — SBAs only
     /assets/questions-flashcard.json   ~5.5 MB — Flashcards only

   The 17 MB monolithic JSON is gone. The header stats/menu load only the
   5 KB index on every page; the 10 MB MCQ file is fetched only when an
   exam starts.
*/
(function () {
  'use strict';

  var ROOT = '/assets/';
  var _indexCache = null;       // Promise<index>
  var _chunkCache = {};         // key → Promise<array>

  // Browser HTTP cache (default behaviour, NOT no-cache) is fine because
  // these files are content-hashed by version field and immutable in practice.
  function fetchJSON(path) {
    return fetch(path).then(function (r) {
      if (!r.ok) throw new Error('HTTP ' + r.status + ' for ' + path);
      return r.json();
    });
  }

  /**
   * Load the small index (chapters meta + totals). Cached after first call.
   * Returns Promise<{version, generated_at, totals, chapters}>
   */
  function loadIndex() {
    if (_indexCache) return _indexCache;
    _indexCache = fetchJSON(ROOT + 'questions-index.json').catch(function (err) {
      _indexCache = null;
      throw err;
    });
    return _indexCache;
  }

  /**
   * Load one question chunk lazily. Cached. Returns Promise<Array>.
   * key = 'mcq' | 'sba' | 'flashcard'
   */
  function loadChunk(key) {
    if (_chunkCache[key]) return _chunkCache[key];
    _chunkCache[key] = fetchJSON(ROOT + 'questions-' + key + '.json').catch(function (err) {
      _chunkCache[key] = null;
      throw err;
    });
    return _chunkCache[key];
  }

  /**
   * Load multiple chunks at once (e.g. MCQ + SBA for a mixed exam).
   * Returns Promise<{mcq: Array, sba: Array}>
   */
  function loadChunks(keys) {
    var p = {};
    keys.forEach(function (k) { p[k] = loadChunk(k); });
    var out = {};
    var promises = keys.map(function (k) {
      return p[k].then(function (data) { out[k] = data; });
    });
    return Promise.all(promises).then(function () { return out; });
  }

  /**
   * Eagerly prefetch a chunk without blocking. Useful right after index
   * load so exam-start is instant.
   */
  function prefetch(key) {
    if (_chunkCache[key]) return;
    // Fire-and-forget. Errors swallowed.
    loadChunk(key).catch(function () {});
  }

  /**
   * Compute chapter display label like "Ch 16 · Cardiology" from a question
   * object (avoids storing chapter_name on every question).
   */
  function chapterLabel(q, indexChapters) {
    var c = indexChapters && indexChapters[q.chapter_num];
    if (!c) return 'Ch ' + q.chapter_num;
    return 'Ch ' + c.num + ' · ' + c.name;
  }

  // Public API
  window.MedSeaDB = {
    loadIndex: loadIndex,
    loadChunk: loadChunk,
    loadChunks: loadChunks,
    prefetch: prefetch,
    chapterLabel: chapterLabel,
    // Convenience: get chapter meta object by num from cached index
    getChapter: function (num, chapters) {
      if (!chapters) return null;
      for (var i = 0; i < chapters.length; i++) {
        if (chapters[i].num === num) return chapters[i];
      }
      return null;
    }
  };
})();
