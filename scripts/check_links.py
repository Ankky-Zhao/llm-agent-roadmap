#!/usr/bin/env python3
"""Check every URL in data/resources.json and data/papers.json.
Writes link_report.md and exits 1 if any link looks broken.
Only 404/410 and DNS/connection failures count as broken; 403/429 are
reported as 'unverifiable' because many sites block automated requests."""
import json, pathlib, sys, concurrent.futures as cf, urllib.request, urllib.error, ssl
root = pathlib.Path(__file__).resolve().parent.parent
items = []
for f in ('resources.json', 'papers.json'):
    for x in json.load(open(root / 'data' / f, encoding='utf-8')):
        items.append((f, x['title'], x['url']))
UA = {'User-Agent': 'Mozilla/5.0 (agent-atlas link checker; +https://github.com/Ankky-Zhao/llm-agent-roadmap)'}
ctx = ssl.create_default_context()

def check(item):
    f, title, url = item
    for method in ('HEAD', 'GET'):
        try:
            req = urllib.request.Request(url, headers=UA, method=method)
            with urllib.request.urlopen(req, timeout=20, context=ctx) as r:
                return item, r.status, 'ok'
        except urllib.error.HTTPError as e:
            # Some servers (e.g. kaggle.com) answer HEAD with 404 but GET with 200,
            # so a HEAD error is never trusted on its own: always confirm with GET.
            if method == 'HEAD':
                continue
            if e.code in (404, 410):
                return item, e.code, 'broken'
            return item, e.code, 'unverifiable'
        except Exception as e:
            if method == 'HEAD':
                continue
            return item, None, f'broken ({type(e).__name__})'
    return item, None, 'unverifiable'

with cf.ThreadPoolExecutor(16) as ex:
    results = list(ex.map(check, items))
broken = [r for r in results if r[2].startswith('broken')]
unver = [r for r in results if r[2] == 'unverifiable']
lines = [f'# Link check', '', f'Checked {len(results)} links: {len(broken)} broken, {len(unver)} unverifiable (403/429 etc.).', '']
if broken:
    lines += ['## Broken', ''] + [f'- [ ] `{f}` · {t} · {u} · {s or ""} {st}' for (f, t, u), s, st in broken] + ['']
if unver:
    lines += ['<details><summary>Unverifiable</summary>', ''] + [f'- `{f}` · {t} · {u} · {s}' for (f, t, u), s, st in unver] + ['', '</details>']
(root / 'link_report.md').write_text('\n'.join(lines), encoding='utf-8')
print('\n'.join(lines[:3]))
sys.exit(1 if broken else 0)
