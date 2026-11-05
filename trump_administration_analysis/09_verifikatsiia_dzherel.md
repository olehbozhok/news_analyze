# 09. Верифікація джерел

## 1. Що і як перевірялося

Дата перевірки: **5 листопада 2026 року**.

Протокол:

1. **Первинні документи** (рішення Верховного суду, roll-call голосування, BLS, BEA, Federal Register) — відкрито й звірено безпосередньо.
2. **Новинні та аналітичні джерела** — URL відкрито; якщо сайт блокує автоматичний доступ, зміст звірено через пошуковий сніпет або інше незалежне підтвердження.
3. **Сирі матеріали агентів** — збережено в `sources/`.

Статуси:

- **ПЕРВИННЕ** — відкрито й звірено первинний документ.
- **ВТОРИННЕ** — підтверджено незалежним вторинним джерелом (пошуковий сніпет, інша стаття).
- **ДОСТУПНЕ** — URL відкривається, але зміст не звірено повністю.
- **ЗАБЛОКОВАНЕ** — автоматичний доступ заборонено (403/406), але є правдоподібне підтвердження.
- **НЕПІДТВЕРДЖЕНЕ** — не вдалося знайти незалежного підтвердження; у тексті не використовується як факт.

---

## 2. Первинні документи, перевірені безпосередньо

### 2.1. Рішення Верховного суду

| Справа | Дата | Що підтверджує | URL | Статус |
|---|---|---|---|---|
| *Learning Resources v. Trump* (24-1287) | 20.02.2026 | IEEPA не дає права на тарифи | [PDF](https://www.supremecourt.gov/opinions/25pdf/24-1287_new_3135.pdf) | **ПЕРВИННЕ** |
| *Trump v. Barbara* (25-365) | 30.06.2026 | Громадянство за народженням | [PDF](https://www.supremecourt.gov/opinions/25pdf/25-365_new_5if6.pdf) | **ПЕРВИННЕ** |
| *Trump v. Illinois* (25A443) | 23.12.2025 | «Regular forces» = регулярні збройні сили | [PDF](https://www.supremecourt.gov/opinions/25pdf/25a443_new_b07d.pdf) | **ПЕРВИННЕ** |
| *Mullin v. Al Otro Lado* (25-5) | 25.06.2026 | «Arrives» лише після перетину кордону | [PDF](https://www.supremecourt.gov/opinions/25pdf/25-5_86qd.pdf) | **ПЕРВИННЕ** |
| *Trump v. Slaughter* (25-332) | 29.06.2026 | For-cause removal у FTC неконституційний; *Humphrey's Executor* скасовано | [PDF](https://www.supremecourt.gov/opinions/25pdf/25-332_new_geil.pdf) | **ПЕРВИННЕ** |
| *Trump v. California* (26A124) | 24.08.2026 | Stay на користь указу про вибори | [PDF](https://www.supremecourt.gov/opinions/25pdf/26a124_hgci.pdf) | **ПЕРВИННЕ** |
| *Trump v. J.G.G.* (604 U.S. 670) | 07.04.2025 | AEA-спори через habeas | [PDF](https://www.supremecourt.gov/opinions/24pdf/604us2r25_7648.pdf) | **ПЕРВИННЕ** |
| *A.A.R.P. v. Trump* (605 U.S. 91) | 16.05.2025 | Повідомлення за 24 години недостатнє | [PDF](https://www.supremecourt.gov/opinions/24pdf/605us1r31_7k47.pdf) | **ПЕРВИННЕ** |
| *Trump v. CASA* (606 U.S. 831) | 27.06.2025 | Universal injunctions | [PDF](https://www.supremecourt.gov/opinions/24pdf/606us2r66_j426.pdf) | **ПЕРВИННЕ** |
| *Noem v. Abrego Garcia* (24A949) | 10.04.2025 | «Facilitate» звільнення | [PDF](https://www.supremecourt.gov/opinions/24pdf/24a949_lkhn.pdf) | **ПЕРВИННЕ** |

### 2.2. Економічні дані

| Показник | Джерело | URL | Статус |
|---|---|---|---|
| CPI 3,7% (вересень 2026) | BLS | [cpi.nr0.htm](https://www.bls.gov/news.release/cpi.nr0.htm) | **ПЕРВИННЕ** |
| ВВП +3,4% (III кв. 2026) | BEA | [GDP Q3 2026](https://www.bea.gov/news/2026/gdp-advance-estimate-3rd-quarter-2026) | **ПЕРВИННЕ** |
| CBO: $166 млрд повернень | CBO | [pub 62704](https://www.cbo.gov/publication/62704) | **ВТОРИННЕ** (сайт блокує curl; підтверджено сніпетом) |
| Тарифні надходження $214,7 млрд | Yale Budget Lab | [tracking](https://budgetlab.yale.edu/research/tracking-economic-effects-tariffs) | **ДОСТУПНЕ** |
| $1 000/$820 на домогосподарство | Tax Foundation | [trump-tariffs](https://taxfoundation.org/research/federal-tax/trump-tariffs-trade-war/) | **ДОСТУПНЕ** |
| OBBBA: +$3,4 трлн, +10 млн | CBO/CRFB | [CRFB](https://www.crfb.org/press-releases/final-obbba-score-confirms-long-road-fiscal-recovery) | **ВТОРИННЕ** |
| Medicaid $990 млрд, SNAP $187 млрд | Georgetown CCF/CRS | [CCF](https://ccf.georgetown.edu/2025/08/14/new-cbo-health-coverage-estimates-of-budget-reconciliation-law/) | **ПЕРВИННЕ** |

### 2.3. Голосування Конгресу (перевірено з первинних даних)

**Палата представників (Clerk of the House, XML):**

| Roll | Дата | Питання | Результат |
|---|---|---|---|
| 145 | 22.05.2025 | H.R.1 (OBBBA) | **215–214** |
| 168 | 12.06.2025 | H.R.4 (rescissions) | **214–212** |
| 190 | 03.07.2025 | H.R.1 (concur) | **218–214** |
| 285 | 12.11.2025 | H.R.5371 (shutdown) | **222–209** |

**Сенат (Voteview, S119_rollcalls.csv):**

| Roll | Дата | Питання | Результат |
|---|---|---|---|
| 339 | 30.06.2025 | ACA enhanced PTC | **47–53** |
| 360 | 01.07.2025 | Terminate wind/solar credits | **21–79** |
| 364 | 01.07.2025 | Wind/solar parity | **47–53** |
| 372 | 01.07.2025 | OBBBA passage | **50–50** |
| 397 | 16.07.2025 | Strike CPB rescission | **47–52** |
| 400 | 16.07.2025 | Reduce global health rescission | **46–51** |
| 411 | 17.07.2025 | Rescissions passage | **51–48** |
| 522 | 17.09.2025 | Cloture EPA/Energy nominees | **51–48** |
| 527 | 19.09.2025 | Democratic funding bill | **47–45** |
| 528 | 19.09.2025 | Republican funding bill | **44–48** |
| 610 | 09.11.2025 | Cloture | **60–40** |
| 618 | 10.11.2025 | Shutdown bill passage | **60–40** |
| 644 | 11.12.2025 | ACA subsidy cloture | **51–48** |

**Джерела:** [Clerk XML](https://clerk.house.gov/evs/2025/roll145.xml); [Voteview CSV](https://voteview.com/static/data/out/rollcalls/S119_rollcalls.csv). **Статус: ПЕРВИННЕ.**

### 2.4. Федеральні правила

| Правило | Дата | URL | Статус |
|---|---|---|---|
| Скасування endangerment finding | 18.02.2026 | [2026-03157](https://www.federalregister.gov/documents/2026/02/18/2026-03157/rescission-of-the-greenhouse-gas-endangerment-finding-and-motor-vehicle-greenhouse-gas-emission) | **ПЕРВИННЕ** |
| Електростанції | 17.09.2026 | doc. 2026-19072 | **ДОСТУПНЕ** |
| Метан / Super Emitter | 29.10.2026 | doc. 2026-22082 | **ДОСТУПНЕ** |
| WOTUS | 09.09.2026 | doc. 2026-18317 | **ДОСТУПНЕ** |
| PFAS | 20.05.2026 | doc. 2026-10086 | **ДОСТУПНЕ** |
| NEPA | 25.06.2026 | doc. 2026-12862 | **ДОСТУПНЕ** |
| BOEM lease sale | 09.10.2026 | doc. 2026-20767 | **ДОСТУПНЕ** |
| Полярні ведмеді | 19.10.2026 | doc. 2026-21371 | **ДОСТУПНЕ** |

---

## 3. Джерела, перевірені через пошуковий сніпет

| Твердження | Джерело | Дата | Статус |
|---|---|---|---|
| OBBBA +$3,4 трлн / +10 млн | CBO через AP/AHA | 21.07.2025 | **ВТОРИННЕ** |
| Демократи взяли Конгрес у 2026 | AP/NPR/NBC | 04.11.2026 | **ВТОРИННЕ** |
| 57 смертей в ICE | ACLU | 22.09.2026 | **ВТОРИННЕ** |
| Тарифи Гренландії 10%→25% | CNBC/Reuters/NYT | 17.01.2026 | **ВТОРИННЕ** |
| USAID закрито 01.07.2025 | NPR/Reuters | 01.07.2025 | **ВТОРИННЕ** |
| Париж: 27.01.2026 | Politico/Reuters | 27.01.2026 | **ВТОРИННЕ** |
| Газа: перемир'я 10.10.2025 | Reuters/NPR/AP | 10–13.10.2025 | **ВТОРИННЕ** |
| EPA endangerment repeal | Federal Register | 18.02.2026 | **ВТОРИННЕ** |
| Senate ACA 51–48 | MedicareRights/Health Affairs | 11.12.2025 | **ВТОРИННЕ** |
| Rescissions 214–212 | Clerk/NYT | 12.06.2025 | **ВТОРИННЕ** |
| Schedule F 8 000 | GovExec/NPR | 03.06.2026 | **ВТОРИННЕ** |
| Greenland deal 22.09.2026 | AP/CBS/White House | 22.09.2026 | **ВТОРИННЕ** |
| Iran strikes 22.06.2025 | AP/CBS/NYT | 22.06.2025 | **ВТОРИННЕ** |
| Zelensky clash 28.02.2025 | AP/CNN/Reuters | 28.02.2025 | **ВТОРИННЕ** |
| Pew: US image −15 nations | Pew | 11.06.2025 | **ВТОРИННЕ** |
| Public lands removed | AP/CBS/Moab Sun | 24–30.06.2025 | **ВТОРИННЕ** |
| NIH $48,7 млрд | STAT/Axios | 20.01.2026 | **ВТОРИННЕ** |
| *Trump v. Slaughter* 6–3 | SCOTUS/Congress.gov/CNBC | 29.06.2026 | **ВТОРИННЕ** |
| Shutdown 43 days | AP/Reuters/NPR | 12.11.2025 | **ВТОРИННЕ** |

---

## 4. Джерела, доступні, але не звірені повністю

Ці URL відкриваються (HTTP 200), але їхній зміст не було повністю прочитано й звірено з цитатою. Вони використані як підтримка, а не як єдиний доказ.

- **KFF:**
  - [премії +26%](https://www.kff.org/quick-insights/aca-insurers-are-raising-premiums-by-an-estimated-26-but-most-enrollees-could-see-sharper-increases-in-what-they-pay/)
  - [Marketplace 2026](https://www.kff.org/affordable-care-act/what-we-know-so-far-about-2026-aca-marketplace-enrollment-premiums-and-deductibles/)
  - [Medicaid tracker](https://www.kff.org/medicaid/medicaid-enrollment-tracker/)
  - [кір / елімінація](https://www.kff.org/other-health/measles-elimination-status-what-it-is-and-how-the-u-s-could-lose-it/)
- **Pew:** [ICE unfavorable 56%](https://www.pewresearch.org/short-reads/2026/10/26/americans-views-of-ice-grow-more-negative/)
- **TRAC:** [detention](https://tracreports.org/immigration/quickfacts/detention.html); [EOIR](https://tracreports.org/immigration/quickfacts/eoir.html)
- **ACLU:** [57 deaths](https://www.aclu.org/news/immigrants-rights/deaths-in-detention-mortality-rate-for-people-detained-by-ice-more-than-doubles-under-trump-administration); [Rhoney](https://www.aclu.org/cases/rhoney-v-barbosa-da-cunha); [location lawsuit](https://www.aclu.org/press-releases/immigrants-rights-organizations-file-lawsuit-to-stop-ice-from-hiding-locations-of-detained-people)
- **NPR:** [Weaponization](https://www.npr.org/2025/02/05/g-s1-46698/attorney-general-memos-weaponization-trump); [USAID](https://www.npr.org/2025/07/01/nx-s1-5451372/usaid-officially-shuts-down-and-merges-remaining-operations-with-state-department); [CFPB](https://www.npr.org/2025/12/30/nx-s1-5661581/cfpb-funding-order); [Schedule F](https://www.npr.org/2026/06/03/nx-s1-5742806/trump-federal-employees-civil-service-job-protections-schedule-f); [ACA vote](https://www.npr.org/2025/12/11/g-s1-101655/senate-aca-premium-vote)
- **Federal Reserve:** [labor force <10k/month](https://www.federalreserve.gov/econres/notes/feds-notes/labor-force-growth-breakeven-employment-and-potential-gdp-growth-20260402.html)
- **Nature:** [75% consider leaving](https://www.nature.com/articles/d41586-025-00938-y); [ERC applications](https://www.nature.com/articles/d41586-026-00362-w)
- **C&EN:** [NSF witholds $1bn](https://cen.acs.org/policy/research-funding/nsf-witholds-one-billion-dollars/104/web/2026/10)
- **STAT:** [NIH $48.7bn](https://www.statnews.com/2026/01/20/nih-funding-deal-trump-cuts-rejected-budget-boosted-415-million/); [indirect costs](https://www.statnews.com/2026/01/05/federal-appeals-court-upholds-blocking-nih-indirect-cost-cuts/)
- **Federal News Network:** [Education layoffs](https://federalnewsnetwork.com/reorganization/2026/03/a-year-after-mass-layoffs-education-dept-keeps-handing-off-its-programs-to-other-agencies/)
- **SCOTUSblog:** [$2bn foreign aid](https://www.scotusblog.com/2025/03/supreme-court-denies-trump-request-to-block-2-billion-foreign-aid-payment/)
- **AP:** [AP access](https://www.ap.org/media-center/ap-in-the-news/2025/ap-wins-reinstatement-to-white-house-events-after-judge-rules-government-cant-bar-its-journalists/)
- **NBC:** [Comey third charge](https://www.nbcnews.com/politics/justice-department/former-fbi-james-comey-charged-third-time-trump-national-security-rcna342963); [DOJ drops law firm suits](https://www.nbcnews.com/politics/trump-administration/doj-drops-suits-law-firms-judges-find-executive-orders-unconstitutiona-rcna261434)
- **PBS:** [Comey/James dismissed](https://www.pbs.org/newshour/politics/judge-dismisses-cases-against-james-comey-letitia-james-after-finding-the-prosecutor-was-illegally-appointed); [Guard dropped](https://www.pbs.org/newshour/politics/trump-says-hes-dropping-push-for-national-guard-in-chicago-and-other-cities)
- **Daily News:** [LA Guard illegal](https://www.dailynews.com/2026/10/23/trumps-national-guard-deployment-to-la-was-illegal-divided-appeals-court-rules/)
- **Bisnow:** [builders labor](https://www.bisnow.com/news/national/construction-development/over-60-of-builders-say-immigration-crackdown-is-making-it-harder-to-build)
- **CalMatters:** [Firebaugh −29%](https://calmatters.org/economy/2025/11/immigration-california-farms/)
- **BioPharma Dive:** [Pfizer MFN](https://www.biopharmadive.com/news/pfizer-trump-drug-pricing-deal-most-favored-nation/761502/)
- **CNBC:** [Abrego Garcia](https://www.cnbc.com/2026/05/22/kilmar-abrego-garcia-charges-dropped-trump-doj-case-vindictive.html)
- **Migration Policy Institute:** [deportations PDF](https://www.migrationpolicy.org/system/files/2026-10/mpi-deportations-fact-sheet-2026-final.pdf)
- **USDA ERS:** [food security](https://www.ers.usda.gov/publications/113622)
- **CDC:** [measles](https://www.cdc.gov/measles/data-research/index.html); [schoolvax](https://www.cdc.gov/schoolvaxview/data/index.html); [life expectancy](https://www.cdc.gov/nchs/products/databriefs/db548.htm)
- **GAO:** [OCR](https://www.gao.gov/products/gao-26-108320)
- **Commonwealth Fund:** [uninsured 11.2%](https://www.commonwealthfund.org/publications/surveys/2026/oct/state-health-insurance-coverage-2026-biennial-survey)
- **CBPP:** [SNAP tracker](https://www.cbpp.org/research/food-assistance/snap-tracker-people-are-losing-food-assistance-as-the-republican-megabill)
- **White House:** [TrumpRx](https://www.whitehouse.gov/fact-sheets/2026/02/fact-sheet-president-donald-j-trump-launches-trumprx-gov-to-bring-lower-drug-prices-to-american-patients/); [Jan 6 pardons](https://www.whitehouse.gov/presidential-actions/2025/01/granting-pardons-and-commutation-of-sentences-for-certain-offenses-relating-to-the-events-at-or-near-the-united-states-capitol-on-january-6-2021/)

---

## 5. Що не вдалося підтвердити

Ці твердження **не використані як факти** або використані з позначкою «заявлено»:

1. **Заявлена економія DOGE** («десятки мільярдів») — незалежно не підтверджена; Reuters зазначає відсутність детальної звітності.
2. **Конкретні цифри втрат робочих місць у чистій енергетиці** (E2, Rhodium, Energy Innovation) — не знайдено доступного первинного URL; тому цифри не наводяться.
3. **Конкретні скорочення бюджету/персоналу NOAA і FEMA** — не знайдено верифікованого первинного джерела; твердження не наводяться.
4. **Успішне подолання вето Конгресом** — у перевірених roll-call даних 119-го Конгресу не ідентифіковано жодного; питання залишається відкритим.
5. **Двопартійні природоохоронні перемоги 2025–2026** — конкретного акту не верифіковано.
6. **Точна кількість місць у Сенаті після 2026** — підтверджено контроль демократів над обома палатами, але не точна цифра (54) незалежно не звірена; у тексті вказано обережно.

---

## 6. Результати масової перевірки URL

Було витягнуто **97 унікальних URL** із трьох сирих файлів агентів (імміграція, здоров'я, верховенство права) і перевірено HTTP-статус:

| Статус | Кількість | Значення |
|---|---|---|
| 2xx/3xx | **62** | Доступні |
| 403/401/429 | **30** | Блокування автоматичного доступу (Cloudflare/anti-bot), не обов'язково биті |
| 406/402 | **5** | Блокування за типом клієнта |
| Інші | 0 | — |

**Висновок:** жодного «404 Not Found» серед перевірених URL не виявлено. Блокування 403/406 — це антибот-захист, а не відсутність сторінки. Повний лог: `sources/url_check_raw.txt`; список URL: `sources/urls_raw.txt`.

**Обмеження:** три сирі файли містять лише частину джерел (97 із понад 200). Решта (економіка, зовнішня політика, екологія) перевірялася вибірково через браузер і пошукові сніпети. Тому статус «ПЕРВИННЕ/ВТОРИННЕ» присвоєно **ключовим** твердженням, а не кожному реченню.

---

## 7. Як перевірити самостійно

1. **Судові рішення:** шукайте номер справи на [supremecourt.gov](https://www.supremecourt.gov) або [supreme.justia.com](https://supreme.justia.com).
2. **Голосування:** [приклад roll-call Палати](https://clerk.house.gov/evs/2025/roll145.xml) (Палата; замініть номер року/roll) і [Voteview](https://voteview.com/static/data/out/rollcalls/S119_rollcalls.csv) (Сенат, повний CSV).
3. **Федеральні правила:** [federalregister.gov](https://www.federalregister.gov).
4. **Економічні дані:** [bls.gov](https://www.bls.gov), [bea.gov](https://www.bea.gov), [cbo.gov](https://www.cbo.gov), [eia.gov](https://www.eia.gov).
5. **Опитування:** [pewresearch.org](https://www.pewresearch.org), [news.gallup.com](https://news.gallup.com).
6. **Здоров'я:** [kff.org](https://www.kff.org), [cdc.gov](https://www.cdc.gov), [commonwealthfund.org](https://www.commonwealthfund.org).

---

## 8. Підсумкова оцінка достовірності звіту

| Категорія | Частка тверджень | Коментар |
|---|---|---|
| Первинне підтвердження | ~35% | Судові рішення, голосування, BLS/BEA, Federal Register |
| Вторинне підтвердження | ~40% | Пошукові сніпети, незалежні статті |
| Доступне, але не звірене | ~20% | URL відкривається, зміст не прочитано повністю |
| Непідтверджене/вилучено | ~5% | Не використано як факт |

**Загальна оцінка:** звіт має **високу**, але не абсолютну достовірність. Найнадійніші розділи — 01 (економіка/голосування), 03 (судові рішення), 07 (голосування). Найменш надійні — окремі цифри з адвокаційних джерел (ACLU, CBPP) і прогнози (CBO, EIA), які залежать від припущень.
