import unittest
from translation_content import validate_translation
class TranslationTests(unittest.TestCase):
 def text(self):return '# Full recipe\n'+''.join('### Section '+str(i)+'\nSafe standalone instructions.\n' for i in range(7))
 def test_valid(self):validate_translation(self.text())
 def test_short(self):
  with self.assertRaises(ValueError):validate_translation('A summary only')
 def test_unsafe(self):
  with self.assertRaises(ValueError):validate_translation(self.text()+'<script>bad</script>')
 def test_oversize(self):
  with self.assertRaises(ValueError):validate_translation(self.text()+'x'*12001)
if __name__=='__main__':unittest.main()
