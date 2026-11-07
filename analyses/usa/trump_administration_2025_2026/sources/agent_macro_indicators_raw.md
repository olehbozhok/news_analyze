# Підтема D: узгодження інфляції з макропоказниками «економіка в нормі» (сирі нотатки Researcher)

Дата: 2026-11-07. Роль: Researcher (agents/researcher.md). Питання scope contract: 6, 7. Сирий файл: у фінальному документі не цитується (AGENTS.md, 6.2); для цитування потрібні source cards.
Мітки: [ФАКТ] виміряне значення; [РОЗРАХУНОК] моя арифметика з опублікованих чисел (перевірити Verifier); [ПРОЄКЦІЯ]; [ПОЗИЦІЯ] заява сторони; [КОНТЕКСТ] методологічний опис.
Інструменти: CH = Chrome MCP (`chrome_get_web_content`, сторінка відкрита, текст прочитано); WF = WebFetch (малa модель переказує сторінку: цифри з WF потребують повторної перевірки в Chrome); WS = WebSearch (сніпети: лише як вказівник, не як джерело). Усі сторінки відкривалися в нових вкладках/вікнах; чужі вкладки не чіпав. 403/429 для основних джерел не було (виняток: senate.gov — «Unauthorized», epi.org через WF — 403, але через CH відкрито).
Не повторюю: CPI/PCE/Cleveland/Atlanta/Truflation/очікування (agent_alternative_measures_raw.md), керівництво BLS/carry-forward/скорочення збору (agent_data_integrity_raw.md, agent_methodology_raw.md), медіанний дохід Census, SCF, S&P 500 (11_zhyttia_bilshosti.md, 08_balans_i_kontrarguventy.md). Нижче лише нове або те, що змінює оцінку.

## Зведення (відповіді за пунктами завдання)

1. **Реальний ВВП vs дефлятор.** Річне оновлення BEA (30.09.2026) разом зі зміною методів дефлювання (3 компоненти PCE-ціни) зсунуло дефлятори вниз, а реальне зростання вгору: Q1 2026 PCE-ціна 4,6 -> 4,2 (ядро 4,4 -> 3,9), реальний ВВП 2,1 -> 2,5 при НЕЗМІННОМУ номінальному ВВП (5,8) (M-01); Q2 реальний ВВП 1,5 -> 1,5 (advance/second) -> 2,2 (third, +0,7 пп), PCE-ціна 5,3 -> 5,0, ядро 3,6 -> 3,3 (M-01). Бухгалтерська тотожність: при фіксованому номіналі нижчий дефлятор дає вищий реальний ВВП. АЛЕ BEA пояснює ревізію реального ВВП в основному новими даними (інвестиції, споживання, держвитрати), а реальний GDI зріс ще більше (Q1 +1,3 пп до 2,5; Q2 2,6) (M-01) — тобто ознак «роздування» ВВП відносно доходу немає. Атрибуція частки ревізії саме методам дефлювання НЕ підтверджена джерелами (прогалина G-1). Q3 2026: реальний ВВП 3,4%, PCE-ціна 2,1% SAAR при CPI 3,7% р/р: розрив зумовлений методом (квартальні середні) і таймінгом (M-03, M-04): вересневий стрибок цін (PCE +0,5% м/м) лише наполовину потрапив у Q3-середнє; перенос у Q4 [РОЗРАХУНОК] ≈ +1,7% SAAR уже «закладено» при нульовому зростанні цін.
2. **Реальні доходи/зарплати.** Вимір вирішує знак: реальна погодинна оплата -0,7% р/р (CPI), але реальний тижневий заробіток -0,1% (бо робочий тиждень +0,6%) (M-06); для production/nonsupervisory -0,6% / -0,3%. Реальний наявний дохід -0,3% м/м у вересні (M-05). Адміністрація історично вибирала ширші виміри (CEA 2018: «зарплата +1,4% з бонусами й пільгами» проти BLS -0,2%) (M-24, прецедент першого терміну, не 2026).
3. **Ринок праці.** U-3 4,1% (жовтень), але U-6 7,9% (+0,3 пп до вересня), неповна зайнятість «з економічних причин» +339 тис. до 4,8 млн; довготривало безробітні 27,6% (M-07, M-08). LFPR 61,9%, EPOP 59,3%; популяційні контролі січня 2026 знизили LFPR на 0,4 пп і EPOP на 0,5 пп, не змінивши U-3 (M-09). Payrolls: +165 тис. у жовтні, але середнє за 12 міс. 48 тис.; серпень/вересень ревізовано +84 тис. (M-07). Prelim. бенчмарк березня 2026: -79 тис. (мало, на фоні фінальних -898 тис. за 2025 і -598 тис. за 2024) (M-10). ФРС (Board): breakeven зайнятості 2026 може бути <10 тис./міс., тож від'ємні місяці майже так само ймовірні, як додатні (M-11): низький приріст payrolls за стабільного U-3 не є ознакою слабкості сам по собі — і водночас «нормальний» U-3 тримається на майже нульовому рості робочої сили. Якість CPS: вибірка 60 000 домогосподарств, відповідь «upper 60 percent», <50 відповідей рухають U-3 на 0,1 пп (M-12); після шатдауну нові когорти відповідають нижче тренду, а загальна відповідь «підпирається» старими когортами (M-13).
4. **Фондовий ринок / концентрація:** нових джерел не додавав, окрім Zandi (лише сніпет, M-22): топ-10% за доходом ≈ 49% споживчих витрат. Решта — у 11_zhyttia_bilshosti.md.
5. **Борг/заощадження.** Норма заощаджень 3,8% (вересень); липень 3,0% до оновлення BEA -> серпень 4,1% після оновлення (M-05, M-14): частина «буфера» — наслідок ревізії, а не поведінки. NY Fed Q2 2026: прострочення 4,7% боргу; flow у серйозне прострочення по картках 6,97% (6,93% рік тому), студентські 7,83% (12,88%), авто 3,00% (2,93%), іпотека 1,52% (1,29%) (M-15). **Увага: у 11_zhyttia_bilshosti.md «12,8% проти 7,6% кварталом раніше» некоректно: за NY Fed 7,6% -> 12,8% — це 2022:Q3 -> 2026:Q1 (stock-міра), а NY Fed прямо пояснює зростання накопиченням списаних (charged-off) боргів, не погіршенням (M-16).** Нових даних за Q3 2026 NY Fed ще немає (сторінка станом на 07.11 показує Q2).
6. **Ставка/іпотека/житло/OER.** FOMC 28.10.2026: ставка 3,75–4%, 10–2 голосів (Cook, Hammack — за підвищення); «Inflation remains elevated» (M-17). Іпотека Freddie Mac (через FRED) 7,18% (05.11), пік 7,40% (08–15.10), 6,65% (20.08) (M-18) — іпотечні відсотки й ціни житла в CPI не входять (BLS: власне житло — капітал; враховується лише OER) (M-19). OER/rent: Zillow фіксує OER 3,25%, rent 2,84% р/р у червні; ринкові оренди (прогноз Zillow): SFR +3,1%, багатоквартирні +2,0% у 2026 (M-20) — тобто у 2026 р. OER НЕ занижує щодо ринкових оренд (скоріше навпаки, відставання вгору); заниження — лише епізод carry-forward жовтня 2025 (див. agent_alternative_measures_raw.md, A-…/MLR BLS).
7. **Ціна тарифів, якість, заміщення.** BLS: shrinkflation додає лише ≈0,01 пп/рік до CPI «товари та послуги» (2015–19), їжа ≈0,04 пп/рік; CPI враховує зміну розміру як зміну ціни за одиницю (M-21). CPI-U: верхній рівень — Laspeyres (нульове заміщення між категоріями), C-CPI-U (з заміщенням) 3,5% проти 3,7% (M-02, M-23). Core goods (commodities less F&E) лише +0,7% р/р у вересні, нові авто +0,6%, вживані -1,5% — тарифний тиск у цінах товарів за CPI слабо видно (M-02); прямої оцінки частки тарифів/якості/shrinkflation за 2026 не знайдено (G-3).
8. **Визначення/таймінг показників.** Жодної зміни визначення U-3/U-6 не знайдено. Змінилися: популяційні контролі (щорічно; 2026 — методологія Census, не «blended base»), відсутній жовтень 2025 в CPS, затримка контролів на місяць; методи дефлювання PCE (M-09, M-01). Відсутні y/y розрахунки за жовтень 2025 і (для CPS) за жовтень 2026 (M-13).
9. **Заяви адміністрації.** Дані не підтримують «інфляції немає»: Hassett 19.10.2026: інфляція «looks like it's back», енергетичний стрибок «temporary» (M-25); Trump 10.06.2026 «I love the inflation» + пояснення «без контексту» (M-26, вторинне); сама ФРС: «Inflation remains elevated», водночас «Economic activity is expanding at a strong pace» (M-17). Адміністрація публікує несприятливі цифри; не знайдено заяви «інфляцію переможено» в 2026 р. у відкритих джерелах (прогалина G-4: 2026 White House-заяви шукав лише через WS-сніпети).

## Картки тверджень

### M-01. BEA, річне оновлення 30.09.2026 + Q2 third estimate: реальний ВВП вгору, ціни вниз [ФАКТ]
- URL: https://bea.gov/news/2026/gdp-third-estimate-industries-corporate-profits-state-gdp-and-state-personal-income-2nd
- Видавець: BEA. Дата: 30.09.2026 (дата з WS-сніпета й змісту; на сторінці дати публікації немає — «Next release: October 29, 2026»). Період: Q1–Q2 2026. Інструмент: CH (повний текст).
- Цитати (дослівно): «Real GDP was revised up 0.7 percentage point from the second estimate, primarily reflecting upward revisions to investment, consumer spending, and government spending.» / «The personal consumption expenditures (PCE) price index increased 5.0 percent, revised down 0.3 percentage point, and the PCE price index excluding food and energy increased 3.3 percent, also revised down 0.3 percentage point.» / «Real GDI is now estimated to have increased 2.5 percent in the first quarter, 1.3 percentage points higher than previously estimated.» / «The PCE price index increased 4.2 percent, also revised down 0.4 percentage point. Excluding food and energy, the PCE price index increased 3.9 percent, revised down 0.5 percentage point.»
- Таблиця релізу (SAAR): Q2 — real GDP adv/2nd/3rd 1,5/1,5/2,2; current-dollar GDP 7,9/8,0/8,5; PCE price 5,1/5,3/5,0; core PCE price 3,4/3,6/3,3; real GDI —/2,2/2,6. Q1 (previous -> revised): real GDP 2,1 -> 2,5; current-dollar GDP 5,8 -> 5,8; PCE price 4,6 -> 4,2; core 4,4 -> 3,9; real GDI 1,2 -> 2,5; gross domestic purchases price 3,6 -> 3,2.
- Caveat: у Q1 номінальний ВВП не змінився, реальний +0,4, ціна -0,4 — арифметично «дефлятор вниз = реальне вгору», але BEA пояснює Q1-ревізію «exports of services and consumer spending», тобто змінилися й кількості. Вплив методів дефлювання окремо не виділено. Статус: ПЕРВИННЕ. Confidence: висока (цифри), низька (атрибуція методам).

### M-02. BLS CPI, вересень 2026 [ФАКТ]
- URL: https://www.bls.gov/news.release/cpi.nr0.htm. Видавець BLS, 14.10.2026. Період: вересень 2026. Інструмент: CH.
- Цитати: «Over the last 12 months, the all items index increased 3.7 percent before seasonal adjustment.» / «The all items less food and energy index rose 2.6 percent over the year» / «The Chained Consumer Price Index for All Urban Consumers (C-CPI-U) increased 3.5 percent over the last 12 months.» / «The Consumer Price Index for Urban Wage Earners and Clerical Workers (CPI-W) increased 3.9 percent over the last 12 months» / «In calculating the index, price changes for the various items in each location are aggregated using weights, which represent their importance in the spending of the appropriate population group.»
- Таблиця A (12 міс., вересень): Commodities less food and energy commodities 0,7; New vehicles 0,6; Used cars and trucks -1,5; Apparel 3,4; Medical care commodities -3,3; Shelter 3,2; Energy 20,4; Gasoline 34,2. Місячні SA All items: бер 0,9; кві 0,6; тра 0,5; чер -0,4; лип 0,1; сер 0,4; вер 0,6. Наступний реліз (жовтень): 10.11.2026.
- Статус: ПЕРВИННЕ.

### M-03. BEA GDP advance Q3 2026 (29.10.2026) [ФАКТ]
- URL: https://bea.gov/news/2026/gdp-advance-estimate-3rd-quarter-2026. Видавець BEA. Дата: 29.10.2026 (за «Next release» і сніпетом пошуку). Інструмент: CH.
- Цитати: «Real gross domestic product (GDP) increased at an annual rate of 3.4 percent in the third quarter of 2026» / «The price index for gross domestic purchases increased 3.0 percent in the third quarter, compared with an increase of 5.6 percent in the second quarter. The personal consumption expenditures (PCE) price index increased 2.1 percent, compared with an increase of 5.0 percent, and the PCE price index, excluding food and energy increased 2.5 percent, compared with an increase of 3.3 percent.»
- Таблиця: real GDP 3,4; current-dollar GDP 5,6; real final sales to private domestic purchasers 4,9. Техн. примітка: приріст зумовлений запасами й обладнанням («information processing equipment (mainly computers and peripheral equipment)»), споживання послуг (охорона здоров'я); експорт знизився. Про SPR: «Because the oil sold by the government is reflected as an increase in other components of GDP, there is no direct effect on GDP.»
- [РОЗРАХУНОК] Неявний дефлятор: 5,6 номінал - 3,4 реальний ≈ 2,1–2,2 (точно (1,056/1,034)^… ≈ 2,1). Наступний реліз: 25.11.2026. Advance-оцінка підлягає ревізіям. Статус: ПЕРВИННЕ.

### M-04. Квартальні середні цін: чому Q3 PCE-ціна 2,1% при CPI 3,7% р/р [РОЗРАХУНОК]
- Джерела даних: FRED PCEPI (https://fred.stlouisfed.org/data/PCEPI; Last Updated 2026-10-29; інструмент: CH, весь ряд прочитано) і FRED CPIAUCSL (https://fred.stlouisfed.org/data/CPIAUCSL; інструмент: WF — потребує повторної перевірки в CH).
- PCEPI (2017=100): січ 128,845; лют 129,293; бер 130,105; кві 130,672; тра 131,241; чер 131,106; лип 131,187; сер 131,611; вер 132,257 (вер 2025: 127,601). Середні кварталів: Q1 129,414; Q2 131,006; Q3 131,685. SAAR Q2 = (131,006/129,414)^4-1 = 5,0%; Q3 = (131,685/131,006)^4-1 = 2,09% -> збігається з BEA (5,0 і 2,1): перевірка, що ряд FRED = вектор BEA.
- CPIAUCSL SA: Q1 328,114; Q2 332,985; Q3 334,414 -> SAAR Q2 ≈ 6,1%, Q3 ≈ 1,7%.
- Вересень 2026 PCE-індекс (132,257) уже на 0,43% вищий за Q3-середнє (131,685): якщо ціни в Q4 не ростуть, Q4/Q3 SAAR ≈ 1,7% «переносу» [РОЗРАХУНОК]. P/y вереснева PCE-ціна: 132,257/127,601 = +3,65% (BEA: 3,6%).
- Висновок для документа: низька Q3-цифра дефлятора — наслідок методу «середнє кварталу» і падіння цін у червні (CPI -0,4% м/м), а не прихованої інфляції; вереснева інфляція (газ +9,1% м/м) потрапить у Q4-дефлятор. Реальний ВВП Q3 3,4% «виграє» від тимчасово низького Q3-дефлятора; ризик ревізії/зниження реального зростання в Q4 при незмінному номіналі [ПРОЄКЦІЯ, не факт].
- Статус: ПЕРВИННЕ (дані) / розрахунок мій. Confidence: висока для PCEPI, середня для CPIAUCSL (WF).

### M-05. BEA Personal Income and Outlays, вересень 2026 (29.10.2026) [ФАКТ]
- URL: https://www.bea.gov/news/2026/personal-income-and-outlays-september-2026. Інструмент: CH.
- Цитати: «the personal saving rate—personal saving as a percentage of DPI—was 3.8 percent.» / «From the same month one year ago, the PCE price index for September increased 3.6 percent. Excluding food and energy, the PCE price index increased 3.1 percent from one year ago.»
- Таблиця (м/м): real DPI серпень 0,0, вересень -0,3; real PCE 0,5 / 0,0; PCE price 0,3 / 0,5; core 0,3 / 0,3; current-dollar PCE 0,9 / 0,5. Заощадження $911,1 млрд.
- Порівняння CPI vs PCE (вересень р/р): headline 3,7 vs 3,6; core 2,6 vs 3,1 (core PCE вище core CPI на 0,5 пп). Статус: ПЕРВИННЕ.

### M-06. BLS Real Earnings, вересень 2026 [ФАКТ]
- URL: https://www.bls.gov/news.release/realer.nr0.htm. BLS, 14.10.2026. Інструмент: CH.
- Цитати: «From September 2025 to September 2026, real average hourly earnings decreased 0.7 percent, seasonally adjusted. The change in real average hourly earnings combined with a 0.6-percent increase in the average workweek resulted in a 0.1-percent decrease in real average weekly earnings over this period.» / production and nonsupervisory: hourly -0,6%, weekly -0,3%. Місячно: real hourly -0,5%.
- Дефлятор тут CPI-U (CPI-W для production). Номінально AHE жовтня: «$38.00… increased by 3.1 percent» (M-07); якщо дефлювати PCE (3,6% у вересні) -> ≈ -0,5% (не -0,7%) [РОЗРАХУНОК, AHE вересня +3,0% за doc 11]. Статус: ПЕРВИННЕ.

### M-07. BLS Employment Situation, жовтень 2026 (06.11.2026) [ФАКТ]
- URL: https://www.bls.gov/news.release/empsit.nr0.htm. Інструмент: CH.
- Цитати: «Total nonfarm payroll employment rose by 165,000 in October, higher than the average monthly gain of 48,000 over the prior 12 months.» / «The unemployment rate has remained in a narrow range of 4.1 percent to 4.3 percent since March.» / «Both the labor force participation rate, at 61.9 percent, and the employment-population ratio, at 59.3 percent, changed little in October. These measures have shown little net change since January.» / «The number of people employed part time for economic reasons increased by 339,000 to 4.8 million in October.» / «The long-term unemployed accounted for 27.6 percent of all unemployed people.» / «Over the past 12 months, average hourly earnings have increased by 3.1 percent.» / «employment in August and September combined is 84,000 higher than previously reported.»
- Примітка: доки 11/08 (безробіття 4,2% = вересень) застаріли на один реліз: жовтень 4,1%. Наступний реліз: 04.12.2026. Статус: ПЕРВИННЕ.

### M-08. BLS Table A-15 (U-1…U-6), жовтень 2026 [ФАКТ]
- URL: https://www.bls.gov/news.release/empsit.t15.htm. Інструмент: CH. Last Modified 06.11.2026.
- Seasonally adjusted: U-3 / U-4 / U-5 / U-6: вересень 4,2 / 4,4 / 5,0 / 7,6; жовтень 4,1 / 4,4 / 5,1 / 7,9; червень 4,2 / 4,5 / 5,2 / 7,9. Примітка: «Data for October 2025 were not collected due to the federal government shutdown.» (колонка жовтня 2025 порожня «-»). Різниця U-6 - U-3 = 3,8 пп (жовтень 2026) [РОЗРАХУНОК]. Порівняння з січнем 2025 не робив (прогалина G-5: немає U-6 січня 2025 у відкритому джерелі). Статус: ПЕРВИННЕ.

### M-09. BLS: популяційні контролі січня 2026 [ФАКТ/КОНТЕКСТ]
- URL: https://www.bls.gov/cps/methods/population-controls/experimental-series-accounting-for-January-2026-population-control-effects.htm. BLS, остання зміна 10.04.2026. Інструмент: CH.
- Цитати: «The adjustment lowered the labor force participation rate by 0.4 percentage point and lowered the employment–population ratio by 0.5 percentage point. The adjustment had little effect on the number of unemployed people (+15,000), and the unemployment rate was unaffected.» / «This marks a departure from the “blended base” introduced in recent years» / «the adjustment increased the number of people not in the labor force by 1.2 million. The total civilian labor force decreased by 1.4 million».
- Висновок: часові ряди LFPR/EPOP/зайнятості CPS розривні між груднем 2025 і січнем 2026 (офіційні дані до грудня не ревізовано). U-3 не зачеплено. Порівнювати LFPR 2025 і 2026 напряму — помилка. Статус: ПЕРВИННЕ.

### M-10. Преліміарний бенчмарк payrolls, березень 2026 [ФАКТ, вторинне джерело]
- URL: https://www.econoday.com/?p=16941 (Econoday, Theresa Sheehan, 28.08.2026). Інструмент: CH. Первинна сторінка BLS https://www.bls.gov/web/empsit/cesprelbmk.htm відкрилась порожньою (динамічна) — первинне НЕ перевірено; відкрито BLS-реліз по штатах https://www.bls.gov/news.release/archives/presae_08282026.htm (CH): «The average absolute preliminary benchmark revision across all states and the District of Columbia was 0.4 percent for March 2026.»
- Цитата Econoday: «The BLS issued the March 2026 preliminary benchmark revision for total nonfarm payrolls as a downward revision of 79,000. The size of the 2026 preliminary revision is substantially smaller than the past few years. The final revision for 2025 was down 898,000 and 2024 was down 598,000.» і «the preliminary annual revision for private payrolls is down 178,000 for March 2026».
- Контекст: EPI 09.09.2025 (CH): прелім. бенчмарк 2025 -911 тис.; EPI: ревізії «are not corrections of mistakes» (позиція). Фінальний бенчмарк 2026 — лютий 2027. Статус: ВТОРИННЕ. Confidence: середня (-79 тис.); високо — що відхилення 2026 мале.
- Важливо для балансу: 2026 prelim -79 тис. ≈ -0,05% рівня; ознак систематичного завищення payrolls у 2026 цей показник не дає (на відміну від 2024–25), але ФРС (M-11) вказує на інший ризик — завищену популяцію.

### M-11. ФРС (Board) FEDS Note: breakeven зайнятості [ПРОЄКЦІЯ/оцінка персоналу ФРС]
- URL: https://federalreserve.gov/econres/notes/feds-notes/labor-force-growth-breakeven-employment-and-potential-gdp-growth-20260402.html. Murray & Vidangos, 02.04.2026. Інструмент: CH.
- Цитати: «near-zero labor force growth implies that breakeven employment growth (i.e. the pace needed to maintain a steady unemployment rate) would also be near-zero—making negative job growth almost as likely as positive job growth in any given month.» / «the BLS may be overestimating the pace of population growth in 2026 as its estimates of population growth rely on the Census Bureau's projection that net immigration will boost population growth in 2026 by about 320,000» / Brookings: net immigration у 2026 «between –925,000 and +185,000» / «it would not be unusual for there to be one or more months in 2026 with declines in total payroll employment as large as -100,000 jobs, even if economic output was growing at the rate of potential output growth» / сноска 5: початкові оцінки payrolls «have tended to be revised down» при бенчмарку.
- Спостереження [ФАКТ, BLS Table A-1, CH https://www.bls.gov/news.release/empsit.t01.htm]: цивільне населення 16+ зросло з 275 166 тис. (червень) до 275 682 тис. (жовтень 2026), ≈ +129 тис./міс. (≈0,56% річних) [РОЗРАХУНОК] — вище за ≈90 тис./міс. (0,4%) січня–лютого за FEDS Note і набагато вище за сценарій Brookings (<0,2%). Це інференція: населення в CPS — модельне (контролі Census), тож LFPR/EPOP/рівні зайнятості можуть бути спотворені, якщо міграція нижча за припущення Census; U-3 як частка менш чутлива. Не доведено. Статус: ПЕРВИННЕ (документ) / оцінка.

### M-12. BLS: звіт до Appropriations про модернізацію CPS (квітень 2026) [ФАКТ]
- URL: https://www.bls.gov/bls/congressional-reports/report-to-the-appropriations-committees-on-modernizing-the-current-population-survey-april-2026.htm. Інструмент: CH.
- Цитати: «Response rates have historically been very high but have declined from the low 90 percent range to the upper 60 percent range over the last 15 years» / «The CPS sample size in 2026, which consists of 60,000 eligible households, is the same as it was in 1981, even though the population used for the CPS has increased by 61%.» / «At current sample sizes, a net change of fewer than 50 survey responses could move the headline unemployment rate by 0.1 percentage point.» / «20 years ago the CPS could detect that an over-the-month change in the unemployment rate as small as 0.18 percentage point was statistically significant, while now it would take two months of data». Інтернет-самозвітування (ISR) і паралельне опитування 45 000 домогосподарств, ≈$60 млн/рік; ризик mode effect («could lead to a change in the unemployment rate»).
- Висновок: ISR не запроваджено; жодна зміна визначення U-3 не заплановано в цьому джерелі. Статус: ПЕРВИННЕ (позиція BLS про власну якість).

### M-13. Atlanta Fed: відповіді CPS після шатдауну (09.04.2026) [ФАКТ/аналіз]
- URL: https://www.atlantafed.org/research-and-data/publications/policy-hub-macroblog/2026/04/09/more-than-missing-data-survey-response-rates-following-2025-government-shutdown. Ben Miller. Інструмент: CH.
- Цитати: «the CPS response rate fell sharply, declining by almost 5 percentage points from the September to November surveys.» / «These significantly higher response rates among pre-shutdown households in their second rotation have propped up the overall response rate, masking the persistent underperformance among post-shutdown cohorts.» / «Cai and Baker (2021) found respondents who indicated they were unemployed or not in the labor force were more likely to be missing in future observations, suggesting that the unemployment rate could be biased downward.» / «any labor force measures that are calculated on a year-over-year basis will be missing in both October 2025 and October 2026».
- Висновок: напрям можливого зміщення — U-3 занижений (non-response), але це гіпотеза з літератури (2021), а не доведений ефект 2026. Статус: ПЕРВИННЕ/аналітика Fed-банку (не офіційна позиція ФРС).

### M-14. BEA: норма заощаджень до і після оновлення [ФАКТ]
- URLs: https://www.bea.gov/news/2026/personal-income-and-outlays-july-2026 (CH): «Personal saving was $712.0 billion in July, and the personal saving rate… was 3.0 percent.»; https://bea.gov/news/2026/personal-income-and-outlays-august-2026 (CH, 30.09.2026): «Personal saving was $990.2 billion, and the personal saving rate… was 4.1 percent.»; вересень 3,8% (M-05).
- Порівняння липня (до) і серпня (після оновлення) змішує зміну поведінки й ревізію; ревізований липень не знайдено в BEA-релізах (прогалина G-2). Вторинне джерело (Axis Intelligence, лише сніпет WS, не відкрито) стверджує перегляд червня 2,7 -> 4,4 і липня 3,0 -> 4,6 — НЕ ВИКОРИСТОВУВАТИ без перевірки по BEA. Статус: ПЕРВИННЕ (3,0 / 4,1 / 3,8), ревізія — НЕПІДТВЕРДЖЕНЕ.
- Також PCE р/р: липень (до оновлення) 3,7%, core 3,3%; серпень (після) 3,4%, core 3,0% (BEA, CH): стрибок вниз частково методологічний [РОЗРАХУНОК: Q1/Q2 ревізії -0,3…-0,5 пп], частково реальний; CPI у липні 3,4%, серпні 3,4%.

### M-15. NY Fed Household Debt and Credit, Q2 2026 (11.08.2026) [ФАКТ]
- URL: https://www.newyorkfed.org/newsevents/news/research/2026/20260811 (CH); також https://www.newyorkfed.org/microeconomics/hhdc.html (CH: на 07.11.2026 — останній звіт Q2 2026).
- Цитати: «Aggregate delinquency rates improved slightly in Q2 2026, with 4.7% of outstanding debt in some stage of delinquency.» / «Delinquency rates across most products have held steady over the past two years… new delinquencies for auto loans and credit cards remain at elevated levels» (Joelle Scally) / «Student loan delinquencies were an exception, with the continued impact of the re-reporting of defaulted student debt causing some distortions.»
- Flow у 90+ днів (Q2 2025 -> Q2 2026): mortgage 1,29 -> 1,52; student 12,88 -> 7,83; auto 2,93 -> 3,00; card 6,93 -> 6,97; all 2,91 -> 2,57. Баланси: $18,771 трлн; card $1,263 трлн; auto $1,713 трлн; student $1,651 трлн. Mean/агрегат (балансова вага), не медіанне домогосподарство. Статус: ПЕРВИННЕ.

### M-16. NY Fed Liberty Street: stock vs flow прострочення за картками [ФАКТ] — ВАЖЛИВО для doc 11
- URL: https://libertystreeteconomics.newyorkfed.org/2026/08/how-distressed-are-consumers-reconciling-diverging-credit-card-delinquency-measures/ (11.08.2026). Інструмент: CH.
- Цитата: «between 2022:Q3 and 2026:Q1, the percentage of credit card balances 90+ days delinquent rose from 7.6 percent to 12.8 percent, prompting concerns that Americans are falling behind on their debt payments at rates not seen since the Great Recession. Yet the flow delinquency rate… has remained relatively stable for almost two years.» / «the stock delinquency rate is rising because of a pool of stale, charged-off debts that lenders have been reporting for longer durations, rather than a fundamental worsening in the incidence of delinquency.» / «the pace of credit card delinquency is elevated but has been largely stable since 2024.» / «more than 23 million Americans still carrying charged-off credit card balances».
- Знахідка для Writer/Verifier: 11_zhyttia_bilshosti.md (рядки ≈134, 145) подає «12,8% (проти 7,6% кварталом раніше)» — за NY Fed 7,6% відноситься до 2022:Q3, а не до попереднього кварталу; і це stock-міра, на яку впливає накопичення списаних боргів. Потенційний MAJOR (число/база порівняння). Не змінюю doc. Статус: ПЕРВИННЕ.

### M-17. FOMC statement 28.10.2026 [ФАКТ/ПОЗИЦІЯ ФРС]
- URL: https://www.federalreserve.gov/newsevents/pressreleases/monetary20261028a.htm. Інструмент: CH.
- Цитати: «maintain the target range for the federal funds rate at 3-3/4 to 4 percent» / «Economic activity is expanding at a strong pace.» / «Job gains have kept pace with the workforce, and the unemployment rate has changed little. Inflation remains elevated.» / «Voting against… Lisa D. Cook and Beth M. Hammack, who preferred to raise the target range… by 1/4 percentage point».
- Реальна ставка [РОЗРАХУНОК]: верхня межа 4,0 - core PCE 3,1 = +0,9 пп; - headline PCE 3,6 = +0,4 пп. Тобто «нейтральна/слабо обмежувальна», за вимірами, які мають значення. Статус: ПЕРВИННЕ.

### M-18. Іпотека 30-year (Freddie Mac PMMS через FRED) [ФАКТ]
- URL: https://fred.stlouisfed.org/data/MORTGAGE30US. Інструмент: WF (малa модель; перевірити в CH). Значення: 20.08 6,65; 27.08 6,66; 03.09 6,71; 10.09 6,76; 17.09 6,95; 24.09 7,03; 01.10 7,28; 08.10 7,40; 15.10 7,40; 22.10 7,32; 29.10 7,24; 05.11 7,18. Статус: ДОСТУПНЕ. Confidence: середня (WF).
- Контекст: раніше doc 11 дає 7,24% (29.10) — узгоджено.

### M-19. BLS: власне житло в CPI [КОНТЕКСТ]
- URL: https://www.bls.gov/cpi/factsheets/owners-equivalent-rent-and-rent.htm (останнє змінення 13.02.2026). Інструмент: CH.
- Цитати: «Owned housing units themselves are not priced in the CPI Housing Survey… Spending to purchase and improve houses and other housing units is treated as investment and not consumption in the CPI. Interest costs (such as mortgage interest), property taxes, real estate fees, most maintenance, and all improvement costs are part of the cost of the capital good and are also not treated as consumption items.» / «The CPI program collects rent data from each sampled unit every 6 months.» / «Dividing the average pure rent for the current month (t) by the average pure rent from 6 months earlier (t-6) yields the 6-month relative of price change. The sixth root of this relative is the 1-month change in OER».
- Висновок: ріст іпотечної ставки з 6,65 до 7,40 за два місяці не відображається в CPI (кошик не містить відсотків); це бюджетний тиск на покупців, що CPI не вимірює за дизайном (та сама дефініція діє з давніх пір, не зміна 2025–26). Статус: ПЕРВИННЕ.

### M-20. Zillow: CPI shelter forecast (червень 2026) [ФАКТ + ПРОЄКЦІЯ]
- URL: https://www.zillow.com/research/cpi-forecast-2026-june/ (07.07.2026). Інструмент: CH.
- Цитати: «Shelter components of the CPI continue to rise at a faster pace than on-market rents, reflecting softer new lease pricing alongside hikes for renewing and longer-term tenants.» Таблиця «actual»: OER р/р квітень 3,30%, травень 3,32%, червень 3,25%; rent р/р 2,79 / 2,92 / 2,84. Прогноз Zillow (проєкція): SFR on-market +3,1%, багатоквартирні +2,0% у 2026; OER 2026 ≈ 3,40%, rent ≈ 3,13%.
- Статус: ДОСТУПНЕ (приватна дослідницька установа; частково прогноз; не BLS). Висновок: у 2026 р. OER/rent не нижчі за ринкові оренди; гіпотеза «OER занижує інфляцію житла» не підтримується для 2026, окрім епізоду жовтня 2025.

### M-21. BLS: shrinkflation у CPI [КОНТЕКСТ/ФАКТ]
- URL: https://www.bls.gov/opub/btn/volume-12/measuring-shrinkflation-and-its-impact-on-inflation.htm (Kari McNair, лютий 2023, з додатком по 2019–23). Інструмент: CH.
- Цитати: «An effective price per standard size, usually a price per ounce, is calculated for items where size is reported.» (приклад: 64 oz -> 60 oz за ту ж ціну = +6,7%) / «product size changes (upsizing and downsizing) increased the CPI all commodity and services index by 0.01 percent per year.» / food and beverages: -0,21% за 2015–19 (≈0,04 пп/рік). Додаток 2019–23 (текст сторінки): household paper products 34,9 vs 31,2 без downsizing (-3,6 пп), snacks 26,4 vs 23,9.
- Обмеження: оцінка BLS про себе (позиція відомства), період 2015–2023, не 2025–26; не охоплює приховану деградацію якості без зміни ваги/об'єму. Статус: ПЕРВИННЕ (позиція BLS).

### M-22. Концентрація витрат: Zandi (Moody's) [лише сніпет WS, НЕ відкрито]
- Через WS: топ-10% за доходом ≈ 49,2% споживчих витрат (рекорд з 1989; ≈43% у 2020). Первинний PDF https://econofact.org/wp-content/uploads/2026/07/EF-Chats-Transcript-Zandi-The-Economy-and-the-Tenuously-Resilient-Consumer.pdf у CH і WF не прочитався (стиснутий PDF) — НЕПІДТВЕРДЖЕНЕ для цитування. Інший сніпет: «AI-spending… half of GDP growth» — джерело не підтверджено, не використовувати.

### M-23. BLS Handbook of Methods: CPI calculation [КОНТЕКСТ]
- URL: https://www.bls.gov/opub/hom/cpi/calculation.htm. Інструмент: CH (сторінка 78 тис. симв., збережена у tool-results; прочитано фрагменти через пошук за ключовими словами).
- Цитата: «In a Laspeyres aggregation, consumer substitution between items is assumed to be zero.» / «Sources of direct quality adjustment information include observable factors such as size or weight, manufacturers' cost data, and hedonic regression models.» / про заміну товару: «The price change between the original item and the noncomparable replacement item is assumed to be the same as the average price change of all similar items in 1 month for the same geographic area».
- Дата: на сторінці у витягу немає «Last Modified» (не встановлено). Outlet-substitution/нові точки продажу: окремого пасажу з цією термінологією не знайдено (прогалина G-3). Статус: ПЕРВИННЕ.

### M-24. CEA 2018 vs BLS: прецедент вибору виміру зарплат [ФАКТ, історичний]
- URL: https://www.scrippsnews.com/business/white-house-wages-are-up-contrary-to-bls-statistics (Scripps News, 06.09.2018). Інструмент: CH.
- Цитата: «Recent data from the Bureau of Labor Statistics shows American workers' hourly earnings were down 0.2 percent over the last year. But a Council of Economic Advisers, or CEA, analysis says wages actually increased 1.4 percent.» / «The CEA says the BLS measurements aren't fully accurate because they don't factor in bonuses and benefits.»
- Це перший термін Трампа; для 2026 р. паралелі в WS-сніпетах (Ways and Means 04.2026 «+1,4%»; White House 12.2025 «real wages on track to rise 4,2%») НЕ відкривав — НЕПІДТВЕРДЖЕНЕ. Статус: ВТОРИННЕ (історичний прецедент).

### M-25. Hassett про інфляцію (19.10.2026) [ПОЗИЦІЯ, вторинне]
- URL: https://www.roic.ai/news/hassett-inflation-looks-like-its-back-needs-work-10-19-2026 (Roic AI, Lila Merrick, 19.10.2026). Інструмент: CH. Агрегатор; повного транскрипту інтерв'ю немає (сайт сам зазначає це).
- Цитата сайту: «Kevin Hassett… said inflation “looks like it's back” and needs work» / «He described the energy increase as “temporary”» / «He urged the Federal Reserve to wait for another month of data before raising interest rates». Також PPI вересня +1,3% м/м і import prices +1,1% (дані сайту, не звірені). Статус: ВТОРИННЕ (слабке; потрібне першоджерело — інтерв'ю/транскрипт).

### M-26. Trump «I love the inflation» (10.06.2026) [ПОЗИЦІЯ, вторинне]
- URL: https://www.ibtimes.co.uk/trump-inflation-remarks-rising-prices-1817296 (IBTimes UK, Robert Gorgonio, 01.09.2026). Інструмент: CH.
- Цитати: «President Donald Trump sparked controversy on 10 June 2026 after telling reporters in the Oval Office, 'I love the inflation'» / Trump пізніше: «'I love the inflation numbers because of what I'm talking about… despite the fact that we're in a war, the numbers are much lower than anticipated'». Сайт: CPI 4,2% у травні, 3,8% у квітні, 2,4% у лютому (дані не звірені з BLS; квітень/травень можна звірити за FRED CPI). Статус: ВТОРИННЕ.

## Таблиця «вимір -> що показує -> кому вигідно» (мій аналіз, не факт)

| Питання | Вимір A | Вимір B | Знак/розрив | Кому вигідно A |
|---|---|---|---|---|
| Інфляція вересня р/р | CPI-U 3,7% (M-02) | PCE 3,6%, core PCE 3,1% vs core CPI 2,6% (M-05) | headline майже збіг; core PCE вище | CPI core 2,6% «м'якше» звучить для адміністрації; PCE core 3,1% — для ФРС-яструбів |
| Інфляція Q3 | PCE 2,1% SAAR (M-03) | CPI-U 3,7% р/р (M-02) | різні бази: квартал SAAR vs 12 міс. | низька Q3-цифра підсилює «реальне зростання 3,4%» |
| Реальна зарплата | hourly -0,7% (M-06) | weekly -0,1% (M-06) | -0,6 пп різниці через довший тиждень | weekly менш негативний |
| Безробіття | U-3 4,1% | U-6 7,9% | 3,8 пп | U-3 |
| Зайнятість | payrolls +165 тис. | 12-міс. середнє 48 тис.; breakeven <10–85 тис. (M-11) | те саме число різно інтерпретується | залежить від позиції |
| Заощадження | 3,8% (після оновлення) | 3,0% (липень до) | змішування ревізії | вищий буфер |
| Прострочення карток | flow 6,97% (стабільно) | stock 12,8% (зростає) | NY Fed: stock підсилений charged-off | flow — «норма»; stock — «криза» |
| Реальний ВВП | real GDP 2,2% (Q2) | GDI 2,6%, avg 2,4% | GDI вище; ревізія вгору | обидва підтримують «норму» |

## Прогалини

- G-1. Частка ревізії реального ВВП/споживання від зміни дефляторів (портфельне управління, юридичні послуги, ПЗ) окремо — BEA SCB-стаття про результати оновлення (Survey of Current Business, жовтень 2026) не відкривалась; відомо лише: методи PCE-ціни змінено для 3 компонентів, ревізії великі (M-01). Вага цих компонентів у PCE мала (не підтверджено цифрами).
- G-2. Ревізовані (post-update) значення заощаджень за 2026 і ревізовані р/р PCE за липень не знайдено у відкритих BEA-сторінках (потрібна таблиця 2.6 BEA).
- G-3. Прямих оцінок «ціни тарифів» у CPI (pass-through vs якість/shrinkflation/заміщення) за 2026 не знайдено; PNC-звіт від 14.07.2026 (PDF не прочитався) — лише сніпет: «core goods… contracted at a 0.5% annualized pace over the past three months» — НЕПІДТВЕРДЖЕНЕ. «Outlet substitution» як термін BLS не знайдено.
- G-4. Офіційні заяви White House/CEA 2026 про інфляцію/реальні зарплати відкрито лише через сніпети; прямих «інфляцію переможено» у 2026 р. не знайдено. White House press statement по CPI вересня 2026 не знайдено (Senate Warren statement: senate.gov «Unauthorized»).
- G-5. U-6 січня 2025 для порівняння, LFPR січня 2025 — не збирав.
- G-6. NY Fed Q3 2026 ще не вийшов (на 07.11). Прострочення Q3 — даних немає.
- G-7. Стейк-фондовий ринок (концентрація, mean vs median) — нових первинних даних не додано; опираємося на 11_zhyttia_bilshosti.md (S&P/SCF).
- G-8. Первинна сторінка BLS prelim benchmark (національна) не відкрилась; використано Econoday (M-10).
- G-9. Жовтневий CPI виходить 10.11.2026, Q3 second GDP та PCE жовтня — 25.11.2026, зайнятість листопада — 04.12.2026: «станом на» треба оновити перед здачею (AGENTS.md, розділ 3, п. 6).

## Контрджерела / що проти тези «підміни»

- Усі основні показники публікуються й показують і погане (real earnings -0,7%, U-6 7,9%, FOMC «inflation remains elevated»), і добре (GDP 3,4%, U-3 4,1%). Ознак зміни визначення U-3/U-6 чи CPI/PCE-формул за політичним мотивом не знайдено; зміни методів дефлювання BEA — стандартне щорічне оновлення з попереднім анонсом (SCB 24.06.2026, блог BEA 17.08.2026), а виправдання — що CPI юридичних послуг не публікувався з вересня 2024 і «exhibited erratic changes» (M-01 пов'язане: https://bea.gov/index.php/news/blog/2026-08-17/annual-update-gdp-industry-and-state-stats-publicly-available-starting-sept-30, CH).
- Реальний GDI також вищий після оновлення — ревізія не лише ціновa.
- Prelim benchmark 2026 мізерний (-79 тис.) порівняно з 2024–25.
- Ризики справжніх спотворень: (а) якість CPS (60 тис. домогосподарств, відповідь «upper 60 percent»), (б) популяція/міграція в CPS-знаменнику, (в) квартальне усереднення дефлятора (Q3), (г) stock vs flow у боргу, (д) вибір CPI vs PCE vs hourly vs weekly.

## Vintage (AGENTS.md, 4.4)

| Показник | Останній період | Джерело | Наступний реліз |
|---|---|---|---|
| CPI-U, core CPI | вересень 2026 | BLS (M-02) | 10.11.2026 (жовтень) |
| PCE price, core PCE, saving rate, real DPI | вересень 2026 | BEA (M-05) | 25.11.2026 (жовтень) |
| Real GDP, PCE-ціна, GDI | Q3 2026 advance (GDI ще немає для Q3); Q2 third; річне оновлення Q1 2021–Q1 2026 | BEA (M-01, M-03) | 25.11.2026 (Q3 second) |
| U-3, U-6, LFPR, payrolls | жовтень 2026 | BLS (M-07, M-08) | 04.12.2026 (листопад) |
| Real earnings | вересень 2026 | BLS (M-06) | 10.11.2026 (жовтень) |
| Prelim. бенчмарк | березень 2026 | Econoday/BLS (M-10) | фінальний — лютий 2027 |
| Household debt | Q2 2026 | NY Fed (M-15) | Q3 — очікується листопад 2026 (дата не підтверджена) |
| Mortgage rate | 05.11.2026 | FRED/Freddie Mac (M-18) | щотижня, четвер |
| FOMC | 28.10.2026 | ФРС (M-17) | наступне засідання (дата не перевірялась) |

Підсумок: карток M-01…M-26 (26). За статусом: ПЕРВИННЕ 16 (M-01, 02, 03, 05, 06, 07, 08, 09, 11, 12, 13, 14, 15, 16, 17, 19; плюс M-23 і M-21 також первинні BLS-сторінки -> 18); ВТОРИННЕ 4 (M-10, M-24, M-25, M-26); ДОСТУПНЕ 2 (M-18, M-20); розрахунковий M-04 (дані ПЕРВИННЕ/WF); НЕПІДТВЕРДЖЕНЕ 1 (M-22).
