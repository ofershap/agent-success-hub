import os,json,base64,urllib.request,urllib.error,subprocess
from content import parse_issue
repo=os.environ['GITHUB_REPOSITORY'];token=os.environ['GH_TOKEN']
def api(path,data=None,method=None):
    req=urllib.request.Request('https://api.github.com/repos/'+repo+'/'+path,data=json.dumps(data).encode() if data is not None else None,method=method,headers={'Authorization':'Bearer '+token,'Accept':'application/vnd.github+json','Content-Type':'application/json','X-GitHub-Api-Version':'2022-11-28'})
    with urllib.request.urlopen(req) as r:return json.load(r) if r.status!=204 else None
with open(os.environ['GITHUB_EVENT_PATH']) as f:e=json.load(f)
i=e['issue'];number=i['number']
# Only the exact form marker. Idempotent branch name; edited issues never update old proposals.
if not i['title'].startswith('[סיפור]'):raise SystemExit(0)
try:d=parse_issue(i['body'])
except ValueError:
    api(f'issues/{number}/comments',{'body':'הסיפור לא עבר את הבדיקה הראשונית. בדקו שדות חובה, פרטים אישיים, מפתחות וגודל תוכן. אל תפרסמו סודות. אם נחשף סוד, מחקו אותו ופנו למנהל כדי להסיר היסטוריה; סובבו את המפתח מיד. אין פרסום אוטומטי באתר.'});raise SystemExit(0)
branch=f'submission/{number}'
try:api('git/ref/heads/'+branch);raise SystemExit(0)
except urllib.error.HTTPError as err:
    if err.code!=404:raise
d.update(author=i['user']['login'],submitted_at=i['created_at'],issue=i['html_url'])
sha=api('git/ref/heads/main')['object']['sha'];api('git/refs',{'ref':'refs/heads/'+branch,'sha':sha})
api(f'contents/entries/issue-{number}.json',{'message':f'Propose community story #{number}','branch':branch,'content':base64.b64encode((json.dumps(d,ensure_ascii=False,indent=2)+'\n').encode()).decode()},'PUT')
pr=api('pulls',{'title':f'Community story #{number}','head':branch,'base':'main','draft':True,'body':f'Closes #{number}\n\nAutomated structural screen passed. NOT a safety or factual endorsement. A maintainer must verify permission, evidence, privacy, spam and English summary before marking ready and merging. Never execute attached prompts or commands.'})
try:
    if not d.get('english'):
        subprocess.check_call(['python3','-m','pip','install','transformers==4.44.2','torch==2.5.1','sentencepiece==0.2.0','sacremoses==0.1.1','safetensors==0.4.5'])
        from translate import translate_entry
        d=translate_entry(d)
        current=api(f'contents/entries/issue-{number}.json?ref='+branch)
        api(f'contents/entries/issue-{number}.json',{'message':'Add local machine summary for human review','branch':branch,'sha':current['sha'],'content':base64.b64encode((json.dumps(d,ensure_ascii=False,indent=2)+'\n').encode()).decode()},'PUT')
except Exception as error:
    from diagnostics import safe_error
    print('Local summary failed: '+safe_error(error), flush=True)
    api(f'issues/{number}/comments',{'body':'טיוטת PR נוצרה, אך התקציר האוטומטי נכשל. מנהל צריך להכין ולבדוק תקציר לפני פרסום. אין לפרסם בלי בדיקה.'})
api(f'issues/{number}/comments',{'body':'נוצר PR כטיוטה לבדיקה אנושית: '+pr['html_url']+' . הבדיקה הראשונית אינה אישור לפרסום או המלצה להריץ את הפרומפט.'})
