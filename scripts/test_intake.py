"""Offline end-to-end API fixture. No GitHub requests or public writes."""
import unittest,tempfile,json,os,runpy,sys,types,urllib.error
from unittest.mock import patch
class Response:
 def __init__(self,data,status=200):self.data=data;self.status=status
 def __enter__(self):return self
 def __exit__(self,*a):pass
 def read(self):return json.dumps(self.data).encode()
class IntakeTest(unittest.TestCase):
 def run_case(self,unsafe=False):
  labels={'title':'כותרת','request':'מה ביקשתי','actions':'מה הסוכן עשה','worked':'מה עבד','failed':'מה לא עבד ומה עוד לא נבדק','prompt':'הסקיל או הפרומפט'}
  values={k:'טקסט בדיקה בלבד - אין לפרסום' for k in labels}
  if unsafe:values['prompt']='-----BEGIN RSA PRIVATE KEY-----'
  body='\n\n'.join('### '+v+'\n\n'+values[k] for k,v in labels.items())+'\n\n### אישור פרסום\n\n- [X] agreed'
  event={'issue':{'title':'[סיפור] בדיקה טכנית בלבד','body':body,'number':123,'user':{'login':'fixture-only'},'created_at':'2026-10-06T10:00:00Z','html_url':'https://example.invalid/fixture'}}
  calls=[]
  def fake(req):
   url=req.full_url;payload=json.loads(req.data) if req.data else None;calls.append((url,payload))
   if '/git/ref/heads/submission/' in url:raise urllib.error.HTTPError(url,404,'Not found',{},None)
   if '/git/ref/heads/main' in url:return Response({'object':{'sha':'trusted-base'}})
   if url.endswith('/pulls'):return Response({'html_url':'https://example.invalid/pr'})
   if '?ref=submission/' in url:return Response({'sha':'old-sha'})
   return Response({})
  with tempfile.NamedTemporaryFile(mode='w') as f:
   json.dump(event,f);f.flush()
   module=types.SimpleNamespace(translate_entry=lambda d:dict(d,english='Technical test only, not for publication.',english_source='machine-local'))
   with patch.dict(os.environ,{'GITHUB_REPOSITORY':'fixture/only','GH_TOKEN':'not-a-secret','GITHUB_EVENT_PATH':f.name}),patch('urllib.request.urlopen',fake),patch('subprocess.check_call',return_value=0),patch.dict(sys.modules,{'translate':module}):
    try:runpy.run_path('scripts/intake.py')
    except SystemExit:pass
  return calls
 def test_form_to_draft_pr_and_summary(self):
  calls=self.run_case();pr=[d for u,d in calls if u.endswith('/pulls')][0]
  self.assertTrue(pr['draft']);self.assertEqual(pr['base'],'main')
  self.assertFalse(any('/merge' in u for u,d in calls))
  self.assertTrue(any(d and d.get('message')=='Add local machine summary for human review' for u,d in calls))
 def test_reject_before_branch_write(self):
  calls=self.run_case(True);self.assertEqual(len(calls),1);self.assertIn('/comments',calls[0][0])
if __name__=='__main__':unittest.main()
