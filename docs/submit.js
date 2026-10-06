(() => {
  const form = document.getElementById('recipe-form');
  const text = document.getElementById('recipe-text');
  const counter = document.getElementById('recipe-counter');
  const status = document.getElementById('recipe-status');
  const button = document.getElementById('recipe-submit');
  let pending = false, finished = false;
  text.addEventListener('input', () => { counter.textContent = `${text.value.length.toLocaleString('en-US')} / 4,000`; });
  form.addEventListener('submit', async (event) => {
    event.preventDefault();
    if (pending || finished || !form.reportValidity()) return;
    const payload = {name: form.elements.name.value.trim(), title: form.elements.title.value.trim(), text: text.value.trim(), website: form.elements.website.value};
    if (!payload.title || !payload.text) { status.textContent = 'השלימו כותרת ומתכון לפני השליחה. / Add a title and recipe before sending.'; return; }
    pending = true; button.disabled = true; button.textContent = 'שולח…'; status.textContent = '';
    const controller = new AbortController();
    const timer = setTimeout(() => controller.abort(), 20000);
    try {
      const response = await fetch('https://recipe-inbox.ofers.workers.dev', {method: 'POST', headers: {'Content-Type': 'application/json'}, body: JSON.stringify(payload), signal: controller.signal});
      if (!response.ok) {
        const messages = {
          400: 'בדקו את השדות ואורך הטקסט ונסו שוב. / Check the fields and text length, then try again.',
          403: 'ההגשה נחסמה. נסו דרך האתר או השתמשו בחלופת GitHub. / Submission blocked. Use this website or the GitHub option.',
          429: 'הגעתם למגבלת ההגשות. המתינו לפני ניסיון נוסף. / Too many submissions. Please wait before trying again.'
        };
        throw new Error(messages[response.status] || 'שירות ההגשה אינו זמין כרגע. הטקסט נשאר בטופס. / The service is unavailable. Your text is still in the form.');
      }
      finished = true;
      status.className = 'submission-success';
      status.textContent = 'המתכון התקבל לבדיקה. ההגשות נבדקות פעמיים ביום ומתפרסמות לאחר סינון ואישור. התוכן יהיה ציבורי מיד עם הפרסום. / Recipe received for review. Submissions are reviewed twice daily and published after screening and approval. Content is public when published.';
      button.textContent = 'המתכון נשלח';
      [...form.elements].forEach(field => { field.disabled = true; });
      status.focus();
    } catch (error) {
      status.className = 'submission-error';
      status.textContent = error.name === 'AbortError' || error instanceof TypeError
        ? 'לא התקבל אישור קליטה. ייתכן שההגשה הגיעה. הטקסט נשאר בטופס; בדקו לפני שליחה חוזרת. / No receipt confirmation. The submission may have arrived. Your text remains in the form; check before resending.'
        : error.message;
      button.disabled = false; button.textContent = 'שלח מתכון לבדיקה';
    } finally { clearTimeout(timer); pending = false; }
  });
})();
