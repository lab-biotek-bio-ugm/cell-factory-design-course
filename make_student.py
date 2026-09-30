"""Generate student/ notebooks from instructor/ notebooks.

Cells tagged `solution` are removed; each run of solution code cells is replaced by one
empty "# Your code here" cell. All outputs are cleared.

    python make_student.py
"""
from pathlib import Path

import nbformat

STUB = "# Your code here\n"

for path in sorted(Path("instructor").glob("*.ipynb")):
    nb = nbformat.read(path, as_version=4)
    cells = []
    for cell in nb.cells:
        if "solution" in cell.metadata.get("tags", []):
            if cell.cell_type == "code" and not (cells and cells[-1].source == STUB):
                stub = nbformat.v4.new_code_cell(STUB)
                del stub["id"]  # cell ids are nbformat 4.5; the course notebooks are 4.4
                cells.append(stub)
            continue
        if cell.cell_type == "code":
            cell.outputs, cell.execution_count = [], None
        cells.append(cell)
    nb.cells = cells
    Path("student").mkdir(exist_ok=True)
    nbformat.write(nb, Path("student") / path.name)
    print(path.name)
