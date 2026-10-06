'use strict';
document.querySelectorAll('[data-copy]').forEach(button => button.addEventListener('click', async () => {
 const english=document.documentElement.lang==='en';
 try { await navigator.clipboard.writeText(document.getElementById(button.dataset.copy).textContent); button.textContent=english?'Copied':'המתכון הועתק'; }
 catch { button.textContent=english?'Select the full recipe text to copy':'סמנו את טקסט המתכון והעתיקו'; }
}));
