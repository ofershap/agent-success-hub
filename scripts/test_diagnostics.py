import unittest
from diagnostics import safe_error
class Tests(unittest.TestCase):
 def test_unknown_error_no_submission(self):self.assertNotIn('private customer',safe_error(ValueError('private customer')))
 def test_known_message(self):self.assertIn('ModuleNotFoundError',safe_error(ModuleNotFoundError("No module named 'dependency'")))
 def test_url_secret(self):
  message=safe_error(OSError('load https://test.invalid/?token=abc\nauthorization: private-secret\nhf_1234abcd'))
  self.assertNotIn('private-secret',message);self.assertNotIn('test.invalid',message);self.assertNotIn('hf_1234abcd',message)
if __name__=='__main__':unittest.main()
