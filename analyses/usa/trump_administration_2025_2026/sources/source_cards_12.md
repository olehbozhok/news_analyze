# Source cards: вимірювання інфляції (документ 12)

> Одне твердження — одне джерело. Якщо джерело підтверджує лише частину, картка розділяється (AGENTS.md, 6.2). Файл — `sources/source_cards_12.md` для документа `12_vymiriuvannia_inflatsii.md`; у тексті документа посилатися як `[SC-01]`, далі `python3 scripts/sc_links.py --fix`.

> Інструмент: усі сторінки відкрито дослідниками через WebFetch/WebSearch/curl; для частини сторінок BLS/BEA/SSA/IRS/FRED використано Chrome (позначено в caveat). Writer нових URL не відкривав. Цитати з WebFetch не звірені з оригінальним HTML. Сирі нотатки (`agent_*_raw.md`) у фінальному документі не цитуються.

## SC-01

**Звільнення комісара BLS 01.08.2025**

- **Claim:** Президент наказав звільнити комісара BLS Еріку Мак-Ентарфер 01.08.2025 після звіту про зайнятість за липень 2025; в.о. комісара — Вільям Війатровскі.
- **URL:** <https://www.aljazeera.com/economy/2025/8/1/trump-fires-official-overseeing-jobs-data-after-dismal-employment-numbers>
- **Дата й видавець:** 01.08.2025, Al Jazeera
- **Цитата (дослівно, мовою оригіналу):** «I have directed my Team to fire this Biden Political Appointee, IMMEDIATELY»
- **Період даних:** 01.08.2025 (липневий звіт: +73 тис. робочих місць; травень і червень переглянуто разом на −258 тис.)
- **Тип:** факт
- **Статус:** ВТОРИННЕ
- **Confidence:** висока
- **Caveat:** Стосується звіту про зайнятість, не CPI. Правка 07.11.2026 (F-9): первинний реліз BLS відкрито через Chrome (https://www.bls.gov/news.release/archives/empsit_08012025.htm): травень переглянуто з +144 000 до +19 000 (−125 000), червень з +147 000 до +14 000 (−133 000), разом «258,000 lower than previously reported»; окремі цифри Al Jazeera (June 120/239) неточні, брати −258 тис. з BLS. В.о. комісара Wiatrowski (серпень 2025 – серпень 2026) підтверджено первинно: https://www.bls.gov/bls/history/commissioners/ ([SC-93]). Інструмент для Al Jazeera: WebFetch/WebSearch.

## SC-02

**Заявлена підстава звільнення (позиція президента)**

- **Claim:** Президент публічно пояснив звільнення тим, що дані про зайнятість «підроблені» (позиція сторони, не встановлений факт).
- **URL:** <https://www.aljazeera.com/economy/2025/8/1/trump-fires-official-overseeing-jobs-data-after-dismal-employment-numbers>
- **Дата й видавець:** 01.08.2025, Al Jazeera
- **Цитата (дослівно, мовою оригіналу):** «In my opinion, today's Jobs Numbers were RIGGED in order to make the Republicans, and ME, look bad.»
- **Період даних:** 01.08.2025
- **Тип:** позиція
- **Статус:** ВТОРИННЕ
- **Confidence:** висока
- **Caveat:** Формулювання посту різниться між виданнями; брати дослівно лише з оригіналу посту. Є лише для звіту про зайнятість; щодо CPI аналогічної заяви в нотатках немає.

## SC-03

**Фактчек: доказів маніпуляції не наведено**

- **Claim:** Фактчекери не знайшли доказів, що McEntarfer чи інші працівники BLS маніпулювали даними, і адміністрація їх не надала.
- **URL:** <https://www.nbcmiami.com/news/national-international/fact-check-no-evidence-for-trumps-claims-of-rigged-or-phony-job-numbers/3672794/>
- **Дата й видавець:** 04.08.2025, FactCheck.org (передрук NBC Miami)
- **Цитата (дослівно, мовою оригіналу):** «There's no evidence the commissioner, or others at BLS, manipulated the data, and Trump hasn't provided any.» (цитату на сторінці знайдено Verifier-ом 07.11.2026, F-7)
- **Період даних:** серпень 2025
- **Тип:** оцінка
- **Статус:** ВТОРИННЕ
- **Confidence:** середня
- **Caveat:** Читати як «доказів не наведено», а не «спростовано» (AGENTS.md, розділ 9). Сторінку в нотатках відкрито через WebFetch/WebSearch.

## SC-04

**Позиція Білого дому щодо ревізій payrolls**

- **Claim:** Радник CEA Мірен пов'язував близько 60% ревізій із сезонним коригуванням, а директор NEC Гассетт ставив під сумнів таймінг бенчмарк-ревізії 2024 (позиції сторони).
- **URL:** <https://www.nbcmiami.com/news/national-international/fact-check-no-evidence-for-trumps-claims-of-rigged-or-phony-job-numbers/3672794/>
- **Дата й видавець:** 04.08.2025, FactCheck.org (передрук NBC Miami)
- **Цитата (дослівно, мовою оригіналу):** Miran: «about 60% of the overall revisions were due to quirks of the seasonal adjustment process…» (цитату на сторінці знайдено Verifier-ом 07.11.2026, F-7)
- **Період даних:** липень–серпень 2025
- **Тип:** позиція
- **Статус:** ВТОРИННЕ
- **Confidence:** низька
- **Caveat:** Пряма цитата Miran є на сторінці фактчекера (див. вище); позицію Гассетта подано переказом. Первинного документа Білого дому (меморандум, заява) з обґрунтуванням не знайдено.

## SC-05

**Колишні комісари BLS про ревізії**

- **Claim:** Колишні комісари (Бич, призначений Трампом; Утгофф) заявили, що ревізії є штатною властивістю опитування, а «підкрутити» цифри неможливо.
- **URL:** <https://www.nbcmiami.com/news/national-international/fact-check-no-evidence-for-trumps-claims-of-rigged-or-phony-job-numbers/3672794/>
- **Дата й видавець:** 04.08.2025, FactCheck.org (передрук NBC Miami)
- **Цитата (дослівно, мовою оригіналу):** Бич: «every time we publish on Friday, there are revisions to the previous two months.»; Утгофф: «Revisions are not mistakes, they are improvements.»
- **Період даних:** серпень 2025
- **Тип:** позиція
- **Статус:** ВТОРИННЕ
- **Confidence:** середня
- **Caveat:** Цитати взято з переказу FactCheck.org (інтерв'ю CNN), а не з першоджерела. Колишні керівники відомства — не нейтральні сторони щодо його репутації.

## SC-06

**Реакція професійної спільноти на звільнення**

- **Claim:** Friends of BLS (ко-голови — колишні комісари) назвали підставу звільнення безпідставною; голова профспілки AFGE заявив про втрату нейтральності агенції (позиції).
- **URL:** <https://www.govexec.com/management/2025/08/neutrality-agency-has-been-eliminated-stats-based-feds-decry-bls-chiefs-firing/407272>
- **Дата й видавець:** 06.08.2025, Government Executive
- **Цитата (дослівно, мовою оригіналу):** Friends of BLS: «This rationale for firing Dr. McEntarfer is without merit»; AFGE (Баррон): «The neutrality of the agency has been eliminated, and public trust has been broken.»
- **Період даних:** серпень 2025
- **Тип:** позиція
- **Статус:** ВТОРИННЕ
- **Confidence:** середня
- **Caveat:** Адвокаційні позиції. Дослівні заяви ASA, AEA, NABE не перевірено (PDF ASA не прочитався).

## SC-07

**Відкликання номінації Antoni 30.09.2025**

- **Claim:** Білий дім відкликав номінацію Е. Дж. Антоні (Heritage) на посаду комісара BLS 30.09.2025.
- **URL:** <https://www.inquirer.com/politics/nation/trump-pulls-bureau-labor-statistics-nomination-ej-antoni-20250930.html>
- **Дата й видавець:** 30.09.2025, Philadelphia Inquirer (AP)
- **Цитата (дослівно, мовою оригіналу):** — (дослівної цитати в нотатках дослідника немає; зміст за переказом/сніпетом)
- **Період даних:** серпень–вересень 2025
- **Тип:** факт
- **Статус:** ВТОРИННЕ
- **Confidence:** висока
- **Caveat:** Причину відкликання сторінка не називає (правка F-8: попереднє припущення про підтримку республіканців у Сенаті з caveat прибрано). Назву в.о. комісара ця сторінка не містить (див. [SC-01], [SC-93]). Сторінку бачено через WebSearch (сніпет).

## SC-08

**Підтвердження Matsumoto Сенатом 07.08.2026**

- **Claim:** Сенат підтвердив Бретта Матсумото комісаром BLS 07.08.2026 (51–47, у блоці номінантів); посада була без підтвердженого комісара близько 12 місяців.
- **URL:** <https://news.bloomberglaw.com/payroll/trumps-bls-pick-brett-matsumoto-confirmed-in-senate-vote>
- **Дата й видавець:** 07.08.2026, Bloomberg Law
- **Цитата (дослівно, мовою оригіналу):** «reinstating a crucial leadership role after President Donald Trump abruptly fired his predecessor last year»; голосування «tallied 51-47»
- **Період даних:** 01.08.2025 – 07.08.2026
- **Тип:** факт
- **Статус:** ВТОРИННЕ
- **Confidence:** висока
- **Caveat:** Цитати за поверненням WebFetch. Номінація (30.01.2026) і слухання HELP (10.06.2026) — лише зі сніпетів. Дванадцять місяців — власний підрахунок за датами.

## SC-09

**Аудит Inspector General Мінпраці: оголошення**

- **Claim:** Inspector General Мінпраці 10.09.2025 оголосив огляд проблем BLS зі збором і публікацією економічних даних (CPI/PPI і ревізії зайнятості).
- **URL:** <https://www-ak-ms.foxbusiness.com/economy/labor-department-inspector-general-announces-audit-bls-data-collection-challenges>
- **Дата й видавець:** 11.09.2025, Fox Business
- **Цитата (дослівно, мовою оригіналу):** «initiating a review of the challenges that Bureau of Labor Statistics encounters collecting and reporting closely watched economic data»
- **Період даних:** вересень 2025
- **Тип:** факт
- **Статус:** ВТОРИННЕ
- **Confidence:** висока
- **Caveat:** Результат аудиту не шукався на момент першого запису; див. наступну картку.

## SC-10

**Аудит Inspector General Мінпраці: статус**

- **Claim:** За сніпетом плану аудитів FY26 проєкт «BLS Challenges in Collecting and Reporting Economic Data» має статус «In Progress»; остаточного звіту станом на 07.11.2026 не знайдено.
- **URL:** <https://www.oig.dol.gov/public/oaprojects/BLS%20Engagement_Letter.pdf>
- **Дата й видавець:** 10.09.2025 (engagement letter), oig.dol.gov
- **Цитата (дослівно, мовою оригіналу):** — (дослівної цитати в нотатках дослідника немає; зміст за переказом/сніпетом)
- **Період даних:** станом на 07.11.2026
- **Тип:** факт
- **Статус:** ДОСТУПНЕ
- **Confidence:** низька
- **Caveat:** PDF зашифрований і не прочитаний; статус зі сніпета WebSearch. oig.dol.gov/auditprojects.htm напряму не переглядався, тож відсутність звіту — не доведена.

## SC-11

**ASA: штат і бюджет BLS**

- **Claim:** За ASA, BLS втратило близько 22% штату з FY24, а запит президента на FY26 — $648 млн (−8% купівельної спроможності проти $704 млн факту FY25); асоціація знизила оцінку захисту незалежності статистики до «CHALLENGING».
- **URL:** <https://www.amstat.org/docs/default-source/amstat-documents/the-nations-data-at-risk-2025/bureau-of-labor-statistics.pdf>
- **Дата й видавець:** листопад 2025 (метадані PDF), American Statistical Association
- **Цитата (дослівно, мовою оригіналу):** «The FY26 President's Budget Request is for $648 million, which represents an 8% loss in purchasing power from FY25 actual.»; «BLS has lost an estimated 22% in staffing since FY24.»
- **Період даних:** FY24–FY26
- **Тип:** позиція
- **Статус:** ПЕРВИННЕ
- **Confidence:** середня
- **Caveat:** PDF відкрито і розібрано pdftotext, але це позиція професійної асоціації. «−8%» — запит, не ухвалене рішення. Цифр «2 175 → 1 999 FTE» в ASA не знайдено (НЕПІДТВЕРДЖЕНЕ).

## SC-12

**Friends of BLS: бюджет FY2026 і втрата персоналу**

- **Claim:** За листом Friends of BLS, ухвалений бюджет BLS на FY2026 — $708,5 млн (вищий за $704 млн FY25), а відомство втратило близько 25% персоналу через дострокові звільнення з лютого 2025.
- **URL:** <https://cossa.org/wp-content/uploads/2026/03/FriendsofBLSFY27RecommendationLetter.pdf>
- **Дата й видавець:** 10.03.2026, Friends of BLS (через COSSA)
- **Цитата (дослівно, мовою оригіналу):** «we propose an increase of $35.5 million (5%) over the FY 2026 enacted budget of $708.5 million»; «having lost approximately 25% of its staff through early separations since February 2025 and nearly 40% of leadership posts remain vacant»
- **Період даних:** FY2026; штат з лютого 2025
- **Тип:** позиція
- **Статус:** ПЕРВИННЕ
- **Confidence:** середня
- **Caveat:** Одне джерело, адвокаційна організація. Закон про асигнування FY2026 первинно не відкривався. Оцінки 22% (ASA) і 25% (Friends of BLS) — різні бази й дати.

## SC-13

**BLS припиняє розрахунок близько 350 індексів PPI**

- **Claim:** З релізом PPI за липень 2025 (14.08.2025) BLS припинив розрахунок і публікацію приблизно 350 індексів PPI.
- **URL:** <https://www.bls.gov/ppi/notices/2025/bls-to-discontinue-selected-ppis.htm>
- **Дата й видавець:** 2025, BLS
- **Цитата (дослівно, мовою оригіналу):** «BLS will end calculation and publication of approximately 350 indexes.»
- **Період даних:** з липня 2025
- **Тип:** факт
- **Статус:** ПЕРВИННЕ
- **Confidence:** висока
- **Caveat:** Причину нотис не називає. Частка (<1% з ~10 000) і відповідь сенатору Gallego — лише вторинні сніпети (Barron's), не відкриті. Дата публікації нотису не зафіксована.

## SC-14

**Heritage/Daily Signal про BLS (сніпет)**

- **Claim:** Antoni (Heritage) названо критиком «problematic post-pandemic BLS data»; сніпет згадує довгострокову консолідацію BLS/BEA/Census.
- **URL:** <https://live.dailysignal.com/?p=120580>
- **Дата й видавець:** дата не зазначена, Daily Signal
- **Цитата (дослівно, мовою оригіналу):** — (дослівної цитати в нотатках дослідника немає; зміст за переказом/сніпетом)
- **Період даних:** н/д
- **Тип:** позиція
- **Статус:** НЕПІДТВЕРДЖЕНЕ
- **Confidence:** низька
- **Caveat:** WebFetch повернув 403; зміст лише зі сніпета. Документа захисту адміністрації з боку Heritage/Cato/Manhattan не знайдено.

## SC-15

**Лист сенатора Warren до Commerce/BEA (недоступний)**

- **Claim:** Сенатор Warren 06.08.2026 направила Commerce/BEA лист із запитом пояснень щодо змін методології PCE (позиція опозиції; зміст листа не прочитано).
- **URL:** <https://www.banking.senate.gov/imo/media/doc/20260806lettertocommercebeaonmethodology.pdf>
- **Дата й видавець:** 06.08.2026, Senate Banking Committee (minority)
- **Цитата (дослівно, мовою оригіналу):** — (дослівної цитати в нотатках дослідника немає; зміст за переказом/сніпетом)
- **Період даних:** серпень 2026
- **Тип:** позиція
- **Статус:** ЗАБЛОКОВАНЕ
- **Confidence:** низька
- **Caveat:** 403 (Akamai) у WebFetch і Chrome; сторінка новини — «Unauthorized». Адресати, термін відповіді 20.08.2026 і питання про публікацію ваг композитного індексу — зі сніпетів. Відповіді BEA не знайдено.

## SC-16

**Нотис BLS: призупинення збору цін CPI**

- **Claim:** BLS призупинив збір цін CPI повністю в Lincoln (NE) і Provo (UT) з квітня 2025 та в Buffalo (NY) з червня 2025 і оцінює вплив на загальний індекс як мінімальний.
- **URL:** <https://www.bls.gov/cpi/notices/2025/collection-reduction.htm>
- **Дата й видавець:** змінено 16.06.2025, BLS
- **Цитата (дослівно, мовою оригіналу):** «In April, BLS suspended CPI data collection entirely in Lincoln, NE, and Provo, UT.»; «In June, BLS suspended collection entirely in Buffalo, NY.»; «These actions have minimal impact on the overall all-items CPI-U and CPI-W indexes.»
- **Період даних:** квітень–червень 2025
- **Тип:** факт
- **Статус:** ПЕРВИННЕ
- **Confidence:** висока
- **Caveat:** Оцінка «minimal impact» — позиція самого BLS. Дослідник перевірив: ~15% скорочення вибірки і «<0,01 п.п.» на цій сторінці відсутні (є лише у CRS). Сторінка містить виправлення помилки в response rate за квітень без чисел.

## SC-17

**CRS: скорочення вибірки на ~15% і симуляція BLS**

- **Claim:** За CRS, у решті 72 зон призупинено в середньому близько 15% вибірки, а симуляція BLS показала розбіжність із фактичним CPI менш ніж 1/100 п.п. у 12-місячній зміні.
- **URL:** <https://www.everycrsreport.com/reports/IN12596.html>
- **Дата й видавець:** 18.08.2025, Congressional Research Service
- **Цитата (дослівно, мовою оригіналу):** «less than 1/100th of a percentage point for 12-month inflation»
- **Період даних:** 2025
- **Тип:** позиція
- **Статус:** ВТОРИННЕ
- **Confidence:** середня
- **Caveat:** CRS переказує оголошення BLS; «<0,01 п.п.» — власна оцінка відомства, а вплив на субнаціональні й окремі індекси, за CRS, не вимірювано. Причина (заморозка найму) — Axios 12.06.2025, 403, лише сніпет. Цифри/цитати отримано через WebFetch (проміжна модель переказує сторінку), дослівність не звірена з оригінальним HTML.

## SC-18

**Частка different-cell imputation: ряд 2019–2026 (xlsx BLS)**

- **Claim:** Частка different-cell серед імпутованих цін (колонки Home cell / Different cell / Carry forward в сумі дають 100) у CPI для товарів і послуг становила 34–40% з листопада 2025 до вересня 2026 (відтворено Verifier-ом за [SC-19]). Базова лінія 7,8% (2019), ~10% (2021–2024), 29–40% з квітня 2025 — з xlsx, НЕ відтворена (xlsx не відкрито Verifier-ом).
- **URL:** <https://www.bls.gov/cpi/tables/imputation-source-201901-present.xlsx>
- **Дата й видавець:** станом на 07.11.2026, BLS
- **Цитата (дослівно, мовою оригіналу):** «The Oct 2025 data values are not available due to the 2025 lapse in appropriations.»
- **Період даних:** 2019 – вересень 2026 (жовтня 2025 немає)
- **Тип:** факт
- **Статус:** ДОСТУПНЕ
- **Confidence:** низька
- **Caveat:** Знижено за F-6/U-1 (07.11.2026): базову лінію не відтворено. Середні за періоди (7,8 / 10,0 / 11,3 / 33,7 / 38,2) порахував дослідник із щомісячних значень локально. Це не загальна частка імпутації: different-cell застосовується, коли у home cell немає жодної ціни. Напрямок зсуву ряд сам по собі не показує. Carry-forward для товарів і послуг = 0 у всіх місяцях.

## SC-19

**Різна частка different-cell: щомісячна таблиця BLS (вересень 2025 – вересень 2026)**

- **Claim:** Частка different-cell у CPI товарів і послуг: вересень 2025 — 40%, листопад — 34%, грудень — 40%, січень–вересень 2026 — 37–40%.
- **URL:** <https://www.bls.gov/cpi/tables/imputation-cs-data.htm>
- **Дата й видавець:** станом на 07.11.2026, BLS
- **Цитата (дослівно, мовою оригіналу):** «The Oct 2025 data values are not available due to the 2025 lapse in appropriations.»
- **Період даних:** вересень 2025 – вересень 2026
- **Тип:** факт
- **Статус:** ПЕРВИННЕ
- **Confidence:** висока
- **Caveat:** Таблицю WebFetch повернув як зведення; значення збігаються з xlsx ([SC-18]). Окреме пояснення BLS: категорію зберігають, географію розширюють. Базова лінія до 2025 за цією сторінкою не береться.

## SC-20

**Collection rate CPI 2019–2026**

- **Claim:** Середній collection rate для цін CPI: 2026 (січень–вересень) — 66,1% (595,1/9); мінімум грудня 2025 — 63,9%. Значення 2024 (72,5%) і 2025 (69,4%) на сторінці відсутні, не відтворені: НЕПІДТВЕРДЖЕНЕ.
- **URL:** <https://www.bls.gov/cpi/tables/response-rates/response-rates-cs-quote-data.htm>
- **Дата й видавець:** змінено 19.10.2026, BLS
- **Цитата (дослівно, мовою оригіналу):** — (попередню цитату «In June 2025, BLS adopted a revised methodology…» на сторінці не знайдено, F-6; знято. Підтверджено лише таблицю значень 2026 і грудня 2025)
- **Період даних:** 2019 – вересень 2026
- **Тип:** факт
- **Статус:** ПЕРВИННЕ
- **Confidence:** середня
- **Caveat:** Середнє 2026 перераховано з таблиці на сторінці. Середні 2024–2025 дослідник брав із xlsx (monthly-response-rates-201901-present.xlsx), який Verifier не відкрив; джерело зміни методології рахунку в червні 2025 не знайдено, тож порівняння 2024 з 2026 у документі не робиться. BLS: response rates вказують на потенціал зсуву, але не на його наявність (за сніпетом).

## SC-21

**BLS відновлює найм і публікує collection rates**

- **Claim:** BLS у листопаді 2025 відновив найм польових співробітників CPI; збір для раніше призупинених частин вибірки відновлюватиметься частково; з червня 2026 BLS щомісяця публікує response rates.
- **URL:** <https://www.bls.gov/cpi/notices/2026/data-collection-update.htm>
- **Дата й видавець:** змінено 22.10.2026, BLS
- **Цитата (дослівно, мовою оригіналу):** «BLS resumed recruitment, hiring, and training of CPI field staff across the nation»; «BLS continues to collect data by telephone, online, or by using non-survey sources»
- **Період даних:** листопад 2025 – жовтень 2026
- **Тип:** факт
- **Статус:** ПЕРВИННЕ
- **Confidence:** висока
- **Caveat:** Сторінка не містить фактичних response rates. Скорочення на 22.10.2026 скасовано лише частково. Цифри/цитати отримано через WebFetch (проміжна модель переказує сторінку), дослівність не звірена з оригінальним HTML.

## SC-22

**Попередня бенчмарк-ревізія payrolls (березень 2026)**

- **Claim:** Попередня річна ревізія зайнятості до березня 2026 — −79 тис. (−0,1%), приватний сектор −178 тис.; фінальна очікується в лютому 2027.
- **URL:** <https://www.bls.gov/news.release/archives/prebmk_08282026.htm>
- **Дата й видавець:** 28.08.2026, BLS
- **Цитата (дослівно, мовою оригіналу):** «−79,000 (−0.1 percent)»
- **Період даних:** до березня 2026
- **Тип:** факт
- **Статус:** ПЕРВИННЕ
- **Confidence:** середня
- **Caveat:** Інший дослідник не зміг відкрити національну сторінку BLS (порожня), тож підтвердження вторинне (Econoday: фінальні ревізії 2025 — −898 тис., 2024 — −598 тис.). Мала ревізія 2026 не підтримує тезу про систематично великі завищення в останньому циклі.

## SC-23

**Методологічні зміни CPI 2025: leased cars**

- **Claim:** З даними за квітень 2025 (реліз 13.05.2025) BLS замінив опитування для оренди авто (leased cars and trucks) закупленими транзакційними даними вендора.
- **URL:** <https://www.bls.gov/cpi/notices/2025/methodology-changes-2025.htm>
- **Дата й видавець:** 2025, BLS
- **Цитата (дослівно, мовою оригіналу):** опитування замінено «transaction data purchased from a vendor»
- **Період даних:** з квітня 2025
- **Тип:** факт
- **Статус:** ПЕРВИННЕ
- **Confidence:** висока
- **Caveat:** Напрямок ефекту на індекс сторінка не наводить. Збіг у часі зі скороченням штату є, але BLS їх не пов'язує; зв'язок НЕПІДТВЕРДЖЕНИЙ. Цифри/цитати отримано через WebFetch (проміжна модель переказує сторінку), дослівність не звірена з оригінальним HTML.

## SC-24

**Методологічні зміни CPI 2025: wireless**

- **Claim:** З даними за липень 2025 (реліз 12.08.2025) BLS замінив опитувальні дані для бездротового зв'язку вторинними джерелами й застосував нетрадиційні індексні методи.
- **URL:** <https://www.bls.gov/cpi/notices/2025/methodology-changes-2025.htm>
- **Дата й видавець:** 2025, BLS
- **Цитата (дослівно, мовою оригіналу):** BLS «has replaced survey data … with secondary source data» і застосовує «non-traditional index methods»
- **Період даних:** з липня 2025
- **Тип:** факт
- **Статус:** ПЕРВИННЕ
- **Confidence:** висока
- **Caveat:** Напрямок ефекту не наведено. Цифри/цитати отримано через WebFetch (проміжна модель переказує сторінку), дослівність не звірена з оригінальним HTML.

## SC-25

**Методологічні зміни CPI 2025: страхування довгострокового догляду**

- **Claim:** З даними за листопад 2025 (реліз 18.12.2025) BLS повністю вилучив страхування довгострокового догляду (LTC) з індексу медичного страхування.
- **URL:** <https://www.bls.gov/cpi/notices/2025/methodology-changes-2025.htm>
- **Дата й видавець:** 2025, BLS
- **Цитата (дослівно, мовою оригіналу):** «BLS removed LTC from the index entirely»
- **Період даних:** з листопада 2025
- **Тип:** факт
- **Статус:** ПЕРВИННЕ
- **Confidence:** висока
- **Caveat:** Напрямок і розмір не наведено; вага LTC у CPI в нотатках не перевірялась. Цифри/цитати отримано через WebFetch (проміжна модель переказує сторінку), дослівність не звірена з оригінальним HTML.

## SC-26

**Оновлення ваг CPI на 2027 і обробка відсутніх даних витрат**

- **Claim:** Для ваг 2027 BLS скоригує на 3 зменшені обсяги витрат (Diary Survey) за липень і жовтень 2025 та створить вагу жовтня як копію вересня, а листопада — як копію грудня; обрано коригування вагів серед трьох розглянутих підходів.
- **URL:** <https://www.bls.gov/cpi/tables/relative-importance/weight-update-information-2027.htm>
- **Дата й видавець:** змінено 30.07.2026, BLS
- **Цитата (дослівно, мовою оригіналу):** «BLS will adjust the 1/3 fewer expenditures in July and October 2025 by 3.»; «BLS will create October weights as a copy of September weights, and November weights as a copy of December weights.»
- **Період даних:** ваги 2027 (оновлення в лютому 2027)
- **Тип:** факт
- **Статус:** ПЕРВИННЕ
- **Confidence:** висока
- **Caveat:** Експертні панелі NABE та CNSTAT. Ефект на рівень інфляції не оцінено. Цифри/цитати отримано через WebFetch (проміжна модель переказує сторінку), дослівність не звірена з оригінальним HTML.

## SC-27

**Шатдаун: відсутні дані CE впливають на ваги 2027 і фінальний C-CPI-U 2025**

- **Claim:** Відсутні дані Consumer Expenditure за жовтень–листопад 2025 впливають на заплановані публікації (річний CE 2025, остаточні ревізії C-CPI-U 2025, індекси CPI-U і CPI-W 2027); BLS обрало метод коригування вагових коефіцієнтів.
- **URL:** <https://www.bls.gov/cpi/additional-resources/2025-federal-government-shutdown-impact-cpi.htm>
- **Дата й видавець:** змінено 15.09.2026, BLS
- **Цитата (дослівно, мовою оригіналу):** «Missing CE data in October and November 2025 affects BLS estimates in planned publications, including the 2025 annual CE release, final revisions of the 2025 Chained CPI-U indexes, and 2027 CPI-U and CPI-W indexes.»; «BLS selected the survey weight adjustment factor approach to prioritize the timely release of planned publications.»
- **Період даних:** 2025–2027
- **Тип:** факт
- **Статус:** ПЕРВИННЕ
- **Confidence:** висока
- **Caveat:** Панель NABE (07.05.2026) рекомендувала повернутися до практики публікації сезонних факторів і ваг за два дні до офіційних даних. Ефект на рівень інфляції не оцінено. Відкрито через Chrome (за описом дослідника).

## SC-28

**MLR: симуляція відсутніх даних CE**

- **Claim:** Стаття MLR (Stockburger & Perrins) показує, що за п'ятьма варіантами обробки відсутніх даних CE річні (annualized) темпи зміни CPI-U за грудень 2023 – грудень 2025 — 2,770–2,848% проти виробничих 2,8%, а різниці від виробничого — 0,004–0,065 п.п. (три підходи вищого рівня — у [SC-26])
- **URL:** <https://www.bls.gov/opub/mlr/2026/article/addressing-missing-consumer-expenditure-data-due-to-the-2025-lapse-in-appropriations.htm>
- **Дата й видавець:** 26.06.2026, BLS (MLR)
- **Цитата (дослівно, мовою оригіналу):** — (дослівної цитати в нотатках дослідника немає; зміст за переказом/сніпетом)
- **Період даних:** грудень 2023 – грудень 2025
- **Тип:** оцінка
- **Статус:** ПЕРВИННЕ
- **Confidence:** середня
- **Caveat:** BLS оцінює власну процедуру (AGENTS.md, розділ 5, п. 18). Числа з WebFetch-переказу. Цифри/цитати отримано через WebFetch (проміжна модель переказує сторінку), дослівність не звірена з оригінальним HTML.

## SC-29

**Відносні ваги CPI-U, грудень 2025 (ваги витрат 2024)**

- **Claim:** Ваги CPI-U у грудні 2025: shelter 35,625, OER 26,204, rent 7,840, energy 6,383; CPI-W: shelter 33,594, rent 10,697, OER 21,798.
- **URL:** <https://www.bls.gov/cpi/tables/relative-importance/2025.htm>
- **Дата й видавець:** змінено 07.10.2026, BLS
- **Цитата (дослівно, мовою оригіналу):** CPI-U: «Shelter 35,625; Rent of primary residence 7,840; Owners' equivalent rent of residences 26,204»; Energy 6,383 (грудень 2025; у грудні 2024 — 6,216 за [SC-30])
- **Період даних:** грудень 2025
- **Тип:** факт
- **Статус:** ПЕРВИННЕ
- **Confidence:** висока
- **Caveat:** Вага житла в PCE (~15–16%) за вторинними джерелами; таблицю BEA не відкрито (НЕПІДТВЕРДЖЕНЕ). Відкрито через Chrome (за описом дослідника).

## SC-30

**Відносні ваги CPI-U, грудень 2024 (ваги витрат 2023)**

- **Claim:** Ваги CPI-U у грудні 2024: shelter 35,483, OER 26,282, rent 7,499, energy 6,216; зміна до грудня 2025 (shelter +0,14 п.п., energy +0,17 п.п.) відповідає рутинному щорічному оновленню.
- **URL:** <https://www.bls.gov/cpi/tables/relative-importance/2024.htm>
- **Дата й видавець:** BLS
- **Цитата (дослівно, мовою оригіналу):** —  (числа в таблиці: shelter 35,483; OER 26,282; rent 7,499)
- **Період даних:** грудень 2024
- **Тип:** факт
- **Статус:** ПЕРВИННЕ
- **Confidence:** середня
- **Caveat:** Тлумачення «рутина» — висновок дослідника: аномальних змін ваг не виявлено, але це специфічно не шукалося для hedonic і кошика. Цифри/цитати отримано через WebFetch (проміжна модель переказує сторінку), дослівність не звірена з оригінальним HTML.

## SC-31

**Handbook BLS: агрегація Laspeyres**

- **Claim:** На верхньому рівні CPI агрегується за Laspeyres, тобто заміщення між категоріями дорівнює нулю.
- **URL:** <https://www.bls.gov/opub/hom/cpi/calculation.htm>
- **Дата й видавець:** дата зміни не встановлена, BLS
- **Цитата (дослівно, мовою оригіналу):** «In a Laspeyres aggregation, consumer substitution between items is assumed to be zero.»
- **Період даних:** постійна методологія
- **Тип:** факт
- **Статус:** ПЕРВИННЕ
- **Confidence:** висока
- **Caveat:** Описує давню методологію, а не зміну 2025–2026.

## SC-32

**BLS про shrinkflation у CPI**

- **Claim:** За BLS, зміни розміру упаковки додавали до індексу товарів і послуг близько 0,01% на рік у 2015–2019 (їжа — близько 0,04 п.п. на рік).
- **URL:** <https://www.bls.gov/opub/btn/volume-12/measuring-shrinkflation-and-its-impact-on-inflation.htm>
- **Дата й видавець:** лютий 2023, BLS (Kari McNair)
- **Цитата (дослівно, мовою оригіналу):** «product size changes (upsizing and downsizing) increased the CPI all commodity and services index by 0.01 percent per year.»
- **Період даних:** 2015–2019 (додаток до 2023)
- **Тип:** оцінка
- **Статус:** ПЕРВИННЕ
- **Confidence:** висока
- **Caveat:** Оцінка BLS про себе; не охоплює 2025–2026 і приховане погіршення якості.

## SC-33

**BLS: збору CPI не було 01.10–12.11.2025**

- **Claim:** BLS не збирав дані CPI з 1 жовтня по 12 листопада 2025 року; відсутні дані вплинули на індекси жовтня і листопада 2025 та на індекси оренди квітня 2026.
- **URL:** <https://www.bls.gov/cpi/additional-resources/2025-federal-government-shutdown-impact-cpi.htm>
- **Дата й видавець:** змінено 15.09.2026, BLS
- **Цитата (дослівно, мовою оригіналу):** «BLS did not collect CPI data from October 1, 2025, through November 12, 2025.»; «Missing October 2025 data also affected April 2026 rent and owner's equivalent rent indexes»
- **Період даних:** жовтень–листопад 2025; квітень 2026
- **Тип:** факт
- **Статус:** ПЕРВИННЕ
- **Confidence:** висока
- **Caveat:** Відкрито через Chrome (за описом дослідника).

## SC-34

**BLS FAQ: carry-forward оренди за жовтень 2025**

- **Claim:** Оренду за жовтень 2025 перенесено з квітня 2025 (carry-forward), місячну зміну rent/OER оцінено через корінь шостого степеня 6-місячної зміни; BLS визнає, що в періоди загального зростання цін метод може давати заниження, а ефект зникне в квітні 2026.
- **URL:** <https://www.bls.gov/cpi/additional-resources/2025-federal-government-shutdown-impact-cpi-faq.htm>
- **Дата й видавець:** змінено 16.09.2026, BLS
- **Цитата (дослівно, мовою оригіналу):** «Rents for October 2025 were carried forward from April 2025»; «In periods of general price increases, the carry-forward method may result in an underestimation.»; «Effects of the carry-forward imputation method utilized in October 2025 will resolve in April 2026»
- **Період даних:** жовтень 2025 – квітень 2026
- **Тип:** факт
- **Статус:** ПЕРВИННЕ
- **Confidence:** висока
- **Caveat:** Визнання заниження — самого BLS (позиція сторони про власну процедуру, але проти її інтересу). Листопад 2025 розраховано за звичайними процедурами. Відкрито через Chrome (за описом дослідника).

## SC-35

**BLS: жовтневого релізу CPI 2025 не було; 12-місячні зміни за жовтень 2026**

- **Claim:** BLS не випускав релізу CPI за жовтень 2025 і не публікуватиме 12-місячних змін за жовтень 2026 для індексів, де даних жовтня 2025 немає.
- **URL:** <https://www.bls.gov/cpi/additional-resources/2025-federal-government-shutdown-impact-cpi-faq.htm>
- **Дата й видавець:** змінено 16.09.2026, BLS
- **Цитата (дослівно, мовою оригіналу):** «BLS did not issue an October 2025 CPI news release.»; «BLS will not publish 12-month percent changes for October 2026 for indexes where October 2025 data are not available.»
- **Період даних:** жовтень 2025; жовтень 2026
- **Тип:** факт
- **Статус:** ПЕРВИННЕ
- **Confidence:** висока
- **Caveat:** Правка 07.11.2026 (F-4): FAQ п. 16 відкрито через Chrome: «For most CPI series, BLS could not publish October 2025 indexes. As a result, BLS will not publish 12-month percent changes for October 2026 for indexes where October 2025 data are not available.» Лише «a few indexes composed entirely of nonsurvey data» мали жовтень 2025 (п. 10). FRED CPIAUCNS не має значення 2025-10, тож р/р all-items за жовтень 2026 не обчислюється з опублікованих рівнів (висновок за обома джерелами). Тверджень «вперше/безпрецедентно» не перевірено.

## SC-36

**Реліз CPI за листопад 2025: збір відновлено 14.11.2025**

- **Claim:** У релізі за листопад 2025 BLS пише, що не збирав опитувальні дані за жовтень 2025, отримав зі збоєм більшість неопитувальних даних і відновив збір 14 листопада 2025.
- **URL:** <https://www.bls.gov/news.release/archives/cpi_12182025.htm>
- **Дата й видавець:** 18.12.2025, BLS
- **Цитата (дослівно, мовою оригіналу):** «BLS did not collect survey data for October 2025 due to a lapse in appropriations.»; «BLS was able to retroactively acquire most of the nonsurvey data for October. CPI data collection resumed on November 14, 2025.»; shelter за два місяці до листопада — «increased 0.2 percent»
- **Період даних:** жовтень–листопад 2025
- **Тип:** факт
- **Статус:** ПЕРВИННЕ
- **Confidence:** висока
- **Caveat:** Дата відновлення (14.11) відрізняється від «не збирав до 12.11» на сторінці про шатдаун ([SC-33]); це може бути узгоджено (13.11 не згадано), записано як є. Відкрито через Chrome (за описом дослідника).

## SC-37

**MNI/BLS: індекси житла за жовтень 2025 без змін**

- **Claim:** BLS підтвердив MNI, що жовтневі індекси rent і OER 2025 дорівнюють вересневим, тобто «нульовий жовтневий ефект» — артефакт методу, а не вимір.
- **URL:** <https://www.mnimarkets.com/articles/bls-confirms-to-mni-that-housing-indices-unchanged-in-october-1766173201066>
- **Дата й видавець:** 19.12.2025, MNI
- **Цитата (дослівно, мовою оригіналу):** «the October 2025 indexes for rent and OER were unchanged from their September 2025 values.»
- **Період даних:** жовтень 2025
- **Тип:** факт
- **Статус:** ВТОРИННЕ
- **Confidence:** висока
- **Caveat:** Цитата в нотатках приписана BLS MLR; сторінку MNI бачено вторинно. За розрахунком дослідника рівні rent: вересень = жовтень = 438,237, листопад 439,002 (BLS API).

## SC-38

**BLS MLR (Bowman & Brown): контрфактичні методи для жовтня 2025**

- **Claim:** За п'ятьма альтернативними методами (Table 2: rent 0,24 / 0,26 / 0,44 / 0,49 / 0,53; OER 0,34 / 0,27 / 0,42 / 0,47 / 0,59) місячна зміна rent за жовтень 2025 була б вищою на 0,24–0,53 п.п., OER — на 0,27–0,59 п.п.; 12-місячний rent 3,02% (опубл.) проти 3,27–3,57% (різниці Table 3: 0,25–0,55), OER 3,29% проти 3,57–3,90% (значення 3,02/3,27/3,56 є лише в графіках); у квітні 2026 розбіжності зникли.
- **URL:** <https://www.bls.gov/opub/mlr/2026/article/counterfactual-imputation-approaches-for-the-housing-component-of-the-october-2025-cpi.htm>
- **Дата й видавець:** 12.05.2026, BLS (MLR)
- **Цитата (дослівно, мовою оригіналу):** «the research indexes and the published indexes for rent and OER all returned to the same general index level in April 2026.»
- **Період даних:** жовтень 2025 – квітень 2026
- **Тип:** оцінка
- **Статус:** ПЕРВИННЕ
- **Confidence:** висока
- **Caveat:** BLS оцінює власну процедуру. Стаття не оцінює вплив на загальний CPI-U/ядро: дослідник перечитав ≈24 тис. знаків за ключовими словами без збігів (повний PDF/додатки не перевірялись). Відкрито через Chrome та WebFetch.

## SC-39

**Mortgage News Daily: заниження shelter і квітень 2026**

- **Claim:** За коментарем MND, shelter могла бути занижена на 0,3–0,6% у річному вимірі, а квітень 2026 'врахував два шестимісячні цикли'; місячна інфляція житла була ближче до 0,3, ніж до 0,6.
- **URL:** <https://www.mortgagenewsdaily.com/news/05152026-cpi-shelter-shutdown>
- **Дата й видавець:** 15.05.2026, Mortgage News Daily
- **Цитата (дослівно, мовою оригіналу):** «April's housing inflation essentially counted two 6-month cycles' worth.»; «monthly housing inflation was more like 0.3 than 0.6.»
- **Період даних:** жовтень 2025 – квітень 2026
- **Тип:** оцінка
- **Статус:** ВТОРИННЕ
- **Confidence:** середня
- **Caveat:** Коментар одного видання; діапазон 0,3–0,6 узгоджується з MLR лише для rent/OER, не для всього CPI. Науковий paper BLS не відкривався.

## SC-40

**Оцінка впливу carry-forward на загальний CPI-U: 0,09–0,20 п.п.**

- **Claim:** Арифметика дослідника: з вагами rent 7,84% і OER 26,20% та діапазоном MLR занижений рівень CPI-U становив близько 0,09–0,20 п.п. (нижня межа 0,0784×0,24 + 0,2620×0,27 ≈ 0,09; верхня 0,0784×0,53 + 0,2620×0,59 ≈ 0,20).
- **URL:** <https://www.bls.gov/opub/mlr/2026/article/counterfactual-imputation-approaches-for-the-housing-component-of-the-october-2025-cpi.htm>
- **Дата й видавець:** розрахунок 07.11.2026 на основі BLS (MLR 12.05.2026) і ваг BLS (грудень 2025)
- **Цитата (дослівно, мовою оригіналу):** — (BLS цієї оцінки не публікував)
- **Період даних:** листопад 2025 – березень 2026 (рівень); дзеркальна база — жовтень 2026
- **Тип:** оцінка
- **Статус:** НЕПІДТВЕРДЖЕНЕ
- **Confidence:** низька
- **Caveat:** Це власна арифметика дослідника (вхідні дані ПЕРВИННЕ), а не джерело. Припускає, що вся жовтнева різниця rent/OER переходить у рівень; ваги грудня 2025 застосовано до жовтня 2025 (грудня 2024 — rent 7,499, OER 26,282: різниця мала). Для CPI-W дослідник дає 0,08–0,19, для PCE 0,04–0,09 (вага ~15% не перевірена). Перевірка Verifier потрібна. Попередню оцінку квітня 2026 (+0,09 п.п. з вхідними rent 0,55 / OER 0,53) знято (F-23): за MLR рівні збіглися в квітні, тож надлишок м/м за побудовою дорівнює всьому діапазону 0,09–0,20 (вхідні 0,55/0,53 не підтверджені карткою). Додатково (red team, оцінка автора): на core CPI ≈ 0,12–0,28 п.п. (ділення на вагу ядра ≈ 0,79); дзеркальний р/р-ефект листопад 2026 – березень 2027. Усе — оцінка автора, не факт; діапазон використано в документі лише з цим маркуванням.

## SC-41

**PPI: шатдаун затримав збір цін; реліз за листопад 2025**

- **Claim:** Шатдаун суттєво затримав передачу запитів на оновлення цін PPI; жовтневі запити надіслано 19 листопада; дані жовтня 2025 опубліковано разом із листопадом 14.01.2026.
- **URL:** <https://www.bls.gov/news.release/archives/ppi_01142026.htm>
- **Дата й видавець:** 14.01.2026, BLS
- **Цитата (дослівно, мовою оригіналу):** «The Federal government shutdown in October and November significantly delayed the transmission of Producer Price Index (PPI) price-update requests. October price-update requests, asking for information as of the October 14 pricing date, were sent to PPI survey respondents on November 19.»
- **Період даних:** жовтень–листопад 2025
- **Тип:** факт
- **Статус:** ПЕРВИННЕ
- **Confidence:** висока
- **Caveat:** Відкрито через Chrome (за описом дослідника).

## SC-42

**BEA: звіт PCE за жовтень і листопад 2025 — спільний, 22.01.2026**

- **Claim:** BEA замінило окремі релізи за жовтень і листопад 2025 (заплановані на 26.11 і 19.12.2025) одним звітом 22.01.2026 через шатдаун.
- **URL:** <https://www.bea.gov/news/2026/personal-income-and-outlays-october-and-november-2025>
- **Дата й видавець:** 22.01.2026, BEA
- **Цитата (дослівно, мовою оригіналу):** «Due to the recent government shutdown, this report for October and November replaces releases originally scheduled for November 26 and December 19, 2025.»
- **Період даних:** жовтень–листопад 2025
- **Тип:** факт
- **Статус:** ПЕРВИННЕ
- **Confidence:** висока
- **Caveat:** Затримка PCE-цін за жовтень ≈ 8 тижнів (власний підрахунок). Затримка торкнулась CPI, PPI і PCE одночасно; вибіркового відтермінування несприятливих релізів у цьому графіку не видно (висновок дослідника).

## SC-43

**BEA: анонс річного оновлення 2026 і змін методології PCE**

- **Claim:** BEA 17.08.2026 анонсувало річне оновлення з публікацією 30.09.2026, ревізіями Q1 2021 – Q1 2026 і змінами для портфельного управління, юридичних послуг та програмного забезпечення.
- **URL:** <https://bea.gov/news/blog/2026-08-17/annual-update-gdp-industry-and-state-stats-publicly-available-starting-sept-30>
- **Дата й видавець:** 17.08.2026, BEA
- **Цитата (дослівно, мовою оригіналу):** «from the first quarter of 2021 through the first quarter of 2026»; юридичні послуги: «This change will replace source data that has become volatile and can’t be corroborated.»; ПЗ: «This change will better reflect the composition of products included in this category.»
- **Період даних:** Q1 2021 – Q1 2026
- **Тип:** факт
- **Статус:** ПЕРВИННЕ
- **Confidence:** висока
- **Caveat:** Анонс не вказує величину й напрямок ефекту. Охоплює також ВВП, GDI та їхні компоненти — не лише PCE. Намір не заявлено як політичний (відсутність мотиву в документі ≠ спростування).

## SC-44

**BEA SCB (червень 2026): превʼю змін PCE-дефляторів**

- **Claim:** BEA у превʼю замінює дефлювання витрат на портфельне управління кількісним екстраполятором на основі BLS CES, для юридичних послуг використовує композит із PPI, бо неопубліковані значення CPI 'не відповідають настановам якості BLS'.
- **URL:** <https://apps.bea.gov/scb/issues/2026/06-june/0626-nea-preview.htm>
- **Дата й видавець:** червень 2026, BEA (Survey of Current Business)
- **Цитата (дослівно, мовою оригіналу):** «the unpublished CPI values do not meet BLS publication quality guidelines»; значення «have recently exhibited erratic changes that cannot be corroborated and are not consistent with other source data»
- **Період даних:** з 2024 (юридичні послуги)
- **Тип:** факт
- **Статус:** ПЕРВИННЕ
- **Confidence:** висока
- **Caveat:** Кількісної оцінки впливу і напрямку в превʼю немає. Опублікування ваг композитного індексу (питання Warren) — окреме питання без відповіді. Цифри/цитати отримано через WebFetch (проміжна модель переказує сторінку), дослівність не звірена з оригінальним HTML.

## SC-45

**BEA SCB (вересень 2026): фактичні ревізії PCE-цін, ВВП і GDI**

- **Claim:** У річних даних ревізії headline і core PCE за 2023–2025 дорівнюють 0,0 п.п. (2021: −0,1; 2022: +0,1), у квартальних за 2020:Q4–2026:Q1 core переглянуто на −0,1 п.п.; реальний ВВП 2025 переглянуто з 2,1% до 2,3%, реальний GDI 2025 — з 2,4% до 2,8%.
- **URL:** <https://apps.bea.gov/scb/issues/2026/09-september/0926-nea-annual-update.htm>
- **Дата й видавець:** вересень 2026, BEA (Survey of Current Business)
- **Цитата (дослівно, мовою оригіналу):** «the price index for PCE increased 4.0 percent, the same as previously published»; core PCE «increased 3.8 percent, revised down 0.1 percentage point»
- **Період даних:** 2021 – Q1 2026
- **Тип:** факт
- **Статус:** ПЕРВИННЕ
- **Confidence:** середня
- **Caveat:** WebFetch прочитав 100 000 із 128 964 символів; графіки 8–10 (напрямок трьох змінених складових) — зображення, не прочитані: напрямок кожної складової НЕПІДТВЕРДЖЕНЕ первинно. Квартальні ревізії core, за BEA, «primarily reflect updated BLS CPIs»; «−0,1 п.п.» — середній річний темп за 2020:Q4–2026:Q1 (5,25 року), кумулятивно ≈ 0,5 п.п. рівня цін, не квартальна ревізія й не стосується окремо Q1 2026 (−0,5). Особистий дохід переглянуто вгору на $137,5 млрд (2024) і $227,7 млрд (2025).

## SC-46

**BEA: Q2 2026 third estimate і ревізія Q1 — реальний ВВП вгору, ціни вниз**

- **Claim:** Q1 2026: реальний ВВП → 2,5% (revised; попереднє значення 2,1% на сторінці не наведене; незмінність номінального 5,8% не звірено), PCE-ціна 4,6 → 4,2, core 4,4 → 3,9, реальний GDI 1,2 → 2,5; Q2: реальний ВВП 2,2% (+0,7 п.п. до другої оцінки; номінальний ВВП теж змінено: 8,0 → 8,5), PCE-ціна 5,0 (−0,3), core 3,3 (−0,3).
- **URL:** <https://bea.gov/news/2026/gdp-third-estimate-industries-corporate-profits-state-gdp-and-state-personal-income-2nd>
- **Дата й видавець:** 30.09.2026 (на сторінці: «EMBARGOED … September 30, 2026, BEA 26-42»), BEA
- **Цитата (дослівно, мовою оригіналу):** «Real GDP was revised up 0.7 percentage point from the second estimate, primarily reflecting upward revisions to investment, consumer spending, and government spending.»; «The PCE price index increased 4.2 percent, also revised down 0.4 percentage point. Excluding food and energy, the PCE price index increased 3.9 percent, revised down 0.5 percentage point.»
- **Період даних:** Q1–Q2 2026 (річні темпи, SAAR)
- **Тип:** факт
- **Статус:** ПЕРВИННЕ
- **Confidence:** висока
- **Caveat:** Арифметично за незмінного номіналу нижчий дефлятор дає вищий реальний ВВП, але BEA пояснює ревізії переважно новими даними (інвестиції, споживання, держвитрати, експорт послуг); частку методів дефлювання не виділено (атрибуція — низька). Реальний GDI зріс ще більше, тож ознак «роздування» ВВП щодо доходу немає. Відкрито через Chrome.

## SC-47

**BEA: PCE за серпень 2026 (30.09.2026, після оновлення)**

- **Claim:** Після річного оновлення PCE-ціни за серпень 2026 зросли на 3,4% р/р, без їжі й енергії — на 3,0% р/р; ревізії місячних доходів і витрат починаються з січня 2021.
- **URL:** <https://www.bea.gov/news/2026/personal-income-and-outlays-august-2026>
- **Дата й видавець:** 30.09.2026, BEA
- **Цитата (дослівно, мовою оригіналу):** «the PCE price index for August increased 3.4 percent»; «Excluding food and energy, the PCE price index increased 3.0 percent from one year ago.»; «The revisions for estimates of personal income and outlays begin with January 2021.»
- **Період даних:** серпень 2026
- **Тип:** факт
- **Статус:** ПЕРВИННЕ
- **Confidence:** висока
- **Caveat:** Ревізованих 12-місячних значень за липень у релізі/PDF не знайдено. Відкрито через WebFetch і Chrome.

## SC-48

**BEA: PCE за липень 2026 (26.08.2026, до оновлення)**

- **Claim:** До річного оновлення PCE-ціни за липень 2026 зростали на 3,7% р/р, без їжі й енергії — на 3,3% р/р.
- **URL:** <https://www.bea.gov/news/2026/personal-income-and-outlays-july-2026>
- **Дата й видавець:** 26.08.2026, BEA
- **Цитата (дослівно, мовою оригіналу):** «the PCE price index for July increased 3.7 percent»; core — 3,3% р/р
- **Період даних:** липень 2026 (первинний друк)
- **Тип:** факт
- **Статус:** ПЕРВИННЕ
- **Confidence:** висока
- **Caveat:** Це значення до ревізії; Правка 07.11.2026 (F-3): ревізоване значення липня підтверджено первинно: FRED PCEPILFE (дані BEA) 2026-07 = 3,00% (перераховано Verifier-ом); [SC-51], [SC-52] — вторинне підтвердження. Цитата core — переказ у нотатках.

## SC-49

**BEA: PCE за вересень 2026 (29.10.2026)**

- **Claim:** PCE-ціни за вересень 2026: +3,6% р/р (м/м +0,5%), без їжі й енергії +3,1% р/р (м/м +0,3%); норма заощаджень 3,8%.
- **URL:** <https://www.bea.gov/news/2026/personal-income-and-outlays-september-2026>
- **Дата й видавець:** 29.10.2026, BEA
- **Цитата (дослівно, мовою оригіналу):** «the personal saving rate—personal saving as a percentage of DPI—was 3.8 percent.»; «Excluding food and energy, the PCE price index increased 3.1 percent from one year ago.»
- **Період даних:** вересень 2026
- **Тип:** факт
- **Статус:** ПЕРВИННЕ
- **Confidence:** висока
- **Caveat:** Відкрито через Chrome. Наступний реліз (жовтень) — 25.11.2026.

## SC-50

**BEA: норма заощаджень до і після оновлення**

- **Claim:** Норма заощаджень: липень 2026 (до оновлення) 3,0%, серпень (після) 4,1%, вересень 3,8%; порівняння липня й серпня змішує зміну поведінки та ревізію.
- **URL:** <https://bea.gov/news/2026/personal-income-and-outlays-august-2026>
- **Дата й видавець:** 26.08.2026 і 30.09.2026, BEA
- **Цитата (дослівно, мовою оригіналу):** «Personal saving was $712.0 billion in July, and the personal saving rate… was 3.0 percent.» (липень, до); «Personal saving was $990.2 billion, and the personal saving rate… was 4.1 percent.» (серпень, після)
- **Період даних:** липень–вересень 2026
- **Тип:** факт
- **Статус:** ПЕРВИННЕ
- **Confidence:** висока
- **Caveat:** Ревізоване значення липня не знайдено; вторинне твердження про перегляд (Axis Intelligence, лише сніпет) НЕПІДТВЕРДЖЕНЕ й не використовується.

## SC-51

**Goodman Macro: липневий core PCE 3,3% → 3,0%**

- **Claim:** За аналітичною компанією Goodman Macro, після ревізії core PCE за липень 2026 р/р переглянуто з 3,3% до 3,0%; ФОМС підняв ставку 16.09.2026 (до публікації ревізій); 'статистична ревізія вниз не веде автоматично до повороту політики'.
- **URL:** <https://www.goodman-macro.com/en/articles/20261003-pce-method-fed-reform/>
- **Дата й видавець:** 03.10.2026 (англ. версія 29.10), Goodman Macro
- **Цитата (дослівно, мовою оригіналу):** «A downward statistical revision does not automatically produce a policy pivot»
- **Період даних:** липень 2026
- **Тип:** оцінка
- **Статус:** ВТОРИННЕ
- **Confidence:** низька
- **Caveat:** Вторинне джерело; значення 3,0% за липень первинно (BEA) не знайдено. Fed-симуляція (внесок ПЗ у core 0,66 → 0,50 п.п.) — модельний сценарій, переказаний цим же джерелом. Ставка 3,75–4,00% з 16.09.2026 — за цим джерелом (FOMC 28.10.2026 тримав 3-3/4–4%, див. [SC-85]).

## SC-52

**TechTimes: ефект ревізії BEA перевищив оцінки**

- **Claim:** За TechTimes, до ревізії липневий PCE був 3,7% (core 3,3%), максимум headline — 4,1% у травні, а фактичний ефект ревізії перевищив оцінки 0,1–0,2 п.п.
- **URL:** <https://www.techtimes.com/articles/328346/20260930/august-pce-inflation-cooled-34-bea-rewrote-how-it-measures-prices.htm>
- **Дата й видавець:** 30.09.2026, TechTimes
- **Цитата (дослівно, мовою оригіналу):** — (дослівної цитати в нотатках дослідника немає; зміст за переказом/сніпетом)
- **Період даних:** 2026
- **Тип:** оцінка
- **Статус:** ВТОРИННЕ
- **Confidence:** низька
- **Caveat:** Слабке вторинне джерело; «перевищив оцінки» не підкріплено первинними таблицями. Максимум 4,1% у травні збігається з цифрою ФРС (липень 2026), але ревізований травень не знайдено.

## SC-53

**RBC: ретроактивна ревізія, не дезінфляційний сигнал**

- **Claim:** RBC оцінює ефект змін BEA в −18 б.п. на річний темп core PCE (core за липень 3,1% замість 3,3%), але підкреслює, що це ретроактивна ревізія, а не дезінфляційний сигнал.
- **URL:** <https://www.rbc.com/en/economics/us-analysis/us-featured-analysis/pce-deflator-update-a-retroactive-revision-not-a-disinflationary-signal/>
- **Дата й видавець:** 24.09.2026, RBC
- **Цитата (дослівно, мовою оригіналу):** «an 18-basis-point reduction in the annual pace of core PCE»; заголовок «a retroactive revision, not a disinflationary signal»
- **Період даних:** липень 2026 (проєкція до публікації 30.09.2026)
- **Тип:** проєкція
- **Статус:** ВТОРИННЕ
- **Confidence:** середня
- **Caveat:** Проєкція банку до релізу, НЕ факт. «Core за липень 3,1% замість 3,3%» не збігається з Goodman (3,0%) — не узгоджено. «Nominal price deflation is being replaced entirely by a CES-based quantity series» — опис змін у RBC. Цифри/цитати отримано через WebFetch (проміжна модель переказує сторінку), дослівність не звірена з оригінальним HTML.

## SC-54

**TD Securities: зміни PCE 'маргінальні'**

- **Claim:** TD Securities (до релізу) оцінювала core PCE за травень 2026 приблизно на 15 б.п. нижчим за 3,4%, середній місячний ефект — близько −1 б.п.
- **URL:** <https://www.fxstreet.com/news/united-states-pce-methodology-tweaks-seen-as-marginal-td-securities-202607231453>
- **Дата й видавець:** 23.07.2026, FXStreet (TD Securities)
- **Цитата (дослівно, мовою оригіналу):** — (дослівної цитати в нотатках дослідника немає; зміст за переказом/сніпетом)
- **Період даних:** травень 2026
- **Тип:** проєкція
- **Статус:** ВТОРИННЕ
- **Confidence:** середня
- **Caveat:** Проєкція банку до релізу, НЕ факт; відрізняється від 'за оцінками аналітиків' у слабких джерелах. Цифри/цитати отримано через WebFetch (проміжна модель переказує сторінку), дослівність не звірена з оригінальним HTML.

## SC-55

**Goldman/JPM: core PCE за травень 3,2%/3,3% замість 3,4% (низька якість)**

- **Claim:** За Crypto Briefing, Goldman Sachs очікував core PCE травня 3,2% (замість 3,4%), JPMorgan — 3,3%, тобто −0,2 і −0,1 п.п. (аналітики не названі, звітів банків не відкрито).
- **URL:** <https://cryptobriefing.com/bea-pce-inflation-revision-fed-impact/>
- **Дата й видавець:** 29.07.2026, Crypto Briefing
- **Цитата (дослівно, мовою оригіналу):** «would land at 3.2%, down from the currently reported 3.4%.»
- **Період даних:** травень 2026
- **Тип:** проєкція
- **Статус:** ВТОРИННЕ
- **Confidence:** низька
- **Caveat:** Слабке джерело; проєкція, НЕ факт; використовується лише щоб показати діапазон очікувань. Первинні звіти банків не відкривались.

## SC-56

**BLS CPI, вересень 2026**

- **Claim:** CPI-U за вересень 2026: +3,7% р/р (м/м SA +0,6%), без їжі й енергії +2,6% (м/м +0,3%), shelter +3,2%, енергія +20,4%, бензин +34,2%, C-CPI-U +3,5%, CPI-W +3,9%, нові авто +0,6%, вживані −1,5%.
- **URL:** <https://www.bls.gov/news.release/cpi.nr0.htm>
- **Дата й видавець:** 14.10.2026, BLS
- **Цитата (дослівно, мовою оригіналу):** «Over the last 12 months, the all items index increased 3.7 percent before seasonal adjustment.»; «The Chained Consumer Price Index for All Urban Consumers (C-CPI-U) increased 3.5 percent over the last 12 months.»
- **Період даних:** вересень 2026
- **Тип:** факт
- **Статус:** ПЕРВИННЕ
- **Confidence:** висока
- **Caveat:** Core та shelter — частково за переказом WebFetch у другому дослідженні; headline, C-CPI-U, CPI-W відкрито в Chrome. Наступний реліз (жовтень) — 10.11.2026.

## SC-57

**Розрахована таблиця CPI/PPI/PCE за 21 місяць (власні обчислення з рядів)**

- **Claim:** З індексів BLS Public API і FRED PCEPI/PCEPILFE: CPI р/р 3,00% (січ. 2025) → 3,01% (вер. 2025) → 2,74% (лист.) → 2,41% (лют. 2026) → 4,25% (трав., пік) → 3,74% (вер. 2026); core CPI 3,26 → 2,56; core PCE 2,81 → 3,12; PPI final demand 6,34% (вер. 2026); rent р/р 3,40% (вер. 2025) → 2,96% (лист. 2025) → 2,56% (бер. 2026) → 2,79% (кв. 2026), OER 3,76 → 3,36 → 3,10 → 3,30.
- **URL:** <https://fred.stlouisfed.org/data/PCEPI>
- **Також URL:** <https://fred.stlouisfed.org/data/PCEPILFE>, <https://fred.stlouisfed.org/data/CPIAUCNS>, <https://fred.stlouisfed.org/data/CPILFENS>, <https://fred.stlouisfed.org/data/PPIFIS>, <https://fred.stlouisfed.org/data/CUUR0000SEHA>, <https://fred.stlouisfed.org/data/CUUR0000SEHC> (ряди, з яких Verifier відтворив числа; F-15)
- **Дата й видавець:** 07.11.2026, власний розрахунок Researcher (BLS Public API; FRED/BEA)
- **Цитата (дослівно, мовою оригіналу):** — (розрахунок)
- **Період даних:** січень 2025 – вересень 2026
- **Тип:** оцінка
- **Статус:** ДОСТУПНЕ
- **Confidence:** середня
- **Caveat:** Темпи пораховано з рівнів, а не взято з релізів; PCE — останній вінтаж FRED після ревізії 30.09.2026, а НЕ перші друки (прогалина: перші друки не збирались). Звірені з релізами лише вересень 2026 (CPI 3,7/2,6; PCE 3,6/3,1). Розбіжність округлення: серпень core 2,45 (розрахунок) проти 2,4 (BLS). URL кінцевої точки BLS Public API у нотатках не зафіксовано (ряди CPI/PPI завантажено curl POST 07.11.2026); посилання — на ряд FRED PCEPI.

## SC-58

**Core PCE вище за core CPI з 2026 року (розрахунок)**

- **Claim:** Різниця core PCE − core CPI (р/р, п.п.): 2025 — від −0,45 (січ.) до 0,00 (трав.); лист. 2025 +0,09; груд. +0,23; 2026 — +0,44 (січ.), +0,51 (бер.), +0,52 (лип.), +0,56 (вер.).
- **URL:** <https://fred.stlouisfed.org/data/PCEPI>
- **Дата й видавець:** 07.11.2026, власний розрахунок Researcher
- **Цитата (дослівно, мовою оригіналу):** — (розрахунок)
- **Період даних:** січень 2025 – вересень 2026
- **Тип:** оцінка
- **Статус:** ДОСТУПНЕ
- **Confidence:** середня
- **Caveat:** Власні обчислення з рядів; перетин нуля збігається з листопадом 2025, але розрив лишається й після вирівнювання рівнів у квітні 2026 (отже carry-forward пояснює не все). Пояснення (вага shelter 35,6% у CPI проти ~15–16% у PCE, тарифи на товари) — гіпотези, не доведені. Minneapolis Fed (28.08.2026) за видачею пошуку давав core PCE 3,3% р/р за липень — URL відсутній, не збігається з 3,00% у рядах.

## SC-59

**SSA: COLA-2027 = 3,6%**

- **Claim:** COLA для виплат з грудня 2026 (виплачуються в січні 2027) — 3,6%: середній CPI-W за Q3 2026 = 328,746 проти 317,265 за Q3 2025.
- **URL:** <https://www.ssa.gov/oact/cola/latestCOLA.html>
- **Дата й видавець:** станом на 07.11.2026, SSA (дата оголошення на сторінці не наведена)
- **Цитата (дослівно, мовою оригіналу):** «The latest COLA is 3.6 percent for Social Security benefits and SSI payments.»; «(328.746 - 317.265) / 317.265 x 100 = 3.6 percent.»
- **Період даних:** Q3 2026 проти Q3 2025
- **Тип:** факт
- **Статус:** ПЕРВИННЕ
- **Confidence:** висока
- **Caveat:** Незалежний перерахунок дослідника: +3,619%. Дата оголошення — вторинно 14.10.2026 (ДОСТУПНЕ). COLA-2026 (2,8%, оголошено 24.10.2025) — за сніпетом. Відкрито через Chrome.

## SC-60

**CRS: R-CPI-E для людей 62+ (COLA-2026)**

- **Claim:** У грудні 2025 COLA за експериментальним R-CPI-E була б 3,0% проти 2,8% за CPI-W; R-CPI-E ≥ чинної COLA майже в усі роки з 1986, окрім шести.
- **URL:** <https://www.everycrsreport.com/files/2026-05-27_IF12675_bbc09e49ba9513d3ecb34c6c7e516257dd38fe32.html>
- **Дата й видавець:** 27.05.2026, CRS (IF12675)
- **Цитата (дослівно, мовою оригіналу):** «The December 2025 COLA using the R-CPI-E (3.0%) would have been 0.2 percentage points higher»; «BLS cautions that the R-CPI-E is experimental and has methodological limitations»
- **Період даних:** COLA 2025/2026; історично з 1986
- **Тип:** факт
- **Статус:** ВТОРИННЕ
- **Confidence:** середня
- **Caveat:** Експериментальний індекс із меншою вибіркою. Даних R-CPI-E за Q3 2026 не знайдено, гіпотетичної COLA-2027 за CPI-E немає. CBO: CPI-E вищий на 0,2 п.п. з 1982, але з грудня 2007 'generally lower' (сніпет). Цифри/цитати отримано через WebFetch (проміжна модель переказує сторінку), дослівність не звірена з оригінальним HTML.

## SC-61

**IRS: коригування на 2027 рік**

- **Claim:** IRS 05.11.2026 оголосив коригування на 2027: стандартне відрахування $33 200 (подружжя) та $16 600 (одинаки), поріг ставки 37% — $661 375 ($793 650 для подружжя); зростання стандартного відрахування для подружжя — 3,1% (33 200 / 32 200).
- **URL:** <https://www.irs.gov/newsroom/irs-releases-tax-inflation-adjustments-for-tax-year-2027-taxpayers-continue-to-benefit-from-the-working-families-tax-cuts>
- **Дата й видавець:** 05.11.2026, IRS (IR-2026-133, Rev. Proc. 2026-35)
- **Цитата (дослівно, мовою оригіналу):** «the standard deduction increases to $33,200 for married couples filing jointly, up $1,000 from 2026.»
- **Період даних:** податковий рік 2027
- **Тип:** факт
- **Статус:** ПЕРВИННЕ
- **Confidence:** висока
- **Caveat:** +3,1% — власний розрахунок для стандартного відрахування; 32 200 — з Rev. Proc. 2025-32 за сніпетом (ДОСТУПНЕ). Зростання порогів брекетів окремо не рахувалось. Метод індексації і трактування жовтня 2025 у прес-релізі не знайдено. Відкрито через Chrome.

## SC-62

**Bloomberg Tax/CBS: прогноз індексації брекетів 3,2% і 11-місячне середнє**

- **Claim:** Bloomberg Tax (за CBS, 11.09.2026) прогнозував підвищення федеральних брекетів на 3,2% у 2027 і рахував індекс як 11-місячне середнє через відсутній жовтень 2025.
- **URL:** <https://www.cbsnews.com/news/2027-tax-brackets-irs-inflation-adjustments/>
- **Дата й видавець:** 11.09.2026, CBS News (Bloomberg Tax)
- **Цитата (дослівно, мовою оригіналу):** «Federal tax brackets are projected to rise 3.2% next year.»
- **Період даних:** податковий рік 2027 (прогноз)
- **Тип:** проєкція
- **Статус:** ВТОРИННЕ
- **Confidence:** низька
- **Caveat:** Прогноз, НЕ факт. CBS подає «up from $31,500 and $15,750» (значення 2025 р.) — суперечить IRS (2026: $32 200/$16 100); тому опора — IRS. Чи IRS справді використав 11 місяців — НЕПІДТВЕРДЖЕНЕ. Цифри/цитати отримано через WebFetch (проміжна модель переказує сторінку), дослівність не звірена з оригінальним HTML.

## SC-63

**Cleveland Fed: median і trimmed-mean CPI (вересень 2026)**

- **Claim:** Median CPI +0,2% м/м, 2,6% за 12 міс.; 16% trimmed-mean +0,3% м/м, 2,7% за 12 міс.; Cleveland використовує інтерпольовані дані за жовтень 2025.
- **URL:** <https://www.clevelandfed.org/indicators-and-data/median-cpi>
- **Дата й видавець:** 14.10.2026, Cleveland Fed
- **Цитата (дослівно, мовою оригіналу):** «Indicators on this webpage use interpolated data for October 2025.»
- **Період даних:** вересень 2026
- **Тип:** факт
- **Статус:** ПЕРВИННЕ
- **Confidence:** середня
- **Caveat:** Це міри, похідні від CPI-U, тож успадковують його похибки (carry-forward, інтерполяція жовтня) — не незалежний вимір. Цифри/цитати отримано через WebFetch (проміжна модель переказує сторінку), дослівність не звірена з оригінальним HTML. Документ Cleveland про інтерполяцію не відкривався.

## SC-64

**FRED: помісячний median CPI Cleveland Fed**

- **Claim:** Помісячні (annualized) значення median CPI: вересень 2025 2,44; жовтень 1,40; листопад 1,40; грудень 3,13; квітень 2026 4,93; вересень 2026 2,81.
- **URL:** <https://fred.stlouisfed.org/data/MEDCPIM158SFRBCLE>
- **Дата й видавець:** станом на 07.11.2026, FRED / Cleveland Fed
- **Цитата (дослівно, мовою оригіналу):** — (числа з таблиці)
- **Період даних:** вересень 2025 – вересень 2026
- **Тип:** факт
- **Статус:** ПЕРВИННЕ
- **Confidence:** середня
- **Caveat:** Однакові 1,40 за жовтень і листопад 2025 схожі на інтерполяцію (спостереження, не висновок; підтверджується приміткою Cleveland, [SC-62]). Пік квітня 2026 збігається з розв'язанням carry-forward. Цифри/цитати отримано через WebFetch (проміжна модель переказує сторінку), дослівність не звірена з оригінальним HTML.

## SC-65

**Dallas Fed: trimmed-mean PCE (вересень 2026)**

- **Claim:** Trimmed-mean PCE за вересень 2026: 1-місячний річний темп 2,8%, 6-місячний 2,4%, 12-місячний 2,3%.
- **URL:** <https://www.dallasfed.org/research/pce>
- **Дата й видавець:** 29.10.2026, Dallas Fed
- **Цитата (дослівно, мовою оригіналу):** —  (числа за переказом WebFetch)
- **Період даних:** вересень 2026
- **Тип:** факт
- **Статус:** ПЕРВИННЕ
- **Confidence:** середня
- **Caveat:** Похідна від PCE; після ревізій BEA 30.09.2026 значення могли змінитися. 2,8% — річний темп м/м, не р/р (виправлення roic.ai, лише сніпет). Цифри/цитати отримано через WebFetch (проміжна модель переказує сторінку), дослівність не звірена з оригінальним HTML.

## SC-66

**Atlanta Fed: sticky-price CPI (вересень 2026)**

- **Claim:** Sticky-price CPI вересня 2026 — +2,8% р/р; flexible — +6,1% р/р.
- **URL:** <https://www.atlantafed.org/research-and-data/data/sticky-price-cpi>
- **Дата й видавець:** 14.10.2026, Atlanta Fed
- **Цитата (дослівно, мовою оригіналу):** «On a year-over-year basis, the series is up 2.8 percent.»; flexible «up 6.1 percent»
- **Період даних:** вересень 2026
- **Тип:** факт
- **Статус:** ПЕРВИННЕ
- **Confidence:** висока
- **Caveat:** Похідна від CPI; відкрито через Chrome.

## SC-67

**Chinn (Econbrowser) про Truflation 0,93%**

- **Claim:** Chinn скептично оцінив швидке падіння Truflation у січні 2026 (0,93%), яке Antoni подав як CPI; Antoni: Truflation відводить житлу ~чверть ваги проти ~третини в CPI.
- **URL:** <https://econbrowser.com/archives/2026/02/truflation-chief-economist-less-than-1-percent-inflation-yes>
- **Дата й видавець:** 04.02.2026, Econbrowser (Menzie Chinn)
- **Цитата (дослівно, мовою оригіналу):** Antoni: «As of today, y/y CPI inflation is 0.93%!»; «CPI assigns housing about one-third of its weight, whereas Truflation is closer to one in four.»
- **Період даних:** січень–лютий 2026
- **Тип:** позиція
- **Статус:** ВТОРИННЕ
- **Confidence:** середня
- **Caveat:** Аргументи сторін; Antoni — відкликаний кандидат на комісара BLS (контекст). Цифри/цитати отримано через WebFetch (проміжна модель переказує сторінку), дослівність не звірена з оригінальним HTML.

## SC-68

**Truflation: січневий звіт 2026**

- **Claim:** Truflation оцінила інфляцію січня 2026 в +1,47% р/р (core +1,61%); житло −0,26% р/р.
- **URL:** <https://predict.truflation.com/blog/truflation-us-monthly-inflation-report-january-2026>
- **Дата й видавець:** ~лютий 2026 (дата на сторінці не вказана), Truflation
- **Цитата (дослівно, мовою оригіналу):** —  (числа: headline +1,47% р/р; core +1,61%)
- **Період даних:** січень 2026
- **Тип:** позиція
- **Статус:** ДОСТУПНЕ
- **Confidence:** низька
- **Caveat:** Самопублікація компанії; методологію OER/rent не описано. Розбіжність спрямована вниз (CPI вищий), тобто не підтримує тезу про недооцінку офіційної інфляції. Цифри/цитати отримано через WebFetch (проміжна модель переказує сторінку), дослівність не звірена з оригінальним HTML.

## SC-69

**Truflation проти BLS, липень 2026 (низька якість)**

- **Claim:** Truflation (TruCPI-US) показала 2,11% на 27.07.2026 проти CPI 3,5% за червень 2026 (BLS: червень 3,53% за розрахунком).
- **URL:** <https://cryptobriefing.com/truflation-us-cpi-2-percent-bls-divergence/>
- **Дата й видавець:** 27.07.2026, Crypto Briefing (передрук Webopedia)
- **Цитата (дослівно, мовою оригіналу):** «The Bureau of Labor Statistics says prices are running at 3.5% year-over-year as of June 2026.»
- **Період даних:** червень–липень 2026
- **Тип:** позиція
- **Статус:** ВТОРИННЕ
- **Confidence:** низька
- **Caveat:** Порівнюються різні дати (27.07 і червень). Truflation за серпень–жовтень 2026 не знайдено. Цифри/цитати отримано через WebFetch (проміжна модель переказує сторінку), дослівність не звірена з оригінальним HTML.

## SC-70

**PriceStats (State Street): сніпети 2026**

- **Claim:** За сніпетами, PriceStats показувала р/р 2,61% (січень), 2,75% (лютий), 4% (березень), понад 5% наприкінці травня і заявляє про близькість до CPI.
- **URL:** <https://www.statestreet.com/ie/en/insights/us-inflation-pricestats-march>
- **Дата й видавець:** 2026, State Street
- **Цитата (дослівно, мовою оригіналу):** — (дослівної цитати в нотатках дослідника немає; зміст за переказом/сніпетом)
- **Період даних:** січень–травень 2026
- **Тип:** факт
- **Статус:** НЕПІДТВЕРДЖЕНЕ
- **Confidence:** низька
- **Caveat:** Сторінки не відкривались, лише сніпети WebSearch; не використовувати як факт. Рівень травня (>5%) суперечить іншим даним (CPI травня 4,25%) — різниця не пояснена.

## SC-71

**NY Fed SCE: очікування інфляції (вересень 2026)**

- **Claim:** Медіанні очікування домогосподарств: 1 рік — 3,9%, 3 роки — 3,3%, 5 років — 3,0%.
- **URL:** <https://www.newyorkfed.org/microeconomics/sce>
- **Дата й видавець:** ~07.10.2026 (дата за URL пресрелізу), NY Fed
- **Цитата (дослівно, мовою оригіналу):** «Expectations remained unchanged at the five-year-ahead horizon at 3.0 percent.»
- **Період даних:** вересень 2026
- **Тип:** факт
- **Статус:** ПЕРВИННЕ
- **Confidence:** висока
- **Caveat:** Опитування домогосподарств: відображає сприйняття, чутливе до цін на бензин і продукти. Цифри/цитати отримано через WebFetch (проміжна модель переказує сторінку), дослівність не звірена з оригінальним HTML.

## SC-72

**University of Michigan: очікування інфляції (попередній листопад 2026)**

- **Claim:** Очікування інфляції на 1 рік знизилися з 4,7% до 4,3%, довгострокові — з 3,5% до 3,4%; sentiment 51,0 проти 48,0 (попередні дані).
- **URL:** <https://www.sca.isr.umich.edu/>
- **Дата й видавець:** 06.11.2026, University of Michigan Surveys of Consumers
- **Цитата (дослівно, мовою оригіналу):** «declined from 4.7% last month to 4.3% this month.»; «inched down from 3.5% in October to 3.4%.»
- **Період даних:** листопад 2026 (попередній)
- **Тип:** факт
- **Статус:** ПЕРВИННЕ
- **Confidence:** середня
- **Caveat:** Попередні дані, фінал — 20.11.2026. Горизонт довгострокових очікувань інструментом не підтверджено. Партійна чутливість опитувань не досліджувалась. Цифри/цитати отримано через WebFetch (проміжна модель переказує сторінку), дослівність не звірена з оригінальним HTML.

## SC-73

**Ринкові очікування: breakevens (FRED)**

- **Claim:** 10-річний breakeven 2,23% (06.11.2026), 5y5y forward 2,17% — значно нижчі за опитувальні очікування (3,0–3,4% довгострокові).
- **URL:** <https://fred.stlouisfed.org/series/T10YIE>
- **Дата й видавець:** 06.11.2026, FRED
- **Цитата (дослівно, мовою оригіналу):** — (числа: 2,23% і 2,17% за T5YIFR)
- **Період даних:** 06.11.2026
- **Тип:** факт
- **Статус:** ПЕРВИННЕ
- **Confidence:** середня
- **Caveat:** Breakeven містить премії ліквідності й інфляційного ризику. T5YIFR (https://fred.stlouisfed.org/series/T5YIFR) — окрема сторінка для 2,17%. Порівняння 'до/після' не збиралось. Цифри/цитати отримано через WebFetch (проміжна модель переказує сторінку), дослівність не звірена з оригінальним HTML.

## SC-74

**Gallup: сприйняття фінансів (квітень 2026)**

- **Claim:** За Gallup (1–15.04.2026, n=1 001), рекордні 55% респондентів кажуть, що їхня фінансова ситуація погіршується (від 2001), і близько 55% — що зростання цін спричинило фінансові труднощі.
- **URL:** <https://www.cbsnews.com/news/americans-finances-getting-worse-gallup-poll-2026/>
- **Дата й видавець:** 28.04.2026, CBS News (переказ Gallup)
- **Цитата (дослівно, мовою оригіналу):** — (дослівної цитати в нотатках дослідника немає; зміст за переказом/сніпетом)
- **Період даних:** квітень 2026
- **Тип:** факт
- **Статус:** ВТОРИННЕ
- **Confidence:** середня
- **Caveat:** Первинний Gallup не відкрито. Вимірює сприйняття й партійну поляризацію, а не інфляцію. Цифри/цитати отримано через WebFetch (проміжна модель переказує сторінку), дослівність не звірена з оригінальним HTML.

## SC-75

**Wells Fargo (2024): core CPI зазвичай вищий за core PCE**

- **Claim:** З 2000 року core CPI в середньому на 0,3 п.п. вищий за core PCE; ваги shelter 43% проти 18% у core PCE (Wells Fargo, 2024).
- **URL:** <https://www.actionforex.com/?p=545993>
- **Дата й видавець:** 01.04.2024, Wells Fargo Securities (ActionForex)
- **Цитата (дослівно, мовою оригіналу):** «Since 2000, the core CPI deflator has run an average of 0.3 percentage points higher than the core PCE deflator.»
- **Період даних:** з 2000 до 2024
- **Тип:** факт
- **Статус:** ВТОРИННЕ
- **Confidence:** низька
- **Caveat:** Дата 2024, не 2026. Для 2026 надійного пояснення розриву немає (PIMCO через pulse.bot — сніпет, НЕПІДТВЕРДЖЕНЕ).

## SC-76

**BLS Real Earnings, вересень 2026**

- **Claim:** Реальна середня погодинна оплата р/р −0,7%, реальна тижнева −0,1% (робочий тиждень +0,6%); production/nonsupervisory: погодинна −0,6%, тижнева −0,3%.
- **URL:** <https://www.bls.gov/news.release/realer.nr0.htm>
- **Дата й видавець:** 14.10.2026, BLS
- **Цитата (дослівно, мовою оригіналу):** «From September 2025 to September 2026, real average hourly earnings decreased 0.7 percent, seasonally adjusted. The change in real average hourly earnings combined with a 0.6-percent increase in the average workweek resulted in a 0.1-percent decrease in real average weekly earnings over this period.»
- **Період даних:** вересень 2025 – вересень 2026
- **Тип:** факт
- **Статус:** ПЕРВИННЕ
- **Confidence:** висока
- **Caveat:** Дефлятор — CPI-U (CPI-W для production). Дослідник писав, що з PCE реальна погодинна оплата ≈ −0,5%; мій перерахунок (1,030/1,0365) дає ≈ −0,6%. Відкрито через Chrome.

## SC-77

**BLS Employment Situation, жовтень 2026**

- **Claim:** Жовтень 2026: payrolls +165 тис. (12-міс. середнє 48 тис.), безробіття в діапазоні 4,1–4,3% з березня, LFPR 61,9%, EPOP 59,3%, неповна зайнятість з економічних причин +339 тис. до 4,8 млн, довготривало безробітні 27,6%, AHE +3,1% р/р.
- **URL:** <https://www.bls.gov/news.release/empsit.nr0.htm>
- **Дата й видавець:** 06.11.2026, BLS
- **Цитата (дослівно, мовою оригіналу):** «Total nonfarm payroll employment rose by 165,000 in October, higher than the average monthly gain of 48,000 over the prior 12 months.»; «The unemployment rate has remained in a narrow range of 4.1 percent to 4.3 percent since March.»
- **Період даних:** жовтень 2026
- **Тип:** факт
- **Статус:** ПЕРВИННЕ
- **Confidence:** висока
- **Caveat:** Наступний реліз (листопад) — 04.12.2026. Відкрито через Chrome.

## SC-78

**BLS Table A-15: U-3 і U-6, жовтень 2026**

- **Claim:** SA: U-3/U-4/U-5/U-6 — вересень 4,2/4,4/5,0/7,6; жовтень 4,1/4,4/5,1/7,9; різниця U-6 − U-3 у жовтні = 3,8 п.п. (розрахунок).
- **URL:** <https://www.bls.gov/news.release/empsit.t15.htm>
- **Дата й видавець:** змінено 06.11.2026, BLS
- **Цитата (дослівно, мовою оригіналу):** «Data for October 2025 were not collected due to the federal government shutdown.»
- **Період даних:** вересень–жовтень 2026
- **Тип:** факт
- **Статус:** ПЕРВИННЕ
- **Confidence:** висока
- **Caveat:** Жовтня 2025 у CPS немає. U-6 січня 2025 не збирався, тож зміну за час адміністрації не порахувати.

## SC-79

**BLS: популяційні контролі січня 2026 і розрив рядів CPS**

- **Claim:** Популяційні контролі січня 2026 знизили LFPR на 0,4 п.п. і EPOP на 0,5 п.п., майже не змінивши безробіття; ряди CPS між груднем 2025 і січнем 2026 розривні.
- **URL:** <https://www.bls.gov/cps/methods/population-controls/experimental-series-accounting-for-January-2026-population-control-effects.htm>
- **Дата й видавець:** змінено 10.04.2026, BLS
- **Цитата (дослівно, мовою оригіналу):** «The adjustment lowered the labor force participation rate by 0.4 percentage point and lowered the employment–population ratio by 0.5 percentage point. The adjustment had little effect on the number of unemployed people (+15,000), and the unemployment rate was unaffected.»
- **Період даних:** січень 2026
- **Тип:** факт
- **Статус:** ПЕРВИННЕ
- **Confidence:** висока
- **Caveat:** Офіційні дані до грудня не ревізовано. Порівнювати LFPR 2025 і 2026 напряму — помилка. Відкрито через Chrome.

## SC-80

**Atlanta Fed: відповідь CPS після шатдауну**

- **Claim:** Response rate CPS впав майже на 5 п.п. між вереснем і листопадом 2025; нові когорти відповідають гірше, а загальний показник 'підпирають' старі когорти; літературою передбачається ухил безробіття вниз (гіпотеза).
- **URL:** <https://www.atlantafed.org/research-and-data/publications/policy-hub-macroblog/2026/04/09/more-than-missing-data-survey-response-rates-following-2025-government-shutdown>
- **Дата й видавець:** 09.04.2026, Atlanta Fed (Ben Miller)
- **Цитата (дослівно, мовою оригіналу):** «the CPS response rate fell sharply, declining by almost 5 percentage points from the September to November surveys.»; «any labor force measures that are calculated on a year-over-year basis will be missing in both October 2025 and October 2026»
- **Період даних:** вересень–листопад 2025
- **Тип:** оцінка
- **Статус:** ПЕРВИННЕ
- **Confidence:** середня
- **Caveat:** Аналітика банку, не офіційна позиція ФРС. Ухил U-3 вниз — гіпотеза з літератури (Cai & Baker 2021), не доведений ефект 2026. Відкрито через Chrome.

## SC-81

**BLS: звіт до Appropriations про модернізацію CPS**

- **Claim:** CPS у 2026 має 60 000 домогосподарств (як 1981 року), response rate впав із ~90% до 'upper 60 percent', а <50 відповідей можуть зсунути безробіття на 0,1 п.п.
- **URL:** <https://www.bls.gov/bls/congressional-reports/report-to-the-appropriations-committees-on-modernizing-the-current-population-survey-april-2026.htm>
- **Дата й видавець:** квітень 2026, BLS
- **Цитата (дослівно, мовою оригіналу):** «At current sample sizes, a net change of fewer than 50 survey responses could move the headline unemployment rate by 0.1 percentage point.»
- **Період даних:** 2026
- **Тип:** факт
- **Статус:** ПЕРВИННЕ
- **Confidence:** висока
- **Caveat:** Позиція BLS про власну якість. Інтернет-самозвітування не запроваджено; зміни визначення U-3 не заплановано. Відкрито через Chrome.

## SC-82

**ФРС (Board): breakeven зайнятості 2026**

- **Claim:** FEDS Note: за майже нульового зростання робочої сили breakeven зайнятості близький до нуля, тож від'ємні місячні прирости payrolls майже так само ймовірні, як додатні; BLS може завищувати зростання населення.
- **URL:** <https://federalreserve.gov/econres/notes/feds-notes/labor-force-growth-breakeven-employment-and-potential-gdp-growth-20260402.html>
- **Дата й видавець:** 02.04.2026, Federal Reserve Board (Murray & Vidangos)
- **Цитата (дослівно, мовою оригіналу):** «near-zero labor force growth implies that breakeven employment growth (i.e. the pace needed to maintain a steady unemployment rate) would also be near-zero—making negative job growth almost as likely as positive job growth in any given month.»
- **Період даних:** 2026
- **Тип:** проєкція
- **Статус:** ПЕРВИННЕ
- **Confidence:** середня
- **Caveat:** Оцінка персоналу ФРС, не офіційна позиція. Інференція дослідника (CPS-населення +129 тис./міс. вище за припущення FEDS Note) — не доведено. Відкрито через Chrome.

## SC-83

**NY Fed: Household Debt and Credit, Q2 2026**

- **Claim:** Прострочення загалом 4,7% боргу; потік у 90+ днів (Q2 2025 → Q2 2026): іпотека 1,29 → 1,52; студентські 12,88 → 7,83; авто 2,93 → 3,00; картки 6,93 → 6,97.
- **URL:** <https://www.newyorkfed.org/newsevents/news/research/2026/20260811>
- **Дата й видавець:** 11.08.2026, NY Fed
- **Цитата (дослівно, мовою оригіналу):** «Aggregate delinquency rates improved slightly in Q2 2026, with 4.7% of outstanding debt in some stage of delinquency.»
- **Період даних:** Q2 2026
- **Тип:** факт
- **Статус:** ПЕРВИННЕ
- **Confidence:** висока
- **Caveat:** Агрегат за балансом, не медіанне домогосподарство. Q3 2026 ще не вийшов. Відкрито через Chrome.

## SC-84

**NY Fed Liberty Street: stock проти flow прострочення за картками**

- **Claim:** Частка балансів карток 90+ днів зросла з 7,6% (2022:Q3) до 12,8% (2026:Q1) завдяки накопиченню списаних боргів, а flow-показник стабільний майже два роки.
- **URL:** <https://libertystreeteconomics.newyorkfed.org/2026/08/how-distressed-are-consumers-reconciling-diverging-credit-card-delinquency-measures/>
- **Дата й видавець:** 11.08.2026, NY Fed (Liberty Street Economics)
- **Цитата (дослівно, мовою оригіналу):** «between 2022:Q3 and 2026:Q1, the percentage of credit card balances 90+ days delinquent rose from 7.6 percent to 12.8 percent»; «the stock delinquency rate is rising because of a pool of stale, charged-off debts that lenders have been reporting for longer durations, rather than a fundamental worsening in the incidence of delinquency.»
- **Період даних:** 2022:Q3 – 2026:Q1
- **Тип:** факт
- **Статус:** ПЕРВИННЕ
- **Confidence:** висока
- **Caveat:** Відкрито через Chrome. 12,8% — stock (2026:Q1), 6,97% — flow (Q2 2026): періоди різні.

## SC-85

**FOMC, 28.10.2026**

- **Claim:** FOMC залишив ставку 3-3/4–4%; 'Economic activity is expanding at a strong pace', 'Inflation remains elevated'; Cook і Hammack голосували за підвищення на 0,25 п.п.
- **URL:** <https://www.federalreserve.gov/newsevents/pressreleases/monetary20261028a.htm>
- **Дата й видавець:** 28.10.2026, Federal Reserve
- **Цитата (дослівно, мовою оригіналу):** «Inflation remains elevated.»; «maintain the target range for the federal funds rate at 3-3/4 to 4 percent»
- **Період даних:** 28.10.2026
- **Тип:** факт
- **Статус:** ПЕРВИННЕ
- **Confidence:** висока
- **Caveat:** Реальна ставка (розрахунок): 4,0 − 3,1 (core PCE) = +0,9 п.п.; 4,0 − 3,6 (headline PCE) = +0,4 п.п. Відкрито через Chrome.

## SC-86

**BLS: власне житло в CPI**

- **Claim:** Власне житло не ціноване в CPI: іпотечні відсотки, податки на нерухомість тощо не входять у споживання; для OER ціну оренди збирають раз на 6 місяців, а місячна зміна — корінь шостого степеня 6-місячної.
- **URL:** <https://www.bls.gov/cpi/factsheets/owners-equivalent-rent-and-rent.htm>
- **Дата й видавець:** змінено 13.02.2026, BLS
- **Цитата (дослівно, мовою оригіналу):** «Owned housing units themselves are not priced in the CPI Housing Survey…»; «The CPI program collects rent data from each sampled unit every 6 months.»
- **Період даних:** постійна методологія
- **Тип:** факт
- **Статус:** ПЕРВИННЕ
- **Confidence:** висока
- **Caveat:** Описує давню методологію, не зміну 2025–2026. Відкрито через Chrome.

## SC-87

**Zillow: OER проти ринкових оренд (червень 2026)**

- **Claim:** OER р/р квітень 3,30%, травень 3,32%, червень 3,25% (rent 2,79/2,92/2,84); Zillow: компоненти shelter ростуть швидше за ринкові оренди.
- **URL:** <https://www.zillow.com/research/cpi-forecast-2026-june/>
- **Дата й видавець:** 07.07.2026, Zillow Research
- **Цитата (дослівно, мовою оригіналу):** «Shelter components of the CPI continue to rise at a faster pace than on-market rents, reflecting softer new lease pricing alongside hikes for renewing and longer-term tenants.»
- **Період даних:** квітень–червень 2026 (+прогноз на 2026)
- **Тип:** факт
- **Статус:** НЕПІДТВЕРДЖЕНЕ
- **Confidence:** низька
- **Caveat:** Правка 07.11.2026 (U-3): сторінка Verifier-у недоступна (403), не перевірено; OER/rent р/р відтворено з FRED, зіставлення з ринковими орендами не підтверджено. Приватна дослідницька установа; прогноз Zillow (SFR +3,1%, багатоквартирні +2,0% у 2026) — проєкція. Гіпотеза «OER занижує інфляцію житла» у 2026 не підтримується, окрім епізоду жовтня 2025. Відкрито через Chrome.

## SC-88

**BEA: ВВП Q3 2026, advance (29.10.2026)**

- **Claim:** Реальний ВВП Q3 2026 +3,4% (річний темп), PCE-ціна +2,1%, core PCE +2,5%; ціни валових закупівель +3,0%; номінальний ВВП +5,6%.
- **URL:** <https://bea.gov/news/2026/gdp-advance-estimate-3rd-quarter-2026>
- **Дата й видавець:** 29.10.2026, BEA
- **Цитата (дослівно, мовою оригіналу):** «Real gross domestic product (GDP) increased at an annual rate of 3.4 percent in the third quarter of 2026»
- **Період даних:** Q3 2026 (advance)
- **Тип:** факт
- **Статус:** ПЕРВИННЕ
- **Confidence:** висока
- **Caveat:** Advance-оцінка, підлягає ревізіям (second estimate 25.11.2026). Неявний дефлятор 5,6 − 3,4 ≈ 2,1–2,2 (розрахунок). Відкрито через Chrome.

## SC-89

**Квартальні середні: чому Q3 PCE-ціна 2,1% при CPI 3,7% р/р (розрахунок)**

- **Claim:** З рядів FRED PCEPI: середні кварталів Q1 129,414, Q2 131,006, Q3 131,685 дають SAAR Q2 5,0% і Q3 2,09% (збіг із BEA); вересневий рівень 132,257 уже на 0,43% вищий за Q3-середнє, тож 'перенос' у Q4 ≈ 1,7% SAAR за нульового зростання цін.
- **URL:** <https://fred.stlouisfed.org/data/PCEPI>
- **Дата й видавець:** оновлено 29.10.2026, FRED/BEA; розрахунок Researcher
- **Цитата (дослівно, мовою оригіналу):** — (розрахунок)
- **Період даних:** Q1–Q3 2026
- **Тип:** оцінка
- **Статус:** ДОСТУПНЕ
- **Confidence:** середня
- **Caveat:** Ряд PCEPI прочитано повністю в Chrome, ряд CPIAUCSL (SAAR Q2 ≈ 6,1%, Q3 ≈ 1,7%) — через WebFetch (потребує повторної перевірки). Перенос у Q4 — розрахунок і ПРОЄКЦІЯ, не факт. Q3 SAAR не порівнювати напряму з CPI р/р.

## SC-90

**CEA 2018: вибір виміру зарплат (історичний прецедент)**

- **Claim:** У 2018 CEA заявило, що зарплати зросли на 1,4% (з бонусами й пільгами), тоді як BLS показував −0,2% за годинну оплату — прецедент вибору ширшого виміру в перший термін Трампа.
- **URL:** <https://www.scrippsnews.com/business/white-house-wages-are-up-contrary-to-bls-statistics>
- **Дата й видавець:** 06.09.2018, Scripps News
- **Цитата (дослівно, мовою оригіналу):** «Recent data from the Bureau of Labor Statistics shows American workers' hourly earnings were down 0.2 percent over the last year. But a Council of Economic Advisers, or CEA, analysis says wages actually increased 1.4 percent.»
- **Період даних:** 2018
- **Тип:** факт
- **Статус:** ВТОРИННЕ
- **Confidence:** середня
- **Caveat:** Історичний прецедент, не 2026. Паралелі 2026 (Ways and Means 04.2026 '+1,4%'; White House 12.2025) — лише сніпети, не відкривались.

## SC-91

**Гассетт про інфляцію, 19.10.2026**

- **Claim:** За агрегатором, директор NEC Гассетт сказав, що інфляція 'looks like it's back' і потребує роботи, а енергетичний стрибок назвав тимчасовим.
- **URL:** <https://www.roic.ai/news/hassett-inflation-looks-like-its-back-needs-work-10-19-2026>
- **Дата й видавець:** 19.10.2026, Roic AI
- **Цитата (дослівно, мовою оригіналу):** «Kevin Hassett… said inflation “looks like it's back” and needs work»
- **Період даних:** жовтень 2026
- **Тип:** позиція
- **Статус:** НЕПІДТВЕРДЖЕНЕ
- **Confidence:** низька
- **Caveat:** Правка 07.11.2026 (U-2): roic.ai дав 403, не відкрито Verifier-ом. Агрегатор; повного транскрипту інтерв'ю немає. Потрібне першоджерело.

## SC-92

**Трамп: «I love the inflation», 10.06.2026**

- **Claim:** Президент 10.06.2026 сказав журналістам «I love the inflation», згодом пояснив, що має на увазі цифри, які 'much lower than anticipated' на тлі війни.
- **URL:** <https://www.ibtimes.co.uk/trump-inflation-remarks-rising-prices-1817296>
- **Дата й видавець:** 01.09.2026, IBTimes UK
- **Цитата (дослівно, мовою оригіналу):** «President Donald Trump sparked controversy on 10 June 2026 after telling reporters in the Oval Office, 'I love the inflation'»
- **Період даних:** 10.06.2026
- **Тип:** позиція
- **Статус:** ВТОРИННЕ
- **Confidence:** низька
- **Caveat:** Вторинне видання; ціни CPI, які воно наводить (4,2% у травні тощо), не звірено з BLS, але кінцеві значення розрахункової таблиці (4,25% у травні) близькі. Контекст фрази — суперечливий.

## SC-93

**BLS: перелік комісарів і в.о. (дати служби)**

- **Claim:** За переліком BLS, Groshen — комісар січень 2013 – січень 2017; Wiatrowski — в.о. січень 2017 – березень 2019, березень 2023 – січень 2024 та серпень 2025 – серпень 2026; Beach — березень 2019 – березень 2023; McEntarfer — січень 2024 – серпень 2025; Matsumoto — з серпня 2026. Тобто вакансія 2017–2019 (в.о.) тривала понад 2 роки, 2025–2026 — 12 місяців.
- **URL:** <https://www.bls.gov/bls/history/commissioners/>
- **Дата й видавець:** змінено 11.08.2026, BLS
- **Цитата (дослівно, мовою оригіналу):** «William J. Wiatrowski, January 2017–March 2019; March 2023–January 2024; August 2025–August 2026»
- **Період даних:** 2012–2026
- **Тип:** факт
- **Статус:** ПЕРВИННЕ
- **Confidence:** висока
- **Caveat:** Перелік не пояснює причин вакансій і не оцінює, чи вакансія сама по собі ознака політизації. Відкрито через Chrome (chrome_navigate + chrome_get_web_content, нова вкладка) 07.11.2026. Додано Editor-ом за red team (D1).

<!-- sc-links: згенеровано scripts/sc_links.py, не редагувати -->

[SC-01]: #sc-01
[SC-18]: #sc-18
[SC-19]: #sc-19
[SC-26]: #sc-26
[SC-30]: #sc-30
[SC-33]: #sc-33
[SC-51]: #sc-51
[SC-52]: #sc-52
[SC-62]: #sc-62
[SC-85]: #sc-85
[SC-93]: #sc-93
