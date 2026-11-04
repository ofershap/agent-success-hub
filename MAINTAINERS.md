## Migration 4 November 2026

The sole published library is https://itzik-community-benefits.pages.dev/library/ . This repository remains reviewed recipe source and GitHub intake, not a separate hub. Merge alone does not publish to the benefits site. Run the benefits `refresh-recipes.py`, regenerate missing WhatsApp actions, preview and verify, then promote. Existing twice-daily intake must check the private inbox and newsite receipt before marking complete. Never treat a successful old Pages redirect deployment as recipe publication.

# בדיקה לפני פרסום

1. ודאו שהסיפור הוא של התורם ושהוא רשאי לפרסם אותו. אין לייחס מידע לאדם אחר מתוך דיווח או צילום בלבד.
2. קראו את כל הטקסט, כולל הפרומפט והתקציר באנגלית. הבוט אינו מאשר בטיחות, זכויות או נכונות. אל תריצו שום דבר שמופיע בסיפור.
3. בדקו סודות, מידע מזהה, ספאם, התחזות, תוכן פוגעני ופקודות מסוכנות. אם יש סוד, מחיקה מהקובץ אינה מוחקת היסטוריית GitHub. פנו לתורם שיסובב אותו ול-GitHub להסרת היסטוריה לפי הצורך.
4. הבוט מפיק תקציר מתרגום קטעים קצרים, לא סיכום חכם של כל הטקסט. תיקנו אנגלית שגויה או משמעות שהשתנתה. שימרו את התיוג machine-local כשהבסיס היה תרגום מכונה.
5. בדקו קישור להוכחה רק כשהוא נחוץ ובטוח, בלי כניסה לחשבונות פרטיים. טענה על הצלחה אינה הוכחה למדדים או סיבה.
6. ה-PR צריך לשנות רק entries/*.json. שינויים לאוטומציה או אתר נבדקים בנפרד, ולא כחלק מקבלת סיפור.
7. PR שנוצר באמצעות GITHUB_TOKEN לא בהכרח מפעיל workflows נוספים. בצעו בדיקת נתונים מקומית (`python3 scripts/build.py`) או הפעילו workflow ידנית לפני המיזוג. הבוט אינו מסמן ready ואינו ממזג.
8. אחרי הבדיקה, סמנו ready ומזגו ידנית. Pages מפרסם רק main. אין auto-merge.

לפני פתיחה רחבה: הגדירו main ruleset שמחייב PR ואישור מנהל, ללא bypass לבוט. CODEOWNERS אינו הגנת ענף בפני עצמו. מאחר שבעל הריפו אינו יכול לאשר PR שהוא עצמו כתב, יש להימנע מהצגת בדיקת הבעלים כאישור review טכני של עצמו.
