"""Validate PR data using trusted base code, without checking out contributor code."""
import json,os,urllib.request,re
from content import validate
from translation_content import validate_translation
with open(os.environ['GITHUB_EVENT_PATH']) as f:event=json.load(f)
pr=event['pull_request'];repo=os.environ['GITHUB_REPOSITORY']
def get(url):
 req=urllib.request.Request(url,headers={'Authorization':'Bearer '+os.environ['GH_TOKEN'],'Accept':'application/vnd.github+json'})
 with urllib.request.urlopen(req) as r:return json.load(r)
base='https://api.github.com/repos/'+repo
files=get(base+'/pulls/'+str(pr['number'])+'/files?per_page=100')
if pr['changed_files']>20:raise ValueError('Too many changed files')
if not files:raise ValueError('No changed files')
# Path-based scope only: labels and contributor instructions cannot exempt content.
if not any(f['filename'].startswith(('entries/','translations/')) for f in files):
 print('No entry data changed: content screen not applicable. This is not code review.');raise SystemExit(0)
for f in files:
 if not re.fullmatch(r'(entries/[a-z0-9][a-z0-9-]{0,100}\.json|translations/issue-[0-9]+\.md)',f['filename']) or f['status'] not in ('added','modified'):
  raise ValueError('Story PR may only add or edit entries/*.json')
 head=pr['head']['repo']['full_name']
 blob=get('https://api.github.com/repos/'+head+'/git/blobs/'+f['sha'])
 import base64
 if blob['size']>50000:raise ValueError('Too large')
 if f['filename'].startswith('translations/'):
  validate_translation(base64.b64decode(blob['content']).decode('utf-8'));continue
 d=validate(json.loads(base64.b64decode(blob['content'])))
 if not d.get('english'):raise ValueError('English summary needs review before merge')
print('Story data screen passed. A maintainer must still review permission, privacy, safety and accuracy.')
