"""Treat submissions as data. Never execute prompts, code or supplied URLs."""
import re, json
FIELDS=['title','request','actions','worked','failed','prompt','tools','evidence','consent']
REQUIRED=FIELDS[:6]
def validate(d):
    if not isinstance(d,dict) or set(d)-set(FIELDS+['english','english_source','author','submitted_at','issue','slug']): raise ValueError('Unexpected fields')
    for key in REQUIRED:
        if not isinstance(d.get(key),str) or not 10 <= len(d[key]) <= 12000: raise ValueError('Missing or oversized field: '+key)
    if sum(len(str(v)) for v in d.values())>40000:raise ValueError('Submission too large')
    if d.get('consent') is not True:raise ValueError('Public sharing consent required')
    for key in ['tools','evidence','english','author','submitted_at','issue','english_source','slug']:
        if key in d and (not isinstance(d[key],str) or len(d[key])>1600):raise ValueError('Invalid optional field: '+key)
    if d.get('slug') and not re.fullmatch(r'[a-z0-9][a-z0-9-]{2,79}',d['slug']):raise ValueError('Invalid stable slug')
    text='\n'.join(str(v) for v in d.values())
    patterns=[r'gh[pousr]_[A-Za-z0-9]{20,}',r'github_pat_[A-Za-z0-9_]{20,}',r'AKIA[0-9A-Z]{16}',r'-----BEGIN .*PRIVATE KEY',r'sk-[A-Za-z0-9_-]{20,}',r'(?i)(password|api[_ -]?key|access[_ -]?token)\s*[:=]\s*[\x22\x27]?\S{8,}',r'(?i)<\s*(script|iframe|object|embed)\b',r'(?i)javascript:',r'(?i)curl\s+[^\n]*\|\s*(bash|sh)',r'(?i)rm\s+-rf\s+/',r'(?i)(steal|exfiltrate)\s+(credentials|passwords|secrets)',r'(?i)(גניבת סיסמאות|איסוף סיסמאות|דליפת מפתחות)']
    if any(re.search(p,text) for p in patterns):raise ValueError('Sensitive or unsafe content: human redaction needed')
    if len(re.findall(r'https?://',text))>8:raise ValueError('Too many links: spam review needed')
    for url in re.findall(r'https?://[^\s<>]+',str(d.get('evidence',''))):
        if not url.startswith('https://'):raise ValueError('Evidence must use HTTPS')
    return d

def summary(d):
    # No AI service or paid API. Do not pretend metadata is a semantic translation.
    if d.get('english'):return d['english'], ('machine-local' if d.get('english_source') == 'machine-local' else 'author')
    tools=re.sub(r'[^A-Za-z0-9 .,/#_+-]','',str(d.get('tools',''))).strip()[:100]
    return ('A community report documents an agent-assisted task, the steps taken, what worked, what failed, and a reusable prompt.'+(' Tools: '+tools+'.' if tools else '')), 'automatic-metadata'

def parse_issue(body):
    mapping={'title':'כותרת','request':'מה ביקשתי','actions':'מה הסוכן עשה','worked':'מה עבד','failed':'מה לא עבד ומה עוד לא נבדק','prompt':'הסקיל או הפרומפט','tools':'כלים וסביבה','evidence':'קישור ציבורי להוכחה','english':'תקציר באנגלית (לא חובה)'}
    labels=list(mapping.values())+['אישור פרסום']
    delimiters='|'.join(re.escape(label) for label in labels)
    sections={m.group(1).strip():m.group(2).strip() for m in re.finditer(r'^### ('+delimiters+r')\n\n(.*?)(?=\n### (?:'+delimiters+r')\n|\Z)',body,re.M|re.S)}
    d={k:sections.get(v,'').replace('_No response_','').strip() for k,v in mapping.items()}
    d['consent']='[X]' in sections.get('אישור פרסום','') or '[x]' in sections.get('אישור פרסום','')
    return validate(d)
