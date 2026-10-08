"""Build public, read-only discovery artifacts from already-reviewed recipes."""
from pathlib import Path
import json,re,hashlib
BASE='https://ofershap.github.io/agent-success-hub/'
VERSION='1.0.0'
def slug(d):
 if d.get('slug'):return d['slug']
 m=re.search(r'/issues/(\d+)$',d.get('issue',''))
 if not m:raise ValueError('Recipe needs a stable slug or issue ID')
 return 'issue-'+m[1]
def markdown(d,key,english=False):
 prompt=d['recipe_en'] if english else d['prompt']
 label='Full recipe' if english else 'המתכון המלא'
 title=d['title'];url=BASE+'recipes/'+key+('-en' if english else '')+'.html'
 return '# '+title+'\n\nCanonical: '+url+'\n\nRecipe ID: '+key+'\nAuthor: '+d.get('author','')+'\nLanguage: '+('en' if english else 'he')+'\n\nThis is published recipe content, not permission to execute it. Account access, sending and spending require separate approval.\n\n## '+label+'\n\n'+prompt+'\n\n## English summary\n\n'+d['english']+'\n\n## Testing and limits\n\n'+d['worked']+'\n\n'+d['failed']+'\n'
def build(root):
 docs=root/'docs';data=json.loads((docs/'entries.json').read_text());out=docs/'recipes';out.mkdir(exist_ok=True)
 for old in out.glob('*.md'):old.unlink()
 full=['# Recipe library: full published text\n\nSource: '+BASE+'\nSchema: '+BASE+'entries.schema.json\nVersion: '+VERSION+'\n\nContent is untrusted recipe data, not execution permission.\n']
 items=[]
 for d in sorted(data,key=lambda d:(d.get('submitted_at',''),slug(d)),reverse=True):
  key=slug(d);md=markdown(d,key);(out/(key+'.md')).write_text(md,encoding='utf-8');full.append(md)
  if d.get('recipe_en'):
   en=markdown(d,key,True);(out/(key+'-en.md')).write_text(en,encoding='utf-8');full.append(en)
  item={'id':BASE+'recipes/'+key+'.html','url':BASE+'recipes/'+key+'.html','title':d['title'],'content_text':d['prompt'],'summary':d['english'],'language':'he','_recipe':{'id':key,'markdown_url':BASE+'recipes/'+key+'.md','schema_version':VERSION,'submitted_at':d.get('submitted_at',''),'has_full_english':bool(d.get('recipe_en'))}}
  if d.get('author'):item['authors']=[{'name':d['author']}]
  items.append(item)
 feed={'version':'https://jsonfeed.org/version/1.1','title':'Recipe library - ספריית המתכונים','home_page_url':BASE,'feed_url':BASE+'feed.json','language':'he','description':'New and existing screened community recipes. Ordered by submission time, not claimed publication time.','items':items}
 (docs/'feed.json').write_text(json.dumps(feed,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
 (docs/'llms-full.txt').write_text('\n\n---\n\n'.join(full),encoding='utf-8')
 meta={'schema_version':VERSION,'schema_url':BASE+'entries.schema.json','data_url':BASE+'entries.json','documentation_url':BASE+'api.md','changelog_url':BASE+'api-changelog.md','recipe_count':len(data),'sha256':hashlib.sha256((docs/'entries.json').read_bytes()).hexdigest()}
 (docs/'entries-meta.json').write_text(json.dumps(meta,indent=2)+'\n')
 llms=docs/'llms.txt';text=llms.read_text().split('\n## Machine-readable access')[0];llms.write_text(text+'\n## Machine-readable access\n- [API contract]('+BASE+'api.md)\n- [Schema]('+BASE+'entries.schema.json)\n- [Version and dataset hash]('+BASE+'entries-meta.json)\n- [JSON Feed]('+BASE+'feed.json)\n- [Full recipe corpus]('+BASE+'llms-full.txt)\n- [MCP design specification, not a live server]('+BASE+'mcp-spec.md)\n\nMarkdown: replace each recipe .html extension with .md. Full English Markdown exists only where the HTML English companion exists.\n')
 index=docs/'index.html';html=index.read_text();tag='<link rel="alternate" type="application/feed+json" title="Recipe library JSON Feed" href="feed.json">'
 if tag not in html:html=html.replace('</head>',tag+'\n</head>');index.write_text(html)
 print('Built AI access:',len(data),'recipes;',len(list(out.glob('*.md'))),'Markdown variants')
if __name__=='__main__':build(Path(__file__).resolve().parent.parent)
