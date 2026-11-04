from pathlib import Path
import json,html,shutil
r=Path(__file__).resolve().parent.parent;p=r/'docs';base='https://itzik-community-benefits.pages.dev/library/'
data=json.loads((p/'entries.json').read_text());routes={'index.html':'','start.html':'start/','about.html':'about/','submit.html':'submit/'}
for d in data:
 k=d.get('slug')or'issue-'+d['issue'].split('/')[-1]
 routes['recipes/'+k+'.html']='recipes/'+k+'/'
 if d.get('recipe_en'):routes['recipes/'+k+'-en.html']='recipes/'+k+'-en/'
for old,dest in routes.items():
 u=base+dest;f=p/old;f.parent.mkdir(parents=True,exist_ok=True);f.write_text('<!doctype html><html lang="he" dir="rtl"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>הספרייה עברה לאתר ההטבות</title><link rel="canonical" href="'+u+'"><meta name="robots" content="noindex,follow"><meta http-equiv="refresh" content="0;url='+u+'"><script>location.replace('+json.dumps(u)+'+location.hash)</script><p>הספרייה עברה לאתר ההטבות. <a href="'+u+'">למתכון באתר החדש</a></p></html>')
(p/'sitemap.xml').write_text('<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"></urlset>')
(p/'robots.txt').write_text('User-agent: *\nAllow: /\nSitemap: https://itzik-community-benefits.pages.dev/sitemap.xml\n')
print('LegacyhumanURLsredirected',len(routes))

for name in ['llms.txt','llms-full.txt','entries.json','entries-meta.json','feed.json','api.md','mcp-connect.md','mcp-spec.md']:
 f=p/name
 if f.exists():
  s=f.read_text().replace('https://ofershap.github.io/agent-success-hub/',base)
  for key in ['submit','start','about']:s=s.replace(base+key+'.html',base+key+'/')
  f.write_text(s)

import hashlib
f=p/"entries-meta.json";meta=json.loads(f.read_text());meta["sha256"]=hashlib.sha256((p/"entries.json").read_bytes()).hexdigest();f.write_text(json.dumps(meta))
