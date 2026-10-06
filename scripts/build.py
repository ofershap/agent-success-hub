from pathlib import Path
import json,html
from content import validate,summary
root=Path(__file__).resolve().parent.parent
items=[]
for path in sorted((root/'entries').glob('*.json')):
 d=validate(json.loads(path.read_text()));
 if not d.get('english'):raise ValueError('English summary required before publication: '+str(path))
 s,kind=summary(d);d.update(english=s,english_kind=kind);items.append(d)
(root/'docs'/'entries.json').write_text(json.dumps(items,ensure_ascii=False))
print('Validated and built',len(items),'published entries')
