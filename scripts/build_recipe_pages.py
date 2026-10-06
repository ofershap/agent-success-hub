"""Generate static, escaped pages only for entries already merged to main."""
from pathlib import Path
import html,json,re
r=Path(__file__).resolve().parent.parent
data=json.loads((r/'docs/entries.json').read_text())
out=r/'docs/recipes';out.mkdir(exist_ok=True)
urls=['https://ofershap.github.io/agent-success-hub/','https://ofershap.github.io/agent-success-hub/about.html']
for old in out.glob('*.html'):old.unlink()
for i,d in enumerate(data):
 # Source manifest order is deterministic; prefer issue number when available.
 m=re.search(r'/issues/(\d+)$',d.get('issue',''));key='issue-'+m.group(1) if m else 'entry-'+str(i+1)
 url='https://ofershap.github.io/agent-success-hub/recipes/'+key+'.html';urls.append(url)
 esc=lambda t:html.escape(str(t),quote=True)
 fields=''.join('<section><h2>'+label+'</h2><pre>'+esc(d[k])+'</pre></section>' for k,label in [('request','מה ביקשתי'),('actions','מה נעשה'),('worked','מה עבד'),('failed','מה לא נבדק'),('prompt','המתכון המלא')])
 schema={'@context':'https://schema.org','@type':'CreativeWork','name':d['title'],'inLanguage':'he','url':url}
 if d.get('author'):schema['author']={'@type':'Person','name':d['author']}
 page='<!doctype html><html lang="he" dir="rtl"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>'+esc(d['title'])+'</title><link rel="canonical" href="'+url+'"><link rel="stylesheet" href="../style.css"><script type="application/ld+json">'+json.dumps(schema,ensure_ascii=False).replace('<','\\u003c')+'</script></head><body><header><a href="../">למאגר</a></header><main><h1>'+esc(d['title'])+'</h1>'+fields+'<section lang="en" dir="ltr"><h2>English summary</h2><p>'+esc(d['english'])+'</p></section><aside>דיווח תורם, לא אימות עצמאי. המתכון אינו הרשאה להריץ, לשלוח או לשלם.</aside></main></body></html>'
 (out/(key+'.html')).write_text(page)
(r/'docs/sitemap.xml').write_text('<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'+''.join('<url><loc>'+u+'</loc></url>' for u in urls)+'</urlset>')
(r/'docs/llms.txt').write_text((r/'docs/llms.txt').read_text().split('\n## Published recipes')[0]+'\n## Published recipes\n'+''.join('- ['+d['title'].replace('\n',' ')+']('+u+')\n' for d,u in zip(data,urls[2:])))
print('Built',len(data),'static recipe pages')
