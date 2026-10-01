# AGENTS.md

Guidance for coding agents (and humans) working on this repository: a 12-notebook course on
genome-scale metabolic models with COBRApy and cameo. See README.md for the course itself.

## Layout

- `instructor/` is the source of truth: notebooks with worked solutions. Edit only these.
- `student/` is generated from `instructor/` by `make_student.py`. Never edit it by hand.
- `data/` holds every model and dataset the notebooks load. Notebooks read `data/...` relative to
  the repo root; the setup cell (tag `setup`) moves there, both locally and on Colab.
- `references.bib` holds all citations; `render_refs.py` renders them into the notebooks.
- `cameo_compat.py` patches cameo 0.13.6 (unmaintained) for Python 3.12+, cobra 0.32, pandas 2,
  IPython 9. Import it before cameo. Extend it there instead of patching site-packages.

## Setup and commands

```bash
mamba env create -f environment.yml && mamba activate cell-factory-design-course
make refs      # render [@key] citations from references.bib into instructor/
make student   # refs + regenerate student/
make check     # refs rendered, student/ in sync, no outputs committed (CI runs this)
make test      # execute all 24 notebooks; outputs go to a temp dir
make clean     # clear outputs in place
```

`make test` takes about 10 min; notebook 08 alone takes 6-8 min with GLPK. To test one notebook:
`jupyter nbconvert --to notebook --execute --output-dir /tmp/out instructor/NN-*.ipynb`
(never `--allow-errors`; a run only passes without it).

## Notebook conventions

- Tags: `setup` (first code cell, after the title; identical in every notebook), `solution`
  (exercise answers, code and markdown; replaced by one `# Your code here` cell in `student/`),
  `references` (one markdown cell at the end, rewritten by `render_refs.py`).
- Each notebook starts with an Overview cell: learning objectives, estimated time, prerequisites,
  background.
- Student notebooks must run without errors as shipped: a student stub that later cells depend on
  needs an untagged placeholder before the `solution` cell.
- Keep notebooks nbformat 4.4 without cell ids, and commit them with outputs cleared.
- No kernelspec in notebook metadata (so Colab and CI use their default `python3`).
- Cite with `[@key]` or `[@key1; @key2]`; add new entries to `references.bib` with a DOI
  (BibTeX from `curl -sLH "Accept: application/x-bibtex" https://doi.org/<DOI>`), key
  `firstauthorYEAR`. Mark claims you could not verify with `[VERIFY: claim — reason]`.
- Numbers quoted in markdown must match what the code prints; re-execute after changing code.
- Plain, concise prose for students new to modeling.

## Dependencies and gotchas

- `requirements.txt` is what Colab installs; keep it compatible with Colab's preinstalled stack
  (Python 3.13, numpy 2.1, pandas 2.2, ipywidgets 7). `requirements-lock.txt` pins exact versions
  (regenerate with `pip list --format=freeze` after a verified run).
- Pins that exist for cameo: `numpy<2.4` (numpy.trapz), `setuptools<81` (pkg_resources),
  `ipywidgets<8` (escher), `pandas<3` (also cobra).
- Solver is GLPK. MILP methods (pathway prediction, OptKnock) are slow and can return different,
  equally good answers between runs; seed OptGene and hedge text about specific designs.
- Notebook 12 sets GLPK to dual simplex (`use_dual_simplex`); the default primal simplex stalls on
  the enzyme-constrained model. The setting is lost on `model.copy()`.
- cameo result `.plot()` needs an explicit `PlotlyPlotter()` argument.
- Escher maps need internet. Bundled SBML files are older BiGG exports; do not replace them with
  current BiGG downloads without re-checking every number quoted in the notebooks and slides.

## Git

Never commit outputs, `.env/` or `__pycache__/`. Run `make check` before committing.
