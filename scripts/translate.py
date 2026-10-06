"""Local, bounded Hebrew-English excerpt translation. Never execute input."""
from pathlib import Path
import json
MODEL='Helsinki-NLP/opus-mt-tc-big-he-en'
REVISION='134c5a850dcaa763eec85bd1f4eb25112fecedbb'
def translate_entry(d):
 if d.get('english'):return d
 from transformers import MarianMTModel,MarianTokenizer
 tokenizer=MarianTokenizer.from_pretrained(MODEL,revision=REVISION)
 model=MarianMTModel.from_pretrained(MODEL,revision=REVISION,use_safetensors=True)
 parts=[]
 for key in ['title','request','worked','failed']:
  text=d[key][:400]
  inputs=tokenizer([text],return_tensors='pt',truncation=True,max_length=160)
  out=model.generate(**inputs,max_new_tokens=100)
  parts.append(tokenizer.decode(out[0],skip_special_tokens=True))
 d['english']=' '.join(parts)[:1400]
 d['english_source']='machine-local'
 return d
if __name__=='__main__':
 for p in Path('entries').glob('*.json'):
  d=translate_entry(json.loads(p.read_text()))
  p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
