import urllib.parse

# Пошукові запити для zakon.rada.gov.ua (кирилиця лише у файлі, не в аргументах командного рядка)
queries = [
    "Звільнити Богдана Керівника Офісу Президента України",
    "Богдана Керівника Офісу Президента",
]
for q in queries:
    print("https://zakon.rada.gov.ua/laws/find/a?text=" + urllib.parse.quote(q))
