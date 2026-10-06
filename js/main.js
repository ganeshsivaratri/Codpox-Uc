/* CodPox — vanilla JS, no dependencies */
(function () {
  'use strict';
  var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  /* ---------- mobile menu ---------- */
  var burger = document.querySelector('.burger');
  var menu = document.getElementById('menu');
  if (burger && menu) {
    burger.addEventListener('click', function () {
      var open = menu.classList.toggle('open');
      burger.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
  }

  /* ---------- the spore: a small 3D node cluster drawn on canvas ---------- */
  var cv = document.querySelector('[data-spore]');
  if (cv) {
    var ctx = cv.getContext('2d');
    var W = 0, H = 0, S = 0, dpr = 1;
    var seed = 7;
    function rnd() { seed = (seed * 16807) % 2147483647; return (seed - 1) / 2147483646; }

    var N = 58, pts = [];
    for (var i = 0; i < N; i++) {
      var y = 1 - (i / (N - 1)) * 2;
      var r = Math.sqrt(1 - y * y);
      var th = i * 2.399963;
      var rad = 0.8 + rnd() * 0.2;
      pts.push({ x: Math.cos(th) * r * rad, y: y * rad, z: Math.sin(th) * r * rad, s: 0.55 + rnd() * 0.85, ink: rnd() < 0.13 });
    }
    pts.push({ x: 0, y: 0, z: 0, s: 2.7, core: true });

    var links = [];
    for (var a = 0; a < pts.length; a++) {
      for (var b = a + 1; b < pts.length; b++) {
        var dx = pts[a].x - pts[b].x, dy = pts[a].y - pts[b].y, dz = pts[a].z - pts[b].z;
        if (dx * dx + dy * dy + dz * dz < 0.34 && !pts[a].core && !pts[b].core) links.push([a, b]);
      }
    }

    var ay = 0, ax = -0.25, tx = -0.25, ty = 0, visible = true, dragging = false, lastX = 0, lastY = 0, spin = 0.0035;

    function resize() {
      var rect = cv.getBoundingClientRect();
      dpr = Math.min(window.devicePixelRatio || 1, 2);
      W = rect.width; H = rect.height; S = Math.min(W, H);
      cv.width = Math.round(W * dpr); cv.height = Math.round(H * dpr);
      ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
      if (reduce) draw();
    }

    function project(p, cy, sy, cx, sx) {
      var x1 = p.x * cy + p.z * sy;
      var z1 = -p.x * sy + p.z * cy;
      var y2 = p.y * cx - z1 * sx;
      var z2 = p.y * sx + z1 * cx;
      var f = 3.2 / (3.2 - z2);
      return { X: W / 2 + x1 * S * 0.36 * f, Y: H / 2 + y2 * S * 0.36 * f, z: z2, f: f };
    }

    function draw() {
      ctx.clearRect(0, 0, W, H);
      var cy = Math.cos(ay), sy = Math.sin(ay), cx = Math.cos(ax), sx = Math.sin(ax);
      var P = pts.map(function (p) { var q = project(p, cy, sy, cx, sx); q.p = p; return q; });

      // ground shadow
      var g = ctx.createRadialGradient(W / 2, H * 0.9, 0, W / 2, H * 0.9, S * 0.3);
      g.addColorStop(0, 'rgba(21,24,27,.16)'); g.addColorStop(1, 'rgba(21,24,27,0)');
      ctx.save(); ctx.translate(0, 0); ctx.scale(1, 0.28); ctx.translate(0, H * 0.9 * (1 / 0.28 - 1));
      ctx.fillStyle = g; ctx.beginPath(); ctx.arc(W / 2, H * 0.9, S * 0.3, 0, 7); ctx.fill(); ctx.restore();

      // links
      ctx.lineWidth = 1.2;
      for (var k = 0; k < links.length; k++) {
        var A = P[links[k][0]], B = P[links[k][1]];
        var d = (A.z + B.z) / 2;
        ctx.strokeStyle = 'rgba(21,24,27,' + (0.12 + 0.3 * ((d + 1) / 2)).toFixed(3) + ')';
        ctx.beginPath(); ctx.moveTo(A.X, A.Y); ctx.lineTo(B.X, B.Y); ctx.stroke();
      }

      // nodes, back to front
      P.sort(function (m, n) { return m.z - n.z; });
      for (var j = 0; j < P.length; j++) {
        var q = P[j], p = q.p;
        var rr = S * 0.034 * p.s * q.f;
        var depth = (q.z + 1) / 2;
        ctx.globalAlpha = p.core ? 1 : 0.5 + 0.5 * Math.max(0, Math.min(1, depth));
        var gr = ctx.createRadialGradient(q.X - rr * 0.35, q.Y - rr * 0.38, rr * 0.08, q.X, q.Y, rr);
        if (p.ink) { gr.addColorStop(0, '#8A9096'); gr.addColorStop(0.5, '#2B3036'); gr.addColorStop(1, '#15181B'); }
        else { gr.addColorStop(0, '#F8FFC4'); gr.addColorStop(0.42, '#C8F31D'); gr.addColorStop(1, '#6F9400'); }
        ctx.fillStyle = gr;
        ctx.beginPath(); ctx.arc(q.X, q.Y, rr, 0, 7); ctx.fill();
        if (p.core) { ctx.lineWidth = 2.5; ctx.strokeStyle = '#15181B'; ctx.stroke(); }
        // specular dot
        ctx.fillStyle = 'rgba(255,255,255,.75)';
        ctx.beginPath(); ctx.arc(q.X - rr * 0.36, q.Y - rr * 0.4, rr * 0.16, 0, 7); ctx.fill();
      }
      ctx.globalAlpha = 1;
    }

    function frame() {
      requestAnimationFrame(frame);
      if (!visible || reduce) return;
      if (!dragging) { ay += spin; ax += (tx - ax) * 0.05; }
      draw();
    }

    cv.addEventListener('pointerdown', function (e) { dragging = true; lastX = e.clientX; lastY = e.clientY; cv.setPointerCapture(e.pointerId); cv.style.cursor = 'grabbing'; });
    cv.addEventListener('pointermove', function (e) {
      if (!dragging) return;
      ay += (e.clientX - lastX) * 0.01; ax += (e.clientY - lastY) * 0.008;
      ax = Math.max(-1.1, Math.min(1.1, ax)); tx = ax;
      lastX = e.clientX; lastY = e.clientY;
      if (reduce) draw();
    });
    function up() { dragging = false; cv.style.cursor = 'grab'; }
    cv.addEventListener('pointerup', up); cv.addEventListener('pointercancel', up);
    window.addEventListener('pointermove', function (e) {
      if (dragging) return;
      var r = cv.getBoundingClientRect();
      var ny = ((e.clientY - r.top) / r.height - 0.5);
      tx = -0.25 + Math.max(-0.5, Math.min(0.5, ny)) * 0.5;
    });
    if ('IntersectionObserver' in window) {
      new IntersectionObserver(function (en) { visible = en[0].isIntersecting; }).observe(cv);
    }
    if ('ResizeObserver' in window) new ResizeObserver(resize).observe(cv); else window.addEventListener('resize', resize);
    resize(); frame();
  }

  /* ---------- 3D tilt (portfolio browser) ---------- */
  var tilt = document.querySelector('[data-tilt]');
  if (tilt && !reduce) {
    var host = tilt.closest('.stage3d') || tilt.parentNode;
    host.addEventListener('pointermove', function (e) {
      var r = host.getBoundingClientRect();
      var px = (e.clientX - r.left) / r.width - 0.5;
      var py = (e.clientY - r.top) / r.height - 0.5;
      tilt.style.setProperty('--ry', (-14 + px * 18).toFixed(2) + 'deg');
      tilt.style.setProperty('--rx', (8 - py * 14).toFixed(2) + 'deg');
    });
    host.addEventListener('pointerleave', function () {
      tilt.style.setProperty('--ry', '-14deg'); tilt.style.setProperty('--rx', '8deg');
    });
  }

  /* ---------- typing address ---------- */
  var typer = document.querySelector('[data-typer]');
  if (typer) {
    var words = ['yourname', 'yourwork', 'yourname'];
    var wi = 0, ci = 0, del = false;
    if (reduce) { typer.textContent = words[0]; }
    else {
      (function tick() {
        var w = words[wi % words.length];
        if (!del) { ci++; typer.textContent = w.slice(0, ci); if (ci === w.length) { del = true; return void setTimeout(tick, 2200); } }
        else { ci--; typer.textContent = w.slice(0, ci); if (ci === 0) { del = false; wi++; return void setTimeout(tick, 380); } }
        setTimeout(tick, del ? 55 : 95);
      })();
    }
  }

  /* ---------- mountain climb drawn by scroll ---------- */
  var climb = document.getElementById('climb');
  if (climb) {
    var mt = climb.closest('.mountain');
    var camps = mt.querySelectorAll('.camp[data-at]');
    var len = climb.getTotalLength();
    climb.style.strokeDasharray = len;
    function climbUpdate() {
      var r = mt.getBoundingClientRect();
      var vh = window.innerHeight;
      var p = (vh * 0.85 - r.top) / (r.height * 0.9 + vh * 0.2);
      p = Math.max(0, Math.min(1, p));
      if (reduce) p = 1;
      climb.style.strokeDashoffset = len * (1 - p);
      camps.forEach(function (c) { c.classList.toggle('on', p >= parseFloat(c.getAttribute('data-at'))); });
    }
    window.addEventListener('scroll', climbUpdate, { passive: true });
    window.addEventListener('resize', climbUpdate);
    climbUpdate();
  }

  /* ---------- portfolio request form ---------- */
  var form = document.getElementById('request');
  if (form) {
    var out = document.getElementById('result');
    var pre = document.getElementById('summary');
    var contact = form.getAttribute('data-contact') || '';
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      var f = new FormData(form);
      var addr = (f.get('address') || '').toString().toLowerCase().replace(/[^a-z0-9-]/g, '');
      var text = 'Portfolio request for CodPox\n' +
        '\nName: ' + f.get('name') +
        '\nCollege and branch: ' + f.get('college') +
        '\nPreferred address: ' + (addr || 'not chosen') + '.codpox.com' +
        '\nProject links: ' + (f.get('links') || 'none yet') +
        '\nContact number: ' + f.get('phone');
      pre.textContent = text;
      out.classList.add('show');
      var note = document.getElementById('result-note');
      if (contact) {
        note.textContent = 'Your email app will open with this request ready to send.';
        window.location.href = 'mailto:' + contact + '?subject=' + encodeURIComponent('Portfolio request: ' + f.get('name')) + '&body=' + encodeURIComponent(text);
      } else {
        note.textContent = 'Copy this request and send it to the CodPox team. Direct submission opens when the contact channel is connected.';
      }
      out.scrollIntoView({ behavior: reduce ? 'auto' : 'smooth', block: 'center' });
    });
    var copy = document.getElementById('copy');
    if (copy) copy.addEventListener('click', function () {
      var done = function () { copy.textContent = 'Copied'; setTimeout(function () { copy.textContent = 'Copy request'; }, 1800); };
      if (navigator.clipboard) navigator.clipboard.writeText(pre.textContent).then(done, done); else done();
    });
  }
})();
