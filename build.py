#!/usr/bin/env python3
"""Generates the four static pages with a shared header and footer.
Run: python3 build.py   (edit the page bodies below, then rebuild)"""
import pathlib
OUT = pathlib.Path(__file__).parent

SPRITE = """<svg width="0" height="0" style="position:absolute" aria-hidden="true"><defs>
<symbol id="i-arrow" viewBox="0 0 24 24"><path d="M7 17 17 7M8 7h9v9"/></symbol>
<symbol id="i-x" viewBox="0 0 24 24"><path d="M5 5l14 14M19 5 5 19" stroke-width="4"/></symbol>
<symbol id="i-spore" viewBox="0 0 48 48"><circle cx="24" cy="24" r="20" fill="#C8F31D" stroke="#15181B" stroke-width="3"/><circle cx="17" cy="19" r="3.4" fill="#15181B"/><circle cx="31" cy="17" r="2.4" fill="#15181B"/><circle cx="29" cy="30" r="4" fill="#15181B"/><circle cx="16" cy="31" r="2" fill="#15181B"/></symbol>
</defs></svg>"""

LOGO_MARK = '<svg viewBox="0 0 48 48" aria-hidden="true"><use href="#i-spore"/></svg>'

def arrow(cls="ico"):
    return f'<svg class="{cls}" viewBox="0 0 24 24" aria-hidden="true"><use href="#i-arrow"/></svg>'

def tape():
    item = '<span>Currently under construction<svg viewBox="0 0 24 24" aria-hidden="true"><use href="#i-x" stroke="#15181B" fill="none"/></svg></span>'
    return f'<div class="tape" role="note" aria-label="CodPox is currently under construction"><div class="track" aria-hidden="true">{item * 16}</div></div>'

NAV = [("index.html", "Home"), ("core-idea.html", "Core Idea"), ("initiatives.html", "Initiatives")]

def head(title, desc, active):
    links = ""
    for href, label in NAV:
        cur = ' aria-current="page"' if href == active else ""
        links += f'<li><a href="{href}"{cur}>{label}</a></li>'
    cur = ' aria-current="page"' if active == "portfolio.html" else ""
    links += f'<li class="cta"><a href="portfolio.html"{cur}>Get your portfolio</a></li>'
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="theme-color" content="#C8F31D">
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 48 48'%3E%3Ccircle cx='24' cy='24' r='20' fill='%23C8F31D' stroke='%2315181B' stroke-width='3'/%3E%3Ccircle cx='17' cy='19' r='3.4'/%3E%3Ccircle cx='31' cy='17' r='2.4'/%3E%3Ccircle cx='29' cy='30' r='4'/%3E%3C/svg%3E">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,500;12..96,700;12..96,800&family=Caveat:wght@600&family=DM+Mono:wght@500&family=Figtree:wght@400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="css/style.css">
</head>
<body>
{SPRITE}
<a class="sr" href="#main">Skip to content</a>
{tape()}
<header class="nav"><div class="wrap">
<a class="logo" href="index.html" aria-label="CodPox home">{LOGO_MARK}codpox</a>
<button class="burger" aria-label="Menu" aria-expanded="false" aria-controls="menu"><span></span><span></span><span></span></button>
<nav aria-label="Main"><ul class="menu" id="menu">{links}</ul></nav>
</div></header>
<main id="main">
"""

FOOT = f"""</main>
<footer class="foot"><div class="wrap">
<div class="cols">
<div><a class="logo" href="index.html">{LOGO_MARK}codpox</a>
<p style="margin-top:1rem">A student builder ecosystem. Currently under construction, and built in the open with real students.</p></div>
<div><h4>Pages</h4><ul><li><a href="index.html">Home</a></li><li><a href="core-idea.html">Core Idea</a></li><li><a href="initiatives.html">Initiatives</a></li><li><a href="portfolio.html">Get your portfolio</a></li></ul></div>
<div><h4>Under CodPox</h4><ul><li><a href="https://sxc.codpox.com" target="_blank" rel="noopener">SintraX Creations (SXC)</a></li><li><span>Padharaksha</span></li><li><span>MemoryWall</span></li></ul></div>
</div>
<div class="fine"><span>© 2026 CodPox. Nothing is handed over. Everything is earned.</span><span>SXC is an initiative under CodPox.</span></div>
</div></footer>
<script src="js/main.js" defer></script>
</body>
</html>
"""

def page(name, title, desc, body):
    (OUT / name).write_text(head(title, desc, name) + body + FOOT, encoding="utf-8")

# ---------- shared bits ----------
def band_words():
    word = lambda w: f'<span>{w}<svg viewBox="0 0 48 48" aria-hidden="true"><use href="#i-spore"/></svg></span>'
    return word("Learn") + word("Build") + word("Prove") + word("Progress")

def x_item(text, color="#C8F31D"):
    return f'<span>{text}<svg viewBox="0 0 24 24" aria-hidden="true" style="width:.7em;height:.7em"><use href="#i-x" stroke="{color}" fill="none"/></svg></span>'

# ================= HOME =================
home = f"""
<section class="hero">
<div class="wrap">
<h1><span class="line"><span style="--i:0">Learn.</span></span><span class="line"><span style="--i:1">Build.</span></span><span class="line"><span style="--i:2">Prove.</span></span><span class="line"><span style="--i:3">Progress.</span></span></h1>
<p class="sub lead">CodPox is a student builder ecosystem where nothing is handed over and everything is earned.</p>
<div class="actions">
<a class="btn" href="core-idea.html">Explore the core idea {arrow()}</a>
<a class="btn btn--ghost" href="initiatives.html">See what is running</a>
</div>
<div class="spore"><canvas data-spore role="img" aria-label="A rotating cluster of connected lime nodes, the CodPox spore. Drag to spin it."></canvas></div>
<div class="note"><span class="hand">drag it. we are<br>still building</span>
<svg viewBox="0 0 54 54" aria-hidden="true"><path d="M8 8c18 2 32 14 36 36M44 44l-10-3M44 44l2-11"/></svg></div>
</div>
</section>

<div class="band" aria-hidden="true"><div class="track">{band_words()*5}</div></div>

<section class="sec">
<div class="wrap split">
<h2>What is CodPox?</h2>
<div>
<p class="lead">CodPox helps students close the gap between learning technology and building something real with it.</p>
<p>A student starts with direction and a practical challenge, builds a project, goes through review, and leaves with proof of the work. Progression to greater responsibility is earned from that proof, not from joining or paying.</p>
</div>
</div>
</section>

<section class="sec" style="padding-top:0">
<div class="wrap">
<div class="head"><h2>The journey</h2><p>Four stages, each earned by the one before. The first two are the practical foundation today.</p></div>
<div class="stages">
<div class="stage"><h3>Challenger</h3><p>Finds direction, learns the fundamentals and takes on a first practical challenge.</p><span class="when">Starting point</span></div>
<div class="stage"><h3>Builder</h3><p>Has shown they can turn a challenge into real work. Earned, never assigned.</p><span class="when">Practical foundation</span></div>
<div class="stage stage--later"><h3>Supervisor</h3><p>Coordinates teams and reviews once there are real Builders to learn from.</p><span class="when">Growing later</span></div>
<div class="stage stage--later"><h3>Mentor</h3><p>Alumni who return to guide the next students.</p><span class="when">Growing later</span></div>
</div>
<div class="actions"><a class="textlink" href="core-idea.html#journey">Read how the journey works {arrow()}</a></div>
</div>
</section>

<section class="sec" style="padding-top:0">
<div class="wrap">
<div class="head"><h2>What is running now</h2><p>CodPox is already doing real things, shown here at their real stage.</p></div>
<div class="bento">
<article class="card c-a"><span class="hand">since 2025</span>
<span class="status s-run" style="align-self:flex-start"><i></i>Running</span>
<h3>Padharaksha</h3><p>An initiative under CodPox, running since 2025.</p>
<div class="push"><a class="textlink" href="initiatives.html">All initiatives {arrow()}</a></div></article>
<article class="card c-b"><span class="status s-run" style="align-self:flex-start"><i></i>Running</span>
<h3>SXC</h3><p>SintraX Creations, a practical student-building initiative under CodPox.</p>
<div class="push"><a class="textlink" href="https://sxc.codpox.com" target="_blank" rel="noopener">sxc.codpox.com {arrow()}</a></div></article>
<article class="card c-c"><span class="status s-dev" style="align-self:flex-start"><i></i>Developing</span>
<h3>MemoryWall</h3><p>A place to store memories.</p></article>
<article class="card c-d"><span class="status" style="align-self:flex-start"><i></i>Coming soon</span>
<h3>More on the way</h3><p>New initiatives are being shaped. They will appear here when they are real.</p></article>
</div>
</div>
</section>

<section class="sec" style="padding-top:0">
<div class="wrap">
<div class="head"><h2>Where to next</h2></div>
<div class="doors">
<a class="door" href="core-idea.html"><svg class="pic" viewBox="0 0 300 120" aria-hidden="true"><path d="M0 110 70 50l40 34 60-62 50 52 40-26 40 62Z" fill="none" stroke="#15181B" stroke-width="3" stroke-linejoin="round"/><circle cx="170" cy="22" r="7" fill="#C8F31D" stroke="#15181B" stroke-width="3"/></svg>
<div><h3>Core Idea</h3><p>Why CodPox exists, how the journey works and why it takes time.</p></div><span class="go">{arrow()}</span></a>
<a class="door" href="initiatives.html"><svg class="pic" viewBox="0 0 300 120" aria-hidden="true"><g fill="none" stroke="#15181B" stroke-width="3"><circle cx="50" cy="60" r="26" fill="#C8F31D"/><circle cx="130" cy="60" r="26" fill="#fff"/><circle cx="210" cy="60" r="26" stroke-dasharray="6 6"/><path d="M76 60h28M156 60h28"/></g></svg>
<div><h3>Initiatives</h3><p>What is running under the CodPox name, and at what stage.</p></div><span class="go">{arrow()}</span></a>
<a class="door" href="portfolio.html"><svg class="pic" viewBox="0 0 300 120" aria-hidden="true"><g fill="none" stroke="#15181B" stroke-width="3"><rect x="40" y="14" width="220" height="92" rx="12" fill="#fff"/><path d="M40 40h220"/><rect x="90" y="22" width="110" height="10" rx="5" fill="#C8F31D"/><path d="M62 62h80M62 80h56"/><circle cx="212" cy="72" r="16" fill="#C8F31D"/></g></svg>
<div><h3>Get your portfolio</h3><p>CodPox developers build your portfolio at yourname.codpox.com.</p></div><span class="go">{arrow()}</span></a>
</div>
</div>
</section>

<section class="sec closing">
<div class="wrap">
<h2>Nothing is handed over.<br>Everything is earned.</h2>
<div class="actions"><a class="btn" href="core-idea.html">Read the core idea {arrow()}</a></div>
</div>
</section>
"""
page("index.html", "CodPox | Learn. Build. Prove. Progress.",
     "CodPox is a student builder ecosystem where nothing is handed over and everything is earned. Currently under construction.", home)

# ================= CORE IDEA =================
def mountain():
    return """
<div class="mountain" id="mountain">
<svg viewBox="0 0 1200 690" role="img" aria-labelledby="mt-t">
<title id="mt-t">A mountain with a climbing path. Challenger and Builder camps are reached; Supervisor and Mentor camps are higher up and still to come.</title>
<defs>
<radialGradient id="sun" cx=".35" cy=".35" r=".8"><stop offset="0" stop-color="#F8FFC4"/><stop offset=".45" stop-color="#C8F31D"/><stop offset="1" stop-color="#8DB400"/></radialGradient>
<linearGradient id="far" x1="0" x2="0" y1="0" y2="1"><stop offset="0" stop-color="#D3E1ED"/><stop offset="1" stop-color="#E7EFF5"/></linearGradient>
</defs>
<circle cx="1040" cy="120" r="54" fill="url(#sun)" stroke="#15181B" stroke-width="3"/>
<path fill="url(#far)" d="M0 380 120 300l100 50 120-110 130 100 130-130 120 110 140-140 140 120 100-50 100 70v500H0Z"/>
<path fill="#BCD0E0" d="M0 470 150 380l130 60 150-110 130 100 140-70 160 90 140-110 200 110v500H0Z"/>
<path fill="#fff" stroke="#15181B" stroke-width="3" stroke-linejoin="round" d="M0 585 200 480l160 50 200-170 140-100 120-140 110 130 110 80 160 150v500H0Z"/>
<path fill="#EEF9BF" d="M820 120 760 190l40-14 30 28 24-26 32 32-44-60Z" opacity=".0"/>
<path d="M820 120 790 160l22-8 8 22 18-24 22 10-40-40Z" fill="#E1ECF5" stroke="#15181B" stroke-width="2.5" stroke-linejoin="round"/>
<path id="later" d="M520 445 600 470 690 335 760 350 820 160" fill="none" stroke="#15181B" stroke-width="5" stroke-dasharray="3 14" stroke-linecap="round" opacity=".55"/>
<path id="climb" d="M120 595 262 548 380 575 520 445" fill="none" stroke="#15181B" stroke-width="7"/>
<circle class="camp" data-at="0.45" cx="262" cy="548" r="15"/>
<circle class="camp" data-at="0.97" cx="520" cy="445" r="15"/>
<circle class="camp later" cx="690" cy="335" r="15"/>
<circle class="camp later" cx="820" cy="160" r="15"/>
<g class="mt-label" transform="translate(95 612)"><rect x="0" y="0" width="190" height="46" rx="23"/><text x="95" y="32" text-anchor="middle">Challenger</text></g>
<g class="mt-label" transform="translate(548 466)"><rect x="0" y="0" width="150" height="46" rx="23"/><text x="75" y="32" text-anchor="middle">Builder</text></g>
<g class="mt-label later" transform="translate(712 328)"><rect x="0" y="0" width="170" height="46" rx="23"/><text x="85" y="32" text-anchor="middle">Supervisor</text></g>
<g class="mt-label later" transform="translate(850 150)"><rect x="0" y="0" width="140" height="46" rx="23"/><text x="70" y="32" text-anchor="middle">Mentor</text></g>
<text class="mt-hand" x="300" y="500" transform="rotate(-6 300 500)">you start here</text>
<text class="mt-hand" x="610" y="262" transform="rotate(-5 610 262)">still to come</text>
</svg>
</div>"""

def loop():
    import math
    labels = [["Student"], ["Build"], ["Proof"], ["Portfolio"], ["People"], ["Network"], ["Projects"], ["More", "builders"]]
    nodes = ""
    for i, ls in enumerate(labels):
        a = math.radians(-90 + 45 * i)
        x, y = 300 + 215 * math.cos(a), 300 + 215 * math.sin(a)
        t = "".join(f'<tspan x="{x:.1f}" dy="{ -8 + 18 * j if len(ls) > 1 else 6 }">{w}</tspan>' if j == 0 else f'<tspan x="{x:.1f}" dy="18">{w}</tspan>' for j, w in enumerate(ls))
        nodes += f'<g class="nd"><circle cx="{x:.1f}" cy="{y:.1f}" r="47"/><text x="{x:.1f}" y="{y:.1f}">{t}</text></g>'
    return f"""<svg class="loop" viewBox="0 0 600 600" role="img" aria-labelledby="lp-t">
<title id="lp-t">The CodPox loop: Student, Build, Proof, Portfolio, People, Network, Projects, More builders, and back to Student.</title>
<circle class="ring" cx="300" cy="300" r="215" fill="none" stroke="#15181B" stroke-width="2.5" stroke-dasharray="10 14"/>
<circle cx="300" cy="300" r="120" fill="#EEF9BF" stroke="#DDEBA1"/>
<text class="core" x="300" y="296">The CodPox</text><text class="core" x="300" y="326">loop</text>
{nodes}</svg>"""

core = f"""
<section class="page-hero">
<div class="wrap">
<h1>The original idea of CodPox is under construction.</h1>
<p class="lead">We are building it with real students, in the open. This page is the idea as it stands today.</p>
</div>
<div class="wrap crossed" aria-hidden="true">
<div class="band"><div class="track">{x_item("Under construction", "#15181B")*14}</div></div>
<div class="band band--ink"><div class="track">{x_item("Real students")*4}{x_item("Real projects")*4}{x_item("Real feedback")*4}</div></div>
</div>
</section>

<section class="sec">
<div class="wrap split">
<h2>What is CodPox?</h2>
<div>
<p class="lead">A student builder ecosystem. It takes a student from direction and practical challenges to real projects, proof of work and earned progression.</p>
<p>The idea is simple: <strong>learn, build, prove, progress.</strong> The product is the journey and the progression system around it.</p>
</div>
</div>
</section>

<section class="sec" style="padding-top:0">
<div class="wrap">
<p class="statement">Nothing is handed over. <em>Everything is earned.</em></p>
<p class="lead" style="margin-top:2rem;max-width:48ch">Joining does not make anyone a Builder. Paying does not either. Progress comes from the work a student can show and explain.</p>
</div>
</section>

<section class="sec" style="padding-top:0">
<div class="wrap">
<div class="head"><h2>The problem we start from</h2><p>Students can learn a lot and still be stuck at the moment of doing.</p></div>
<div class="qlist">
<div class="q"><h3>What should I build?</h3><p>CodPox gives you a practical challenge that fits your direction.</p></div>
<div class="q"><h3>Can I build on my own?</h3><p>You solve problems that have no ready-made solution, then get reviewed.</p></div>
<div class="q"><h3>Can I explain what I made?</h3><p>You walk through your project and defend your decisions, with or without AI.</p></div>
<div class="q"><h3>Can I work with others?</h3><p>Real projects need communication, teamwork and responsibility.</p></div>
<div class="q"><h3>How do I prove it?</h3><p>A resume lists skills. Finished work shows them.</p></div>
</div>
</div>
</section>

<section class="sec" id="journey" style="padding-top:0">
<div class="wrap">
<div class="head"><h2>The student journey</h2><p>One path, six steps. Each one has to be done before the next.</p></div>
<div class="steps">
<div class="step"><h3>Direction</h3><p>Understand your goals and choose a technology.</p></div>
<div class="step"><h3>Challenge</h3><p>Receive a practical problem to solve.</p></div>
<div class="step"><h3>Build</h3><p>Make the project yourself.</p></div>
<div class="step"><h3>Review</h3><p>Explain your work and take feedback.</p></div>
<div class="step"><h3>Proof</h3><p>Finish with work you can show.</p></div>
<div class="step"><h3>Progression</h3><p>Earn more responsibility.</p></div>
</div>
</div>
</section>

<section class="sec" style="padding-top:0">
<div class="wrap">
<div class="head"><h2>The climb</h2><p>Four stages from learning to guiding others. Scroll to watch the path.</p></div>
{mountain()}
<div class="chapters">
<div class="chapter"><span class="quote">"I am learning."</span><h3>Challenger</h3><p>Starts with a 1:1 conversation about goals, picks a direction, builds fundamentals and takes a first challenge.</p></div>
<div class="chapter"><span class="quote">"I can build."</span><h3>Builder</h3><p>Has turned a challenge into meaningful work. Builders can take on real projects, teamwork and, over time, guide Challengers.</p></div>
<div class="chapter chapter--later"><span class="quote">"I can coordinate."</span><h3>Supervisor</h3><p>Managing teams and reviews. We will shape this from real Builder experience, not guess it on paper.</p><span class="tag">Growing later</span></div>
<div class="chapter chapter--later"><span class="quote">"I can guide."</span><h3>Mentor</h3><p>People who grew through CodPox return to share experience with new students.</p><span class="tag">Growing later</span></div>
</div>
</div>
</section>

<section class="sec" style="padding-top:0">
<div class="wrap">
<div class="panel panel--lime"><div class="split">
<div><h2>AI is a builder's tool.</h2><p class="lead" style="margin-top:1.2rem">Use ChatGPT, Gemini or any tool you like. It does not replace understanding what you built.</p></div>
<ul class="checks"><li>Understand the code</li><li>Explain the architecture</li><li>Modify it</li><li>Debug it</li><li>Keep developing it</li></ul>
</div></div>
</div>
</section>

<section class="sec" style="padding-top:0">
<div class="wrap">
<div class="head"><h2>What CodPox is not</h2><p>Saying it plainly so nobody is misled.</p></div>
<div class="nots">
<div class="not"><svg viewBox="0 0 24 24" fill="none" stroke-width="2.4" stroke-linecap="round"><path d="M6 6l12 12M18 6 6 18"/></svg><div><h3>Not a course platform</h3><p>Learning content is not the product. The journey is.</p></div></div>
<div class="not"><svg viewBox="0 0 24 24" fill="none" stroke-width="2.4" stroke-linecap="round"><path d="M6 6l12 12M18 6 6 18"/></svg><div><h3>Not certificate-first</h3><p>Work you can show matters more than a certificate.</p></div></div>
<div class="not"><svg viewBox="0 0 24 24" fill="none" stroke-width="2.4" stroke-linecap="round"><path d="M6 6l12 12M18 6 6 18"/></svg><div><h3>Not a job guarantee</h3><p>We make no promise of placement or hiring.</p></div></div>
<div class="not"><svg viewBox="0 0 24 24" fill="none" stroke-width="2.4" stroke-linecap="round"><path d="M6 6l12 12M18 6 6 18"/></svg><div><h3>Not against college CRT</h3><p>CRT prepares you for interviews. CodPox focuses on building. They sit side by side.</p></div></div>
</div>
</div>
</section>

<section class="sec" style="padding-top:0">
<div class="wrap">
<div class="head"><h2>Why it takes time</h2><p>A real ecosystem is more than software. You cannot design it perfectly on paper.</p></div>
<div class="panel">
<p class="lead">It needs all of this, tested with real students:</p>
<div class="chips"><span class="chip">Students</span><span class="chip">Challenges</span><span class="chip">Projects</span><span class="chip">Teams</span><span class="chip">Reviews</span><span class="chip">Standards</span><span class="chip">Feedback</span><span class="chip">Mentors</span><span class="chip">Processes</span><span class="chip">Tools</span><span class="chip">Experience</span></div>
<div class="cycle" aria-label="Build, test, learn, improve, build again"><span class="n">Build</span><svg class="sep" viewBox="0 0 24 24"><path d="M5 12h14M13 6l6 6-6 6"/></svg><span class="n">Test</span><svg class="sep" viewBox="0 0 24 24"><path d="M5 12h14M13 6l6 6-6 6"/></svg><span class="n">Learn</span><svg class="sep" viewBox="0 0 24 24"><path d="M5 12h14M13 6l6 6-6 6"/></svg><span class="n">Improve</span><svg class="sep" viewBox="0 0 24 24"><path d="M5 12h14M13 6l6 6-6 6"/></svg><span class="n">Build again</span></div>
<p style="margin-top:1.6rem">Value comes before scale. We would rather grow slowly and get it right.</p>
</div>
</div>
</section>

<section class="sec" style="padding-top:0">
<div class="wrap loopwrap">
<div><h2>The CodPox loop</h2>
<p class="lead" style="margin-top:1.2rem">Students build projects. Projects become proof. Proof becomes a portfolio. Portfolios make work visible, visibility creates connections, and connections lead to new projects and more builders.</p>
<p style="margin-top:1rem">The network is a long-term layer. It becomes meaningful only after CodPox has created real value.</p></div>
{loop()}
</div>
</section>

<section class="sec closing">
<div class="wrap">
<h2>We are building it.</h2>
<p class="lead" style="margin-top:1.2rem">See what is already running under the CodPox name.</p>
<div class="actions"><a class="btn" href="initiatives.html">Our initiatives {arrow()}</a><a class="btn btn--ghost" href="index.html">Back to home</a></div>
</div>
</section>
"""
page("core-idea.html", "Core Idea | CodPox",
     "The original idea of CodPox: a student builder ecosystem that turns learning into building, proof and earned progression. Currently under construction.", core)

# ================= INITIATIVES =================
inits = f"""
<section class="page-hero">
<div class="wrap">
<h1>Our initiatives</h1>
<p class="lead">Everything running under the CodPox name, shown at its real stage.</p>
<div class="legend"><span class="status s-run"><i></i>Running</span><span class="status s-dev"><i></i>Developing</span><span class="status"><i></i>Coming soon</span></div>
</div>
</section>

<section class="sec--tight" style="padding-bottom:clamp(64px,9vw,128px)">
<div class="wrap"><div class="rows">
<article class="row"><div><h2>Padharaksha</h2><p>An initiative under CodPox, running since 2025.</p></div>
<div class="side"><span class="status s-run"><i></i>Running since 2025</span></div></article>
<article class="row"><div><h2>SXC</h2><p>SintraX Creations, a practical student-building initiative. An initiative under CodPox.</p></div>
<div class="side"><span class="status s-run"><i></i>Running</span><a class="btn" href="https://sxc.codpox.com" target="_blank" rel="noopener">Visit sxc.codpox.com {arrow()}</a></div></article>
<article class="row"><div><h2>MemoryWall</h2><p>A place to store memories. Being developed now.</p></div>
<div class="side"><span class="status s-dev"><i></i>Developing</span></div></article>
<article class="row row--soon"><div><h2>More coming soon</h2><p>New initiatives are on the way. We list them here when they are real.</p></div>
<div class="side"><span class="status"><i></i>Coming soon</span></div></article>
</div></div>
</section>

<section class="sec closing" style="padding-top:0">
<div class="wrap"><div class="panel panel--lime split" style="align-items:center">
<div><h2>Need a place for your work?</h2></div>
<div><p class="lead">CodPox developers build your portfolio and host it at your own address.</p>
<div class="actions"><a class="btn" href="portfolio.html">Get your portfolio {arrow()}</a></div></div>
</div></div>
</section>
"""
page("initiatives.html", "Initiatives | CodPox",
     "Initiatives under CodPox: Padharaksha, SXC (SintraX Creations), MemoryWall and more coming soon.", inits)

# ================= PORTFOLIO =================
port = f"""
<section class="phero">
<div class="wrap">
<div>
<h1>Your work deserves a place.</h1>
<p class="lead">CodPox developers build your portfolio and host it at your own address.</p>
<div class="actions"><a class="btn" href="#request-form">Request your portfolio {arrow()}</a><a class="btn btn--ghost" href="#how">How it works</a></div>
</div>
<div class="stage3d"><div class="tilt" data-tilt>
<div class="browser">
<div class="chrome"><div class="dots" aria-hidden="true"><i></i><i></i><i></i></div>
<div class="addr" role="img" aria-label="Browser address: yourname.codpox.com"><b><span data-typer>yourname</span></b><span class="caret" aria-hidden="true"></span>.codpox.com</div></div>
<div class="site" aria-hidden="true">
<div class="who"><div class="avatar"></div><div><h3>Your Name</h3><p>Your college, your branch</p></div></div>
<div class="sec-chips"><span>About</span><span>Skills</span><span>Projects</span><span>Contact</span></div>
<div class="pgrid"><div class="pcard"><div class="shot"></div><i></i><i></i></div><div class="pcard"><div class="shot"></div><i></i><i></i></div></div>
</div></div>
<span class="float f1" aria-hidden="true">Projects</span><span class="float f2" aria-hidden="true">Your own address</span>
<div class="demo-tag" aria-hidden="true"><span class="hand">demo layout, not a real student</span></div>
</div></div>
</div>
</section>

<section class="sec">
<div class="wrap split">
<h2>What is this service?</h2>
<div>
<p class="lead">A personal website built for you by CodPox developers, in your name, at studentname.codpox.com.</p>
<p>It shows who you are and what you have built. You bring the work. We design it, develop it and host it.</p>
</div>
</div>
</section>

<section class="sec" style="padding-top:0">
<div class="wrap">
<div class="head"><h2>What you get</h2></div>
<div class="get">
<article class="card g1 panel--lime"><h3>Built by CodPox developers</h3><p>Designed and developed for you, not a template you fill in alone.</p></article>
<article class="card g2 panel--sky"><h3>Your own address</h3><p>A subdomain in your name, like yourname.codpox.com.</p></article>
<article class="card g3"><h3>Hosting included</h3><p>We put it online and keep it running.</p></article>
<article class="card g4"><h3>Works on mobile</h3><p>It reads well on a phone, a tablet and a laptop.</p></article>
<article class="card g5 panel--peach"><h3>Your story, in sections</h3><p>About, Education, Skills, Projects, Achievements and Contact.</p></article>
</div>
</div>
</section>

<section class="sec" id="how" style="padding-top:0">
<div class="wrap">
<div class="head"><h2>How it works</h2></div>
<div class="steps" style="grid-template-columns:repeat(4,1fr)">
<div class="step"><h3>Share</h3><p>Send your details and links to your work.</p></div>
<div class="step"><h3>We build</h3><p>CodPox developers design and develop your site.</p></div>
<div class="step"><h3>You review</h3><p>Look it over and ask for changes.</p></div>
<div class="step"><h3>Go live</h3><p>It goes online at your own address.</p></div>
</div>
</div>
</section>

<section class="sec" style="padding-top:0">
<div class="wrap">
<div class="head"><h2>More than a PDF</h2><p>A portfolio is evidence of your journey, not a longer resume.</p></div>
<div class="vs">
<div class="panel"><h3>A resume</h3><ul><li>Lists the skills you say you have</li><li>Fits on a page, then disappears in a pile</li><li>Is the same as everyone else's</li></ul></div>
<div class="panel panel--lime"><h3>A CodPox portfolio</h3><ul><li>Shows the projects you actually built</li><li>Lives at an address you can share</li><li>Carries the proof behind your progress</li></ul></div>
</div>
</div>
</section>

<section class="sec" id="request-form" style="padding-top:0">
<div class="wrap formwrap">
<div><h2>Request your portfolio</h2><p class="lead" style="margin-top:1.2rem">Tell us who you are and where your work lives. We will take it from there.</p>
<p style="margin-top:1rem">We confirm the timeline and any cost with you after your request.</p></div>
<div>
<form id="request" data-contact="">
<div class="two">
<label>Your name<input name="name" required autocomplete="name"></label>
<label>College and branch<input name="college" required placeholder="College, branch"></label>
</div>
<label>Preferred address<span class="field"><input name="address" required placeholder="yourname" pattern="[A-Za-z0-9\\-]+" title="Letters, numbers and hyphens only" autocapitalize="none"><span>.codpox.com</span></span></label>
<label>Links to your projects <small>Optional. GitHub, live sites, anything you want shown.</small><textarea name="links"></textarea></label>
<label>Contact number<input name="phone" type="tel" required autocomplete="tel"></label>
<div><button class="btn" type="submit">Request your portfolio {arrow()}</button></div>
</form>
<div class="result" id="result" role="status" aria-live="polite">
<h3>Your request is ready</h3>
<pre id="summary"></pre>
<p id="result-note"></p>
<div class="actions" style="margin-top:1rem"><button class="btn btn--ghost" id="copy" type="button">Copy request</button></div>
</div>
</div>
</div>
</section>

<section class="sec" style="padding-top:0">
<div class="wrap">
<div class="head"><h2>Questions</h2></div>
<details><summary>Who builds the portfolio?</summary><p>CodPox developers design and develop it for you.</p></details>
<details><summary>What will my address look like?</summary><p>A subdomain in your name, such as yourname.codpox.com. If the name you want is taken, we will agree on another with you.</p></details>
<details><summary>Can I ask for changes?</summary><p>Yes. You review the portfolio before it goes live and can ask for changes then.</p></details>
<details><summary>How long does it take, and what does it cost?</summary><p>We confirm both with you after you send your request.</p></details>
<details><summary>Do I need to be in CodPox or SXC?</summary><p>Your portfolio shows the work you have built. Send your request and we will confirm the details with you.</p></details>
</div>
</section>
"""
page("portfolio.html", "Get your portfolio | CodPox",
     "CodPox developers build your portfolio and host it at yourname.codpox.com. Your work deserves a place.", port)
print("built", [p.name for p in OUT.glob("*.html")])
