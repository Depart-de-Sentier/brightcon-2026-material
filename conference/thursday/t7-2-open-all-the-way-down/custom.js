/* Bespoke slide renderers — match the visual richness of the two source decks.
   Each returns inner HTML for .slide-content. Signature: fn(slide, L, esc).
   Animation hooks: anim-kicker/title/body/item/flow/arrow/grow/pop/foot + bespoke .draw* classes.
   Number formatting is locale-aware via window.__fmtNum (set in engine.js). */
(function () {
  function head(slide, L, esc, opts) {
    opts = opts || {};
    var h = '';
    if (L(slide.kicker)) h += '<div class="kicker anim-kicker">' + esc(L(slide.kicker)) + '</div>';
    if (L(slide.title)) h += '<h2 class="title anim-title"' + (opts.titleStyle ? ' style="' + opts.titleStyle + '"' : '') + '>' + L(slide.title) + '</h2>';
    if (L(slide.body)) h += '<p class="body anim-body">' + L(slide.body) + '</p>';
    return h;
  }
  function foot(slide, L) { return L(slide.footnote) ? '<div class="footnote anim-foot">' + L(slide.footnote) + '</div>' : ''; }

  // describe an SVG donut arc
  function donutArc(cx, cy, r, a0, a1) {
    var rad = function (a) { return (a - 90) * Math.PI / 180; };
    var x0 = cx + r * Math.cos(rad(a0)), y0 = cy + r * Math.sin(rad(a0));
    var x1 = cx + r * Math.cos(rad(a1)), y1 = cy + r * Math.sin(rad(a1));
    var large = (a1 - a0) > 180 ? 1 : 0;
    return 'M' + x0.toFixed(1) + ' ' + y0.toFixed(1) + ' A' + r + ' ' + r + ' 0 ' + large + ' 1 ' + x1.toFixed(1) + ' ' + y1.toFixed(1);
  }

  window.CUSTOM = {

    // SLIDE 12: the ORIGINAL two-lane design + text, rendered 1:1. The tile wall is clickable;
    // by default the two lanes + the body sentence name Strom & SALCA verbatim. Picking a tile
    // swaps that lane + updates the body sentence + drives slides 13-16. Only the part UNDER the
    // tiles (#tsel-dynamic) re-renders on click — the title/tiles stay put (see __selectTributary).
    'tributary-selector': function (slide, L, esc) {
      var tribs = (window.DECK.tributaries) || [];
      var sel = window.DECK.selected || [];
      // tile wall: one clickable tile per tributary — identical <span class="ttile"> to the original
      // two-lane (14px rounded rectangles, one row). data-tid selects; data-name drives a tooltip.
      var tiles = tribs.map(function (t) {
        var on = sel.indexOf(t.id) >= 0;
        return '<span class="ttile tsel-dot' + (on ? ' on' : '') + '" data-tid="' + esc(t.id) + '" data-name="' + esc(t.name) + '"></span>';
      }).join('');
      return '<div class="pad pad-top" style="padding:58px 64px 36px;">' +
        '<div class="kicker anim-kicker">' + esc(L(slide.kicker)) + '</div>' +
        '<h2 class="title anim-title">' + L(slide.title) + '</h2>' +
        '<div class="twall tsel-wall anim-foot" id="tsel-wall">' + tiles + '</div>' +
        '<div id="tsel-dynamic">' + window.CUSTOM.__tselDynamic(slide, L, esc) + '</div>' +
        foot(slide, L) + '</div>';
    },

    // The re-buildable part under the tiles. BEFORE the user clicks a tile it shows the deck-wide
    // SUMMARY (headline + 3 key points about all 73 tributaries). AFTER the first click it switches
    // to the two chosen example lanes. Only this sub-tree re-renders/animates on a tile click.
    __tselDynamic: function (slide, L, esc) {
      var tribs = (window.DECK.tributaries) || [];
      var sel = window.DECK.selected || [];
      var tc = window.DECK.tributaryContent || {};
      var defaults = slide.defaultIds || [];

      function nameFor(slot) {
        var id = sel[slot];
        var di = defaults.indexOf(id);                 // is this id one of the two defaults? (any slot)
        if (di >= 0) { var o = di === 0 ? slide.laneA : slide.laneB; return L((o || {}).head); }
        var t = tribs.filter(function (x) { return x.id === id; })[0];
        return t ? t.name : '—';
      }
      // body sentence with the two current picks substituted in
      var nameA = nameFor(0), nameB = nameFor(1);
      var tmpl = L(slide.bodyTemplate) || (L(slide.body) || '');
      var body = tmpl.replace('{A}', '<b>' + nameA + '</b>').replace('{B}', '<b>' + nameB + '</b>');
      function lane(slot) {
        var id = sel[slot];
        var di = defaults.indexOf(id);                 // default tributary? use its original lane text (any slot)
        var orig = di === 0 ? (slide.laneA || {}) : (slide.laneB || {});
        var head_, sub, items;
        if (di >= 0) {
          head_ = L(orig.head); sub = L(orig.sub); items = (orig.items || []).map(L);
        } else {
          var t = tribs.filter(function (x) { return x.id === id; })[0];
          var c = tc[id] || {}, s1 = c.slide1 || {}, s2 = c.slide2 || {};
          head_ = t ? t.name : '—';
          sub = s1.title ? L(s1.title) : '';
          // pull up to 3 short facts — works across ALL renderer types (bullets / stats / bars /
          // bigstat figures+items / wet-dry-bars / stacked-bar segments), trying slide1 then slide2.
          function facts(s) {
            if (!s) return [];
            if (s.bullets) return s.bullets.map(L);
            if (s.stats) return s.stats.map(function (x) { return L(x.num) + ' · ' + L(x.label); });
            if (s.figures) return s.figures.map(function (x) { return (L(x.label) ? (x.n + (L(x.suffix) || '') + ' · ' + L(x.label)) : (x.n + (L(x.suffix) || ''))); });
            if (s.bars) return s.bars.map(function (x) { return L(x.disp) + ' · ' + L(x.label); });
            if (s.segments) return s.segments.map(function (x) { return L(x.disp) + ' · ' + L(x.label); });
            if (s.renderer === 'wet-dry-bars' && s.wet && s.dry) return [(L(s.ratio) || '') ? (L(s.ratio) + ' · ' + L(s.wet.label) + ' vs ' + L(s.dry.label)) : (L(s.wet.disp) + ' · ' + L(s.wet.label)), L(s.dry.disp) + ' · ' + L(s.dry.label)];
            return [];
          }
          var arr = facts(s1);
          if (arr.length < 2) arr = arr.concat(facts(s2));   // top up from slide2 if slide1 was thin
          items = arr.slice(0, 3);
        }
        var bul = items.map(function (x) { return '<div class="bullet anim-item bullet-static"><span class="tick">✓</span><span>' + x + '</span></div>'; }).join('');
        return '<div class="lane" data-slot="' + slot + '"><div class="lane-h anim-item">' + head_ + '</div><div class="lane-sub anim-item">' + sub + '</div>' + bul + '</div>';
      }
      var gut = L(slide.gutterLabel);
      return '<p class="body anim-body" style="margin-bottom:10px;">' + body + '</p>' +
        '<div class="lanes">' + lane(0) +
          '<div class="lane-gutter">' + (gut ? '<span class="indep">' + gut + '</span>' : '') + '</div>' +
          lane(1) +
        '</div>';
    },

    // DYNAMIC DEEP-DIVE (slides 13-16): content resolved at render time from the selected tributary.
    // slide.slot = 0|1 (which selected tributary); slide.which = 'slide1'|'slide2'.
    'dyn-deepdive': function (slide, L, esc) {
      var sel = window.DECK.selected || [];
      var id = sel[slide.slot];
      var tc = (window.DECK.tributaryContent || {})[id];
      if (!tc) return '<div class="pad"><div class="kicker">—</div><h2 class="title">Kein Tributary gewählt</h2></div>';
      var spec = tc[slide.which] || {};
      // RICH DELEGATION: if the spec names an original bespoke renderer + carries its data,
      // render through that renderer (so electricity/SALCA keep their full wet-dry-bars /
      // bigstat / stacked-bar visuals — not the generic fallback below).
      if (spec.renderer && window.CUSTOM[spec.renderer]) {
        var rich = {};
        for (var kk in spec) { if (spec.hasOwnProperty(kk)) rich[kk] = spec[kk]; }
        rich.kicker = tc.kicker || spec.kicker || '';
        return window.CUSTOM[spec.renderer](rich, L, esc);
      }
      // normalized spec fields: kicker, title{de,en}, body{de,en}, bars[], stats[], bullets[], footnote{de,en}
      var k = tc.kicker || '';
      var inner = '';
      // stats row (big figures)
      if (spec.stats && spec.stats.length) {
        inner += '<div class="kpirow" style="margin-top:10px;">' + spec.stats.map(function (s) {
          return '<div class="kpibox anim-pop"><div class="kpi-num">' + L(s.num) + '</div><div class="kpi-lbl">' + L(s.label) + '</div></div>';
        }).join('') + '</div>';
      }
      // bars (simple labelled horizontal bars 0..max)
      if (spec.bars && spec.bars.length) {
        var max = Math.max.apply(null, spec.bars.map(function (b) { return b.value || 0; })) || 1;
        inner += '<div class="dyn-bars">' + spec.bars.map(function (b) {
          return '<div class="dyn-bar-row anim-item"><span class="dyn-bar-lbl">' + L(b.label) + '</span>' +
            '<div class="dyn-bar-track"><div class="dyn-bar-fill anim-grow" style="width:' + Math.round((b.value || 0) / max * 100) + '%;background:' + (b.color || '#16a34a') + ';"></div></div>' +
            '<span class="dyn-bar-val">' + L(b.disp) + '</span></div>';
        }).join('') + '</div>';
      }
      // bullets
      if (spec.bullets && spec.bullets.length) {
        inner += '<div class="bullets" style="flex-direction:column;margin-top:8px;">' + spec.bullets.map(function (x) {
          return '<div class="bullet anim-item bullet-static"><span class="tick">✓</span><span>' + L(x) + '</span></div>';
        }).join('') + '</div>';
      }
      var shead = { kicker: k, title: spec.title, body: spec.body };
      return '<div class="pad pad-top" style="padding:54px 64px 32px;">' + head(shead, L, esc) + inner +
        (L(spec.footnote) ? '<div class="footnote anim-foot">' + L(spec.footnote) + '</div>' : '') + '</div>';
    },

    // LICENSES: open-license pills (left) + license-distribution donut (right)
    'license-grid': function (slide, L, esc) {
      var pills = (slide.licenses || []).map(function (l) {
        return '<div class="licpill anim-item"><span class="lic-open">🔓</span><span class="lic-name">' + L(l.name) + '</span><span class="lic-tag">' + L(l.tag) + '</span></div>';
      }).join('');
      var segs = slide.donut || [], total = segs.reduce(function (s, x) { return s + x.n; }, 0) || 1;
      var a = 0, arcs = '';
      segs.forEach(function (s) { var a1 = Math.min(a + s.n / total * 360, a + 359.99); /* a single 360° segment would collapse to an empty arc */ arcs += '<path class="donut-arc anim-grow-arc" d="' + donutArc(110, 110, 80, a, a1) + '" fill="none" stroke="' + s.color + '" stroke-width="34"/>'; a = a1; });
      var legend = segs.map(function (s) { return '<div class="dleg anim-item"><span style="background:' + s.color + '"></span>' + s.n + ' ' + L(s.label) + '</div>'; }).join('');
      // center label fades in WITH the donut (anim-pop) so it isn't visible before the animation
      var donut = '<svg viewBox="0 0 220 220" width="240" height="240">' + arcs +
        '<g class="anim-pop">' +
        '<text x="110" y="104" text-anchor="middle" font-size="34" font-weight="800" fill="#083118">' + total + '</text>' +
        '<text x="110" y="128" text-anchor="middle" font-size="13" fill="#5b6b60">' + (L(slide.donutCenter) || 'OPEN') + '</text>' +
        '</g></svg>';
      return '<div class="pad pad-top" style="padding:58px 72px 36px;">' + head(slide, L, esc) +
        '<div style="display:flex;gap:56px;align-items:center;flex:1;">' +
          '<div style="flex:0 0 460px;display:flex;flex-direction:column;gap:12px;">' + pills + '</div>' +
          '<div style="flex:1;display:flex;flex-direction:column;align-items:center;gap:10px;">' + donut +
            '<div class="dlegwrap">' + legend + '</div>' +
            (L(slide.donutSub) ? '<div class="dsub anim-foot">' + L(slide.donutSub) + '</div>' : '') +
          '</div>' +
        '</div>' + foot(slide, L) + '</div>';
    },

    // TRIBUTARY CATALOGUE: KPI stat boxes (poster style) + full tributary list as grouped pills
    'tributary-catalogue': function (slide, L, esc) {
      var kpis = (slide.kpis || []).map(function (k) {
        return '<div class="kpibox anim-pop"><div class="kpi-num">' + L(k.num) + '</div><div class="kpi-lbl">' + L(k.label) + '</div></div>';
      }).join('');
      // heading on the LEFT of its pills (inline rows) to save vertical space
      var groups = (slide.groups || []).map(function (g) {
        var pills = (g.items || []).map(function (it) { return '<span class="tpill anim-flow">' + L(it) + '</span>'; }).join('');
        return '<div class="tgroup"><div class="tgroup-h">' + L(g.head) + '</div><div class="tpills">' + pills + '</div></div>';
      }).join('');
      return '<div class="pad pad-top" style="padding:54px 64px 32px;">' + head(slide, L, esc) +
        '<div class="kpirow">' + kpis + '</div>' +
        '<div class="tgroups">' + groups + '</div>' +
        foot(slide, L) + '</div>';
    },

    // INTEGRATION MAP: central hub + two rings of named project/standard satellites; optional size bars + provenance bar
    'integration-map': function (slide, L, esc) {
      // size comparison bars
      var sz = slide.sizes || null;
      var sizeBars = sz ? (L(slide.sizesHead) ? '<div class="grouphead">' + L(slide.sizesHead) + '</div>' : '') + '<div class="szbars">' +
        '<div class="szrow"><span class="szlbl">' + L(sz.a.label) + '</span><div class="szbar"><div class="szfill anim-grow" style="width:100%;background:#b0bec5;"></div></div><span class="szval">' + L(sz.a.val) + '</span></div>' +
        '<div class="szrow"><span class="szlbl">' + L(sz.b.label) + '</span><div class="szbar"><div class="szfill anim-grow" style="width:' + sz.b.pct + '%;background:#16a34a;"></div><div class="szgap" style="left:' + sz.b.pct + '%;">' + (L(sz.gapLabel) || '') + '</div></div><span class="szval">' + L(sz.b.val) + '</span></div>' +
      '</div>' : '';
      // provenance bar (must sum to 100). Widths via flex-basis (immune to GSAP clearProps);
      // the whole bar reveals left→right with a clip-path wipe so segment widths never collapse.
      var prov = slide.provenance || null;
      var provBar = prov ? '<div class="provwrap">' + (L(slide.provHead) ? '<div class="grouphead">' + L(slide.provHead) + '</div>' : '') + '<div class="provbar prov-reveal">' +
        prov.segments.map(function (s) { return '<div class="provseg" style="flex:0 0 ' + s.pct + '%;background:' + s.color + ';" title="' + L(s.label) + '"><span>' + s.pct + '%</span></div>'; }).join('') +
      '</div><div class="provlegend">' + prov.segments.map(function (s) { return '<span class="pl"><i style="background:' + s.color + '"></i>' + L(s.label) + '</span>'; }).join('') + '</div>' +
        (L(prov.caption) ? '<div class="provcap">' + L(prov.caption) + '</div>' : '') + '</div>' : '';
      // hub + satellites. Single ring only (no overlapping outer ring); standards listed below as a caption.
      var hub = slide.hub || {}, inner = slide.inner || [], outer = slide.outer || [];
      function ring(items, radius, cls) {
        var n = items.length;
        return items.map(function (it, i) {
          var ang = (i / n) * 2 * Math.PI - Math.PI / 2;
          var x = 50 + Math.cos(ang) * radius, y = 50 + Math.sin(ang) * radius;
          var txt = L(it);
          // "open slot" style for invitation placeholders (text ends with ? or starts with +)
          var open = /\?$|^[+→]/.test(txt.trim()) ? ' sat-open' : '';
          return '<div class="sat ' + cls + open + ' anim-pop" style="left:' + x.toFixed(1) + '%;top:' + y.toFixed(1) + '%;">' + txt + '</div>';
        }).join('');
      }
      var map = '<div class="intmap">' +
        '<div class="hub ' + (slide.resolved ? 'resolved' : '') + ' anim-pop">' + L(hub.label) + (L(hub.badge) ? '<span class="hub-badge">' + L(hub.badge) + '</span>' : '') + '</div>' +
        ring(inner, 38, 'sat-inner') +
        (outer.length ? '<div class="sat-caption anim-item">' + outer.map(L).join(' · ') + '</div>' : '') +
      '</div>';
      // left column: size+provenance (S8) OR trust-badge cards (WRAPUP) OR fallback text
      var badges = (slide.badges || []).map(function (b) { return '<div class="trustbadge anim-item"><span class="tick">✓</span>' + L(b) + '</div>'; }).join('');
      var left = sizeBars + provBar + (badges ? '<div class="trustcol">' + badges + '</div>' : '');
      return '<div class="pad pad-top" style="padding:58px 64px 36px;">' + head(slide, L, esc) +
        '<div style="display:flex;gap:40px;align-items:flex-start;flex:1;min-height:0;">' +
          '<div style="flex:1 1 0;min-width:0;display:flex;flex-direction:column;gap:18px;">' + (left || '') + '</div>' +
          '<div style="flex:0 0 420px;align-self:center;display:flex;align-items:center;justify-content:center;">' + map + '</div>' +
        '</div>' + foot(slide, L) + '</div>';
    },

    // SCREENSHOT SPLIT: live iframe of a site in mock browser chrome + annotation callouts
    'screenshot-split': function (slide, L, esc) {
      var sideFirst = slide.visualSide === 'left';
      var ann = (slide.annotations || []).map(function (a) { return '<div class="anno anim-item"><div class="anno-t">' + L(a.title) + '</div>' + (L(a.sub) ? '<div class="anno-s">' + L(a.sub) + '</div>' : '') + '</div>'; }).join('');
      var capList = (slide.capabilities || []).map(function (c, i) { return (i > 0 ? '<div class="drill-chev anim-arrow">⌄</div>' : '') + '<div class="drillrow anim-item">' + L(c) + '</div>'; }).join('');
      var sfx = slide.frameId || 'wb';
      // viewport content: either a live iframe, or a static panel (for sites that block framing, e.g. X-Frame-Options)
      var viewport;
      if (slide.image && !L(slide.embedUrl)) {
        var mock = '<div class="ffm"><div class="ffm-side"><div class="ffm-brand"><img src="assets/firefly-3.webp" alt=""/><span>Brightway Firefly<small>LCA Navigator</small></span></div>' +
          ['Activities', 'Browse', 'Graph', 'Cascades', 'Composer', 'EOS Review', 'Calculator', 'Compare', 'Parameters', 'Docs', 'Permissions'].map(function (x) { return '<div class="ffm-nav' + (x === (slide.mockActive || '') ? ' on' : '') + '">' + x + '</div>'; }).join('') + '</div>' +
          '<div class="ffm-main"><div class="ffm-top"><span>' + esc(slide.mockActive || 'Firefly') + '</span><span class="ffm-search">Search… ⌘K</span></div><div class="ffm-center">' + (L(slide.mockText) || '') + '</div></div></div>';
        viewport = '<div class="bimgwrap">' + mock + '<img class="bimg' + (slide.imageFit === 'contain' ? ' contain' : slide.imageFit === 'contain-light' ? ' contain contain-light' : '') + '" src="' + slide.image + '" alt="" onerror="' + (slide.imageFallback ? 'if(!this.__fb){this.__fb=1;this.src=\'' + slide.imageFallback + '\'}else{this.style.display=\'none\'}' : 'this.style.display=\'none\'') + '"/></div>';
      } else if (slide.staticPanel === 'firefly') {
        viewport = '<div class="ff-mock">' +
          '<div class="ff-nav"><span class="ff-logo"><img src="assets/firefly-logo.svg" alt="Firefly"/> Firefly</span><span class="ff-links">Features · Download · GitLab ↗</span></div>' +
          '<div class="ff-body">' +
            '<div class="ff-left">' +
              '<div class="ff-eyebrow">OPEN SOURCE · AGPL-3.0</div>' +
              '<div class="ff-h">The Modern Interface<br>for <span>Life Cycle Assessment</span></div>' +
              '<div class="ff-p">Search 18,000+ activities, calculate environmental impacts, visualize supply chains. Powered by Brightway2.</div>' +
              '<div class="ff-stats"><span>18,000+ activities</span><span>10+ methods</span><span>3 platforms</span><span>100% open source</span></div>' +
            '</div>' +
            '<div class="ff-card"><img class="ff-icon-img" src="assets/firefly-logo.svg" alt="Firefly"/><div class="ff-ct">Brightway Firefly</div><div class="ff-cs">Login to your account</div><div class="ff-tabs"><span class="on">Login</span><span>Register</span></div><div class="ff-field"></div><div class="ff-field"></div><div class="ff-btn">Login</div></div>' +
          '</div></div>';
      } else {
        viewport = '<div id="flit-fallback-' + sfx + '" class="bfallback' + (slide.image ? ' bfallback-img' : '') + '">' + (slide.image ? '<img class="bimg" src="' + slide.image + '" alt=""/>' : (L(slide.fallback) || '')) + '</div>' +
          '<iframe id="flit-frame-' + sfx + '" src="' + L(slide.embedUrl) + '" title="" loading="eager" referrerpolicy="no-referrer" sandbox="allow-scripts allow-same-origin allow-forms allow-popups" style="position:absolute;inset:0;width:100%;height:100%;border:0;background:#fff;opacity:0;transition:opacity .4s;z-index:2;"></iframe>';
      }
      var badge = (slide.staticPanel || (slide.image && !L(slide.embedUrl))) ? '<span class="flit-badge" style="background:#46CC00;">' + (slide.badge || 'live') + '</span>' : '<span class="flit-badge" id="flit-badge-' + sfx + '">…</span>';
      var browser = slide.noChrome
        ? '<div class="rawshot" style="height:' + (slide.frameHigh || 386) + 'px;"><img style="width:100%;height:100%;object-fit:contain;display:block;" src="' + slide.image + '" alt=""/></div>'
        : '<div class="browser"><div class="bchrome"><span class="bdot r"></span><span class="bdot y"></span><span class="bdot g"></span><span class="baddr">' + (L(slide.url) || '') + '</span>' + badge + '</div>' +
        '<div class="bviewport"' + (slide.frameHigh ? ' style="height:' + slide.frameHigh + 'px"' : '') + '>' + viewport + '</div></div>';
      var textCol = '<div style="flex:1;display:flex;flex-direction:column;gap:8px;">' + (slide.icon ? '<img class="slide-icon anim-pop" src="' + slide.icon + '" alt=""/>' : '') + head(slide, L, esc) + (ann || capList ? '<div style="display:flex;flex-direction:column;gap:6px;">' + ann + capList + '</div>' : '') + '</div>';
      var visCol = '<div style="flex:0 0 ' + (slide.frameWide || 600) + 'px;">' + browser + '</div>';
      return '<div class="pad pad-top" style="padding:58px 64px 36px;">' +
        '<div style="display:flex;gap:48px;align-items:center;flex:1;">' + (sideFirst ? visCol + textCol : textCol + visCol) + '</div>' +
        foot(slide, L) + '</div>';
    },

    // TWO-LANE: two clearly-independent example columns separated by a gutter
    'two-lane': function (slide, L, esc) {
      var tiles = ''; for (var i = 0; i < 59; i++) tiles += '<span class="ttile' + (i === 12 || i === 40 ? ' on' : '') + '"></span>';
      function lane(l) {
        var items = (l.items || []).map(function (x) { return '<div class="bullet anim-item bullet-static"><span class="tick">✓</span><span>' + L(x) + '</span></div>'; }).join('');
        return '<div class="lane"><div class="lane-h anim-item">' + L(l.head) + '</div><div class="lane-sub anim-item">' + L(l.sub) + '</div>' + items + '</div>';
      }
      var gut = L(slide.gutterLabel);
      return '<div class="pad pad-top" style="padding:58px 64px 36px;">' + head(slide, L, esc) +
        '<div class="twall anim-foot">' + tiles + '</div>' +
        '<div class="lanes">' + lane(slide.laneA || {}) +
          '<div class="lane-gutter">' + (gut ? '<span class="indep">' + gut + '</span>' : '') + '</div>' +
          lane(slide.laneB || {}) +
        '</div>' + foot(slide, L) + '</div>';
    },


    // 1 — HERO: big "Flit" + A–E chips on dark ground
    hero: function (slide, L, esc) {
      var bands = ['a', 'b', 'c', 'd', 'e'];
      // A–E rating chips by default; slide.chipsText (e.g. export formats) renders text pills instead
      var chips = slide.chipsText
        ? slide.chipsText.map(function (c) { return '<span class="chip chip-text anim-pop">' + esc(L(c)) + '</span>'; }).join('')
        : bands.map(function (b) { return '<span class="chip band-' + b + ' anim-pop">' + b.toUpperCase() + '</span>'; }).join('');
      var logos = (slide.logos || []).map(function (src) { return '<span class="hero-logo' + (slide.logoPlain ? ' plain' : '') + ' anim-pop"><img src="' + src + '" alt=""/></span>'; }).join('');
      return '<div class="hero hero-dark">' +
        '<div class="hero-grid"></div>' +
        (logos ? '<div class="hero-logos">' + logos + '</div>' : '') +
        (L(slide.kicker) ? '<div class="kicker anim-kicker" style="color:#7CDB5B;">' + esc(L(slide.kicker)) + '</div>' : '') +
        '<h1 class="anim-title hero-mark' + (String(L(slide.title)).length > 14 ? ' hero-mark-long' : '') + '">' + L(slide.title) + '</h1>' +
        (L(slide.body) ? '<p class="body anim-body" style="color:#cdebd8;max-width:760px;margin-top:22px;">' + L(slide.body) + '</p>' : '') +
        '<div class="chips">' + chips + '</div>' +
        (L(slide.footnote) ? '<div class="hero-foot anim-foot">' + L(slide.footnote) + '</div>' : '') +
        '</div>';
    },

    // ONE OBJECT, THREE FACES (Apple fashion): a triangular prism of square app icons on black, no text.
    // Each "next" (click, →, space) turns the prism 120° to the next face; two full rounds, then the deck moves on.
    // Face 1 is a generic "interface" glyph — the Firefly bee is only revealed on the following slide.
    'three-icons': function (slide, L, esc) {
      var svg = window.CUSTOM.__iconSvg;
      var faces = (slide.icons || []).map(function (it, i) {
        return '<div class="prism-face face-' + esc(it.icon) + '" style="transform:rotateY(' + (i * 120) + 'deg) translateZ(var(--apothem))">' + (svg[it.icon] || '') + '</div>';
      }).join('');
      var first = (slide.icons || [])[0] || {};
      return '<div class="one-icon-stage">' +
        '<div class="prism-col"><div class="prism-wrap anim-pop"><div class="prism" id="one-icon-prism" data-step="0" style="transform:rotateY(0deg)">' + faces + '</div></div>' +
        '<div class="prism-label anim-item" id="one-icon-label">' + esc(L(first.label) || '') + '</div></div>' +
        '</div>';
    },
    __iconSvg: {
      ui: '<svg viewBox="0 0 64 64" fill="none" stroke="#fff" stroke-width="3.2" stroke-linecap="round" stroke-linejoin="round"><rect x="8" y="12" width="48" height="40" rx="6"/><path d="M8 22h48"/><circle cx="15" cy="17" r="1.6" fill="#fff"/><circle cx="21" cy="17" r="1.6" fill="#fff"/><path d="M16 30h14M16 38h22M16 46h10"/><path d="M40 30l6 6-6 6"/></svg>',
      db: '<svg viewBox="0 0 64 64" fill="none" stroke="#fff" stroke-width="3.2" stroke-linecap="round"><ellipse cx="32" cy="16" rx="20" ry="8"/><path d="M12 16v16c0 4.4 9 8 20 8s20-3.6 20-8V16"/><path d="M12 32v16c0 4.4 9 8 20 8s20-3.6 20-8V32"/></svg>',
      ai: '<svg viewBox="0 0 64 64" fill="#fff"><path d="M30 6l4.6 13.4L48 24l-13.4 4.6L30 42l-4.6-13.4L12 24l13.4-4.6z"/><path d="M48 36l2.3 6.7L57 45l-6.7 2.3L48 54l-2.3-6.7L39 45l6.7-2.3z"/><path d="M14 44l1.7 4.3L20 50l-4.3 1.7L14 56l-1.7-4.3L8 50l4.3-1.7z"/></svg>',
      firefly: '<img src="assets/firefly-3.webp" alt="Firefly"/>'
    },
    // called by engine.next(): returns true when the step was consumed by the slide
    __beforeNext: function (slide, el) {
      if (!slide || slide.custom !== 'three-icons') return false;
      var prism = el && el.querySelector('#one-icon-prism'); if (!prism) return false;
      var step = parseInt(prism.getAttribute('data-step') || '0', 10);
      var n = (slide.icons || []).length, rounds = slide.rounds || 2;
      if (step >= n * rounds - 1) return false;                    // last face of the last round shown → move on
      if (prism.__turning) return true;                            // ignore double taps mid-turn
      prism.__turning = true;
      var label = el.querySelector('#one-icon-label');
      var nextLabel = ((slide.icons || [])[(step + 1) % n] || {}).label || '';
      var done = function () { prism.setAttribute('data-step', String(step + 1)); prism.__turning = false; };
      // round 1: a plain 120° turn. Round 2 (Jobs' repeat): go the long way round (+240°), so the
      // other face flashes past — the same face ends up in front either way.
      // always the same direction: round 1 turns −120° per step, round 2 turns −480° (a full extra turn,
      // so the other faces flash past) — the face in front is the same either way
      var extra = Math.max(0, step + 1 - n);
      var target = -120 * (step + 1) - 360 * extra;
      if (window.gsap) {
        gsap.to(prism, { rotationY: target, duration: extra ? 1.3 : 0.9, ease: 'power2.inOut', onComplete: done });
        if (label) gsap.timeline().to(label, { opacity: 0, y: 8, duration: 0.3 }).call(function () { label.textContent = nextLabel; }).to(label, { opacity: 1, y: 0, duration: 0.35 }, '+=0.15');
      } else { prism.style.transform = 'rotateY(' + target + 'deg)'; if (label) label.textContent = nextLabel; done(); }
      return true;
    },

    // FULL IMAGE: one screenshot, nothing else (contained on black)
    'full-image': function (slide, L, esc) {
      return '<div class="full-image-stage nofit" style="background:' + (slide.bg || '#000') + ';"><img class="full-image' + (slide.bleed ? ' bleed' : '') + '" src="' + slide.image + '" alt=""' + (slide.imageFallback ? ' onerror="if(!this.__fb){this.__fb=1;this.src=\'' + slide.imageFallback + '\'}"' : '') + '/>' + (L(slide.caption) ? '<div class="fi-caption">' + L(slide.caption) + '</div>' : '') + '</div>';
    },

    // DIALOG PAIR: lean re-renderings of Firefly's NewProjectDialog (import) and ExportDialog — the labels,
    // tiles, sources and formats are the component's own (frontend/src/components/NewProjectDialog.tsx,
    // components/export/ExportDialog.tsx, lib/exportFormats.ts), drawn as clean cards instead of a screenshot.
    'dialog-pair': function (slide, L, esc) {
      var ico = {
        folder: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M3 7a2 2 0 0 1 2-2h4l2 2h8a2 2 0 0 1 2 2v9a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/><path d="M12 11v6M9 14h6"/></svg>',
        cloud: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"><path d="M7 18h10a4 4 0 0 0 .5-8A6 6 0 0 0 6 11a3.5 3.5 0 0 0 1 7z"/></svg>',
        pack: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round"><path d="M12 3l8 4.5v9L12 21l-8-4.5v-9z"/><path d="M4 7.5l8 4.5 8-4.5M12 12v9"/></svg>',
        archive: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round"><path d="M6 3h8l4 4v14H6z"/><path d="M14 3v4h4M10 12h4M10 16h4"/></svg>',
        dl: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 4v11M7 10l5 5 5-5M4 19h16"/></svg>'
      };
      var imp = slide.importDialog || {}, exp = slide.exportDialog || {};
      var tile = function (t) { return '<div class="fd-tile' + (t.on ? ' on' : '') + '">' + (ico[t.icon] || '') + '<span>' + esc(L(t.label)) + '</span></div>'; };
      var left = '<div class="fd-card anim-item">' +
        '<div class="fd-h">' + esc(L(imp.title) || 'Create New Project') + '</div><div class="fd-sub">' + esc(L(imp.sub) || '') + '</div>' +
        '<div class="fd-lbl">' + esc(L(imp.group1) || '') + '</div><div class="fd-tiles">' + (imp.tiles || []).map(tile).join('') + '</div>' +
        '<div class="fd-lbl">' + esc(L(imp.group2) || '') + '</div><div class="fd-tiles"><div class="fd-tile-w">' + (imp.restore ? tile(imp.restore) : '') + '</div></div>' +
        '<div class="fd-note">' + esc(L(imp.note) || '') + '</div>' +
        '<div class="fd-lbl">' + esc(L(imp.sourceLabel) || 'Source') + '</div><div class="fd-seg">' + (imp.sources || []).map(function (x, i) { return '<span class="' + (i === 0 ? 'on' : '') + '">' + esc(L(x)) + '</span>'; }).join('') + '</div>' +
        '<div class="fd-lbl">' + esc(L(imp.fileLabel) || 'Package File') + '</div><div class="fd-field">' + esc(L(imp.fileHint) || '') + '</div>' +
        '</div>';
      var right = '<div class="fd-card anim-item">' +
        '<div class="fd-h">' + ico.dl + esc(L(exp.title) || 'Export / Backup') + '</div><div class="fd-sub">' + esc(L(exp.sub) || '') + '</div>' +
        '<div class="fd-lbl">Scope</div><div class="fd-select">' + esc(L(exp.scope) || 'Whole project') + '<i>⌄</i></div>' +
        '<div class="fd-lbl">Format</div><div class="fd-list">' + (exp.formats || []).map(function (f, i) { return '<div class="fd-opt' + (i === 0 ? ' on' : '') + '"><span>' + esc(L(f.label)) + '</span>' + (i === 0 ? '<b>✓</b>' : '') + '</div>'; }).join('') + '</div>' +
        '<div class="fd-note">' + esc(L((exp.formats || [{}])[0].desc) || '') + '</div>' +
        '<div class="fd-btn">' + esc(L(exp.button) || 'Start export') + '</div>' +
        '</div>';
      var ann = (slide.annotations || []).map(function (a) { return '<div class="anno anim-item"><div class="anno-t">' + L(a.title) + '</div>' + (L(a.sub) ? '<div class="anno-s">' + L(a.sub) + '</div>' : '') + '</div>'; }).join('');
      return '<div class="pad pad-top" style="padding:58px 64px 36px;">' +
        '<div style="display:flex;gap:40px;align-items:center;flex:1;">' +
          '<div style="flex:1;display:flex;flex-direction:column;gap:8px;">' + head(slide, L, esc) + '<div style="display:flex;flex-direction:column;gap:6px;">' + ann + '</div></div>' +
          '<div class="fd-pair">' + left + right + '</div>' +
        '</div>' + foot(slide, L) + '</div>';
    },

    // WIDE SHOT: head on top, one wide illustration across the slide, a row of short points beneath
    'wide-shot': function (slide, L, esc) {
      var cards = (slide.annotations || []).map(function (a) { return '<div class="anno anim-item" style="flex:1;"><div class="anno-t">' + L(a.title) + '</div>' + (L(a.sub) ? '<div class="anno-s">' + L(a.sub) + '</div>' : '') + '</div>'; }).join('');
      var hd = slide.iconSvg
        ? (L(slide.kicker) ? '<div class="kicker anim-kicker">' + esc(L(slide.kicker)) + '</div>' : '') + '<h2 class="title anim-title ws-title"><span class="ws-icon">' + slide.iconSvg + '</span>' + L(slide.title) + '</h2>' + (L(slide.body) ? '<p class="body anim-body">' + L(slide.body) + '</p>' : '')
        : head(slide, L, esc);
      return '<div class="pad pad-top" style="padding:54px 64px 34px;">' + hd +
        '<div class="wideshot"><img src="' + slide.image + '" alt=""/></div>' +
        (cards ? '<div style="display:flex;gap:14px;margin-top:16px;">' + cards + '</div>' : '') +
        foot(slide, L) + '</div>';
    },

    // REVEAL: three huge words front and centre on a dark ground, the licence facts small below
    'reveal': function (slide, L, esc) {
      var words = (slide.words || []).map(function (w, i) { return '<div class="rv-word anim-pop" style="animation-delay:' + (i * 0.25) + 's">' + esc(L(w)) + '</div>'; }).join('');
      var rows = (slide.rows || []).map(function (r) { return '<div class="rv-row anim-item"><span class="rv-chip">' + esc(L(r.chip)) + '</span><span class="rv-what">' + L(r.what) + '</span><span class="rv-where">' + L(r.where) + '</span></div>'; }).join('');
      return '<div class="rv-stage">' +
        (L(slide.kicker) ? '<div class="rv-kicker anim-kicker">' + esc(L(slide.kicker)) + '</div>' : '') +
        '<div class="rv-words">' + words + '</div>' +
        (L(slide.line) ? '<div class="rv-line anim-body">' + L(slide.line) + '</div>' : '') +
        '<div class="rv-rows">' + rows + '</div>' +
        '</div>';
    },

    // ASSISTANT: screenshot wide, two logos, one line
    'assistant': function (slide, L, esc) {
      var logos = (slide.logos || []).map(function (l) { return '<span class="as-logo"><img src="' + l.src + '" alt="' + esc(l.alt || '') + '"' + (l.h ? ' style="height:' + l.h + 'px"' : '') + '/></span>'; }).join('<span class="as-plus">+</span>');
      var pts = (slide.points || []).map(function (x) { return '<span class="as-pt anim-item">' + L(x) + '</span>'; }).join('');
      return '<div class="pad pad-top" style="padding:50px 64px 30px;">' +
        '<div style="display:flex;align-items:flex-end;justify-content:space-between;gap:24px;">' +
          '<div>' + (L(slide.kicker) ? '<div class="kicker anim-kicker">' + esc(L(slide.kicker)) + '</div>' : '') + '<h2 class="title anim-title" style="margin-bottom:0">' + L(slide.title) + '</h2></div>' +
          '<div class="as-logos anim-pop">' + logos + '</div>' +
        '</div>' +
        '<div class="wideshot as-shot" style="margin-top:14px;"><img src="' + slide.image + '" alt=""/></div>' +
        (pts ? '<div class="as-pts">' + pts + '</div>' : '') +
        '</div>';
    },

    // LIVE BOARD: a live page (the lci-workbench flow chart) rendered at its natural size and scaled to fill the slide;
    // a hi-res PNG sits behind it until the frame loads (and stays if it never does). embed:true keeps it clickable.
    'live-board': function (slide, L, esc) {
      var W = slide.renderW || 1280, H = slide.renderH || 1124, s = slide.scale || 0.8;
      var top = slide.titleBand ? 78 : 0;
      var bx = slide.boardX || 0, by = slide.boardY || 0, bw = slide.boardW || W, bh = slide.boardH || H;   // the board's box inside the page
      var ox = (1280 - bw * s) / 2 - bx * s, oy = top + (720 - top - bh * s) / 2 - by * s;
      var band = slide.titleBand ? '<div class="lb-band">' + (L(slide.kicker) ? '<div class="kicker anim-kicker" style="margin:0 0 2px">' + esc(L(slide.kicker)) + '</div>' : '') + '<h2 class="title anim-title" style="margin:0;font-size:34px">' + L(slide.title) + '</h2></div>' : '';
      var fb = slide.image ? '<img class="lb-fallback" src="' + slide.image + '" alt="" style="left:' + (ox + bx * s).toFixed(1) + 'px;top:' + (oy + by * s).toFixed(1) + 'px;width:' + (bw * s).toFixed(1) + 'px;height:' + (bh * s).toFixed(1) + 'px;"/>' : '';
      // clip to the board's box so the page's own padding and chrome (e.g. the "All tributaries" chip) stay outside
      var clip = '<div class="lb-clip" style="left:' + (ox + bx * s).toFixed(1) + 'px;top:' + (oy + by * s).toFixed(1) + 'px;width:' + (bw * s).toFixed(1) + 'px;height:' + (bh * s).toFixed(1) + 'px;">' +
        '<iframe id="flit-frame-lb" class="lb-frame" src="' + slide.embedUrl + '" title="" loading="eager" referrerpolicy="no-referrer" scrolling="no" sandbox="allow-scripts allow-same-origin allow-popups" style="width:' + W + 'px;height:' + H + 'px;transform:translate(' + (-bx * s).toFixed(1) + 'px,' + (-by * s).toFixed(1) + 'px) scale(' + s + ');"></iframe></div>';
      return '<div class="lb-stage nofit">' + band + fb + clip +
        (L(slide.footnote) ? '<div class="lb-foot">' + L(slide.footnote) + '</div>' : '') +
        '</div>';
    },

    // CHAT MOCK: the assistant drawer (left) + the MCP tool groups and facts (right)
    'chat-mock': function (slide, L, esc) {
      var msgs = (slide.chat || []).map(function (m) {
        var tools = (m.tools || []).map(function (t) { return '<span class="cm-tool">⚙ ' + esc(t) + '</span>'; }).join('');
        return '<div class="cm-msg cm-' + m.who + ' anim-item">' + (tools ? '<div class="cm-tools">' + tools + '</div>' : '') + '<div class="cm-bubble">' + L(m.text) + '</div></div>';
      }).join('');
      var drawer = '<div class="cm-drawer anim-pop">' +
        '<div class="cm-head"><span>✦ Assistant</span><span class="cm-kbd">⌘J</span></div>' +
        '<div class="cm-body">' + msgs + '</div>' +
        '<div class="cm-input"><span>Ask about the open project …</span><span class="cm-send">↑</span></div>' +
      '</div>';
      var groups = (slide.toolGroups || []).map(function (g) {
        return '<div class="tgroup"><div class="tgroup-h">' + L(g.head) + '</div><div class="tpills">' + (g.items || []).map(function (x) { return '<span class="tpill anim-flow">' + L(x) + '</span>'; }).join('') + '</div></div>';
      }).join('');
      var facts = (slide.facts || []).map(function (f) { return '<div class="bullet anim-item bullet-static"><span class="tick">✓</span><span>' + L(f) + '</span></div>'; }).join('');
      return '<div class="pad pad-top" style="padding:54px 64px 34px;">' + head(slide, L, esc) +
        '<div style="display:flex;gap:36px;align-items:flex-start;flex:1;min-height:0;margin-top:6px;">' +
          '<div style="flex:0 0 470px;">' + drawer + '</div>' +
          '<div style="flex:1;display:flex;flex-direction:column;gap:10px;">' +
            '<div class="grouphead">Brightway MCP · tools</div><div class="tgroups">' + groups + '</div>' +
            '<div style="display:flex;flex-direction:column;gap:6px;margin-top:4px;">' + facts + '</div>' +
          '</div>' +
        '</div>' + foot(slide, L) + '</div>';
    },

    // 2 — MOSAIC: ~600 tiles flood in, settle into A–E proportioned bands, 100k overlaid
    mosaic: function (slide, L, esc) {
      var COLS = 30, ROWS = 12, N = COLS * ROWS; // 360 tiles — fewer = smoother flood
      // A–E proportions (realistic-ish skew toward B/C)
      var props = [0.18, 0.30, 0.27, 0.16, 0.09], bandcol = ['#43A047', '#8BC34A', '#FFC107', '#FF9800', '#E53935'];
      var cum = [], acc = 0; props.forEach(function (p) { acc += p; cum.push(acc); });
      var tiles = '';
      for (var i = 0; i < N; i++) {
        var f = i / N, bi = 0; while (bi < 4 && f > cum[bi]) bi++;
        tiles += '<span class="mtile" style="background:' + bandcol[bi] + '"></span>';
      }
      var overlayPills = (slide.pills || []).map(function (p) { return '<span class="ov-pill anim-pop">✓ ' + L(p) + '</span>'; }).join('');
      return '<div class="pad" style="padding:40px 64px;">' +
        '<div style="display:flex;align-items:flex-end;justify-content:space-between;gap:24px;">' +
          '<div>' + head(slide, L, esc, { titleStyle: 'margin-bottom:4px;' }) + '</div>' +
          (L(slide.kicker2) ? '<span class="kicker" style="margin-bottom:10px;">' + esc(L(slide.kicker2)) + '</span>' : '') +
        '</div>' +
        '<div class="mosaic-wrap"><div class="mosaic" style="grid-template-columns:repeat(' + COLS + ',1fr);">' + tiles + '</div>' +
          '<div class="mosaic-overlay"><div class="mosaic-num"><span data-count="100000" data-num="1">0</span></div>' +
          '<div class="mosaic-pills">' + overlayPills + '</div></div>' +
        '</div>' + foot(slide, L) +
        '</div>';
    },

    // 3 — PHONE SPLIT: numbered steps left, phone with rating + confidence bar right
    'phone-split': function (slide, L, esc) {
      var steps = (slide.steps || []).map(function (s, i) {
        return '<div class="numstep anim-item"><span class="numdot">' + (i + 1) + '</span><div><div class="ns-t">' + L(s.title) + '</div><div class="ns-d">' + L(s.desc) + '</div></div></div>';
      }).join('');
      var p = slide.phone || {};
      // Live-app phone: an iframe of the real Flit app inside the phone screen, with a
      // static product card as fallback until the iframe loads (same pattern as `close`).
      var phoneInner = slide.live
        ? '<div class="screen">' +
            '<span class="flit-badge" id="flit-badge-3">…</span>' +
            '<div id="flit-fallback-3" class="phone-card" style="position:absolute;inset:0;z-index:3;background:#fff;">' +
              '<div class="pc-name">' + (L(p.name) || '') + '</div>' +
              '<div class="band band-' + (p.band || 'b') + ' pc-band">' + (p.band ? p.band.toUpperCase() : 'B') + '</div>' +
              '<div class="pc-co2"><span data-count="' + (p.co2 || 1.9) + '" data-dec="1">0</span> ' + (L(p.co2unit) || 'kg CO₂e') + '</div>' +
              '<div class="pc-conflbl">' + (L(p.confLabel) || 'Confidence') + '</div>' +
              '<div class="confbar"><div class="conffill" data-fill="' + (p.conf || 82) + '"></div></div>' +
              '<div class="pc-confval"><span data-count="' + (p.conf || 82) + '">0</span>%</div>' +
            '</div>' +
            // Render the app at a fixed mobile resolution (390px wide) and scale it to fit the
            // screen, so the app's own layout/breakpoint decides how it looks — independent of the
            // phone-frame size. screen ≈ 246×536 logical; 246/390 ≈ 0.631 → iframe 390×850.
            '<iframe id="flit-frame-3" src="' + (window.DECK.flitUrl || 'https://flit.eaternity.org') + '" title="Flit" loading="eager" referrerpolicy="no-referrer" sandbox="allow-scripts allow-same-origin allow-forms allow-popups" style="position:absolute;top:0;left:0;width:' + (slide.phoneWidth || 390) + 'px;height:' + Math.round(536 / (246 / (slide.phoneWidth || 390))) + 'px;border:0;background:#fff;opacity:0;transition:opacity .4s;z-index:2;transform:scale(' + (246 / (slide.phoneWidth || 390)).toFixed(4) + ');transform-origin:top left;"></iframe>' +
          '</div>'
        : '<div class="screen phone-card">' +
            '<div class="pc-name">' + (L(p.name) || '') + '</div>' +
            '<div class="band band-' + (p.band || 'b') + ' pc-band">' + (p.band ? p.band.toUpperCase() : 'B') + '</div>' +
            '<div class="pc-co2"><span data-count="' + (p.co2 || 1.9) + '" data-dec="1">0</span> ' + (L(p.co2unit) || 'kg CO₂e') + '</div>' +
            '<div class="pc-conflbl">' + (L(p.confLabel) || 'Confidence') + '</div>' +
            '<div class="confbar"><div class="conffill" data-fill="' + (p.conf || 82) + '"></div></div>' +
            '<div class="pc-confval"><span data-count="' + (p.conf || 82) + '">0</span>%</div>' +
          '</div>';
      // Title + steps BOTH on the right so the app gets the full slide height on the left.
      return '<div class="pad pad-top" style="padding:48px 72px 36px;">' +
        '<div style="display:flex;gap:64px;align-items:center;flex:1;">' +
          // LEFT: live app embed, angled toward the viewer (full height)
          '<div class="phone-stage anim-pop" style="flex:0 0 360px;">' +
            '<div class="phone phone-angled">' + phoneInner + '</div>' +
          '</div>' +
          // RIGHT: title/body, then numbered steps + url chip
          '<div style="flex:1;">' + head(slide, L, esc) + steps +
            (L(slide.urlChip) ? '<div class="urlchip anim-item">' + L(slide.urlChip) + '</div>' : '') +
          '</div>' +
        '</div>' + foot(slide, L) +
        '</div>';
    },

    // 4 — FORMULA + DISTRIBUTION CURVE (manual path draw, neutral % illustration)
    'formula-curve': function (slide, L, esc) {
      var svg =
        '<svg viewBox="0 0 460 300" width="100%" height="300" preserveAspectRatio="xMidYMid meet">' +
          '<rect class="fc-band anim-pop" x="150" y="30" width="160" height="210" fill="#46CC00" opacity="0.16"/>' +
          '<line class="fc-bound" x1="150" y1="30" x2="150" y2="240" stroke="#16a34a" stroke-width="2" stroke-dasharray="5 5"/>' +
          '<line class="fc-bound" x1="310" y1="30" x2="310" y2="240" stroke="#16a34a" stroke-width="2" stroke-dasharray="5 5"/>' +
          '<line x1="30" y1="240" x2="430" y2="240" stroke="#999" stroke-width="1.5"/>' +
          '<path class="fc-fill" d="M150,240 C175,180 200,95 230,95 C260,95 285,180 310,240 Z" fill="#16a34a" opacity="0.22"/>' +
          '<path class="fc-curve draw-path" d="M30,240 C120,240 150,70 230,70 C310,70 340,240 430,240" fill="none" stroke="#16a34a" stroke-width="4"/>' +
          '<line class="fc-point" x1="230" y1="62" x2="230" y2="240" stroke="#083118" stroke-width="3"/>' +
          '<circle class="fc-point" cx="230" cy="62" r="7" fill="#083118"/>' +
          '<text class="fc-lab" x="230" y="22" text-anchor="middle" font-size="15" font-weight="700" fill="#16a34a">' + (L(slide.bandLabel) || 'tolerance band') + '</text>' +
          '<text class="fc-lab" x="230" y="266" text-anchor="middle" font-size="14" fill="#666">' + (L(slide.axisLabel) || 'prediction') + '</text>' +
        '</svg>';
      var ghost = L(slide.withheldLabel) ? '<div class="withheld-tag anim-pop">' + L(slide.withheldLabel) + '</div>' : '';
      return '<div class="pad" style="padding:54px 72px;">' +
        '<div style="display:flex;gap:56px;align-items:center;flex:1;">' +
          '<div style="flex:0 0 460px;text-align:center;">' + svg + ghost +
            '<div class="fc-cap">' + (L(slide.caption) || '') + '</div></div>' +
          '<div style="flex:1;">' + head(slide, L, esc) +
            (L(slide.callout) ? '<div class="callout anim-item">' + L(slide.callout) + '</div>' : '') +
          '</div>' +
        '</div>' + foot(slide, L) +
        '</div>';
    },

    // 5 — STEP FLOW with a formula callout on top
    'step-flow': function (slide, L, esc) {
      var formula = L(slide.formula) ? '<div class="formula-box anim-pop">' + L(slide.formula) + (L(slide.formulaSub) ? '<span class="fb-sub">' + L(slide.formulaSub) + '</span>' : '') + '</div>' : '';
      var steps = (slide.steps || []).map(function (s, i) {
        var arrow = i > 0 ? '<div class="flowarrow anim-arrow">→</div>' : '';
        return arrow + '<div class="stepcard anim-flow"><span class="numdot">' + (i + 1) + '</span><div class="sc-t">' + L(s.title) + '</div><div class="sc-d">' + L(s.desc) + '</div></div>';
      }).join('');
      return '<div class="pad" style="align-items:center;text-align:center;">' +
        head(slide, L, esc) + formula +
        '<div class="flowrow" style="margin-top:18px;width:100%;">' + steps + '</div>' +
        foot(slide, L) + '</div>';
    },

    // 6 — OPEN STACK + unlocking padlock + standards badges
    'open-stack': function (slide, L, esc) {
      var layers = (slide.layers || []).map(function (l) {
        return '<div class="openlayer anim-item"><div class="ol-t">' + L(l.title) + '</div><span class="ol-chip">' + L(l.chip) + '</span><div class="ol-sub">' + L(l.sub) + '</div></div>';
      }).join('');
      var badges = (slide.standards || []).map(function (s) { return '<span class="stdbadge anim-pop"><span class="tick">✓</span>' + L(s) + '</span>'; }).join('');
      var lock =
        '<svg viewBox="0 0 120 140" width="120" height="140">' +
          '<path class="lock-shackle" d="M35,62 V44 a25,25 0 0 1 50,0 V62" fill="none" stroke="#16a34a" stroke-width="9" stroke-linecap="round"/>' +
          '<rect class="lock-body anim-pop" x="26" y="60" width="68" height="56" rx="10" fill="#083118"/>' +
          '<circle cx="60" cy="84" r="7" fill="#46CC00"/><rect x="57" y="88" width="6" height="16" rx="3" fill="#46CC00"/>' +
        '</svg>';
      return '<div class="pad" style="padding:54px 72px;">' +
        '<div style="display:flex;gap:56px;align-items:center;flex:1;">' +
          '<div style="flex:1;">' + head(slide, L, esc) +
            '<div style="display:flex;flex-direction:column;gap:12px;margin-top:8px;">' + layers + '</div></div>' +
          '<div style="flex:0 0 320px;display:flex;flex-direction:column;align-items:center;gap:18px;">' + lock +
            '<div class="stdrow">' + badges + '</div></div>' +
        '</div>' + foot(slide, L) + '</div>';
    },

    // 7 — PARTNER CARDS with logo + role + stat chips + funding strip
    'partner-cards': function (slide, L, esc) {
      var cards = (slide.partners || []).map(function (p) {
        var chips = (p.chips || []).map(function (c) { return '<span class="pc-stat">' + L(c) + '</span>'; }).join('');
        var logo = p.logo ? '<div class="pcd-logobox"><img src="' + p.logo + '" alt="' + (L(p.name) || '') + '"/></div>'
                          : '<div class="pcd-logo">' + (L(p.name) || '') + '</div>';
        return '<div class="partnercard anim-item">' + logo + '<div class="pcd-role">' + L(p.role) + '</div><div class="pcd-chips">' + chips + '</div></div>';
      }).join('');
      var fundLogos = (slide.fundLogos || []).map(function (f) { return '<img class="fundlogo" src="' + f + '" alt="funding"/>'; }).join('');
      // Funding strip: logos + grant text only (one tidy row). Phase-2 note rendered as its own
      // quiet line below so nothing is crammed into one row / pushed off the slide edge.
      var fund = (L(slide.fund) || fundLogos)
        ? '<div class="fundstrip anim-foot">' + fundLogos + '<span class="fund-txt">' + (L(slide.fund) || '') + '</span></div>'
        : '';
      var phase2 = L(slide.phase2) ? '<div class="phase2line anim-foot"><span class="phase2pill">' + L(slide.phase2) + '</span></div>' : '';
      return '<div class="pad pad-top" style="padding:58px 72px 36px;">' +
        head(slide, L, esc) +
        '<div style="display:flex;gap:18px;margin-top:8px;">' + cards + '</div>' +
        fund + phase2 +
        foot(slide, L) + '</div>';
    },

    // 8 — SWAP + FUNNEL: locked ecoinvent → open BAFU, funnel to match stats
    'swap-funnel': function (slide, L, esc) {
      var d = slide.swap || {};
      var stats = (slide.stats || []).map(function (s) { return '<div class="funnel-stat anim-pop"><div class="fs-num">' + L(s.num) + '</div><div class="fs-lbl">' + L(s.label) + '</div></div>'; }).join('<div class="flowarrow anim-arrow">→</div>');
      return '<div class="pad" style="padding:54px 72px;">' +
        head(slide, L, esc) +
        '<div style="display:flex;align-items:center;gap:20px;margin:18px 0 8px;">' +
          '<div class="swapbox locked anim-item">🔒 ' + (L(d.from) || 'ecoinvent') + '<span class="sb-sub">' + (L(d.fromSub) || 'proprietary') + '</span></div>' +
          '<div class="swaparrow anim-arrow">⇒</div>' +
          '<div class="swapbox open anim-item">✓ ' + (L(d.to) || 'BAFU/UVEK') + '<span class="sb-sub">' + (L(d.toSub) || 'official, open') + '</span></div>' +
        '</div>' +
        '<div class="funnelrow">' + stats + '</div>' +
        foot(slide, L) + '</div>';
    },

    // 9 — DATA TABLE (scientific, with weight bars / totals)
    'data-table': function (slide, L, esc) {
      var t = slide.table || {};
      var thead = '<tr>' + (t.cols || []).map(function (c) { return '<th>' + L(c) + '</th>'; }).join('') + '</tr>';
      var rows = (t.rows || []).map(function (r) {
        var cls = r.total ? ' class="trow-total anim-item"' : ' class="anim-item"';
        var cells = r.cells.map(function (c, ci) {
          if (c && c.bar != null) return '<td><div class="wbar"><span style="width:' + c.bar + '%"></span></div>' + L(c.label) + '</td>';
          return '<td' + (ci === 0 ? ' class="td-first"' : '') + '>' + L(c) + '</td>';
        }).join('');
        return '<tr' + cls + '>' + cells + '</tr>';
      }).join('');
      return '<div class="pad pad-top" style="padding:58px 72px 36px;">' +
        head(slide, L, esc) +
        '<table class="sci-table" style="margin-top:10px;"><thead>' + thead + '</thead><tbody>' + rows + '</tbody></table>' +
        foot(slide, L) + '</div>';
    },

    // 10 — REGISTRY TRIANGULATION: 3 disks → fixed dot cloud, count overlays
    'registry-triangulation': function (slide, L, esc) {
      var r = slide.registries || [];
      var disks =
        '<circle class="tri-disk anim-pop" cx="150" cy="120" r="86" fill="#16a34a" opacity="0.30"/>' +
        '<circle class="tri-disk anim-pop" cx="250" cy="120" r="86" fill="#46CC00" opacity="0.30"/>' +
        '<circle class="tri-disk anim-pop" cx="200" cy="200" r="86" fill="#8BC34A" opacity="0.30"/>';
      // a small fixed decorative dot cloud
      var dots = '';
      var seed = 7;
      for (var i = 0; i < 54; i++) { seed = (seed * 9301 + 49297) % 233280; var rx = seed / 233280; seed = (seed * 9301 + 49297) % 233280; var ry = seed / 233280; var cx = 60 + rx * 280, cy = 40 + ry * 240; dots += '<circle class="tri-dot" cx="' + cx.toFixed(0) + '" cy="' + cy.toFixed(0) + '" r="2.4" fill="#083118" opacity="0.55"/>'; }
      var labels = r.map(function (x, i) { var pos = [[150, 116], [250, 116], [200, 206]][i] || [200, 160]; return '<text x="' + pos[0] + '" y="' + pos[1] + '" text-anchor="middle" font-size="13" font-weight="800" fill="#083118">' + L(x.name) + '</text><text x="' + pos[0] + '" y="' + (pos[1] + 16) + '" text-anchor="middle" font-size="12" fill="#0a5">' + L(x.count) + '</text>'; }).join('');
      var svg = '<svg viewBox="0 0 400 300" width="100%" height="320">' + disks + '<g class="tri-cloud" opacity="0">' + dots + '</g><g class="anim-pop">' + labels + '</g></svg>';
      var resultStats = (slide.results || []).map(function (s) { return '<div class="bigfig anim-pop"><div class="bf-num"><span data-count="' + s.n + '">0</span></div><div class="bf-lbl">' + L(s.label) + '</div></div>'; }).join('');
      return '<div class="pad pad-top" style="padding:58px 72px 36px;">' +
        '<div style="display:flex;gap:48px;align-items:center;flex:1;">' +
          '<div style="flex:0 0 420px;">' + svg + '</div>' +
          '<div style="flex:1;">' + head(slide, L, esc) +
            '<div style="display:flex;gap:22px;margin-top:14px;flex-wrap:wrap;">' + resultStats + '</div>' +
            (L(slide.callout) ? '<div class="callout anim-item" style="margin-top:18px;">' + L(slide.callout) + '</div>' : '') +
          '</div>' +
        '</div>' + foot(slide, L) + '</div>';
    },

    // 11 — BIGSTAT split: large figure + supporting note (locale-aware count-up)
    bigstat: function (slide, L, esc) {
      var figs = (slide.figures || []).map(function (f) { return '<div class="bigfig anim-pop"><div class="bf-num"><span data-count="' + f.n + '">0</span>' + (L(f.suffix) || '') + '</div><div class="bf-lbl">' + L(f.label) + '</div></div>'; }).join('');
      var items = (slide.items || []).map(function (it) { return '<div class="bullet anim-item bullet-static"><span class="tick">✓</span><span>' + L(it) + '</span></div>'; }).join('');
      return '<div class="pad" style="padding:54px 72px;">' +
        '<div style="display:flex;gap:56px;align-items:center;flex:1;">' +
          '<div style="flex:0 0 380px;display:flex;flex-direction:column;gap:24px;">' + figs + '</div>' +
          '<div style="flex:1;display:flex;flex-direction:column;justify-content:center;">' + head(slide, L, esc) +
            '<div style="display:flex;flex-direction:column;gap:12px;margin-top:6px;">' + items + '</div>' +
          '</div>' +
        '</div>' + foot(slide, L) + '</div>';
    },

    // 12 — NODE PIPELINE: left→right chain + OPEN-standard source ribbon
    'node-pipeline': function (slide, L, esc) {
      var nodes = (slide.nodes || []).map(function (n, i) {
        var arrow = i > 0 ? '<div class="pl-arrow anim-arrow">→</div>' : '';
        return arrow + '<div class="plnode anim-flow">' + L(n) + '</div>';
      }).join('');
      var srcs = (slide.sources || []).map(function (s) { return '<span class="srcpill anim-pop">' + L(s) + '</span>'; }).join('');
      return '<div class="pad" style="padding:50px 64px;">' +
        head(slide, L, esc) +
        '<div class="pipelinewrap">' + nodes + '</div>' +
        (srcs ? '<div class="srcribbon"><span class="sr-lbl">' + (L(slide.sourceLabel) || 'Sources') + '</span>' + srcs + '</div>' : '') +
        foot(slide, L) + '</div>';
    },

    // 13 — RANGE BAR: single value with literature bracket + dataset tag
    'range-bar': function (slide, L, esc) {
      var v = slide.range || {};
      // scale: 0..max across 100%
      var max = v.max || 8, val = v.val || 5.2, lo = v.lo || 4, hi = v.hi || 6.5;
      var pVal = (val / max * 100).toFixed(1), pLo = (lo / max * 100).toFixed(1), pHi = (hi / max * 100).toFixed(1);
      var svg = '<div class="rangebar-wrap">' +
        '<div class="rb-track">' +
          '<div class="rb-bracket anim-grow" style="left:' + pLo + '%;width:' + (pHi - pLo) + '%;"></div>' +
          '<div class="rb-fill anim-grow" style="width:' + pVal + '%;"></div>' +
          '<div class="rb-marker" style="left:' + pVal + '%;"><div class="rb-val">' + (L(v.valLabel) || val) + '</div></div>' +
        '</div>' +
        '<div class="rb-axis"><span>0</span><span>' + (L(v.bracketLabel) || ('bracket ' + lo + '–' + hi)) + '</span><span>' + max + '</span></div>' +
      '</div>';
      return '<div class="pad" style="padding:54px 72px;">' +
        '<div style="display:flex;gap:56px;align-items:center;flex:1;">' +
          '<div style="flex:1;">' + head(slide, L, esc) +
            (L(slide.tag) ? '<div class="callout anim-item">' + L(slide.tag) + '</div>' : '') + '</div>' +
          '<div style="flex:0 0 480px;">' + svg + '</div>' +
        '</div>' + foot(slide, L) + '</div>';
    },

    // 14 — CALC STACK: the multiplicative chain → dominant term
    'calc-stack': function (slide, L, esc) {
      var terms = (slide.terms || []).map(function (t) { return '<div class="calc-term anim-item"><span class="ct-op">' + (L(t.op) || '') + '</span><span class="ct-val">' + L(t.val) + '</span><span class="ct-lbl">' + L(t.label) + '</span></div>'; }).join('');
      var res = slide.result || {};
      return '<div class="pad" style="padding:54px 72px;">' +
        '<div style="display:flex;gap:56px;align-items:center;flex:1;">' +
          '<div style="flex:1;">' + head(slide, L, esc) +
            (L(slide.badge) ? '<div class="dom-badge anim-pop">' + L(slide.badge) + '</div>' : '') + '</div>' +
          '<div style="flex:0 0 440px;" class="calc-wrap">' + terms +
            '<div class="calc-result anim-pop"><span class="cr-eq">=</span><span class="cr-val">' + L(res.val) + '</span><span class="cr-lbl">' + L(res.label) + '</span></div>' +
          '</div>' +
        '</div>' + foot(slide, L) + '</div>';
    },

    // 15 — STACKED BAR: accumulating contributions to a total. Labels live in a side legend
    // (not inside the segments) so even a thin 1% slice stays legible.
    'stacked-bar': function (slide, L, esc) {
      var segs = slide.segments || [], total = slide.total || {};
      var max = total.max || 12;
      var bars = segs.map(function (s) {
        var hpct = (s.value / max * 100).toFixed(1);
        return '<div class="stk-seg" style="height:' + hpct + '%;background:' + (s.color || '#16a34a') + ';"></div>';
      }).join('');
      var legend = segs.slice().reverse().map(function (s) {
        return '<div class="stk-leg anim-item"><span class="stk-dot" style="background:' + (s.color || '#16a34a') + '"></span><span class="stk-leg-lbl">' + L(s.label) + '</span><b class="stk-leg-val">' + L(s.disp) + '</b></div>';
      }).join('');
      return '<div class="pad pad-top" style="padding:58px 72px 36px;">' +
        '<div style="display:flex;gap:40px;align-items:center;flex:1;">' +
          '<div style="flex:0 0 260px;display:flex;align-items:flex-end;gap:14px;height:340px;">' +
            '<div class="stacked-col">' + bars + '</div>' +
            '<div class="stk-total"><div class="stk-tnum">' + L(total.disp) + '</div><div class="stk-tlbl">' + L(total.label) + '</div></div>' +
          '</div>' +
          '<div style="flex:0 0 230px;display:flex;flex-direction:column;gap:9px;">' + legend + '</div>' +
          '<div style="flex:1;">' + head(slide, L, esc) +
            (L(slide.callout) ? '<div class="callout anim-item">' + L(slide.callout) + '</div>' : '') + '</div>' +
        '</div>' + foot(slide, L) + '</div>';
    },

    // 16 — WET vs DRY bars, ~3× divergence, "one global number" ghost line (no fake value)
    'wet-dry-bars': function (slide, L, esc) {
      var w = slide.wet || {}, d = slide.dry || {}, max = slide.barMax || 8;
      var hw = (w.value / max * 100).toFixed(0), hd = (d.value / max * 100).toFixed(0);
      // ghost line: if a numeric ghostValue is given, place it at the correct height (value/max);
      // otherwise omit it (a vague "global average" line at a fixed height misleads when the
      // label states a concrete number). Render the line only when there is something to anchor.
      var ghost = '';
      if (L(slide.ghostLabel)) {
        var gv = (typeof slide.ghostValue === 'number') ? slide.ghostValue : null;
        if (gv != null) {
          var gpct = Math.max(0, Math.min(100, gv / max * 100)).toFixed(1);
          ghost = '<div class="wd-ghost" style="top:auto;bottom:' + gpct + '%;"><span>' + L(slide.ghostLabel) + '</span></div>';
        }
        // if no ghostValue, we deliberately drop the line — the label alone (if needed) belongs in the callout
      }
      var svg = '<div class="wd-wrap">' +
        '<div class="wd-col"><div class="wd-bar" style="height:' + hw + '%;background:#16a34a;"><span class="wd-v">' + L(w.disp) + '</span></div><div class="wd-lbl">' + L(w.label) + '</div></div>' +
        '<div class="wd-col"><div class="wd-bar" style="height:' + hd + '%;background:#FF9800;"><span class="wd-v">' + L(d.disp) + '</span></div><div class="wd-lbl">' + L(d.label) + '</div></div>' +
        ghost +
        '<div class="wd-ratio anim-pop">' + (L(slide.ratio) || '≈ 3×') + '</div>' +
      '</div>';
      return '<div class="pad" style="align-items:center;text-align:center;padding:48px 72px;">' +
        head(slide, L, esc) +
        '<div style="display:flex;gap:64px;align-items:center;justify-content:center;flex:1;width:100%;">' +
          '<div style="flex:0 0 420px;">' + svg + '</div>' +
          (L(slide.callout) ? '<div style="flex:1;max-width:460px;text-align:left;"><div class="callout anim-item">' + L(slide.callout) + '</div></div>' : '') +
        '</div>' + foot(slide, L) + '</div>';
    },

    // 17 — BLACK BOX vs OPEN: two opaque boxes → one open base
    'blackbox-vs-open': function (slide, L, esc) {
      var boxes = (slide.boxes || []).map(function (b) { return '<div class="bbox anim-item"><div class="bb-q">?</div><div class="bb-t">' + L(b.title) + '</div><div class="bb-s">' + L(b.sub) + '</div></div>'; }).join('');
      var open = slide.open || {};
      var openBullets = (open.bullets || []).map(function (x) { return '<div class="ob-item anim-pop"><span class="tick">✓</span>' + L(x) + '</div>'; }).join('');
      return '<div class="pad" style="padding:50px 72px;">' +
        head(slide, L, esc) +
        '<div style="display:flex;gap:40px;align-items:stretch;flex:1;margin-top:8px;">' +
          '<div style="flex:0 0 380px;"><div class="bb-head">' + (L(slide.todayLabel) || 'Today') + '</div><div style="display:flex;flex-direction:column;gap:14px;">' + boxes + '</div></div>' +
          '<div class="vs-arrow anim-arrow">→</div>' +
          '<div style="flex:1;"><div class="ob-head">' + (L(open.title) || 'One open base') + '</div><div class="openbase">' + openBullets + '</div></div>' +
        '</div>' + foot(slide, L) + '</div>';
    },

    // 18 — CLOSE: QR + live Flit phone + contacts
    close: function (slide, L, esc) {
      return '<div class="closewrap">' +
        '<div style="flex:1;">' +
          (L(slide.kicker) ? '<div class="kicker anim-kicker">' + esc(L(slide.kicker)) + '</div>' : '') +
          '<h1 class="anim-title" style="font:800 50px/1.05 system-ui;color:var(--green-950);letter-spacing:-1px;margin:8px 0 0;">' + L(slide.title) + '</h1>' +
          (L(slide.body) ? '<p class="anim-body" style="font:400 21px/1.4 system-ui;color:var(--muted);margin:18px 0 26px;max-width:520px;">' + L(slide.body) + '</p>' : '') +
          '<div style="display:flex;align-items:center;gap:22px;">' +
            '<div class="qrbox anim-pop"><div id="qr-target" style="width:100%;height:100%;"></div></div>' +
            '<div class="anim-item">' +
              '<div style="font:700 16px system-ui;color:var(--green-950);">' + (L(slide.urlLabel) || 'flit.eaternity.org') + '</div>' +
              ((slide.contacts || []).map(function (c) { return '<div style="font:500 15px system-ui;color:var(--muted);margin-top:8px;"><span class="tick" style="color:var(--lime);">✓</span> ' + L(c) + '</div>'; }).join('')) +
            '</div>' +
          '</div>' +
        '</div>' +
        (slide.noPhone ? '' : '<div class="phone anim-pop" style="flex:none;"><div class="screen">' +
          '<div id="flit-fallback" style="position:absolute;inset:0;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:14px;background:var(--bg-soft);z-index:3;">' +
            '<div style="font:800 22px system-ui;color:var(--green-950);">Flit</div><div class="band band-b">B</div>' +
            '<div style="font:600 15px system-ui;color:var(--muted);text-align:center;padding:0 24px;">' + (L(slide.phoneCaption) || '') + '</div></div>' +
          // render at fixed mobile resolution (390px) and scale to fit, like slide 3
          '<iframe id="flit-frame" src="' + (window.DECK.flitUrl || 'https://flit.eaternity.org') + '" title="Flit" loading="eager" referrerpolicy="no-referrer" sandbox="allow-scripts allow-same-origin allow-forms allow-popups" style="position:absolute;top:0;left:0;width:390px;height:850px;border:0;background:#fff;opacity:0;transition:opacity .4s;z-index:2;transform:scale(0.631);transform-origin:top left;"></iframe>' +
        '</div></div>') +
      '</div>';
    }
  };
})();
