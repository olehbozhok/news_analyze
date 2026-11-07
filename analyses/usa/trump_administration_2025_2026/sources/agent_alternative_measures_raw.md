# Підтема C: альтернативні й неофіційні виміри інфляції 2025–2026 (сирі нотатки Researcher)

Дата: 2026-11-07. Роль: Researcher (agents/researcher.md). Питання scope contract: 4, 7. Сирий файл: у фінальному документі не цитується (AGENTS.md, 6.2); для цитування потрібні source cards.
Позначки: [ФАКТ] виміряне значення; [ПРОЄКЦІЯ] оцінка/прогноз; [ПОЗИЦІЯ] заява сторони/коментатора. Інструмент вказано біля кожного пункту. Chrome (chrome_get_web_content) використано для Atlanta Fed і Adobe (WebFetch повернув неповний текст); 403/429 не траплялося.

## Зведення

1. Станом на вересень 2026 (CPI-U реліз 14.10.2026): headline CPI 3,7% р/р, core CPI 2,6% р/р, shelter 3,2% р/р. Медіана Cleveland 2,6%, trimmed-mean 2,7%, Atlanta sticky 2,8% р/р (flexible 6,1% р/р). Тобто «внутрішня» інфляція за робастними мірами (2,6–2,8%) помітно нижча за headline (3,7%): розрив зумовлений енергетикою/flexible-компонентами, а не прихованою недооцінкою ядра.
2. Core PCE (3,1% р/р, вересень, BEA 29.10.2026) вищий за core CPI (2,6%) — зворотний до звичного напрямок розриву. Це не свідчить про недооцінку CPI ядра одноосібно (різні кошики/ваги), але потребує пояснення в документі (гіпотеза: оренда, вага shelter, програмне забезпечення/ПО; джерела пояснень слабкі, див. H-3).
3. Carry-forward оренди (жовтень 2025): BLS MLR (12.05.2026) кількісно підтверджує заниження rent/OER 12-міс. змін (напр., OER 3,29% опубліковано проти 3,57–3,90% за контрфактичними методами), але до квітня 2026 індекси зійшлися. Вплив на all-items/core BLS не кількісно оцінює.
4. Truflation систематично нижча за BLS у 2026 (0,93–1,47% на початку року проти ~2,4%; 2,11% 27.07 проти 3,5% за червень), але методологія слабо задокументована, ваги shelter нижчі; розбіжність спрямована саме в бік «CPI вищий», тобто Truflation НЕ підтверджує недооцінки офіційних даних.
5. PriceStats (State Street) 2026 близька до CPI (за власним твердженням), без стандартних коригувань якості.
6. Очікування: UMich (попередній листопад 2026) 1 рік 4,3%, довгострокові 3,4%; NY Fed SCE (вересень) 1 р. 3,9%, 3 р. 3,3%, 5 р. 3,0%; 10-річний breakeven 2,23% (6.11.2026), 5y5y 2,17%. Ринкові breakevens значно нижчі за опитування — розходження опитувань і ринку.

## Картки тверджень

### A-01. Cleveland Fed: median та 16% trimmed-mean CPI, вересень 2026 [ФАКТ]
- URL: https://www.clevelandfed.org/indicators-and-data/median-cpi
- Видавець: Federal Reserve Bank of Cleveland. Оновлено 14.10.2026 (наступне 10.11.2026). Період: вересень 2026. Інструмент: WebFetch.
- Зміст (переказ інструмента, не дослівна цитата): median CPI +0,2% м/м, 2,6% за 12 міс.; trimmed-mean +0,3% м/м, 2,7% за 12 міс.
- Цитата (дослівно за WebFetch): «Indicators on this webpage use interpolated data for October 2025.»
- Статус: ПЕРВИННЕ (сторінка відкрита; цифри звірено лише через конвертований текст — потребує повторної перевірки в Chrome перед source card). Confidence: середня-висока.
- Обмеження: обидві міри похідні від CPI-U, тож успадковують його похибки (carry-forward оренди, інтерполяція жовтня 2025); не є незалежним виміром.

### A-02. Cleveland Fed median CPI, помісячна серія (FRED) [ФАКТ]
- URL: https://fred.stlouisfed.org/data/MEDCPIM158SFRBCLE
- Видавець: FRED/Cleveland Fed; сезонно скоригований, % зміни у річному вимірі. Інструмент: WebFetch.
- Значення (annualized, %): 2025-09 2,44; 2025-10 1,40; 2025-11 1,40 (однакові — ознака інтерполяції); 2025-12 3,13; 2026-01 2,35; 2026-02 2,06; 2026-03 2,31; 2026-04 4,93; 2026-05 3,66; 2026-06 2,11; 2026-07 3,11; 2026-08 2,10; 2026-09 2,81.
- Спостереження: квітень 2026 — пік 4,93 (збігається з розв'язанням carry-forward: April panel). Грудень 2025 – квітень 2026 нижчі/нестабільні значення; ≈ нижчі значення жовтня–листопада 2025 збігаються з заниженням shelter.
- Статус: ПЕРВИННЕ/ДОСТУПНЕ (дані FRED). Confidence: середня (сума «до/після» залежить від інтерполяції Cleveland, її документ не відкривався). Прогалина: документ про інтерполяцію.

### A-03. Dallas Fed trimmed-mean PCE, вересень 2026 [ФАКТ]
- URL: https://www.dallasfed.org/research/pce
- Видавець: Federal Reserve Bank of Dallas. Оновлено 29.10.2026. Період: вересень 2026. Інструмент: WebFetch.
- Значення (переказ): 1-місячний річний темп 2,8; 6-місячний 2,4; 12-місячний 2,3.
- Статус: ПЕРВИННЕ (за конвертованим текстом; потребує повторної перевірки). Confidence: середня.
- Обмеження: похідна від PCE; після ретроспективних змін BEA (30.09.2026) значення можуть бути ревізовані; 12-міс. значення 2,3 помітно нижче за headline PCE 3,6% (див. A-04).
- Вторинне: roic.ai (29.10.2026) https://www.roic.ai/news/dallas-fed-trimmed-mean-inflation-jumps-to-28-in-september-challenging-feds-patience-10-29-2026 — лише сніпет у WebSearch (сторінка не відкривалась); містить виправлення, що 2,8% — річний темп м/м, не р/р.

### A-04. BEA PCE: серпень і вересень 2026 [ФАКТ]
- URL (серпень): https://bea.gov/news/2026/personal-income-and-outlays-august-2026 — реліз 30.09.2026. Дослівно: «From the same month one year ago, the PCE price index for August increased 3.4 percent.»; «Excluding food and energy, the PCE price index increased 3.0 percent from one year ago.» Інструмент: WebFetch. Реліз містить щорічне оновлення, «The revisions for estimates of personal income and outlays begin with January 2021.»
- URL (вересень): https://bea.gov/news/2026/personal-income-and-outlays-september-2026 — реліз 29.10.2026. Дослівно: «Excluding food and energy, the PCE price index increased 3.1 percent from one year ago.» Headline 3,6% р/р; м/м 0,5% і core 0,3%. Інструмент: WebFetch.
- Статус: ПЕРВИННЕ. Confidence: висока.
- Обмеження: у релізі не показано величину ефекту методологічних змін на core PCE (потрібна окрема таблиця ревізій BEA — прогалина).

### A-05. BEA: анонс змін методології PCE у щорічному оновленні [ФАКТ анонсу]
- URL: https://bea.gov/news/blog/2026-08-17/annual-update-gdp-industry-and-state-stats-publicly-available-starting-sept-30
- Видавець: BEA, блог, 17.08.2026. Інструмент: WebFetch.
- Дослівно: «This change will replace source data that has become volatile and can’t be corroborated.» (юридичні послуги, складений індекс із PPI, з 2024); «This change will better reflect the composition of products included in this category.» (ПЗ); портфельне управління — екстраполятор на основі зайнятості BLS замість дефлятора PPI. Період ревізій: Q1 2021 – Q1 2026.
- Статус: ПЕРВИННЕ. Confidence: висока.
- Висновок: BEA змінює три компоненти (портфельне управління, юридичні послуги, ПЗ). Намір не заявлено як політичний; напрямок ефекту в самому анонсі не вказано.

### A-06. Оцінки аналітиків ефекту змін BEA на core PCE (до реліза) [ПРОЄКЦІЯ]
- URL: https://cryptobriefing.com/bea-pce-inflation-revision-fed-impact/
- Видавець: Crypto Briefing (Editorial Team), 29.07.2026. Інструмент: WebFetch.
- Зміст: Goldman Sachs: core PCE за травень 2026 «would land at 3.2%, down from the currently reported 3.4%.»; JPMorgan: 3,3%; тобто -0,2 і -0,1 п.п. Аналітики не названі. Первинних звітів банків не відкрито.
- Статус: ВТОРИННЕ (низької якості видавець). Confidence: низька-середня.
- Обмеження: пошукові сніпети також згадують ANIMA Sgr «Never mind the gap» (https://www.animasgr.it/en/research/pages/news/never-mind-the-gap.aspx) і турецький BIT (core PCE за липень 3,3% → 3,0%) — не відкривались; НЕПІДТВЕРДЖЕНЕ. Фактична ревізія в релізі 30.09: core PCE серпня 3,0% (A-04); порівняння «до/після» з опублікованим раніше значенням для серпня потребує попереднього релізу (ПРОГАЛИНА).

### A-07. BLS Monthly Labor Review: контрфактичні підходи до жовтня 2025 [ФАКТ]
- URL: https://www.bls.gov/opub/mlr/2026/article/counterfactual-imputation-approaches-for-the-housing-component-of-the-october-2025-cpi.htm
- Видавець: BLS (MLR), 12.05.2026. Інструмент: WebFetch.
- Дослівно: «all returned to the same general index level in April 2026.»; «namely the reduction in index levels and 12-month changes for the rent and OER indexes».
- Числа (р/р, жовтень 2025): rent опубл. 3,02% проти 3,27–3,56% за дослідницькими методами; OER опубл. 3,29% проти 3,57–3,90%. 1-міс. зміна жовтня: опубл. 0%, дослідницькі 0,24–0,59 п.п. Квітень 2026 збіжність: rent 2,79–2,81%, OER 3,28–3,29%.
- «Article does not quantify the effect… on all-items or core» (інструмент). Арифметика: заниження 12-міс. OER 0,28–0,61 п.п., rent 0,25–0,54 п.п. (мій розрахунок з наведених чисел; потребує перевірки).
- Статус: ПЕРВИННЕ (позиція відомства щодо власної методології). Confidence: висока щодо чисел; BLS — сторона, що оцінює власну процедуру (AGENTS.md, 5, п. 18).

### A-08. Mortgage News Daily про заниження shelter та квітень 2026 [ВТОРИННЕ]
- URL: https://www.mortgagenewsdaily.com/news/05152026-cpi-shelter-shutdown
- Видавець: MND, Matthew Graham, 15.05.2026. Інструмент: WebFetch.
- Дослівно: shelter могла бути занижена «roughly 0.3% to 0.6% on a year-over-year basis during the affected stretch.»; «April's housing inflation essentially counted two 6-month cycles' worth.»; «monthly housing inflation was more like 0.3 than 0.6.»
- Статус: ВТОРИННЕ; confidence середня. Діапазон 0,3–0,6 п.п. узгоджується з MLR (A-07) лише для rent/OER, не для всього CPI.
- Висновок для питання «чи недооцінка»: сліди заниження в жовтні 2025 – березні 2026 доведені (BLS визнає), але ефект тимчасовий (до квітня 2026). Рівень індексу відновлено, тож у вересні 2026 р/р базова розбіжність через carry-forward мала бути знята; BLS не публікує 12-міс. зміни за жовтень 2026 для індексів без даних жовтня 2025 (за M-09 у agent_methodology_raw.md).

### A-09. Atlanta Fed sticky-price CPI, вересень 2026 [ФАКТ]
- URL: https://www.atlantafed.org/research-and-data/data/sticky-price-cpi
- Видавець: Federal Reserve Bank of Atlanta. Оновлено 14.10.2026. Інструмент: Chrome (chrome_get_web_content).
- Дослівно: «On a year-over-year basis, the series is up 2.8 percent.»; sticky core 12-міс. 2,8%; flexible «up 6.1 percent» р/р; flexible +22,2% у річному вимірі за вересень.
- Статус: ПЕРВИННЕ. Confidence: висока. Обмеження: похідна від CPI; сортування на sticky/flexible за частотою зміни цін.

### A-10. Офіційний CPI-U, вересень 2026 [ФАКТ]
- URL: https://www.bls.gov/news.release/cpi.nr0.htm
- Видавець: BLS, реліз 14.10.2026. Інструмент: WebFetch.
- Дослівно: «The all items index rose 3.7 percent for the 12 months ending September.»; м/м +0,6% (SA). Core 12-міс. 2,6%, м/м 0,3%; shelter 12-міс. 3,2% (переказ інструмента). Тест не містив згадки carry-forward (на сторінці без неї).
- Статус: ПЕРВИННЕ. Confidence: висока (core/shelter — за переказом, звірити).
- Підтвердження 3,7% і 3,4% за серпень: ВТОРИННЕ (WebSearch, сніпети investing/forexfundamentals), https://forexfundamentals.com/economic-calendar/us-cpi/2026-10-14 — не відкривався.

### A-11. Truflation: Econbrowser (Chinn) про 0,93% [ПОЗИЦІЯ + критика]
- URL: https://econbrowser.com/archives/2026/02/truflation-chief-economist-less-than-1-percent-inflation-yes
- Видавець: Econbrowser, Menzie Chinn, 04.02.2026 (відповідь на колонку E.J. Antoni, Townhall). Інструмент: WebFetch.
- Дослівно: Antoni: «As of today, y/y CPI inflation is 0.93%!» (це Truflation, не CPI); «CPI assigns housing about one-third of its weight, whereas Truflation is closer to one in four.» Chinn: «dubious about overall dropping as rapidly as Truflation indicates in January»; вимагає повнішої документації (проти трекера Cavallo).
- Статус: ВТОРИННЕ (аргументи сторін). Confidence: середня. Скептик: Chinn; захисник/промоутер: Antoni, Truflation.
- Примітка: Antoni — відкликаний кандидат на комісара BLS (див. agent_methodology_raw.md, M-02) — конфлікт інтересів/контекст.

### A-12. Truflation: січневий звіт 2026 [ПОЗИЦІЯ компанії]
- URL: https://predict.truflation.com/blog/truflation-us-monthly-inflation-report-january-2026
- Видавець: Truflation, ~лютий 2026 (дата на сторінці не вказана). Інструмент: WebFetch.
- Числа: headline +1,47% р/р; core +1,61%; Housing −0,79% м/м, −0,26% р/р; прогноз BLS CPI січня 2,2–2,4% (прогноз). Дослівно: «tariff pass-through to goods prices contributed a cumulative 0.8 percentage points» (до листопада 2025).
- Статус: ДОСТУПНЕ; confidence низька-середня (самопублікація, методологія OER/rent не описана; «housing» а не shelter).
- Обмеження: розбіжність Truflation–CPI спрямована вниз; не підтримує тезу про недооцінку офіційної інфляції.

### A-13. Truflation vs BLS, липень 2026 [ФАКТ-вторинний]
- URL: https://cryptobriefing.com/truflation-us-cpi-2-percent-bls-divergence/
- Видавець: Crypto Briefing (передрук Webopedia), 27.07.2026. Інструмент: WebFetch.
- Дослівно: «The Bureau of Labor Statistics says prices are running at 3.5% year-over-year as of June 2026.» Truflation (TruCPI-US) 2,11% на 27.07.2026. Розрив 1,39 п.п. (заголовок казав «a full percentage point»). Порівняння різних періодів (27.07 vs червень).
- Статус: ВТОРИННЕ; confidence низька-середня (неоднорідний видавець; різні дати). Інший матеріал того ж видавця (cryptobriefing.com/truflation-cpi-index-vs-bls-inflation-gap/: Truflation 1,82% проти BLS 4,20%) — не відкривався, дата невідома: НЕПІДТВЕРДЖЕНЕ.
- Прогалина: Truflation за серпень–жовтень 2026 не знайдено; є лише прогноз Truflation (13.07.2026) про CPI червня 3,9% (сніпет Webull, не відкривався).

### A-14. PriceStats (State Street) 2026 [ФАКТ компанії]
- URL: https://www.statestreet.com/ie/en/insights/us-inflation-pricestats-march (також -january, -february, -may у пошуку)
- Видавець: State Street. Інструмент: WebSearch (сніпети; сторінки не відкривались) — ДОСТУПНЕ/НЕПІДТВЕРДЖЕНЕ до відкриття.
- Зміст за сніпетами: січень р/р 2,61% (мін. з кінця вересня 2025); лютий 2,75%; березень 4% (м/м 1,4%, найбільше з 2008); кінець травня >5%. «Design to provide a low-latency… comparable to official CPI»; використовує ваги CPI, без стандартних коригувань якості; похибка проти BLS у березні–квітні «a couple of basis points» (самооцінка).
- Обмеження: власна оцінка точності; рівень травень >5% суперечить іншим даним? (CPI червня 3,5% за A-13; різниця не пояснена; ПРОГАЛИНА: потрібно відкрити сторінки й звірити).
- Позначка: НЕ використовувати як факт до відкриття.

### A-15. Adobe Digital Price Index [ФАКТ методології; дані не отримано]
- URL: https://business.adobe.com/resources/digital-price-index.html
- Інструмент: Chrome. Видавець: Adobe. Сторінка показує «DPI for July 2025» (застарілі дані на кешованій/статичній версії); методологія: «modeled after the Consumer Price Index… uses the Fisher Price Index to track online prices.»
- Прогалина: DPI за 2026 не отримано. WebSearch згадав (без дати) «Online Prices Fall to 40-Month Low, Down 3.2% In August» і, за Cavallo-пошуком, «largest monthly online price increase in a dozen years» (лютий 2026) — НЕПІДТВЕРДЖЕНЕ.
- Обмеження: лише онлайн-ціни; не містять послуг/оренди; не порівнянне з CPI напряму.

### A-16. Harvard Pricing Lab (Cavallo) tariff tracker [ФАКТ-вторинний]
- URL: https://www.hks.harvard.edu/centers/mrcbg/programs/growthpolicy/tracking-tariffs-are-retailers-passing-costs-consumers (також NBER WP 34496 https://ideas.repec.org/p/nbr/nberwo/34496.html)
- Інструмент: WebSearch (сніпети; не відкривались) — НЕПІДТВЕРДЖЕНЕ щодо чисел 2026. Сніпети: у лютому 2026 Cavallo — ціни імпортних товарів +2,3% (кінець листопада – 10 лютого); Fortune 11.05.2026 https://fortune.com/2026/05/11/trumptariff-cost-full-pass-through-on-consumers/ — не відкривався.
- Роль: незалежна академічна онлайн-база (на відміну від Truflation, документована; Chinn цитує її як взірець).

### A-17. NY Fed SCE, вересень 2026 [ФАКТ]
- URL: https://www.newyorkfed.org/microeconomics/sce
- Видавець: Federal Reserve Bank of New York. Дата релізу за URL пресрелізу 2026-10-07 (не явна). Інструмент: WebFetch.
- Значення (медіани): 1 рік 3,9% (+0,3), 3 роки 3,3% (+0,1), 5 років 3,0%. Дослівно: «Expectations remained unchanged at the five-year-ahead horizon at 3.0 percent.»
- Статус: ПЕРВИННЕ. Confidence: висока. Обмеження: опитування домогосподарств; чутливі до цін на бензин/продукти; відображають сприйняття, не прогноз.

### A-18. UMich, попередній листопад 2026 [ФАКТ]
- URL: https://www.sca.isr.umich.edu/
- Видавець: University of Michigan Surveys of Consumers, 6.11.2026 (попередній). Інструмент: WebFetch.
- Дослівно: «declined from 4.7% last month to 4.3% this month.» (1 рік); довгострокові «inched down from 3.5% in October to 3.4%.» (горизонт 5–10 р. не підтверджено інструментом); sentiment 51,0 проти 48,0. Фінал — 20.11.2026.
- Статус: ПЕРВИННЕ (попередній). Confidence: середня-висока. Обмеження: відома партійна чутливість опитувань (у цій сесії не шукалося — ПРОГАЛИНА).

### A-19. Ринкові очікування: breakevens (FRED) [ФАКТ]
- URL: https://fred.stlouisfed.org/series/T10YIE — 10-річний breakeven 2,23% (6.11.2026); URL: https://fred.stlouisfed.org/series/T5YIFR — 5y5y forward 2,17% (6.11.2026). Інструмент: WebFetch.
- Статус: ПЕРВИННЕ. Confidence: висока. Обмеження: breakevens містять премію ліквідності/інфляційного ризику; нижчі за опитування (3,0–3,4% довгострокові) — розбіжність ринок/домогосподарства. Значення за 2025 і для порівняння «до/після» не збирались.

### A-20. Gallup: сприйняття, квітень 2026 [ФАКТ опитування]
- URL: https://www.cbsnews.com/news/americans-finances-getting-worse-gallup-poll-2026/
- Видавець: CBS News (переказ Gallup), 28.04.2026. Інструмент: WebFetch. Gallup, 1–15.04.2026, n=1 001.
- Зміст: рекордні 55% кажуть, що фінансова ситуація погіршується (від 2001); ~55% — що зростання цін спричинило фінансові труднощі. Через WebSearch: 31% називають вартість життя/інфляцію головною фінансовою проблемою (проти 29% 2025); у вересні 2026 (Gallup 1–17.09) «high cost of living/inflation» 13% серед «найважливіших проблем країни» (https://news.gallup.com/file/poll/715526/2026_10_13_Party-DSA-MAGA%20Topline%20and%20Tabs.pdf — URL лише зі сніпета, не відкривався).
- Статус: ВТОРИННЕ (первинний Gallup не відкрито). Confidence: середня. Обмеження: вимірює сприйняття, партійна поляризація; не інфляцію.

### A-21. R-CPI-E (CPI для літніх), CRS травень 2026 [ФАКТ]
- URL: https://www.everycrsreport.com/files/2026-05-27_IF12675_bbc09e49ba9513d3ecb34c6c7e516257dd38fe32.html
- Видавець: CRS (In Focus IF12675), 27.05.2026. Інструмент: WebSearch (сніпети; сторінка не відкривалась) — ДОСТУПНЕ.
- Дослівно (за сніпетом): «The December 2025 COLA using the R-CPI-E (3.0%) would have been 0.2 percentage points higher than the COLA using the CPI-W (2.8%).» CBO (https://www.cbo.gov/publication/44090): з 1982 CPI-E вище на 0,2 п.п., але з грудня 2007 «generally lower».
- Обмеження: BLS: R-CPI-E «experimental»; по децилях/квінтилях (R-CPI-I, Stanford/Harvard/Jackson Hole) конкретних 2025–26 джерел НЕ знайдено — ПРОГАЛИНА.

### A-22. ShadowStats [ПОЗИЦІЯ, відсутність наукової довіри]
- URL: https://en.wikipedia.org/wiki/Shadowstats.com
- Інструмент: WebFetch (Wikipedia — тертинне/агрегатор; первинні критики не відкрито).
- Дослівно: економісти вважають індекс «conceptually wrong»; Dolan: «implausibly high»; Williams: «using that as an add factor to the reported statistics» (не перераховує дані, додає константу). Ramey: зміни методології «after academic economists did decades of research».
- Значення 2026 не отримано (доступ платний; сніпет сайту: «Last Updated» 1970 — заглушка). НЕПІДТВЕРДЖЕНЕ. Не рекомендується як вимір; лише як позиція.

### A-23. Cost of Thriving (American Compass) [ПОЗИЦІЯ]
- URL: https://cosm.aei.org/the-cost-of-thriving-has-fallen-correcting-and-rejecting-the-american-compass-cost-of-thriving-index/
- Інструмент: WebSearch (сніпет). Видавець: AEI (Winship, Horpedahl), 2023. Критика: «the cost of thriving rose by less than four weeks of work» (проти 22 тижнів за American Compass).
- Оновлення 2026 не знайдено (Daily Citizen — недатована згадка). Прогалина. Обмеження: це індекс «тижнів роботи», не інфляція; залежить від вибору кошика.

### A-24. Розрив core CPI і core PCE [ПОЗИЦІЯ/пояснення, джерело застаріле]
- URL: https://www.actionforex.com/?p=545993 — Wells Fargo Securities, 1.04.2024 (НЕ 2026): «Since 2000, the core CPI deflator has run an average of 0.3 percentage points higher than the core PCE deflator.»; ваги shelter 43% проти 18% core PCE. Інструмент: WebFetch.
- Для 2026 надійного джерела немає (PIMCO через pulse.bot — сніпет, не відкривався; НЕПІДТВЕРДЖЕНЕ). Власне спостереження за A-04/A-10: вересень 2026 core PCE 3,1% > core CPI 2,6% — зворотний звичному. Причину не встановлено.

## Підсумок за питаннями

- Питання 4 (чи розходяться альтернативні виміри з офіційними): робастні міри (median/trimmed/sticky) 2,6–2,8% < headline CPI 3,7%, але в узгодженому напрямку (енергія). Truflation нижча, PriceStats (за самооцінкою) збігається. Вимір, що показує вищу інфляцію за офіційну, — лише очікування домогосподарств та, умовно, core PCE > core CPI.
- Питання 7 (недооцінка до/після carry-forward та BEA): до квітня 2026 shelter занижена на ~0,3–0,6 п.п. р/р (BLS визнав, A-07); після квітня 2026 індекси зійшлися (A-07), тож недооцінка тимчасова. Вплив ревізій BEA 30.09.2026 на core PCE за оцінками Goldman/JPM −0,1…−0,2 п.п. (проєкція, A-06), фактичну величину не знайдено. Core PCE після ревізій 3,0–3,1% не нижчий за core CPI, тож ревізії не створили розриву «офіційної недооцінки» у напрямку, який вигідний адміністрації (за наявними даними).
- Скептики: Chinn (про Truflation), AEI (Winship/Horpedahl, Cost of Thriving), економісти проти ShadowStats; Warren (лист до BEA, див. agent_methodology_raw.md, M-12). Захисники: Truflation/Antoni (низькі вимірювання); BLS (власна MLR-оцінка); RBC (зміни BEA як ретроактивні, не дезінфляційний сигнал; M-11).

## Прогалини

1. Truflation за серпень–жовтень 2026; PriceStats за літо–осінь 2026 (сторінки не відкривались); Adobe DPI 2026; Cavallo tracker 2026 числа.
2. Документ Cleveland про інтерполяцію жовтня 2025; 12-міс. значення median/trimmed за вересень 2025 (для «до/після»).
3. Фактична величина ревізії core PCE BEA (таблиця ревізій від 30.09.2026); первинні звіти Goldman/JPM.
4. R-CPI-I, децильні/Harvard/Stanford/Jackson Hole дослідження 2025–26; первинний Gallup; Pew; Cost of Thriving 2026.
5. Пояснення розриву core PCE > core CPI у 2026.
