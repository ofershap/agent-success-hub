"""Build escaped recipe pages with reviewed text and canonical action links."""
from pathlib import Path
import html,json,re
r=Path(__file__).resolve().parent.parent
BASE='https://ofershap.github.io/agent-success-hub/'
SUBMIT=BASE+'submit.html'
esc=lambda t:html.escape(str(t),quote=True)
links_manifest=json.loads((r/'docs/recipe-whatsapp-links.json').read_text())
def markdown(text):
 # Deliberately small renderer: no raw HTML or executable links from contributions.
 parts=[];paragraph=[];kind=None;seen_title=False
 def flush():
  if paragraph:parts.append('<p>'+esc('\n'.join(paragraph))+'</p>');paragraph.clear()
 def close_list():
  nonlocal kind
  if kind:parts.append('</'+kind+'>');kind=None
 for line in text.splitlines():
  if line.strip().startswith('```'):flush();close_list();continue
  heading=re.match(r'^(#{1,6})\s+(.*)',line)
  bullet=re.match(r'^\s*(- |\d+\. )(.*)',line)
  if heading:
   flush();close_list()
   if len(heading[1])==1 and not seen_title:seen_title=True;continue
   level=min(4,max(2,len(heading[1])))
   parts.append('<h'+str(level)+'>'+esc(heading[2])+'</h'+str(level)+'>')
  elif bullet:
   flush();newkind='ul' if bullet[1]=='- ' else 'ol'
   if kind!=newkind:close_list();kind=newkind;parts.append('<'+kind+'>')
   parts.append('<li>'+esc(bullet[2])+'</li>')
  elif not line.strip():flush();close_list()
  else:close_list();paragraph.append(line)
 flush();close_list();return ''.join(parts)
def actions(page,english):
 if page not in links_manifest:raise ValueError('Generate WhatsApp action with canonical link tool before publication: '+page)
 send='Send to your agent on WhatsApp' if english else 'שלח לסוכן בוואטסאפ'
 add='Add your own recipe' if english else 'הוסף מתכון משלך'
 note='Opens a short request with this recipe link. Review and send it yourself.' if english else 'פותח בקשה קצרה עם קישור למתכון. אתם בודקים ושולחים.'
 return '<div class="recipe-actions"><a class="button" href="'+esc(links_manifest[page])+'" rel="noopener noreferrer">'+send+' ↗</a><a class="button secondary" href="'+esc(SUBMIT)+'">'+add+' ↗</a></div><p class="recipe-note">'+note+'</p>'
def shell(title,desc,url,english,body,schema):
 lang='en' if english else 'he';direction='ltr' if english else 'rtl'
 home='Recipe library' if english else 'מאגר המתכונים'
 brand='Instinct Israel' if english else 'אינסטינקט ישראל'
 about='About the library' if english else 'על המאגר'
 disclaimer='Execution, account access, messages and spending need separate permission. Testing status is the contributor\'s report.' if english else 'הרשאות להרצה, חשבונות, שליחה ותשלום ניתנות בנפרד. רמת הבדיקה היא דיווח של התורם.'
 return '<!doctype html><html lang="'+lang+'" dir="'+direction+'"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>'+esc(title)+' | Personal AI agent recipes</title><meta name="description" content="'+esc(desc[:150])+'"><link rel="canonical" href="'+url+'"><link rel="stylesheet" href="../style.css"><script type="application/ld+json">'+json.dumps(schema,ensure_ascii=False).replace('<','\\u003c')+'</script></head><body><header><a class="brand" href="../"><img src="../instinct-logo.png" alt="" class="brand-logo">'+brand+'</a><nav><a href="../about.html">'+about+'</a><a href="https://github.com/ofershap/agent-success-hub">GitHub ↗</a></nav></header><main class="recipe-main">'+body+'</main><footer><p><img src="../instinct-logo.png" alt="Instinct" class="instinct-logo">Instinct · Personal AI agent recipes</p><p>'+disclaimer+'</p><a href="../">'+home+'</a></footer><script src="../recipe-copy.js"></script></body></html>'
data=json.loads((r/'docs/entries.json').read_text());out=r/'docs/recipes';out.mkdir(exist_ok=True)
links=[];urls=[BASE,BASE+'about.html',BASE+'submit.html']
for old in out.glob('*.html'):old.unlink()
for i,d in enumerate(data):
 m=re.search(r'/issues/(\d+)$',d.get('issue',''));key='issue-'+m[1] if m else 'entry-'+str(i+1)
 page=key+'.html';url=BASE+'recipes/'+page;urls.append(url);links.append((d['title'],url))
 labels=[('request','מה ביקשתי'),('actions','מה נעשה'),('worked','מה עבד'),('failed','מה לא נבדק'),('prompt','המתכון המלא')]
 nav='<nav class="recipe-nav" aria-label="תוכן המתכון"><p>בתוך המתכון</p>'+''.join('<a href="#'+k+'">'+label+'</a>' for k,label in labels)+'</nav>'
 fields=''.join('<section class="recipe-section" id="'+k+'"><h2>'+label+'</h2>'+('<div class="recipe-text">'+markdown(d[k])+'</div>' if k=='prompt' else '<pre>'+esc(d[k])+'</pre>')+'</section>' for k,label in labels)
 schema={'@context':'https://schema.org','@type':'CreativeWork','name':d['title'],'inLanguage':'he','url':url}
 if d.get('author'):schema['author']={'@type':'Person','name':d['author']}
 enlink='<a class="recipe-lang" lang="en" dir="ltr" href="'+key+'-en.html">Read in English ↗</a>' if d.get('recipe_en') else ''
 intro='<section class="recipe-intro"><p class="eyebrow">מתכון מהקהילה / סוכן AI אישי</p><h1>'+esc(d['title'])+'</h1>'+enlink+actions(page,False)+'</section>'
 summary='<section class="recipe-summary" lang="en" dir="ltr"><h2>English summary</h2><p>'+esc(d['english'])+'</p></section>'
 provenance='<p class="recipe-provenance">GitHub: '+esc(d.get('author',''))+'</p>'
 (out/page).write_text(shell(d['title'],d['request'],url,False,intro+'<div class="recipe-layout">'+nav+'<div>'+fields+summary+provenance+'<aside>ההגשות בטופס באתר נבדקות פעמיים ביום ומתפרסמות אחרי סינון ואישור. התוכן ציבורי עם הפרסום. מגישים תוכן מאושר לשיתוף, בלי סודות או מידע פרטי.</aside></div></div>',schema))
 if d.get('recipe_en'):
  title=d['recipe_en'].splitlines()[0].lstrip('# ').removeprefix('Draft: ').removeprefix('Review draft: ')
  enpage=key+'-en.html';enurl=BASE+'recipes/'+enpage;urls.append(enurl);links.append((title,enurl))
  enschema={'@context':'https://schema.org','@type':'CreativeWork','name':title,'inLanguage':'en','url':enurl}
  headings=[line.lstrip('# ') for line in d['recipe_en'].splitlines() if line.startswith('## ')]
  entoc='<nav class="recipe-nav" aria-label="Recipe contents"><p>Inside this recipe</p><a href="#recipe-body">The full recipe</a><a href="#copy-recipe">Copy recipe</a></nav>'
  intro='<section class="recipe-intro"><p class="eyebrow">COMMUNITY RECIPE / PERSONAL AI AGENT</p><h1>'+esc(title)+'</h1><a class="recipe-lang" href="'+key+'.html">עברית ↗</a>'+actions(enpage,True)+'</section>'
  content='<div class="recipe-layout">'+entoc+'<div><p class="recipe-summary">English translation of the contributor recipe. Check its testing status and limits before use.</p><button id="copy-recipe" type="button">Copy English recipe</button><article id="recipe-body" class="recipe-text">'+markdown(d['recipe_en'])+'</article><pre id="recipe-en" hidden>'+esc(d['recipe_en'])+'</pre><aside>Website submissions are reviewed twice daily and published after screening and approval. Content is public when published. Share only approved content, without secrets or private information.</aside></div></div>'
  (out/enpage).write_text(shell(title,d['english'],enurl,True,intro+content,enschema))
(r/'docs/sitemap.xml').write_text('<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'+''.join('<url><loc>'+u+'</loc></url>' for u in urls)+'</urlset>')
(r/'docs/llms.txt').write_text((r/'docs/llms.txt').read_text().split('\n## Published recipes')[0]+'\n## Published recipes\n'+''.join('- ['+title.replace('\n',' ')+']('+u+')\n' for title,u in links))
print('Built',len(data),'bilingual recipe pages')
