import json,unittest,re
from pathlib import Path
from urllib.parse import urlparse,parse_qs
class RecipeActions(unittest.TestCase):
 def test_canonical_links(self):
  root=Path(__file__).resolve().parent.parent
  links=json.loads((root/'docs/recipe-whatsapp-links.json').read_text())
  for filename,link in links.items():
   self.assertLessEqual(len(link),2048)
   self.assertEqual(urlparse(link).path,'/16508702892')
   message=parse_qs(urlparse(link).query)['text'][0]
   self.assertTrue(message.endswith('https://ofershap.github.io/agent-success-hub/recipes/'+filename))
 def test_all_current_recipes_have_actions(self):
  root=Path(__file__).resolve().parent.parent
  links=json.loads((root/'docs/recipe-whatsapp-links.json').read_text())
  for file in (root/'entries').glob('*.json'):
   data=json.loads(file.read_text());key='issue-'+re.search(r'/issues/(\d+)$',data['issue'])[1]
   self.assertIn(key+'.html',links)
   if (root/'translations'/f'{key}.md').exists():self.assertIn(key+'-en.html',links)
