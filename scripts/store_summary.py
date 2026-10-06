import os,json,base64,urllib.request
repo=os.environ['GITHUB_REPOSITORY'];n=os.environ['NUMBER']
if not n.isdigit():raise ValueError('Invalid ID')
url=f'https://api.github.com/repos/{repo}/contents/entries/issue-{n}.json'
headers={'Authorization':'Bearer '+os.environ['GH_TOKEN'],'Accept':'application/vnd.github+json'}
with urllib.request.urlopen(urllib.request.Request(url+'?ref=submission/'+n,headers=headers)) as r:old=json.load(r)
with open(f'entries/issue-{n}.json','rb') as f:content=base64.b64encode(f.read()).decode()
data={'message':'Add local machine summary for human review','sha':old['sha'],'branch':'submission/'+n,'content':content}
with urllib.request.urlopen(urllib.request.Request(url,headers=headers,data=json.dumps(data).encode(),method='PUT')) as r:print('Stored summary for review:',r.status)
