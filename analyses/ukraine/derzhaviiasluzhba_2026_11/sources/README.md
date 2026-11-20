# Sources: derzhaviiasluzhba_2026_11

Стан: research завершено 20.11.2026 (Researcher); чернетка 01 написана 20.11.2026 (Writer), source cards SC-01 — SC-22 — у `source_cards_01.md`. Фінальний пошук новин Writer 20.11.2026 (WebSearch; Chrome-інструменти chrome_* у субагента не завантажені, WebSearch — запасний варіант за розд. 2.1): знайдено статтю Інтерфакс-України (додано картку SC-23, синхронізовано з документом; перекази shelter.in.ua і rayon.in.ua нових фактів не дають — карток не відкривали); нових офіційних заяв на 20.11 не знайдено. Документ [01_obshuky.md](../01_obshuky.md) — ГОТОВО (Verifier 20.11.2026: PASS WITH CORRECTIONS; виправлення V-1–V-8 внесено Editor 20.11.2026; targeted re-check 20.11.2026 — PASS, addendum у звіті).

| Файл | Що містить |
|---|---|
| [../scope_contract.md](../scope_contract.md) | Scope contract (6.1): ключові питання, межі, контраргументи |
| [agent_researcher_obshuky_raw.md](agent_researcher_obshuky_raw.md) | Сирі нотатки Researcher (20.11.2026): твердження за питаннями scope contract, негативи з формулами, аномалії джерел (R-12). Не редагувати |
| [research_brief_obshuky.md](research_brief_obshuky.md) | Research brief: підтверджене за 6 питаннями, контрсвідчення за контраргументами, прогалини, метод і обмеження, vintage-дані |
| [url_check_researcher_obshuky_raw.txt](url_check_researcher_obshuky_raw.txt) | Журнал URL: інструмент і результат для кожного відкритого/невдалого адреси |
| [source_cards_01.md](source_cards_01.md) | Source cards документа [01_obshuky.md](../01_obshuky.md): SC-01 — SC-22 (Researcher 20.11.2026), SC-23 (Writer, фінальний пошук новин 20.11.2026); SC-07, SC-12, SC-15, SC-17 доповнено Editor'ом 20.11.2026 (виправлення V-2, V-3, V-5, V-8 звіту verification_01_obshuky.md) |
| [url_check_verifier_obshuky_raw.txt](url_check_verifier_obshuky_raw.txt) | Журнал URL Verifier'а (20.11.2026) |
| [url_check_editor_obshuky_raw.txt](url_check_editor_obshuky_raw.txt) | Журнал URL Editor'а (20.11.2026, виправлення V-1–V-8): повторне відкриття avia.gov.ua/kerivnitstvo для SC-15 (V-3) |
| [url_check_recheck_obshuky_raw.txt](url_check_recheck_obshuky_raw.txt) | Журнал URL Verifier'а (20.11.2026, targeted re-check V-1–V-8): avia.gov.ua/kerivnitstvo, epravda 814184, zaxid.net, t.me/s/press_kobl; локальні перевірки (sc_links, BMP, лічильники персон) |
| [verification_01_obshuky.md](verification_01_obshuky.md) | Звіт перевірки 01_obshuky.md (Verifier, 20.11.2026): PASS WITH CORRECTIONS, знахідки V-1–V-8, таблиця «Статус виправлень», addendum розд. 11 — targeted re-check 20.11.2026 PASS |

## Особливості сайтів

- `t.me/<канал>/<id>` — прямі URL таймаутяться через web_extractor; повний текст читати через прев'ю `t.me/s/<канал>/<id>` (зазначено в картках SC-03, SC-11, SC-12).
- kobl.gp.gov.ua — перелік новин підвантажується скриптом, fetch-витяг порожній; прямий домен kyivobl.gp.gov.ua не існує (DNS-помилка) (SC-12).
- reyestr.court.gov.ua — асинхронний пошук: чекати завершення і читати підсумок «знайдено документів: N», заглушку «На Ваш запит не знайдено жодного документа» за результат не брати; реєстр працює «в тестовому (обмеженому) режимі» (SC-14).
- avianews.com.ua — 20.11.2026 редірект на сторонній спам-домен; джерело не використовувати (R-12).
- Мінінфра дублирує тг-пости у фейсбуці: URL фейсбук-поста наведений у статті Укрінформу, сам пост не відкривався (SC-09).

## Ключові первинні джерела теми

- Тг-пост Мінінфраструктури від 19.11.2026 — https://t.me/MinInfraUA/17826 (SC-03; читано через прев'ю t.me/s)
- УП-первинка (оригінальна публікація УП/ЕП) — https://epravda.com.ua/biznes/pravoohoronci-provodyat-obshuki-u-derzhaviasluzhbi-dzherela-up-827830/ (SC-01; pravda.com.ua/news/2026/11/19/8063658 редіректить на неї, той самий text_version)
- Керівництво ДАСУ — https://avia.gov.ua/kerivnitstvo (SC-15)
- Розпорядження КМУ від 20.08.2025 № 868-р — https://www.kmu.gov.ua/npas/pro-porushennia-dystsyplinarnoho-provadzhennia-stosovno-holovy-derzhavnoi-aviatsiinoi-s868200825 (SC-16)
- ЄДРСР — https://reyestr.court.gov.ua/ (SC-14: негатив на 19–20.11.2026 з валідованим контрольним запитом)
