#!/usr/bin/env python3
"""Build index.html from template.html + data/*.json.  Usage: python build.py [--fragment out.html]"""
import json, sys, pathlib
root = pathlib.Path(__file__).parent
data = {k: json.load(open(root/'data'/f'{k}.json', encoding='utf-8')) for k in ('content','resources','papers')}
D = dict(data['content']); D['resources'] = data['resources']; D['papers'] = data['papers']
# sanity checks contributors get for free
mods = set(D['modules']); used = [m for s in D['stages'] for m in s['modules']]
assert set(used) == mods, f"stage/module mismatch: {set(used) ^ mods}"
bad = {r['topic'] for r in D['resources']} - mods; assert not bad, f"resources with unknown topic: {bad}"
urls = [r['url'] for r in D['resources']]; assert len(urls) == len(set(urls)), "duplicate resource urls"
tpl = open(root/'template.html', encoding='utf-8').read()
tr = D['tracks']
tpl = tpl.replace('__TRJOB_ZH__', tr['job']['zh']).replace('__TRRES_ZH__', tr['research']['zh']).replace('__TRJOB_EN__', tr['job']['en']).replace('__TRRES_EN__', tr['research']['en'])
payload = json.dumps(D, ensure_ascii=False, separators=(',',':')).replace('</', '<\\/')
html = tpl.replace('__DATA__', payload)
open(root/'index.html', 'w', encoding='utf-8').write(html)
print('index.html', len(html), 'bytes;', len(D['resources']), 'resources;', len(D['papers']), 'papers;', len(mods), 'modules')
if '--fragment' in sys.argv:
    out = sys.argv[sys.argv.index('--fragment')+1]
    frag = html.split('<head>',1)[1]
    head, body = frag.split('</head>',1)
    head = head.replace('<meta charset="utf-8">','').replace('<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">','')
    body = body.split('<body>',1)[1].rsplit('</body>',1)[0]
    open(out,'w',encoding='utf-8').write(head.strip()+'\n'+body.strip())
    print('fragment', out)
