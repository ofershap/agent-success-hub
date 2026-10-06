import unittest,json,xml.etree.ElementTree as ET
from pathlib import Path
from urllib.parse import urlparse,parse_qs
r=Path(__file__).resolve().parent.parent
class DiscoveryTests(unittest.TestCase):
 def test_sitemap(self):ET.parse(r/'docs/sitemap.xml')
 def test_button(self):
  from html.parser import HTMLParser
  class P(HTMLParser):
   urls=[]
   def handle_starttag(self,t,a):
    if t=='a':self.urls.extend(v for k,v in a if k=='href' and v.startswith('https://wa.me/'))
  p=P();p.feed((r/'docs/index.html').read_text());self.assertEqual(len(p.urls),1)
  u=urlparse(p.urls[0]);self.assertEqual(u.path,'/16508702892');text=parse_qs(u.query)['text'][0];self.assertIn('והמיזוג שלי',text);self.assertIn('הצג לי את הטקסט המלא לפני הגשה',text);self.assertLessEqual(len(p.urls[0]),2048)
 def test_about(self):self.assertIn('מה נבדק',(r/'docs/about.html').read_text())
if __name__=='__main__':unittest.main()
