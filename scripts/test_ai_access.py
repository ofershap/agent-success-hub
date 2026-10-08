import unittest,json,tempfile,shutil,re
from pathlib import Path
from build_ai_access import build,slug
class AIAccessTests(unittest.TestCase):
 def test_artifacts_preserve_sources_and_shape(self):
  root=Path(__file__).resolve().parent.parent
  with tempfile.TemporaryDirectory() as t:
   r=Path(t);shutil.copytree(root/'docs',r/'docs');raw=(r/'docs/entries.json').read_bytes();build(r);self.assertEqual(raw,(r/'docs/entries.json').read_bytes());data=json.loads(raw);feed=json.loads((r/'docs/feed.json').read_text());self.assertEqual(len(data),len(feed['items']));self.assertEqual(feed['version'],'https://jsonfeed.org/version/1.1');self.assertEqual(len(set(x['id'] for x in feed['items'])),len(data));self.assertEqual(json.loads((r/'docs/entries-meta.json').read_text())['recipe_count'],len(data))
   by={x['_recipe']['id']:x for x in feed['items']}
   for d in data:
    k=slug(d);self.assertEqual(by[k]['content_text'],d['prompt']);self.assertNotIn('date_published',by[k]);self.assertIn(d['prompt'],(r/'docs/recipes'/ (k+'.md')).read_text());self.assertIn(d['prompt'],(r/'docs/llms-full.txt').read_text());self.assertEqual((r/'docs/recipes'/(k+'-en.md')).exists(),bool(d.get('recipe_en')))
 def test_schema_matches_current_data(self):
  r=Path(__file__).resolve().parent.parent;s=json.loads((r/'docs/entries.schema.json').read_text());data=json.loads((r/'docs/entries.json').read_text())
  for d in data:
   self.assertFalse(set(d)-set(s['items']['properties']));self.assertTrue(set(s['items']['required'])<=set(d));self.assertTrue(d.get('slug') or d.get('issue'))
if __name__=='__main__':unittest.main()
