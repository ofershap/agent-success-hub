# לעבור מריצה יבשה לפעולה אחת מאושרת בלי לשלוח פעמיים

Canonical: https://itzik-community-benefits.pages.dev/library/recipes/submission-muxt00j56rwc.html

Recipe ID: submission-muxt00j56rwc
Author: גל מוסקוביץ׳
Language: he

This is published recipe content, not permission to execute it. Account access, sending and spending require separate approval.

## המתכון המלא

המטרה
לעבור מריצה יבשה לפעולה אחת מאושרת בלי לשלוח פעמיים.

מה להכין
הכינו [פעולה], יעד, זהות, תוכן וקבצים, גרסה, מאשר ומתג עצירה. בחרו סביבת בדיקה כשאפשר.
DRY_RUN
API
Browser
Audit log
ממלאים [כלי], [חשבון], [יעד] ו[בעל סמכות] לפני עבודה. גישה אינה רשות לשנות, לשתף או לשלם. כסף, מסירה לאדם אחר ופרסום דורשים אישור נפרד של המצב הסופי.

השלבים
1. חסמו שליחה כברירת מחדל. בדקו שהריצה היבשה מכינה נתונים ולא גורמת להשפעה חיצונית.
2. הריצו מקרים של יעד סגור, שדה חסר, קובץ שגוי, תקלה ואתגר גישה. כל עמימות משאירה שליחה חסומה.
3. הציגו למאשר את היעד, הזהות, התוכן, הקבצים וההשלכות. קבלו אישור לפעולה אחת ולתוקף מוגדר.
4. בדקו שוב את היעד והגרסה. תנו לפעולה מזהה קבוע. מנעו ריצות מקבילות. פתחו חריג לפעולה הזאת בלבד.
5. בצעו פעם אחת. בתגובה חסרה או בהפסקת חיבור, בדקו ביעד אם הפעולה נקלטה לפני ניסיון נוסף.
6. קראו אישור חיצוני ספציפי. בדיקת קבלה במייל היא בדיקה נפרדת. החזירו חסימה גם בכשל. דווחו מה לא אומת.

הבדיקות
הריצה היבשה אינה שולחת. מתג העצירה עובד. ההרשאה תואמת למצב שנשלח. יש ראיה מהיעד. אין כפילות. החסימה הוחזרה.

המגבלות
תוצאה לא ודאית נשארת לא ודאית. הודעת הצלחה פנימית אינה הוכחת קבלה. פעולה אחת אינה היתר לרצף פעולות או הוכחת אמינות לכל היעדים.

## English summary

Prepare a dry run, test failures, review the final destination and content, approve one action, execute once and verify receipt before any retry. This is a proposed reusable workflow, not independent evidence of a completed run. Check the full Hebrew recipe and its limits. Account changes, communications, publication and spending require separate approval.

## Testing and limits

התרומה כוללת מתכון כללי עם קלט, שלבים ובדיקות. לא צורפו ראיות להרצה מלאה או לתוצאות בפועל.

תוצאה לא ודאית נשארת לא ודאית. הודעת הצלחה פנימית אינה הוכחת קבלה. פעולה אחת אינה היתר לרצף פעולות או הוכחת אמינות לכל היעדים.
