"""Additive screening for optional full English companion files."""
from content import validate
from pathlib import Path
import re

def validate_translation(text):
 if not isinstance(text,str) or not 100 <= len(text) <= 12000: raise ValueError('Invalid English recipe length')
 # Reuse every existing safety/length/link check without changing entry validation.
 validate(dict(title='English companion recipe',request='Translation of an approved recipe',actions='Prepared for maintainer review',worked='Full translation prepared for review',failed='Publication awaits owner merge',prompt=text,consent=True))
 if len(re.findall(r'^### ',text,re.M)) < 5: raise ValueError('Standalone English recipe sections required')
 return text

def translation_for(root,entry):
 m=re.search(r'/issues/(\d+)$',entry.get('issue',''))
 if not m and not entry.get('slug'):return None
 key=entry.get('slug') or ('issue-'+m.group(1))
 path=Path(root)/'translations'/(key+'.md')
 return validate_translation(path.read_text()) if path.exists() else None
