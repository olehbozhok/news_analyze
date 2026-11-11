#!/usr/bin/env python3
"""Клікабельні посилання на source cards (SC-NN) у документах аналізів.

Конвенція (AGENTS.md, 6.2):
  - у документі NN_*.md посилання на власні картки — [SC-07],
    на картки іншого документа теми — [01/SC-07];
  - картки лежать у sources/source_cards_NN.md із заголовками "## SC-07";
  - в кінці файлу після маркера скрипт генерує визначення reference-посилань,
    тож [SC-07] рендериться як посилання на sources/source_cards_NN.md#sc-07.

Режими:
  --fix    обгорнути голі SC-NN / NN/SC-NN у [..], нормалізувати заголовки
           карток до "## SC-NN" (назва переходить у рядок нижче),
           перегенерувати блок посилань. Ідемпотентний.
  Також: посилання на папку (`](dir/)`) замінюються на `](dir/README.md)`
  (AGENTS.md, розділ 10).

  --check  нічого не змінює; помилка (код 1), якщо є голі посилання,
           посилання на неіснуючі картки, биті відносні посилання або
           застарілий блок посилань; попередження — картки без посилань.

  --persons  маркери [P:slug] у документах аналізів (не в sources/) стають
             посиланнями на persons/<країна>/<slug>/README.md; у картках
             персон після маркера генерується блок «Згадки в аналізах»:
             на кожен документ — посилання, під ним заголовок документа
             і всі місця згадки у цьому файлі. Кожне місце — клікабельне:
             рядок навколо згадки з виділеним ПІБ як посилання на якір
             найближчого заголовка над згадкою (GitHub-стиль).
             Невідомий slug — помилка.

Аргументи: шляхи до тек тем (analyses/<країна>/<тема>) або до файлів;
без аргументів — усі теми в analyses/.
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MARKER = "<!-- sc-links: згенеровано scripts/sc_links.py, не редагувати -->"

DOC_RE = re.compile(r"^(\d{2})_.+\.md$")
CARDS_RE = re.compile(r"^source_cards_(\d{2})\.md$")
CARD_HEAD_RE = re.compile(r"^## SC-(\d{2,})(?:\.\s*(.*\S))?\s*$")
# голе посилання: не всередині [..], не частина слова чи шляху
BARE_RE = re.compile(r"(?<![\[\w/-])(?:(\d{2})/)?SC-(\d{2,})(?![\w\]-])")
LABEL_RE = re.compile(r"(?<!\])\[(?:(\d{2})/)?SC-(\d{2,})\](?![\[(:])")
LINK_RE = re.compile(r"\]\(([^)\s]+)\)")
CODE_SPAN_RE = re.compile(r"`[^`]*`")


def card_ids(cards_file: Path) -> set[str]:
    if not cards_file.exists():
        return set()
    ids = set()
    for line in cards_file.read_text(encoding="utf-8").splitlines():
        m = CARD_HEAD_RE.match(line)
        if m:
            ids.add(m.group(1))
    return ids


def split_footer(text: str) -> tuple[str, str]:
    idx = text.find(MARKER)
    if idx == -1:
        return text.rstrip("\n"), ""
    return text[:idx].rstrip("\n"), text[idx:]


def iter_body_segments(body: str):
    """Yield (is_code, chunk) by lines; fenced blocks and inline code are code."""
    in_fence = False
    for line in body.split("\n"):
        if line.lstrip().startswith("```"):
            in_fence = not in_fence
            yield True, line
            continue
        yield in_fence, line


def transform_line(line: str, fn) -> str:
    """Apply fn to non-code parts of a line (skips inline code spans)."""
    out, pos = [], 0
    for m in CODE_SPAN_RE.finditer(line):
        out.append(fn(line[pos:m.start()]))
        out.append(m.group(0))
        pos = m.end()
    out.append(fn(line[pos:]))
    return "".join(out)


def non_code_text(body: str) -> str:
    parts = []
    for is_code, line in iter_body_segments(body):
        if not is_code:
            parts.append(CODE_SPAN_RE.sub("", line))
    return "\n".join(parts)


class Topic:
    def __init__(self, path: Path):
        self.path = path
        self.sources = path / "sources"
        self.cards = {}
        if self.sources.is_dir():
            for f in self.sources.iterdir():
                m = CARDS_RE.match(f.name)
                if m:
                    self.cards[m.group(1)] = f

    def files(self):
        for f in sorted(self.path.iterdir()):
            if DOC_RE.match(f.name):
                yield f, DOC_RE.match(f.name).group(1)
        for num, f in sorted(self.cards.items()):
            yield f, num

    def target(self, file: Path, own: str, prefix: str | None) -> tuple[Path | None, str]:
        num = prefix or own
        cards = self.cards.get(num)
        if cards is None:
            return None, num
        if file.resolve() == cards.resolve():
            return None, num  # те саме: якір у межах файлу
        return cards, num


def normalize_card_headings(text: str) -> str:
    out = []
    for line in text.split("\n"):
        m = CARD_HEAD_RE.match(line)
        if m and m.group(2):
            out.append(f"## SC-{m.group(1)}")
            out.append("")
            out.append(f"**{m.group(2)}**")
        else:
            out.append(line)
    return "\n".join(out)


def wrap_bare(body: str) -> str:
    def fn(chunk: str) -> str:
        return BARE_RE.sub(lambda m: "[" + m.group(0) + "]", chunk)

    lines = []
    for is_code, line in iter_body_segments(body):
        if is_code or line.startswith("#"):
            lines.append(line)
        else:
            lines.append(transform_line(line, fn))
    return "\n".join(lines)


def build_footer(topic: Topic, file: Path, own: str, body: str) -> tuple[str, list[str]]:
    errors, defs = [], {}
    text = non_code_text(body)
    for m in LABEL_RE.finditer(text):
        prefix, nn = m.group(1), m.group(2)
        label = f"{prefix}/SC-{nn}" if prefix else f"SC-{nn}"
        target, num = topic.target(file, own, prefix)
        cards_file = topic.cards.get(num)
        if cards_file is None or nn not in card_ids(cards_file):
            errors.append(f"{file}: [{label}] — картки SC-{nn} у source_cards_{num}.md немає")
            continue
        if target is None:
            href = f"#sc-{nn}"
        else:
            href = Path(_relpath(target, file.parent)).as_posix() + f"#sc-{nn}"
        defs[label] = href

    def key(lbl: str):
        pre, _, nn = lbl.rpartition("SC-")
        return (pre, int(nn))

    if not defs:
        return "", errors
    lines = [MARKER, ""] + [f"[{lbl}]: {defs[lbl]}" for lbl in sorted(defs, key=key)]
    return "\n".join(lines) + "\n", errors


def _relpath(target: Path, start: Path) -> str:
    import os
    return os.path.relpath(target, start)


def check_links(file: Path, body: str) -> list[str]:
    errors = []
    for m in LINK_RE.finditer(non_code_text(body)):
        href = m.group(1)
        if re.match(r"^[a-z]+:", href) or href.startswith("#"):
            continue
        path = href.split("#", 1)[0]
        if path and not (file.parent / path).exists():
            errors.append(f"{file}: бите відносне посилання ({href})")
    return errors


def process(topic: Topic, fix: bool) -> tuple[list[str], list[str], list[Path]]:
    errors, warnings, changed = [], [], []
    used: dict[str, set[str]] = {n: set() for n in topic.cards}
    for file, own in topic.files():
        original = file.read_text(encoding="utf-8")
        body, old_footer = split_footer(original)
        if file in topic.cards.values() and fix:
            body = normalize_card_headings(body)
        if fix:
            body = wrap_bare(body)
        else:
            text = non_code_text("\n".join(l for l in body.split("\n") if not l.startswith("#")))
            for m in BARE_RE.finditer(text):
                errors.append(f"{file}: голе посилання {m.group(0)} (запустіть --fix)")
            if file in topic.cards.values():
                for line in body.split("\n"):
                    m = CARD_HEAD_RE.match(line)
                    if m and m.group(2):
                        errors.append(f"{file}: заголовок картки не нормалізовано: {line[:40]}")
        footer, errs = build_footer(topic, file, own, body)
        errors += errs
        errors += check_links(file, body)
        for m in LABEL_RE.finditer(non_code_text(body)):
            num = m.group(1) or own
            if num in used:
                used[num].add(m.group(2))
        if not footer and not old_footer and body == original.rstrip("\n"):
            new = original  # нічого змінювати: не чіпати пробіли в кінці файлу
        else:
            new = body + "\n" + (("\n" + footer) if footer else "")
        if new != original:
            if fix:
                file.write_text(new, encoding="utf-8")
                changed.append(file)
            elif footer.strip() != old_footer.strip():
                errors.append(f"{file}: блок посилань застарів (запустіть --fix)")
    for num, cards_file in topic.cards.items():
        for nn in sorted(card_ids(cards_file) - used[num], key=int):
            warnings.append(f"{cards_file}: картка SC-{nn} не має посилань")
    return errors, warnings, changed


def topics_from_args(args: list[str]) -> list[Topic]:
    if not args:
        return [Topic(p) for p in sorted((ROOT / "analyses").glob("*/*")) if p.is_dir()]
    topics = []
    for a in args:
        p = Path(a).resolve()
        if p.is_file():
            p = p.parent.parent if p.parent.name == "sources" else p.parent
        topics.append(Topic(p))
    return topics


DIR_LINK_RE = re.compile(r"\]\(((?![a-z]+:)[^)#\s]*/)(#[^)]*)?\)")
RAW_RE = re.compile(r"agent_.*_raw\.md$")


def dir_link_files(paths: list[str]) -> list[Path]:
    """Markdown-файли для перевірки посилань на папки (без сирих логів)."""
    if not paths:
        files = [f for f in ROOT.rglob("*.md") if ".claude" not in f.parts and ".git" not in f.parts]
    else:
        files = []
        for t in topics_from_args(paths):
            files += list(t.path.rglob("*.md"))
    return sorted(f for f in files if not RAW_RE.search(f.name))


def dir_links(files: list[Path], fix: bool) -> tuple[list[str], list[Path]]:
    """Посилання на папку мають вести на її README.md (AGENTS.md, розділ 10)."""
    errors, changed = [], []
    for f in files:
        text = f.read_text(encoding="utf-8")
        in_templates = (ROOT / "_templates") in f.parents
        # шаблони розраховані на копію в analyses/<країна>/<тема>/
        base = ROOT / "analyses" / "x" / "y" if in_templates else f.parent

        def repl(m):
            target = (base / m.group(1)).resolve()
            if (target / "README.md").is_file():
                if fix:
                    return f"]({m.group(1)}README.md{m.group(2) or ''})"
                errors.append(f"{f}: посилання на папку {m.group(1)} — вести на {m.group(1)}README.md")
            else:
                errors.append(f"{f}: посилання на папку без README.md ({m.group(1)})")
            return m.group(0)

        new = DIR_LINK_RE.sub(repl, text)
        if fix and new != text:
            f.write_text(new, encoding="utf-8")
            changed.append(f)
    return errors, changed


PERSONS = ROOT / "persons"
P_MARKER = "<!-- persons-backlinks: згенеровано scripts/sc_links.py --persons, не редагувати -->"
P_RE = re.compile(r"\[P:([a-z0-9_]+)\]")
P_LINK_RE = re.compile(r"\]\([^)\s]*persons/([a-z]+)/([a-z0-9_]+)/README\.md(?:#[^)]*)?\)")


def person_index() -> tuple[dict[str, tuple[str, str]], list[str]]:
    """slug -> (країна, заголовок картки); помилки для дублів slug."""
    idx, dupes = {}, []
    if not PERSONS.is_dir():
        return idx, dupes
    for country in sorted(p for p in PERSONS.iterdir() if p.is_dir()):
        for pdir in sorted(p for p in country.iterdir() if p.is_dir()):
            readme = pdir / "README.md"
            if not readme.is_file():
                continue
            first = readme.read_text(encoding="utf-8").splitlines()[0]
            title = first.lstrip("#").strip() or pdir.name
            if pdir.name in idx:
                dupes.append(f"persons: slug «{pdir.name}» існує в двох країнах")
                continue
            idx[pdir.name] = (country.name, title)
    return idx, dupes


def person_docs() -> list[Path]:
    """Документи, у яких шукаються згадки персон: аналізи (без sources/) і нотатки персон."""
    docs = []
    for p in sorted((ROOT / "analyses").rglob("*.md")):
        if "sources" in p.parts or "_templates" in p.parts:
            continue
        docs.append(p)
    persons = ROOT / "persons"
    if persons.is_dir():
        for p in sorted(persons.rglob("*.md")):
            # лише документи в папці персони: persons/<країна>/<slug>/*.md
            if len(p.relative_to(persons).parts) >= 3 and "_templates" not in p.parts:
                docs.append(p)
    return docs


def _rel(target: Path, start: Path) -> str:
    import os
    return os.path.relpath(target, start).replace(os.sep, "/")


def person_link(slug: str, country: str, title: str, file: Path) -> str:
    target = PERSONS / country / slug / "README.md"
    return f"[{title}]({_rel(target, file.parent)})"


def fix_person_markers(files: list[Path], idx: dict[str, tuple[str, str]]) -> tuple[list[str], list[Path]]:
    errors, changed = [], []
    for f in files:
        text = f.read_text(encoding="utf-8")
        out = []
        for is_code, line in iter_body_segments(text):
            if is_code:
                out.append(line)
                continue

            def fn(chunk: str) -> str:
                def repl(m):
                    slug = m.group(1)
                    if slug not in idx:
                        errors.append(f"{f}: невідома персона у маркері [P:{slug}]")
                        return m.group(0)
                    country, title = idx[slug]
                    return person_link(slug, country, title, f)
                return P_RE.sub(repl, chunk)

            out.append(transform_line(line, fn))
        new = "\n".join(out)
        if new != text:
            f.write_text(new, encoding="utf-8")
            changed.append(f)
    return errors, changed


def check_person_markers(files: list[Path], idx: dict[str, tuple[str, str]]) -> list[str]:
    errors = []
    for f in files:
        for m in P_RE.finditer(non_code_text(f.read_text(encoding="utf-8"))):
            if m.group(1) not in idx:
                errors.append(f"{f}: невідома персона у маркері [P:{m.group(1)}]")
    return errors


SNIP_BEFORE = 80
SNIP_AFTER = 140
HEAD_MAX = 100
MD_LINK_RE = re.compile(r"\[([^\]]+)\]\([^)]*\)")
EMPH_RE = re.compile(r"[*_]+")


def _clean_frag(s: str) -> str:
    s = EMPH_RE.sub("", s)
    return re.sub(r"\s+", " ", s).strip()


def _clean_with_map(line: str) -> tuple[str, list[int]]:
    """Рядок без markdown-посилань ([текст](href) -> текст) + мапа raw->clean індексів."""
    out: list[str] = []
    imap: list[int] = []
    pos = 0
    for m in MD_LINK_RE.finditer(line):
        for i in range(pos, m.start()):
            out.append(line[i])
            imap.append(len(out) - 1)
        txt_start = len(out)
        for ch in m.group(1):
            out.append(ch)
        for _i in range(m.start(), m.end()):
            imap.append(txt_start)
        pos = m.end()
    for i in range(pos, len(line)):
        out.append(line[i])
        imap.append(len(out) - 1)
    return "".join(out), imap


def _doc_title(text: str) -> str:
    """Заголовок першого рівня документа (для контексту згадки)."""
    for line in text.split("\n"):
        if line.startswith("# "):
            t = _clean_frag(line[2:])
            if len(t) > HEAD_MAX:
                t = t[: HEAD_MAX - 1].rstrip() + "…"
            return t
    return ""


def _around(cleaned: str, s: int, e: int) -> str:
    """Фрагмент чистого рядка навколо згадки [s:e]: до + виділена згадка + після."""
    before = _clean_frag(cleaned[max(0, s - SNIP_BEFORE) : s])
    mention = _clean_frag(cleaned[s:e]) or "згадка"
    after = _clean_frag(cleaned[e : e + SNIP_AFTER])
    prefix = "… " if s > SNIP_BEFORE else ""
    suffix = " …" if e + SNIP_AFTER < len(cleaned.rstrip()) else ""
    return f"{prefix}{before} **{mention}** {after}{suffix}".strip()


def _heading_anchor(text: str) -> str:
    """GitHub-якір заголовка: нижній регістр, без пунктуації, пробіли -> дефіси."""
    t = text.strip().lower()
    t = re.sub(r"[^\w\s-]", "", t)
    t = re.sub(r"\s", "-", t)
    return t.strip("-")


def mentions(idx: dict[str, tuple[str, str]]) -> dict[str, dict[Path, tuple[str, list[tuple[str, str]]]]]:
    """slug -> {файл: (заголовок документа, [(фрагмент навколо згадки, якір розділу)])}."""
    found: dict[str, dict[Path, tuple[str, list[tuple[str, str]]]]] = {slug: {} for slug in idx}
    by_path = {
        (PERSONS / country / slug / "README.md").resolve(): slug
        for slug, (country, _t) in idx.items()
    }
    for f in person_docs():
        text = f.read_text(encoding="utf-8")
        title = _doc_title(text)
        head_counts: dict[str, int] = {}
        cur_anchor = ""
        for is_code, line in iter_body_segments(text):
            if is_code:
                continue
            if line.startswith("#"):
                head = _clean_frag(line.lstrip("#").strip())
                base = _heading_anchor(head)
                n = head_counts.get(base, 0)
                head_counts[base] = n + 1
                cur_anchor = base if n == 0 else f"{base}-{n}"
            cands: dict[str, tuple[int, int, int | None]] = {}
            for m in P_RE.finditer(line):
                if m.group(1) in found and m.group(1) not in cands:
                    cands[m.group(1)] = (m.start(), m.end(), None)
            for m in LINK_RE.finditer(line):
                href = m.group(1)
                if re.match(r"^[a-z]+:", href) or href.startswith("#"):
                    continue
                target = (f.parent / href.split("#", 1)[0]).resolve()
                slug = by_path.get(target)
                if not slug or slug in cands or slug not in found:
                    continue
                country = idx[slug][0]
                if (PERSONS / country / slug) in f.parents:
                    continue  # документ у папці самої персони не є згадкою про неї
                s = line.rfind("[", 0, m.start())  # [, що відкриває текст цього посилання
                if s == -1:
                    continue
                text_len = m.start() - s - 1  # текст між [ і ](
                cands[slug] = (s, m.end(), text_len)
            if not cands:
                continue
            cleaned, imap = _clean_with_map(line)
            for slug, (s, _e, text_len) in cands.items():
                cstart = imap[s]
                cend = cstart + text_len if text_len is not None else imap[_e - 1] + 1
                found[slug].setdefault(f, (title, []))[1].append(
                    (_around(cleaned, cstart, cend), cur_anchor)
                )
    return found


def backlinks_block(
    slug: str, docs: dict[Path, tuple[str, list[tuple[str, str]]]], readme: Path
) -> str:
    if not docs:
        return ""
    lines = [P_MARKER, "", "## Згадки в аналізах", ""]
    for d in sorted(docs):
        title, spots = docs[d]
        rel = _rel(d, readme.parent)
        lines.append(f"- [{d.relative_to(ROOT).as_posix()}]({rel})")
        if title:
            lines.append(f"  {title}")
        for sp, anchor in spots:
            text = sp.replace("][", ", ").replace("[", "").replace("]", "")
            if anchor:
                lines.append(f"  - [{text}]({rel}#{anchor})")
            else:
                lines.append(f"  - {text}")
    return "\n".join(lines) + "\n"


def person_backlinks(fix: bool) -> tuple[list[str], list[Path]]:
    idx, errors = person_index()
    found = mentions(idx)
    changed = []
    for slug, (country, _title) in sorted(idx.items()):
        readme = PERSONS / country / slug / "README.md"
        text = readme.read_text(encoding="utf-8")
        pos = text.find(P_MARKER)
        body = text[:pos].rstrip("\n") if pos != -1 else text.rstrip("\n")
        want = backlinks_block(slug, found[slug], readme)
        new = body + ("\n\n" + want if want else "\n")
        if new == text:
            continue
        if fix:
            readme.write_text(new, encoding="utf-8")
            changed.append(readme)
        else:
            errors.append(f"{readme}: блок «Згадки в аналізах» застарів (запустіть --persons --fix)")
    return errors, changed


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    mode = ap.add_mutually_exclusive_group(required=True)
    mode.add_argument("--fix", action="store_true")
    mode.add_argument("--check", action="store_true")
    ap.add_argument("--persons", action="store_true",
                    help="маркери [P:slug] і блок «Згадки в аналізах» у картках persons/")
    ap.add_argument("paths", nargs="*")
    ns = ap.parse_args()
    all_err, all_warn = [], []
    for topic in topics_from_args(ns.paths):
        errors, warnings, changed = process(topic, fix=ns.fix)
        all_err += errors
        all_warn += warnings
        for f in changed:
            print(f"оновлено: {f.relative_to(ROOT)}")
    errors, changed = dir_links(dir_link_files(ns.paths), fix=ns.fix)
    all_err += errors
    for f in changed:
        print(f"оновлено (посилання на README): {f.relative_to(ROOT)}")
    if ns.persons:
        idx, perr = person_index()
        all_err += perr
        docs = person_docs()
        if ns.fix:
            perr, pchanged = fix_person_markers(docs, idx)
            all_err += perr
            for f in pchanged:
                print(f"оновлено (маркери персон): {f.relative_to(ROOT)}")
        else:
            all_err += check_person_markers(docs, idx)
        perr, pchanged = person_backlinks(fix=ns.fix)
        all_err += perr
        for f in pchanged:
            print(f"оновлено (згадки персон): {f.relative_to(ROOT)}")
    for w in all_warn:
        print(f"попередження: {w}")
    for e in all_err:
        print(f"помилка: {e}", file=sys.stderr)
    if ns.check:
        print(f"перевірка: {len(all_err)} помилок, {len(all_warn)} попереджень")
    return 1 if all_err else 0


if __name__ == "__main__":
    sys.exit(main())
