# TODO: документ 12_vymiriuvannia_inflatsii.md

**Тема:** вимірювання інфляції за другої адміністрації Трампа (методологія, офіційні vs альтернативні виміри, цілісність даних, критичний аналіз «нормальної економіки»).
**Регламент:** цикл AGENTS.md, розділ 3. Ворктрії: `D:\news\worktrees\dev` (гілка `wt/dev`).
**Оновлено:** 2026-11-07 (кроки 2–10).

## Статус

| # | Крок циклу | Артефакти | Статус |
|---|---|---|---|
| 1 | Scope: тема, питання, контраргументи | `scope_contract.md` (питання теми інфляції) | ✅ Завершено |
| 2 | Research, підтема A: методологія CPI/PCE/PPI, керівництво BLS, скорочення, незалежність статистики | `sources/agent_methodology_raw.md`, `sources/url_check_raw_methodology.txt` | ✅ Завершено |
| 3 | Research, підтема B: офіційні серії 2025–2026, пропуски через шатдаун, графік релізів, vintage | `sources/agent_official_data_raw.md`, `sources/url_check_raw_official_data.txt` | ✅ Завершено |
| 4 | Research, підтема C: альтернативні виміри (Cleveland/Atlanta/Dallas Fed, Truflation, очікування, COLA) | `sources/agent_alternative_measures_raw.md`, `sources/url_check_raw_alternative_measures.txt` | ✅ Завершено |
| 5 | Research, підтема D: узгодження з макропоказниками «нормальної економіки» (ВВП, праця, ринок, борг) | `sources/agent_macro_indicators_raw.md`, `sources/url_check_raw_macro_indicators.txt` | ✅ Завершено |
| 6 | Research, підтема E: цілісність даних — тиск, заяви про «фальшиві» дані, приховування (факт/позиція/не підтверджено) | `sources/agent_data_integrity_raw.md`, `sources/url_check_raw_data_integrity.txt` | ✅ Завершено |
| 7 | Writer: чернетка документа 12 + `sources/source_cards_12.md` + рядок у README аналізу | `12_vymiriuvannia_inflatsii.md`, `sources/source_cards_12.md` | ✅ Завершено (07.11.2026) |
| 8 | Red team: adversarial check, матеріал для steelman | `sources/agent_red_team_inflation_raw.md` | ✅ Завершено (07.11.2026) |
| 9 | Verifier (окремий агент, чистий контекст) | `sources/verification_12_vymiriuvannia_inflatsii.md` | ✅ PASS WITH CORRECTIONS (6 MAJOR, 18 MINOR, 5 UNVERIFIABLE) |
| 10 | Editor: виправлення за звітом, таблиця «Статус виправлень» | оновлений `12_vymiriuvannia_inflatsii.md`, заповнений звіт | ✅ Виправлення внесено 07.11.2026 (документ 12, картки, точкові правки в 01/08/11, таблиця «Статус виправлень») |
| 11 | Final check: `sc_links.py --fix`/`--check`, пошук новин за 30 днів, статус `НА ПЕРЕВІРЦІ`/`ГОТОВО` в README аналізу | README, git-коміт у `wt/dev` | 🔶 `sc_links.py --fix/--check` виконано; статус `НА ПЕРЕВІРЦІ`; **потрібен targeted addendum Verifier** (документ 12 і блоки «Зміни 2026-11-07» у 01, 08, 11); коміт — не робився; пошук новин за 30 днів перед здачею |

## Легенда

- ✅ завершено; 🔶 в роботі; ⬜ не почато / чекає на залежність.

## Примітки

- Дослідники запускаються послідовно (середовище обмежує паралельні агенти; помилка «model concurrency limit exceeded»).
- Основний інструмент веб-перевірки в цій теці — навичка browser-use:control-browser; `chrome_*` недоступні (див. пам'ять).
- Після отримання PASS — вирішити: мердж `wt/dev` → `main` (з комітом у ворктрії).
