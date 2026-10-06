import unittest
from pathlib import Path
from html.parser import HTMLParser
ROOT=Path(__file__).resolve().parent.parent
FORM='https://ofershap.github.io/agent-success-hub/submit.html'
class SubmissionTests(unittest.TestCase):
 def test_schema_and_destination(self):
  page=(ROOT/'docs/submit.html').read_text();script=(ROOT/'docs/submit.js').read_text()
  for term in ['name="website"','maxlength="80"','maxlength="140"','maxlength="4000"','recipe-consent','submit.js']:self.assertIn(term,page)
  for term in ['https://recipe-inbox.ofers.workers.dev','JSON.stringify(payload)','400:','403:','429:','AbortController','finished = true']:self.assertIn(term,script)
 def test_instructions_have_url(self):
  for path in ['docs/llms.txt','AGENTS.md','docs/about.html']:self.assertIn(FORM,(ROOT/path).read_text())
 def test_recipe_destination(self):
  self.assertIn("SUBMIT=BASE+'submit.html'",(ROOT/'scripts/build_recipe_pages.py').read_text())
