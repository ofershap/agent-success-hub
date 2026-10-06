import json, unittest
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parent.parent

class CarRecipe(unittest.TestCase):
    def test_credit_and_testing_status(self):
        entry = json.loads((ROOT / 'entries/issue-25.json').read_text())
        self.assertEqual(entry['author'], 'נתנאל באבא')
        self.assertIn('לא נמסרו תוצאות', entry['worked'])
        self.assertIn('לא הוכח', entry['prompt'])
        self.assertIn('בלי אישור נפרד', entry['prompt'])
        self.assertEqual(urlparse(entry['issue']).path, '/ofershap/agent-success-hub/issues/25')
        english = (ROOT / 'translations/issue-25.md').read_text()
        self.assertIn('No results from a completed comparison', english)
        self.assertIn('without separate approval', english)

if __name__ == '__main__':
    unittest.main()
