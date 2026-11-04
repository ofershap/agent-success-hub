# לולאת קידום לפרויקט קוד פתוח עם סוכן

Canonical: https://itzik-community-benefits.pages.dev/library/recipes/issue-9.html

Recipe ID: issue-9
Author: ofershap
Language: he

This is published recipe content, not permission to execute it. Account access, sending and spending require separate approval.

## המתכון המלא

```text
# טיוטה: לולאת קידום לפרויקט קוד פתוח עם סוכן

## היכולת
לבחון פרויקט כמו משתמש חדש, לתקן חסמי אימוץ, להכין הפצה רלוונטית ולמדוד את התוצאה. אין רכישת כוכבים, ספאם או הבטחת טראפיק. אין כאן סיפור על אדם מסוים או מספרי הצלחה שלא אומתו.

## המתכון לסוכן חדש

### מטרה
בנה לולאת צמיחה מדודה לפרויקט קוד פתוח: baseline -> first-use test -> fixes -> approved distribution -> measurement -> next experiment. המטרה הראשונה היא שאדם מתאים יבין ויוכל להשתמש בפרויקט, לא כמות פרסומים.

### קלט והרשאות
URL של ריפו בבעלות המשתמש, גרסה/commit, רישיון, קהל יעד, צורך שהפרויקט פותר וחלופות. נדרשים runtime, הוראות build, demo אם יש והרשאות לקריאת נתוני traffic/downloads. ציין מי רשאי למזג, לשחרר גרסה ולפרסם בכל ערוץ. אסוף טקסט עובדתי ומקורות לכל claim. בלי נתוני analytics אין baseline traffic; אפשר להתחיל מדדי בדיקה מקומיים בלבד. קבע חלון ניסוי, ערוצים מותרים, תקציב ותקרת זמן. טיוטות outreach אינן הרשאה לשלוח.

### כלים
Git/GitHub, sandbox ללא סודות לבדיקת קוד, runtime לפי lockfile, browser לבדיקת docs/demo, issue tracker וגיליון/קובץ מדדים פרטי. ניתן להשתמש בנתוני GitHub/registry שהחשבון מורשה לראות; אין לפרסם נתוני traffic פרטיים. אין צורך לקנות כלי שיווק.

### שלבים
1. קרא README, רישיון, release notes, issues ו-PRs. כתוב במשפט אחד למי הפרויקט מתאים, מה עושה ומה אינו עושה. אם אין אפשרות לבסס claim, השאר אותו מחוץ להודעת קידום.
2. הקפא baseline עם תאריך, commit וגרסה. רשום רק מדדים שיש להם מקור: views/unique visitors, clones, downloads, stars, issues ותוצאות demo. רשום טווח הזמן והגדרת המדד; אלה אינם כולם "משתמשים". כשאין נתון סמן unavailable, לא אפס.
3. בצע first-use test בסביבה נקייה ומבודדת. קרא scripts לפני install. עקוב בדיוק אחר README: התקנה, import/API, דוגמה מינימלית ו-build. אל תשתמש בקבצים/ידע שהקורא החדש לא יקבל. רשום כל צעד חסר, זמן עד תוצאה, error והסביבה.
4. בדוק demo כמו משתמש חיצוני: כניסה חדשה, מובייל/מחשב, שגיאות קונסול, הוראות ומצבי כשל. בפרויקט סנכרון למשל בדוק שני contexts וניתוק/reconnect לפי חוזה הפרויקט; אל תמציא תמיכה שהקוד אינו מצהיר עליה.
5. סדר חסמים: broken install/docs/demo לפני פיצ'ר חדש. לכל חסם צור reproduction קטן וציפייה מול בפועל. לפני פתיחת issue ציבורי הראה את הטקסט והיעד לבעלים. חפש issue קיים כדי לא להציף כפילות.
6. הכן תיקוני README, quickstart ו-examples ב-PR נפרד. דוגמה חייבת להיות ניתנת להרצה על הגרסה שמפיצים. אמת פקודות בסביבה נקייה, קישורים ורישיון. בקוד חדש: regression tests, build וסקירת diff. אין מיזוג/שחרור אוטומטיים ללא הרשאה.
7. הכין asset pack: משפט פתיחה עובדתי, בעיה, שימוש מתאים, snippet שנבדק, תמונת demo שבדקת בפיקסלים, limitations וקישור canonical. לא משתמשים בפרטי משתמשים/שיחות/analytics כהוכחה ציבורית בלי אישור.
8. בחר ערוצים לפי audience fit: דיון מקצועי, פורום, dev.to/בלוג או קהילה שכבר מדברת על הבעיה. לכל יעד קרא את הכללים בפועל ואת מדיניות self-promotion. לא מניחים ש-Reddit או כל subreddit מרשים קידום. כשלא ברור, הכין טיוטה/פנייה למודרטור לביקורת.
9. כתוב לכל ערוץ הודעה קצרה שמסבירה מה יכול לעזור לקורא, עם disclosure שאתה היוצר/פועל מטעם הפרויקט, גבולות ודוגמה. אל תתחזה למשתמש חיצוני שממליץ. אל תעתיק אותו פוסט לעשרות קהילות ואל תבקש מעורבות מזויפת.
10. הצג לבעלים את הערוץ/הקהילה, החשבון, הטקסט, המדיה והזמן ביחד. אחרי אישור בדוק שלא כבר נשלח/נענה ושאין שינוי בכללי הערוץ. שלח פעם אחת ושמור URL אמיתי. עצור אם מודרטור מבקש להסיר/אם ערוץ מגביל אוטומציה.
11. אם מותר להשיב, טפל בתגובות ענייניות במסגרת ההרשאה. שאלה שלא מכוסה בתיעוד חוזרת לבעלים, לא הופכת להבטחת פיצ'ר. ביקורת או bug הם נתוני מוצר, לא יעד למשחק במדדים.
12. בסוף חלון הניסוי קרא שוב את אותם מקורות מדידה ובאותה הגדרה. הפרד הפניות, downloads ו-conversions ככל שיש מדידה תקינה. שינוי לצד פרסום אינו הוכחה לסיבתיות; release, bots או ערוץ אחר יכולים להשפיע. אל תתבסס על star count בלבד.
13. החזר report: פעולות שבוצעו, URLs, baseline/end, חסמי אימוץ שנפתרו, feedback, עלות וסייגים. בחר ניסוי אחד הבא על בסיס feedback, לא על "עוד פוסטים". כל ניטור עתידי דורש תחום ותאריך סיום; אין הקמת מנוע outreach תמידי מתוך המתכון.

### בדיקות
README עובד מסביבה נקייה; example תואם לגרסה; ה-demo נבדק בפיקסלים; links תקינים; תוכן שיווקי תואם עובדות; code/issue/metric אינם חושפים סוד; אין duplicate issue/post; ערוץ מאפשר את הפרסום; analytics source וטווחים זהים. אם אין telemetry, אין טענת growth.

### מוכן
משתמש חדש יכול להגיע לדוגמה עובדת לפי הוראות בלבד, או blockers מוגדרים. חומרי הפצה נבדקו ונמצאים לביקורת. אם אושר פרסום, קישורו אומת. דוח הניסוי מציג נתונים שנקראו בפועל ומפריד בין תיקוני מוצר, קידום ותוצאה עסקית. טיוטות ופרסום שלא בוצע מסומנים כך.

### מלכודות ומגבלות
stars אינם משתמשים; clones/downloads יכולים לכלול CI/bots; חלונות analytics שונים אינם comparison. post עם engagement אינו אימוץ מוצר. community code אינו קוד של הסוכן. ערוץ עשוי לאסור self-promotion גם אם הודעה דומה הופיעה בעבר. אלה גבולות המתכון, לא נתוני תוצאה.

## מקורות ציבוריים שנקראו
https://docs.github.com/en/communities/setting-up-your-project-for-healthy-contributions/adding-a-code-of-conduct-to-your-project
https://docs.github.com/en/repositories/viewing-activity-and-data-for-your-repository/viewing-a-summary-of-repository-activity
https://www.redditinc.com/policies/content-policy

הכללים של היעד הספציפי ונתוני הפרויקט נקראים במועד היישום. אין במקורות האלה אישור לפרסם בקהילה מסוימת.
```

## English summary

A proposed workflow for growing an open-source project: establish sourced baseline metrics, test first use in a clean environment, fix adoption barriers, prepare channel-specific materials for owner review and measure an approved experiment. It separates product improvements, distribution and business outcomes. Stars are not users, draft outreach is not permission to send, and this recipe promises neither traffic nor adoption.

## Testing and limits

בנה לולאת צמיחה מדודה לפרויקט קוד פתוח: baseline -> first-use test -> fixes -> approved distribution -> measurement -> next experiment. המטרה הראשונה היא שאדם מתאים יבין ויוכל להשתמש בפרויקט, לא כמות פרסומים.

stars אינם משתמשים; clones/downloads יכולים לכלול CI/bots; חלונות analytics שונים אינם comparison. post עם engagement אינו אימוץ מוצר. community code אינו קוד של הסוכן. ערוץ עשוי לאסור self-promotion גם אם הודעה דומה הופיעה בעבר. אלה גבולות המתכון, לא נתוני תוצאה.
