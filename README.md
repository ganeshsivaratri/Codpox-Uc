# CodPox website
Static site: HTML + CSS + vanilla JS. No build step needed to deploy.

- Pages: index.html, core-idea.html, initiatives.html, portfolio.html
- Deploy: Cloudflare Pages -> upload this folder (build command: none, output directory: /)
- Edit shared header/footer or page copy in build.py, then run `python3 build.py`
- Portfolio form: set your contact email in portfolio.html on <form id="request" data-contact="you@example.com"> (or in build.py)
- Images: the mountain and spore are drawn in code, so there are no image files to host
