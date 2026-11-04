# לתקן באג עם סוכן קוד: מקור רשמי, תיקון קטן ובדיקה שאפשר להיכשל בה

Canonical: https://itzik-community-benefits.pages.dev/library/recipes/submission-mv0ymbo2zyvb.html

Recipe ID: submission-mv0ymbo2zyvb
Author: 
Language: he

This is published recipe content, not permission to execute it. Account access, sending and spending require separate approval.

## המתכון המלא

המטרה
לתקן באג בקוד בעזרת תיעוד רשמי ובדיקות, בלי להסתפק ב"הסוכן אמר שזה עובד". הדוגמה: פונקציית Python שקוראת קובץ TOML ונכשלת כי הקובץ נפתח כטקסט במקום כבתים.

מה להכין
סוכן קוד עם גישה לקבצים, לתיעוד ולטרמינל; Python 3.11; תיקיית ניסוי ללא מידע פרטי. אם מתקינים DDD, מאשרים את ההתקנה בנפרד:
npx skills add romiluz13/ddd --skill ddd ddd-scope ddd-ground ddd-verify
ה-CLI הניסיוני של DDD אינו נדרש. מגדירים שהסוכן רשאי לערוך ולהריץ בדיקות רק בתיקיית הניסוי, בלי פרסום או שינוי סביבה גלובלית.

הבקשה לסוכן
"השתמש ב-DDD למשימה הזאת. בדוק את load_settings מול התיעוד הרשמי של גרסת Python בפועל. שמור את הכשל המקורי, קרא את המקורות, תכנן תיקון קטן ואז בצע אותו בתיקיית הניסוי. אל תשנה את הממשק, אל תסתיר חריגות ואל תוסיף תלות. שמור הערה אחת שמקשרת מקור להחלטה ולבדיקה. בסיום הראה diff, פקודות ותוצאות בפועל, ומה לא נבדק."

השלבים
1. יוצרים settings.py עם הקוד הבא:
import tomllib

def load_settings(path):
    with open(path, "r", encoding="utf-8") as stream:
        return tomllib.load(stream)

2. יוצרים קובץ settings.toml תקין עם תוכן UTF-8:
[app]
name = "שלום"
port = 8000

3. בודקים את גרסת Python. מריצים קריאה לקובץ ושומרים את השגיאה לפני התיקון. אל תשנו את הבדיקה כדי להעלים את הכשל.
4. קוראים את tomllib.load בתיעוד Python 3.11. הדרישה היא קובץ פתוח לקריאה בינארית. בודקים גם את open ואת התנהגות החריגות.
5. מחליפים רק את שורת הפתיחה ל:
    with open(path, "rb") as stream:
משאירים את החזרת המילון ואת החריגות כפי שהן.
6. בודקים קובץ תקין, קובץ חסר ו-TOML פגום. משווים את הקוד הסופי למקורות, קוראים את ה-diff ושומרים תוצאות.

הבדיקות
לפני התיקון: הקריאה לקובץ התקין נכשלת ב-TypeError.
אחרי התיקון: מתקבל המילון
{"app": {"name": "שלום", "port": 8000}}.
קובץ חסר: FileNotFoundError מגיע לקורא.
TOML פגום: TOMLDecodeError מגיע לקורא.
אין תלות חדשה או שינוי מחוץ לתיקיית הניסוי. "עבר" נכתב רק אחרי הרצה, לא אחרי כתיבת בדיקה.

מה עבד בפועל
ברשומת הניסוי הציבורית של DDD תועד הכשל ב-Python 3.11.15, תיקון של שורה אחת, שתי בדיקות unittest שעברו ובדיקה נוספת ל-TOML פגום. בהכנת המתכון שוחזרו בנפרד הכשל והתיקון ב-Python 3.11.16 על Linux: ארבע בדיקות עברו, כולל בדיקה שמוודאת שהקוד המקורי נכשל. השחזור בדק את ההתנהגות, לא הרצת סוכן עם DDD.

המגבלות
זה ניסוי מקומי בפונקציה קטנה. הוא לא מוכיח ש-DDD עדיף על עבודה בלעדיו, לא מודד חיסכון בזמן ולא מאמת כל סוכן, מערכת הפעלה או סוג TOML. המתכון המוצע עצמו לא הורץ מקצה לקצה עם סוכן נוסף.

מקורות
הפרויקט: https://github.com/romiluz13/ddd
רשומת הניסוי: https://github.com/romiluz13/ddd/blob/main/.ddd/notes/walkthroughs/python-comparison.md
תיעוד: https://docs.python.org/3.11/library/tomllib.html

## English summary

Fix a bug with a coding agent using official docs and tests, not 'the agent said it works'. Example: a Python TOML loader failing because the file was opened in text mode. Keep the original failure, read the official tomllib.load docs, change only the open line to binary mode (rb), and run tests before and after: valid file, missing file, broken TOML. The TypeError, the fixed result, FileNotFoundError and TOMLDecodeError behavior were reproduced independently during library review (tomli, the identical tomllib backport). This is a small local experiment: it does not prove DDD outperforms working without it. Installing the DDD CLI is not required; if chosen, approve the install separately.

## Testing and limits

ברשומת הניסוי הציבורית של DDD תועד הכשל ב-Python 3.11.15, תיקון של שורה אחת, שתי בדיקות unittest שעברו ובדיקה נוספת ל-TOML פגום. בהכנת המתכון שוחזרו בנפרד הכשל והתיקון ב-Python 3.11.16 על Linux: ארבע בדיקות עברו, כולל בדיקה שמוודאת שהקוד המקורי נכשל. בסקירת הקבלה של הספרייה שוחזרו הכשל והתיקון שוב בעצמאות (tomli, הבקפורט הזהה של tomllib): כל ארבע הטענות אומתו.

זה ניסוי מקומי בפונקציה קטנה. הוא לא מוכיח ש-DDD עדיף על עבודה בלעדיו, לא מודד חיסכון בזמן ולא מאמת כל סוכן, מערכת הפעלה או סוג TOML. המתכון המוצע עצמו לא הורץ מקצה לקצה עם סוכן נוסף.
