"""Render citations in instructor/ notebooks from references.bib.

In markdown cells, cite with `[@key]` or `[@key1; @key2]`. This script turns each citation into
DOI links, e.g. `[Orth et al., 2010](https://doi.org/10.1038/nbt.1614)`, and rewrites the markdown
cell tagged `references` with the full list of works cited in that notebook. Rendered links are
recognized again on the next run, so the script is idempotent and picks up edits to references.bib.

    python render_refs.py          # render in place
    python render_refs.py --check  # exit 1 if anything would change (used in CI)
"""
import re
import sys
from pathlib import Path

import bibtexparser
import nbformat

with open("references.bib") as f:
    BIB = {e["ID"]: e for e in bibtexparser.load(f).entries}


def url(e):  # parentheses (e.g. in Elsevier DOIs) would end a markdown link early
    u = f"https://doi.org/{e['doi']}" if "doi" in e else e["url"]
    return u.replace("(", "%28").replace(")", "%29")


BY_URL = {url(e): key for key, e in BIB.items()}


def surnames(e):
    names = [a.strip() for a in e["author"].replace("\n", " ").split(" and ")]
    return [n.split(",")[0].strip("{} ") if "," in n else n.split()[-1].strip("{}") for n in names]


def short(e):
    s = surnames(e)
    who = s[0] if len(s) == 1 else f"{s[0]} & {s[1]}" if len(s) == 2 else f"{s[0]} et al."
    return f"{who}, {e['year']}"


def full(e):
    s = surnames(e)
    authors = ", ".join(s[:3]) + (" et al." if len(s) > 3 else "")
    venue = e.get("journal") or e.get("publisher") or e.get("booktitle") or ""
    vol = f" {e['volume']}" if "volume" in e else ""
    pages = f":{e['pages'].replace('--', '-')}" if "pages" in e else ""
    title = re.sub(r"[{}]", "", e["title"]).replace("\n", " ").rstrip(".")
    title += "" if title.endswith(("?", "!")) else "."
    return f"{authors} ({e['year']}). {title} *{venue}*{vol}{pages}. [{url(e).removeprefix('https://')}]({url(e)})"


CITE = re.compile(r"\[(@[\w:-]+(?:\s*;\s*@[\w:-]+)*)\]")  # [@a; @b]
LINK = re.compile(r"\[[^\]]+\]\((https://doi\.org/[^)\s]+|[^)\s]+)\)")  # a rendered citation


def render_cell(text, cited):
    def cite(m):
        keys = [k.strip().lstrip("@") for k in m.group(1).split(";")]
        missing = [k for k in keys if k not in BIB]
        if missing:
            sys.exit(f"unknown citation key(s): {missing}")
        cited.update(keys)
        return "; ".join(f"[{short(BIB[k])}]({url(BIB[k])})" for k in keys)

    def relink(m):  # refresh the text of an already rendered citation
        key = BY_URL.get(m.group(1))
        if key is None or not re.fullmatch(r"\[[^\]]*, \d{4}[a-z]?\]", m.group(0).split("](")[0] + "]"):
            return m.group(0)
        cited.add(key)
        return f"[{short(BIB[key])}]({url(BIB[key])})"

    return LINK.sub(relink, CITE.sub(cite, text))


def render(nb):
    cited, ref_cell = set(), None
    for cell in nb.cells:
        if "references" in cell.metadata.get("tags", []):
            ref_cell = cell
        elif cell.cell_type == "markdown":
            cell.source = render_cell(cell.source, cited)
    if cited and ref_cell is None:
        sys.exit("notebook cites works but has no markdown cell tagged `references`")
    if ref_cell is not None:
        entries = sorted(cited, key=lambda k: (surnames(BIB[k])[0], BIB[k]["year"]))
        ref_cell.source = "## References\n\n" + "\n".join(f"- {full(BIB[k])}" for k in entries)


if __name__ == "__main__":
    changed = []
    for path in sorted(Path("instructor").glob("*.ipynb")):
        nb = nbformat.read(path, as_version=4)
        before = nbformat.writes(nb)
        render(nb)
        if nbformat.writes(nb) != before:
            changed.append(path.name)
            if "--check" not in sys.argv:
                nbformat.write(nb, path)
    print("changed:" if changed else "up to date", *changed)
    sys.exit(1 if changed and "--check" in sys.argv else 0)
