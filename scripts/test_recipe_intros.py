import json,unittest,re
from pathlib import Path
ROOT=Path(__file__).resolve().parent.parent
class RecipeIntros(unittest.TestCase):
 def test_all_published_recipes_have_editorial_frame(self):
  intros=json.loads((ROOT/'docs/recipe-intros.json').read_text())
  for path in (ROOT/'entries').glob('*.json'):
   data=json.loads(path.read_text());key=data.get('slug') or ('issue-'+re.search(r'/issues/(\d+)$',data['issue'])[1])
   for field in ['title','description','prepare','tools','en_title','en_description','en_prepare','en_tools']:self.assertTrue(intros[key][field])
 def test_getting_started_is_linked(self):
  for file in ['docs/index.html','docs/about.html','docs/llms.txt']:self.assertIn('start.html',(ROOT/file).read_text())
