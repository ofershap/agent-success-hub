"""Offline content gate scope fixtures; never execute contributor code."""
import unittest,tempfile,json,os,runpy,urllib.request
from unittest.mock import patch
class Resp:
 def __init__(self,data):self.data=data
 def __enter__(self):return self
 def __exit__(self,*a):pass
 def read(self):return json.dumps(self.data).encode()
class GateTests(unittest.TestCase):
 def check(self,files):
  with tempfile.NamedTemporaryFile(mode='w') as f:
   json.dump({'pull_request':{'number':1,'changed_files':len(files),'head':{'repo':{'full_name':'fixture/only'}}}},f);f.flush()
   with patch.dict(os.environ,{'GITHUB_EVENT_PATH':f.name,'GITHUB_REPOSITORY':'fixture/only','GH_TOKEN':'fixture-only'}),patch('urllib.request.urlopen',return_value=Resp(files)):
    runpy.run_path('scripts/check_pr.py')
 def test_code_scope_not_applicable(self):
  with self.assertRaises(SystemExit) as c:self.check([{'filename':'scripts/content.py','status':'modified'}])
  self.assertEqual(c.exception.code,0)
 def test_entries_still_screened(self):
  with self.assertRaises(ValueError):self.check([{'filename':'entries/not-a-json.py','status':'added'}])
 def test_mixed_content_code_rejected(self):
  with self.assertRaises(ValueError):self.check([{'filename':'scripts/content.py','status':'modified'},{'filename':'entries/safe.json','status':'added'}])
if __name__=='__main__':unittest.main()
