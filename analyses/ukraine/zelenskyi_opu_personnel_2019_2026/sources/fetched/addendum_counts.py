# -*- coding: utf-8 -*-
# Addendum verifier: file-based pattern counts (no Cyrillic in argv)
import io, sys, re

base = 'D:/news/worktrees/zelenskyi_opu_personnel_2019_2026/analyses/ukraine/zelenskyi_opu_personnel_2019_2026/'
doc = io.open(base + '01_liudy_opu.md', encoding='utf-8').read()
pre = io.open(base + 'persons/README.md', encoding='utf-8').read()
cards = io.open(base + 'sources/source_cards_01.md', encoding='utf-8').read()
scope = io.open(base + 'scope_contract.md', encoding='utf-8').read()
topic_readme = io.open(base + 'README.md', encoding='utf-8').read()
dem = io.open(base + 'persons/ruslan_demchenko/README.md', encoding='utf-8').read()

pats = {
    'doc sprouchanykh': doc.count('спростован'),
    'doc vidmovylas': doc.count('відмов'),
    'doc yedynyy': doc.count('єдиний'),
    'doc vynyatok': doc.count('виняток'),
    'doc zviryaetsya': doc.count('звіряється'),
    'doc do utvorennia OP': doc.count('до утворення ОП'),
    'doc pershouyu zastupnytseyu': doc.count('першою заступницею'),
    'doc 18 osib': doc.count('18 осіб'),
    'doc 19 osib': doc.count('19 осіб'),
    'doc minister': doc.count('міністерськ'),
    'doc Sobolyev-ye': doc.count('Соболєв'),
    'doc Sobolev-e': doc.count('Соболев'),
    'doc ni_mets': doc.count('німець'),
    'doc bude dodano kartkoyu': doc.count('буде додано карткою'),
    'doc zastariy zvirky (demchenko note src)': doc.count('звірити послідовність'),
    'persons_readme Sobolyev-ye': pre.count('Соболєв'),
    'persons_readme Sobolev-e': pre.count('Соболев'),
    'persons_readme shefir period 21.05': pre.count('21.05.2019 - 30.03.2024'),
    'persons_readme demchenko bez poz nachky': pre.count('без позначки «поза штатом»'),
    'cards SC-11 title fixed': cards.count('Пошук указу про першу заступницю'),
    'cards SC-21 date': cards.count('від 21.05.2019'),
    'cards SC-22 date': cards.count('від 30.03.2024'),
    'scope updateovazheni mezha': scope.count('Уповноважені Президента України» покритий'),
    'topic_readme 19 osib': topic_readme.count('19 осіб'),
    'topic_readme 67 periodiv': topic_readme.count('67 посадових періодів'),
    'dem note stale zvirka': dem.count('звірити послідовність при верифікації'),
}
for k, v in sorted(pats.items()):
    print(k, '=', v)

# where SC-11 appears in doc body (before sc-links marker)
body = doc.split('<!-- sc-links')[0]
lines = body.splitlines()
for c in ['[SC-11]', '[SC-120]', '[SC-121]', '[SC-122]', '[SC-123]', '[SC-124]', '[SC-125]']:
    idx = [i + 1 for i, l in enumerate(lines) if c in l]
    print(c, '-> lines', idx)

# section 16 contains no 311/2019, 305/2019, 207/2024
i16 = doc.find('## 16.')
i17 = doc.find('## 17.')
r16 = doc[i16:i17]
print('r16 has 311/2019:', '311/2019' in r16)
print('r16 has 305/2019:', '305/2019' in r16)
print('r16 has 207/2024:', '207/2024' in r16)
print('r16 has SC-124:', '[SC-124]' in r16)
print('r16 has SC-125:', '[SC-125]' in r16)
print('r16 has SC-121:', '[SC-121]' in r16)
print('r16 has SC-122:', '[SC-122]' in r16)

# card quotes verbatim match against snapshots
u46 = io.open(base + 'sources/fetched/u46_2020.txt', encoding='utf-8').read()
u311 = io.open(base + 'sources/fetched/u311_2019.txt', encoding='utf-8').read()
add46 = io.open(base + 'sources/fetched/addendum_46.txt', encoding='utf-8').read()
rt_ukr = io.open(base + 'sources/fetched/rt_ukrinform_podolyak.txt', encoding='utf-8').read()
rt_un = io.open(base + 'sources/fetched/rt_ukranews_vitu.txt', encoding='utf-8').read()
q120 = 'Звільнити БОГДАНА Андрія Йосиповича з посади Керівника Офісу Президента України.'
q123 = 'Призначити ЄРМАКА Андрія Борисовича помічником Президента України.'
q124 = 'Після звільнення Андрія Єрмака з посади керівника Офісу Президента його помічники і радники були також звільнені, але Сергій Лещенко, Михайло Подоляк та Олександ Бевз переведені на інші посади в ОП.'
q125 = 'У відповіді на запит Українських Новин щодо кадрових ротацій в Офісі Президента України на Банковій, серед іншого повідомили, що звільнення та призначення на посади в ОП у зазначений час проводились через накази Керівника Апарату Офісу Президента України.'
print('q120 in u46:', q120 in u46, '| in addendum46:', q120 in add46, '| snapshots same content:', u46.strip() == add46.strip())
print('q123 in u311:', q123 in u311)
print('q124 in rt_ukrinform:', q124 in rt_ukr)
print('q125 in rt_ukranews:', q125 in rt_un)
print('leschenko quote in rt_ukrinform:', 'Я і Михайло Подоляк ми перепризначені на посаду радників Офісу Президента' in rt_ukr)
print('vitiushok-za-dany-my in rt_ukranews:', 'Згідно з даними офіційного порталу президента України, у зазначений час цю посаду обіймала Вітушок Марія Анатоліївна' in rt_un)
print('dates in snapshots: u46 11.02.2020:', '11.02.2020' in u46, '| u311 21.05.2019:', '21.05.2019' in u311)
