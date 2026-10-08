"""Build escaped recipe pages with reviewed text and canonical action links."""
from pathlib import Path
import html,json,re
r=Path(__file__).resolve().parent.parent
BASE='https://ofershap.github.io/agent-success-hub/'
SUBMIT=BASE+'submit.html'
esc=lambda t:html.escape(str(t),quote=True)
links_manifest=json.loads((r/'docs/recipe-whatsapp-links.json').read_text())
intros=json.loads((r/'docs/recipe-intros.json').read_text())
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
 note='WhatsApp opens a short request with this recipe link. Review it before sending. You can also copy the full recipe below.' if english else 'בוואטסאפ נפתחת בקשה קצרה עם קישור למתכון. אתם קוראים ושולחים. אפשר גם להעתיק את המתכון המלא בהמשך.'
 return '<div class="recipe-actions"><a class="button" href="'+esc(links_manifest[page])+'" rel="noopener noreferrer">'+send+' ↗</a><a class="button secondary" href="'+esc(SUBMIT)+'">'+add+' ↗</a></div><p class="recipe-note">'+note+'</p>'
def orientation(key,english):
 d=intros[key];prefix='en_' if english else ''
 label='Before you start' if english else 'לפני שמתחילים'
 prepare='Prepare' if english else 'מה להכין'
 tools='Tools and permission' if english else 'כלים והרשאות'
 steps=['Read the full recipe and check it fits your task.','Add your details, links and allowed actions.','Share it with your agent, then check the result.'] if english else ['קראו את המתכון המלא ובדקו שהוא מתאים למשימה.','הוסיפו את הפרטים, הקישורים והפעולות שמותר לבצע.','תנו לסוכן את המתכון ובדקו את התוצאה.']
 guide='New to recipes? Read the short guide (Hebrew)' if english else 'לשימוש ראשון: קראו את המדריך הקצר'
 return '<section id="before-start" class="recipe-quick"><h2>'+label+'</h2><dl><dt>'+prepare+'</dt><dd>'+esc(d[prefix+'prepare'])+'</dd><dt>'+tools+'</dt><dd>'+esc(d[prefix+'tools'])+'</dd></dl><ol>'+''.join('<li>'+x+'</li>' for x in steps)+'</ol><a href="../start.html">'+guide+' ←</a></section>'
def shell(title,desc,url,english,body,schema):
 lang='en' if english else 'he';direction='ltr' if english else 'rtl'
 home='Recipe library' if english else 'ספריית המתכונים'
 brand='Instinct Israel' if english else 'אינסטינקט ישראל'
 about='About the library' if english else 'על הספרייה'
 disclaimer='Execution, account access, messages and spending need separate permission. Testing status is the contributor\'s report.' if english else 'הרשאות להרצה, חשבונות, שליחה ותשלום ניתנות בנפרד. רמת הבדיקה היא דיווח של התורם.'
 return '<!doctype html><html lang="'+lang+'" dir="'+direction+'"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>'+esc(title)+' | Personal AI agent recipes</title><meta name="description" content="'+esc(desc[:150])+'"><link rel="canonical" href="'+url+'"><link rel="stylesheet" href="../style.css"><script type="application/ld+json">'+json.dumps(schema,ensure_ascii=False).replace('<','\\u003c')+'</script></head><body><a class="skip-link" href="#recipe-content">'+('Skip to recipe' if english else 'למתכון')+'</a><header><a class="brand" href="../"><img src="../instinct-logo.png" alt="" class="brand-logo">'+brand+'</a><nav><a href="../start.html">'+('Getting started (Hebrew)' if english else 'מתחילים כאן')+'</a><a href="../about.html">'+about+'</a><a href="https://github.com/ofershap/agent-success-hub">GitHub ↗</a></nav></header><main id="recipe-content" class="recipe-main">'+body+'</main><footer><p><img src="../instinct-logo.png" alt="Instinct" class="instinct-logo">Instinct · Personal AI agent recipes</p><p>'+disclaimer+'</p><a href="../">'+home+'</a></footer><script src="../recipe-copy.js"></script></body></html>'
data=json.loads((r/'docs/entries.json').read_text());out=r/'docs/recipes';out.mkdir(exist_ok=True)
links=[];urls=[BASE,BASE+'about.html',BASE+'submit.html',BASE+'start.html']
for old in out.glob('*.html'):old.unlink()
for i,d in enumerate(data):
 m=re.search(r'/issues/(\d+)$',d.get('issue',''));key=d.get('slug') or ('issue-'+m[1] if m else 'entry-'+str(i+1))
 dmeta=intros[key]
 page=key+'.html';url=BASE+'recipes/'+page;urls.append(url);links.append((d['title'],url))
 labels=[('before-start','לפני שמתחילים'),('prompt','המתכון המלא'),('background','רקע ובדיקות')]
 nav='<nav class="recipe-nav" aria-label="תוכן המתכון"><p>בעמוד הזה</p>'+''.join('<a href="#'+k+'">'+label+'</a>' for k,label in labels)+'</nav>'
 fields=orientation(key,False)+'<section class="recipe-section" id="prompt"><h2>המתכון המלא</h2><p class="recipe-note">הטקסט המקורי המאושר של התורם. התאימו את הפרטים למשימה שלכם.</p><button class="copy-recipe-button" data-copy="recipe-he" type="button">העתק מתכון</button><div class="recipe-text">'+markdown(d['prompt'])+'</div><pre id="recipe-he" hidden>'+esc(d['prompt'])+'</pre></section>'
 background=[('request','הבקשה המקורית'),('actions','דרך העבודה'),('worked','מה התורם דיווח שעבד'),('failed','מגבלות ובדיקות נוספות')]
 fields+='<details class="recipe-background" id="background"><summary>רקע המתכון ומה נבדק</summary>'+''.join('<section class="recipe-section"><h3>'+label+'</h3><pre>'+esc(d[k])+'</pre></section>' for k,label in background)+'</details>'
 schema={'@context':'https://schema.org','@type':'CreativeWork','name':dmeta['title'],'inLanguage':'he','url':url}
 if d.get('author'):schema['author']={'@type':'Person','name':d['author']}
 enlink='<a class="recipe-lang" lang="en" dir="ltr" href="'+key+'-en.html">Read in English ↗</a>' if d.get('recipe_en') else ''
 intro='<section class="recipe-intro"><p class="eyebrow">מתכון מהקהילה / סוכן AI אישי</p><h1>'+esc(dmeta['title'])+'</h1><p class="recipe-deck">'+esc(dmeta['description'])+'</p>'+enlink+actions(page,False)+'</section>'
 summary='<section class="recipe-summary" lang="en" dir="ltr"><h2>English summary</h2><p>'+esc(d['english'])+'</p></section>'
 provenance='<p class="recipe-provenance">מאת: '+esc(d.get('author',''))+'</p>'
 (out/page).write_text(shell(dmeta['title'],dmeta['description'],url,False,intro+'<div class="recipe-layout">'+nav+'<div>'+fields+summary+provenance+'<aside>ההגשות בטופס באתר נבדקות פעמיים ביום ומתפרסמות אחרי סינון ואישור. התוכן ציבורי עם הפרסום. מגישים תוכן מאושר לשיתוף, בלי סודות או מידע פרטי.</aside></div></div>',schema))
 if d.get('recipe_en'):
  title=dmeta['en_title']
  enpage=key+'-en.html';enurl=BASE+'recipes/'+enpage;urls.append(enurl);links.append((title,enurl))
  enschema={'@context':'https://schema.org','@type':'CreativeWork','name':title,'inLanguage':'en','url':enurl}
  if d.get('author'):enschema['author']={'@type':'Person','name':d['author']}
  headings=[line.lstrip('# ') for line in d['recipe_en'].splitlines() if line.startswith('## ')]
  entoc='<nav class="recipe-nav" aria-label="Recipe contents"><p>Inside this recipe</p><a href="#before-start">Before you start</a><a href="#recipe-body">The full recipe</a><a href="#copy-recipe">Copy recipe</a></nav>'
  intro='<section class="recipe-intro"><p class="eyebrow">COMMUNITY RECIPE / PERSONAL AI AGENT</p><h1>'+esc(title)+'</h1><p class="recipe-deck">'+esc(dmeta['en_description'])+'</p><a class="recipe-lang" href="'+key+'.html">עברית ↗</a>'+actions(enpage,True)+'</section>'
  content='<div class="recipe-layout">'+entoc+'<div>'+orientation(key,True)+'<p class="recipe-summary">English translation of the contributor recipe. Check its testing status and limits before use.</p><button id="copy-recipe" class="copy-recipe-button" data-copy="recipe-en" type="button">Copy recipe</button><article id="recipe-body" class="recipe-text">'+markdown(d['recipe_en'])+'</article><pre id="recipe-en" hidden>'+esc(d['recipe_en'])+'</pre><aside>Website submissions are reviewed twice daily and published after screening and approval. Content is public when published. Share only approved content, without secrets or private information.</aside></div></div>'
  (out/enpage).write_text(shell(title,d['english'],enurl,True,intro+content+'<p class="recipe-provenance">By: '+esc(d.get('author',''))+'</p>',enschema))
(r/'docs/sitemap.xml').write_text('<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'+''.join('<url><loc>'+u+'</loc></url>' for u in urls)+'</urlset>')
(r/'docs/llms.txt').write_text((r/'docs/llms.txt').read_text().split('\n## Published recipes')[0]+'\n## Published recipes\n'+''.join('- ['+title.replace('\n',' ')+']('+u+')\n' for title,u in links))
print('Built',len(data),'bilingual recipe pages')
# Keep all public discovery formats synchronized with the HTML deployment.
from build_ai_access import build as build_ai_access
build_ai_access(r)
