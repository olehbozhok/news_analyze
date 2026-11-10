# Аналітичні дослідження

Аналізи політичних, правових і соціальних тем з верифікацією джерел. Мова документів — українська.

Регламент роботи (ролі, верифікація, статуси джерел, структура документа, неймінг) — [`AGENTS.md`](AGENTS.md).

---

## Країни

- [`analyses/ukraine/`](analyses/ukraine/README.md)
- [`analyses/usa/`](analyses/usa/README.md)

Перелік аналізів зі статусами — у `README.md` кожної країни. Картки персон, які фігурують в аналізах, — у [`persons/`](persons/README.md) (одна особа — одна картка незалежно від кількості тем).

## Службове

| Шлях | Призначення |
|---|---|
| [`AGENTS.md`](AGENTS.md) | Спільний регламент |
| [`CLAUDE.md`](CLAUDE.md) | Імпортує `AGENTS.md` для Claude Code |
| [`agents/`](agents/README.md) | Канонічні файли ролей агентів (researcher, writer, verifier, editor, red_team) |
| [`_templates/`](_templates/README.md) | Заготовки для нового аналізу |
| [`persons/`](persons/README.md) | Картки персон за країнами (6.5) |
| [`TODO.md`](TODO.md) | Поточний список робіт: картки персон, рішення власника, верифікація |

---

## Як додати новий аналіз

1. Скопіювати [`_templates/`](_templates/README.md): `cp -r _templates analyses/<країна>/<тема>` (латиниця, `snake_case`).
2. Заповнити [`scope_contract.md`](_templates/scope_contract.md) — без нього research не починається.
3. Додати рядок у `README.md` країни зі статусом `ЧЕРНЕТКА`. Нова країна — нова папка з `README.md` і посилання в списку «Країни» вище.
4. Пройти цикл з [`AGENTS.md`, розділ 3](AGENTS.md): research → draft → verification → corrections.
5. Після PASS від Verifier — змінити статус на `ГОТОВО`.
