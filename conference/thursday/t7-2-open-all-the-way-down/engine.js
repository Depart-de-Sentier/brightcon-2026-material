/* Klimabündnis deck engine — data-driven, bilingual, GSAP.
   Slide content lives in window.DECK (slides.js). This file renders + drives. */
(function () {
  'use strict';
  // Physical canvas is 1920×1080 (full-HD) so it renders crisp on large screens / projectors.
  // Slides are still authored in 1280×720 logical coordinates and upscaled 1.5× to fill it,
  // so no per-slide CSS needed changing.
  var STAGE_W = 1920, STAGE_H = 1080;
  var SLIDE_W = 1280, SLIDE_H = 720, SLIDE_SCALE = STAGE_W / SLIDE_W; // 1.5
  var REDUCED = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  // ---- language ----
  var LANG = (location.hash.replace('#', '') === 'de') ? 'de' : 'en';   // ESFC deck: English by default, #de switches
  function L(obj) { if (obj == null) return ''; if (typeof obj === 'string') return obj; return obj[LANG] != null ? obj[LANG] : (obj.de != null ? obj.de : ''); }

  // locale-aware number formatting: DE uses ' as thousands sep + , decimal; EN uses , and .
  window.__fmtNum = function (v, dec) {
    dec = dec || 0;
    var neg = v < 0; v = Math.abs(v);
    var fixed = v.toFixed(dec);
    var parts = fixed.split('.');
    var intp = parts[0], frac = parts[1];
    var sep = LANG === 'de' ? "’" : ',';      // DE apostrophe vs EN comma
    var dp = LANG === 'de' ? ',' : '.';
    intp = intp.replace(/\B(?=(\d{3})+(?!\d))/g, sep);
    return (neg ? '-' : '') + intp + (frac ? dp + frac : '');
  };

  var stage = document.getElementById('stage');
  var viewport = document.getElementById('viewport');
  var slidesWrap = document.getElementById('slides');
  var barFill = document.getElementById('progress-bar-fill');
  var countText = document.getElementById('count-text');
  var dotsWrap = document.getElementById('dots');

  var SLIDES = window.DECK.slides;
  var TOTAL = SLIDES.length;
  var current = 1;

  // ---- build slide DOM from data ----
  // Each slide object: { id, render(el, slide) }  OR  generic { kicker,title,body,bullets,footnote,layout }
  function esc(s) { return String(s).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;'); }

  function renderGeneric(slide) {
    var bg = slide.bg || (slide.dark ? '#04140b' : '#ffffff');
    var html = '<div class="pad' + (slide.dark ? ' dark' : '') + '" style="background:' + bg + ';">';
    if (L(slide.kicker)) html += '<div class="kicker anim-kicker">' + esc(L(slide.kicker)) + '</div>';
    if (L(slide.title)) html += '<h2 class="title anim-title"' + (slide.bigTitle ? ' style="font-size:64px;letter-spacing:-2px"' : '') + '>' + L(slide.title) + '</h2>';
    if (L(slide.body)) html += '<p class="body anim-body">' + L(slide.body) + '</p>';
    // bullets is a language-separated object {de:[...], en:[...]} so DE/EN lists
    // stay independent (no index-zipping, which previously leaked one language
    // into the other when the two lists differed in length).
    var bullets = slide.bullets || [];
    if (bullets && !Array.isArray(bullets)) bullets = bullets[LANG] || bullets.de || [];
    if (bullets.length) {
      html += '<div class="bullets">';
      bullets.forEach(function (b) {
        if (b && b.stat != null) {
          html += '<div class="statcard anim-item"><div class="statnum">' + L(b.stat) + '</div><div class="statlbl">' + L(b.label) + '</div></div>';
        } else {
          html += '<div class="bullet anim-item"><span class="tick">✓</span><span>' + L(b) + '</span></div>';
        }
      });
      html += '</div>';
    }
    if (L(slide.footnote)) html += '<div class="footnote anim-foot">' + L(slide.footnote) + '</div>';
    html += '</div>';
    return html;
  }

  SLIDES.forEach(function (slide, i) {
    var sec = document.createElement('section');
    sec.className = 'slide';
    sec.setAttribute('data-slide', i + 1);
    if (slide.custom && window.CUSTOM && window.CUSTOM[slide.custom]) {
      sec.innerHTML = '<div class="slide-content">' + window.CUSTOM[slide.custom](slide, L, esc) + '</div>';
    } else {
      sec.innerHTML = '<div class="slide-content">' + renderGeneric(slide) + '</div>';
    }
    slidesWrap.appendChild(sec);
  });
  var slideEls = Array.prototype.slice.call(document.querySelectorAll('.slide'));

  // dots
  for (var i = 1; i <= TOTAL; i++) { var d = document.createElement('span'); d.className = 'dot'; dotsWrap.appendChild(d); }
  var dotEls = Array.prototype.slice.call(dotsWrap.querySelectorAll('.dot'));
  dotEls.forEach(function (d, idx) { d.title = 'Slide ' + (idx + 1); d.addEventListener('click', function (e) { e.stopPropagation(); show(idx + 1); }); });

  function fitStage() {
    var vw = viewport.clientWidth, vh = viewport.clientHeight;
    var scale = Math.min(vw / STAGE_W, vh / STAGE_H);   // letterbox: largest scale that fits, keeps 16:9
    // The viewport flex-centers the stage; we only scale from its center. This keeps the
    // slide perfectly centered and filling the window (one axis touches the edges) at any size.
    stage.style.transform = 'scale(' + scale + ')';
  }
  window.addEventListener('resize', fitStage);

  // ---- QR (closing slide) ----
  var _qrDone = false;
  function renderQR() {
    if (_qrDone) return;
    var el = document.getElementById('qr-target');
    if (!el || typeof qrcode !== 'function') return;
    try {
      var qr = qrcode(0, 'M'); qr.addData(window.DECK.qrUrl || 'https://flit.eaternity.org'); qr.make();
      var n = qr.getModuleCount(), ns = 'http://www.w3.org/2000/svg';
      var svg = document.createElementNS(ns, 'svg');
      svg.setAttribute('viewBox', '0 0 ' + n + ' ' + n); svg.setAttribute('width', '100%'); svg.setAttribute('height', '100%');
      svg.setAttribute('shape-rendering', 'crispEdges');
      var dd = '';
      for (var r = 0; r < n; r++) for (var c = 0; c < n; c++) if (qr.isDark(r, c)) dd += 'M' + c + ' ' + r + 'h1v1h-1z';
      var path = document.createElementNS(ns, 'path'); path.setAttribute('d', dd); path.setAttribute('fill', '#083118');
      el.innerHTML = ''; svg.appendChild(path); el.appendChild(svg); _qrDone = true;
    } catch (e) { }
  }

  // ---- generic per-slide animation (works for all data-driven slides) ----
  // Robustness: browsers throttle requestAnimationFrame in background tabs, which
  // can freeze a GSAP timeline mid-`from()` and leave content stuck at opacity 0.
  // We keep a handle on the current timeline and force-complete it whenever the
  // tab regains focus, and guarantee a final visible state via clearProps.
  var activeTl = null;
  function forceComplete() { if (activeTl && activeTl.progress() < 1) activeTl.progress(1); }
  document.addEventListener('visibilitychange', function () { if (!document.hidden) forceComplete(); });
  window.addEventListener('focus', forceComplete);

  function settleStatic(sec) {
    // no-animation fallback: show every value at its final state
    sec.querySelectorAll('[data-count]').forEach(function (el) { el.textContent = window.__fmtNum(parseFloat(el.getAttribute('data-count')), parseInt(el.getAttribute('data-dec') || '0', 10)); });
    sec.querySelectorAll('.conffill').forEach(function (el) { el.style.width = (el.getAttribute('data-fill') || '0') + '%'; });
    sec.querySelectorAll('.tri-cloud').forEach(function (g) { g.style.opacity = '1'; });
  }

  function animate(sec, slide) {
    var content = sec.querySelector('.slide-content');
    if (REDUCED || !window.gsap) { if (content) content.style.opacity = '1'; settleStatic(sec); return; }
    if (activeTl) activeTl.kill();
    // Reveal gate: hide the slide synchronously NOW (so nothing — incl. SVG labels, headings,
    // chart values without an anim-* class — is painted before the animation), then fade it in
    // as the timeline's first step. Per-element anim-* tweens play on top for the staggered feel.
    if (content) content.style.opacity = '0';
    var tl = gsap.timeline({ onComplete: function () { activeTl = null; } });
    activeTl = tl; window.__lastTL = tl;   // debug hook for automated animation-order verification
    if (content) tl.to(content, { opacity: 1, duration: 0.3, ease: 'power1.out' }, 0);
    var q = function (s) { return sec.querySelectorAll(s); };
    // F: add a `from` tween only if the selector matches, with clearProps so the
    // element is guaranteed to settle at its natural CSS state (never stuck hidden).
    function F(sel, vars, pos) { var els = q(sel); if (!els.length) return; vars.clearProps = 'opacity,transform'; tl.from(els, vars, pos); }
    F('.anim-kicker', { opacity: 0, y: -12, duration: 0.4 });
    F('.anim-title', { opacity: 0, y: 18, duration: 0.5, ease: 'power3.out' }, '-=0.15');
    F('.anim-body', { opacity: 0, y: 12, duration: 0.45 }, '-=0.25');
    F('.anim-item', { opacity: 0, y: 24, scale: 0.97, duration: 0.45, stagger: 0.1, ease: 'power2.out' }, '-=0.15');
    // stagger capped to a total window so many pills (e.g. 60+ on the catalogue) all animate fast,
    // instead of trickling in over several seconds.
    (function () { var els = q('.anim-flow'); if (els.length) tl.from(els, { opacity: 0, x: -10, scale: 0.9, duration: 0.32, stagger: { each: Math.min(0.06, 0.9 / els.length), from: 'start' }, ease: 'back.out(1.5)', clearProps: 'opacity,transform' }, '-=0.1'); })();
    F('.anim-arrow', { opacity: 0, duration: 0.2, stagger: 0.09 }, '-=0.8');
    // horizontal grows (range bar, weight bars) vs vertical grows (stacked/wet-dry) handled below
    F('.anim-grow', { scaleX: 0, transformOrigin: 'left', duration: 0.55, ease: 'power2.out' }, '-=0.2');
    F('.anim-pop', { opacity: 0, scale: 0.7, duration: 0.45, stagger: 0.08, ease: 'back.out(1.6)' }, '-=0.2');
    F('.anim-foot', { opacity: 0, y: 10, duration: 0.4 }, '-=0.1');

    // ---- bespoke behaviours ----
    // SVG path draw (distribution curve) via stroke-dashoffset
    q('.draw-path').forEach(function (p) {
      try { var len = p.getTotalLength(); p.style.strokeDasharray = len; tl.fromTo(p, { strokeDashoffset: len }, { strokeDashoffset: 0, duration: 0.9, ease: 'power1.inOut', clearProps: 'strokeDasharray,strokeDashoffset' }, '-=0.3'); } catch (e) { }
    });
    // donut: all segments draw together as ONE synchronized sweep (same start + duration),
    // so it reads as a single motion rather than several staggered arcs.
    var arcs = q('.anim-grow-arc');
    if (arcs.length) {
      var pos = '-=0.1';
      arcs.forEach(function (p) {
        try { var len = p.getTotalLength(); p.style.strokeDasharray = len; tl.fromTo(p, { strokeDashoffset: len }, { strokeDashoffset: 0, duration: 0.7, ease: 'power2.out', clearProps: 'strokeDasharray,strokeDashoffset' }, pos); } catch (e) { }
        pos = '<'; // every subsequent arc starts at the SAME time as the first
      });
    }
    // provenance bar: reveal the whole bar left→right via clip-path (segment widths stay intact)
    q('.prov-reveal').forEach(function (el) {
      tl.fromTo(el, { clipPath: 'inset(0 100% 0 0)' }, { clipPath: 'inset(0 0% 0 0)', duration: 0.7, ease: 'power2.out', clearProps: 'clipPath' }, '-=0.1');
    });
    // vertical bars grow from the bottom
    q('.stk-seg, .wd-bar').forEach(function (el, i) {
      tl.from(el, { scaleY: 0, transformOrigin: 'bottom', duration: 0.5, ease: 'power2.out', clearProps: 'transform' }, i === 0 ? '-=0.1' : '-=0.35');
    });
    // confidence bar fill width
    q('.conffill').forEach(function (el) {
      var pct = el.getAttribute('data-fill') || '0';
      el.style.width = '0%';
      tl.to(el, { width: pct + '%', duration: 0.9, ease: 'power2.out' }, '-=0.2');
    });
    // mosaic flood-in: opacity-only (no per-tile scale → no layout thrash), smooth left-to-right wave
    var mtiles = q('.mtile');
    if (mtiles.length) {
      gsap.set(mtiles, { willChange: 'opacity' });
      tl.from(mtiles, { opacity: 0, duration: 0.4, ease: 'none', stagger: { each: 0.003, from: 'start', grid: 'auto' }, clearProps: 'opacity,willChange' }, 0);
    }
    // triangulation dot cloud crossfade in
    q('.tri-cloud').forEach(function (g) { tl.to(g, { opacity: 1, duration: 0.6 }, '-=0.2'); });

    // locale-aware count-ups ([data-count])
    q('[data-count]').forEach(function (el) {
      var target = parseFloat(el.getAttribute('data-count'));
      var dec = parseInt(el.getAttribute('data-dec') || '0', 10);
      var obj = { v: 0 };
      tl.to(obj, { v: target, duration: 1.1, ease: 'power2.out', onUpdate: function () { el.textContent = window.__fmtNum(obj.v, dec); } }, '-=1.0');
    });
  }

  // Animate just a freshly swapped-in subtree (slide-12's #tsel-dynamic on a tile click).
  // Deliberately VERY subtle: a single short opacity cross-fade of the whole subtree — no motion,
  // no per-item stagger — so swapping the example feels like a quiet content change, not a replay.
  function animateScope(el) {
    if (!el) return;
    if (REDUCED || !window.gsap) { el.style.opacity = '1'; return; }
    gsap.fromTo(el, { opacity: 0.55 }, { opacity: 1, duration: 0.18, ease: 'power1.out', clearProps: 'opacity' });
  }

  function updateChrome(n) {
    countText.textContent = n + ' / ' + TOTAL;
    dotEls.forEach(function (d, idx) { d.classList.toggle('on', idx + 1 === n); });
    var pct = TOTAL === 1 ? 100 : ((n - 1) / (TOTAL - 1)) * 100;
    if (window.gsap && !REDUCED) gsap.to(barFill, { width: pct + '%', duration: 0.5, ease: 'power2.out' });
    else barFill.style.width = pct + '%';
  }

  // ---- interactive: re-render a slide's DOM from its current (possibly dynamic) spec ----
  function renderSlideHTML(slide) {
    if (slide.custom && window.CUSTOM && window.CUSTOM[slide.custom]) return window.CUSTOM[slide.custom](slide, L, esc);
    return renderGeneric(slide);
  }
  function rebuildSlide(idx /* 0-based */) {
    var slide = SLIDES[idx];
    var sec = slideEls[idx];
    if (!slide || !sec) return;
    sec.innerHTML = '<div class="slide-content">' + renderSlideHTML(slide) + '</div>';
  }

  // tributary selection state lives on window.DECK.selected. Selecting rebuilds the 4 dyn slides.
  var DYN_SLOTS = {};   // map slot -> [slide indices], built from SLIDES
  SLIDES.forEach(function (s, i) { if (s.custom === 'dyn-deepdive') { (DYN_SLOTS[s.slot] = DYN_SLOTS[s.slot] || []).push(i); } });
  function rebuildDynamicSlides() {
    Object.keys(DYN_SLOTS).forEach(function (slot) { DYN_SLOTS[slot].forEach(function (idx) { rebuildSlide(idx); if (idx + 1 === current) animate(slideEls[idx], SLIDES[idx]); }); });
  }
  // Round-robin slot pointer: the next NEW pick replaces this slot, then flips. This keeps the
  // other example in place (no side-shuffle) and the deck always has exactly two picks.
  var nextSlot = 0;
  window.__selectTributary = function (id) {
    var sel = window.DECK.selected = (window.DECK.selected || []).slice();
    while (sel.length < 2) sel.push(sel[0] || id);    // safety: never fewer than 2 entries
    var firstPick = !window.DECK.userPicked;          // first interaction switches summary → lanes
    window.DECK.userPicked = true;
    if (sel.indexOf(id) >= 0) {
      // already selected: only meaningful as the FIRST click (reveals lanes); otherwise a no-op
      if (!firstPick) return;
    } else {
      sel[nextSlot] = id;                             // replace one slot in place
      nextSlot = nextSlot === 0 ? 1 : 0;              // alternate which slot the NEXT pick replaces
    }
    // On the selector slide, update ONLY the part under the tiles: flip the tile highlights in
    // place (no re-render of the wall) and rebuild just #tsel-dynamic (body sentence + lanes),
    // then animate that sub-tree alone — the title and tile wall stay put, no full-slide replay.
    var selIdx = -1;
    SLIDES.forEach(function (s, i) { if (s.custom === 'tributary-selector') selIdx = i; });
    if (selIdx >= 0) {
      var sec = slideEls[selIdx];
      Array.prototype.forEach.call(sec.querySelectorAll('.ttile'), function (t) {
        t.classList.toggle('on', sel.indexOf(t.getAttribute('data-tid')) >= 0);
      });
      var dyn = sec.querySelector('#tsel-dynamic');
      if (dyn && window.CUSTOM.__tselDynamic) {
        dyn.innerHTML = window.CUSTOM.__tselDynamic(SLIDES[selIdx], L, esc);
        if (selIdx + 1 === current) animateScope(dyn);   // animate only the swapped-in subtree
      }
    }
    rebuildDynamicSlides();
  };
  // delegate dot clicks (selector slide)
  slidesWrap.addEventListener('click', function (e) {
    var dot = e.target.closest && e.target.closest('.tsel-dot');
    if (dot) { e.stopPropagation(); window.__selectTributary(dot.getAttribute('data-tid')); }
  });

  function show(n) {
    n = Math.max(1, Math.min(TOTAL, n)); current = n;
    slideEls.forEach(function (s, idx) { s.classList.toggle('active', idx + 1 === n); });
    var slide = SLIDES[n - 1];
    // dynamic deep-dive slides: rebuild from current selection before showing
    if (slide && slide.custom === 'dyn-deepdive') rebuildSlide(n - 1);
    if (slide && (slide.embed || slide.custom === 'tributary-selector')) stage.classList.add('embed-active'); else stage.classList.remove('embed-active');
    updateChrome(n);
    if (location.hash.replace('#', '') !== String(n)) { suppressHashReload = true; history.replaceState(null, '', '#' + n); suppressHashReload = false; }
    if (slide && slide.custom === 'close') renderQR();
    autoFit(slideEls[n - 1]);
    animate(slideEls[n - 1], slide);
  }

  // Safety net: if a slide's content is taller/wider than the 1280×720 stage (e.g. a
  // longer language string), scale the inner content down just enough to fit. No-op
  // when content already fits, so it never shrinks well-sized slides.
  function autoFit(sec) {
    var content = sec.querySelector('.slide-content');
    if (!content) return;
    content.style.transform = ''; content.style.transformOrigin = 'top left';
    var inner = content.firstElementChild; if (!inner) return;
    if (inner.classList.contains('nofit')) return;   // deliberate overflow (e.g. a screenshot bleeding out at the bottom)
    // Measure natural content size against the LOGICAL slide box (1280×720).
    // Safari quirk: a flex child with overflowing content can report scrollHeight equal to its
    // *constrained* height (~720) instead of the true content height, so an overflowing slide
    // looks like it fits and autoFit never shrinks → visible overlap. Force the box to its
    // natural height for the measurement, then read the real extent from the children's bounds.
    var prevH = inner.style.height, prevMaxH = inner.style.maxHeight, prevOv = inner.style.overflow;
    inner.style.height = 'auto'; inner.style.maxHeight = 'none'; inner.style.overflow = 'visible';
    var sh = inner.scrollHeight, sw = inner.scrollWidth;
    // also take the furthest child bottom/right relative to inner (robust across engines)
    var ir = inner.getBoundingClientRect();
    var kids = inner.querySelectorAll('*');
    for (var ki = 0; ki < kids.length; ki++) {
      var kr = kids[ki].getBoundingClientRect();
      var bottom = (kr.bottom - ir.top) / SLIDE_SCALE, right = (kr.right - ir.left) / SLIDE_SCALE;
      if (bottom > sh) sh = bottom; if (right > sw) sw = right;
    }
    inner.style.height = prevH; inner.style.maxHeight = prevMaxH; inner.style.overflow = prevOv;
    var fy = sh > SLIDE_H ? SLIDE_H / sh : 1;
    var fx = sw > SLIDE_W ? SLIDE_W / sw : 1;
    var f = Math.min(fx, fy);
    if (f < 0.999) {
      content.style.transformOrigin = 'top center';   // shrink toward the top so the title never lifts out of frame
      content.style.transform = 'scale(' + f.toFixed(4) + ')';
    }
  }
  function next() {
    var s = SLIDES[current - 1];
    if (s && window.CUSTOM && window.CUSTOM.__beforeNext && window.CUSTOM.__beforeNext(s, slideEls[current - 1])) return;   // slide consumed the step
    if (current < TOTAL) show(current + 1);
  }
  function prev() { if (current > 1) show(current - 1); }

  document.addEventListener('keydown', function (e) {
    switch (e.key) {
      case 'ArrowRight': case 'PageDown': case ' ': case 'Spacebar': e.preventDefault(); next(); break;
      case 'ArrowLeft': case 'PageUp': case 'Backspace': e.preventDefault(); prev(); break;
      case 'Home': e.preventDefault(); show(1); break;
      case 'End': e.preventDefault(); show(TOTAL); break;
      case 'l': case 'L': toggleLang(); break;
    }
  });
  document.getElementById('nav-right').addEventListener('click', next);
  document.getElementById('nav-left').addEventListener('click', prev);
  var langBtn = document.getElementById('lang-toggle');
  function applyLang(lang) {
    if (lang !== 'en' && lang !== 'de') return;
    if (lang === LANG) return;
    LANG = lang;
    document.documentElement.lang = LANG;
    if (langBtn) langBtn.textContent = LANG === 'de' ? 'EN' : 'DE';
    // re-render every slide in the new language, then stay on the current slide (no reload)
    for (var i = 0; i < SLIDES.length; i++) rebuildSlide(i);
    slideEls = Array.prototype.slice.call(document.querySelectorAll('.slide'));
    _qrDone = false; renderQR();   // the close slide was rebuilt — draw the QR again
    wireFlitFrames();               // …and re-wire the rebuilt live Flit iframe
    show(current);
  }
  function toggleLang() {
    if (window.DECK.singleLang) return;   // this deck is authored in one language
    var next = (LANG === 'de') ? 'en' : 'de';
    // keep the address-bar hash in sync WITHOUT triggering a reload via the hashchange handler
    suppressHashReload = true; location.hash = next;
    applyLang(next);
  }
  // navigating the address-bar hash (#en/#de) directly should also switch language in place
  var suppressHashReload = false;
  window.addEventListener('hashchange', function () {
    if (suppressHashReload) { suppressHashReload = false; return; }
    var h = location.hash.replace('#', '');
    if (h === 'en' || h === 'de') applyLang(h);
    else if (/^\d+$/.test(h) && +h !== current) show(+h);   // #12 → jump to slide 12
  });
  // deep link: ?s=12 or #12 opens that slide directly
  function startSlide() {
    var q = new URLSearchParams(location.search).get('s'), h = location.hash.replace('#', '');
    var n = parseInt(q || (/^\d+$/.test(h) ? h : ''), 10);
    return (n >= 1 && n <= TOTAL) ? n : 1;
  }
  if (langBtn) { langBtn.textContent = LANG === 'de' ? 'EN' : 'DE'; langBtn.addEventListener('click', toggleLang); }

  // live Flit embed reveal — wires up EVERY Flit iframe on the page (slide 3 and the
  // close slide), each revealing its own fallback card + badge once it loads.
  // Must be re-run after applyLang(): the rebuilt slides carry NEW iframe elements, and an
  // unwired iframe leaves the static fallback card on top forever (seen on the close slide).
  function wireFlitFrames() {
    Array.prototype.forEach.call(document.querySelectorAll('iframe[id^="flit-frame"]'), function (frame) {
      if (frame.__wired) return; frame.__wired = true;
      var sfx = frame.id.replace('flit-frame', '');           // '' or '-3'
      var fallback = document.getElementById('flit-fallback' + sfx);
      var badge = document.getElementById('flit-badge' + sfx);
      var revealed = false;
      function goLive() { if (revealed) return; revealed = true; frame.style.opacity = '1'; if (fallback) fallback.style.zIndex = '0'; if (badge) { badge.textContent = 'live'; badge.style.background = '#46CC00'; } }
      frame.addEventListener('load', function () { setTimeout(goLive, 350); });
      setTimeout(function () { if (!revealed && badge) badge.textContent = 'preview'; }, 3500);
    });
  }
  wireFlitFrames();

  fitStage();
  show(startSlide());
})();
