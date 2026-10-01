# Cell factory design course

[![notebooks](https://github.com/lab-biotek-bio-ugm/cell-factory-design-course/actions/workflows/notebooks.yml/badge.svg)](https://github.com/lab-biotek-bio-ugm/cell-factory-design-course/actions/workflows/notebooks.yml)

An introduction to genome-scale metabolic models (GEMs) and model-guided strain design with
[COBRApy](https://github.com/opencobra/cobrapy) and [cameo](https://github.com/biosustain/cameo),
in 12 Jupyter notebooks. Originally developed at DTU Biosustain; updated in 2026 to run on current
Python and on Google Colab.

- `student/`: notebooks for students; exercise solutions are replaced by empty `# Your code here` cells.
- `instructor/`: the same notebooks with worked solutions (cells tagged `solution`). This is the source of truth.
- `data/`: all models and datasets the notebooks use, bundled so results are reproducible.

## Notebooks

| # | Topic | Open in Colab | Runtime* |
|---|-------|---------------|----------|
| 01 | Load a model, run FBA, read fluxes | [student](https://colab.research.google.com/github/lab-biotek-bio-ugm/cell-factory-design-course/blob/main/student/01-Getting-started.ipynb) · [instructor](https://colab.research.google.com/github/lab-biotek-bio-ugm/cell-factory-design-course/blob/main/instructor/01-Getting-started.ipynb) | 10 s |
| 02 | Metabolites, reactions, genes, GPRs, the S matrix | [student](https://colab.research.google.com/github/lab-biotek-bio-ugm/cell-factory-design-course/blob/main/student/02-Genome-scale-metabolic-models.ipynb) · [instructor](https://colab.research.google.com/github/lab-biotek-bio-ugm/cell-factory-design-course/blob/main/instructor/02-Genome-scale-metabolic-models.ipynb) | 10 s |
| 03 | Draw fluxes on Escher maps (needs internet) | [student](https://colab.research.google.com/github/lab-biotek-bio-ugm/cell-factory-design-course/blob/main/student/03-Pathway-visualization.ipynb) · [instructor](https://colab.research.google.com/github/lab-biotek-bio-ugm/cell-factory-design-course/blob/main/instructor/03-Pathway-visualization.ipynb) | 10 s |
| 04 | Flux variability analysis, phenotypic phase planes | [student](https://colab.research.google.com/github/lab-biotek-bio-ugm/cell-factory-design-course/blob/main/student/04-Analyzing-metabolic-models.ipynb) · [instructor](https://colab.research.google.com/github/lab-biotek-bio-ugm/cell-factory-design-course/blob/main/instructor/04-Analyzing-metabolic-models.ipynb) | 40 s |
| 05 | Contexts, media, adding reactions and pathways | [student](https://colab.research.google.com/github/lab-biotek-bio-ugm/cell-factory-design-course/blob/main/student/05-Manipulating-models.ipynb) · [instructor](https://colab.research.google.com/github/lab-biotek-bio-ugm/cell-factory-design-course/blob/main/instructor/05-Manipulating-models.ipynb) | 10 s |
| 06 | Single-gene deletions, essentiality per carbon source | [student](https://colab.research.google.com/github/lab-biotek-bio-ugm/cell-factory-design-course/blob/main/student/06-Gene-essentiality.ipynb) · [instructor](https://colab.research.google.com/github/lab-biotek-bio-ugm/cell-factory-design-course/blob/main/instructor/06-Gene-essentiality.ipynb) | 10 s |
| 07 | Molar, C-mol and mass yields; growth vs. yield | [student](https://colab.research.google.com/github/lab-biotek-bio-ugm/cell-factory-design-course/blob/main/student/07-Theoretical-maximum-yields.ipynb) · [instructor](https://colab.research.google.com/github/lab-biotek-bio-ugm/cell-factory-design-course/blob/main/instructor/07-Theoretical-maximum-yields.ipynb) | 10 s |
| 08 | Pathway prediction with a universal reaction model | [student](https://colab.research.google.com/github/lab-biotek-bio-ugm/cell-factory-design-course/blob/main/student/08-Predict-heterologous-pathways.ipynb) · [instructor](https://colab.research.google.com/github/lab-biotek-bio-ugm/cell-factory-design-course/blob/main/instructor/08-Predict-heterologous-pathways.ipynb) | 6-8 min |
| 09 | Growth coupling, OptGene, OptKnock | [student](https://colab.research.google.com/github/lab-biotek-bio-ugm/cell-factory-design-course/blob/main/student/09-Predict-gene-knockout-strategies.ipynb) · [instructor](https://colab.research.google.com/github/lab-biotek-bio-ugm/cell-factory-design-course/blob/main/instructor/09-Predict-gene-knockout-strategies.ipynb) | 2 min |
| 10 | FSEOF, differential FVA | [student](https://colab.research.google.com/github/lab-biotek-bio-ugm/cell-factory-design-course/blob/main/student/10-Predict-gene-expression-modulation-targets.ipynb) · [instructor](https://colab.research.google.com/github/lab-biotek-bio-ugm/cell-factory-design-course/blob/main/instructor/10-Predict-gene-expression-modulation-targets.ipynb) | 10 s |
| 11 | Dynamic FBA of a glucose/xylose batch culture | [student](https://colab.research.google.com/github/lab-biotek-bio-ugm/cell-factory-design-course/blob/main/student/11-dynamic-fba.ipynb) · [instructor](https://colab.research.google.com/github/lab-biotek-bio-ugm/cell-factory-design-course/blob/main/instructor/11-dynamic-fba.ipynb) | 15 s |
| 12 | Enzyme-constrained model + proteomics | [student](https://colab.research.google.com/github/lab-biotek-bio-ugm/cell-factory-design-course/blob/main/student/12-Proteomics-Integration.ipynb) · [instructor](https://colab.research.google.com/github/lab-biotek-bio-ugm/cell-factory-design-course/blob/main/instructor/12-Proteomics-Integration.ipynb) | 2 min |

\* Instructor version, measured on a Linux workstation with GLPK; expect longer on smaller machines. On Colab, the first cell
also installs the dependencies (about 1-2 min).

## Run on Google Colab

Click a Colab link above and run the first (setup) cell. It clones this repository into
`/content/cell-factory-design-course`, installs `requirements.txt` and enables Colab's widget
manager (needed for Escher maps). Save a copy to your Drive (*File → Save a copy in Drive*) to keep
your work.

To get the whole course at once, open
[colab-setup.ipynb](https://colab.research.google.com/github/lab-biotek-bio-ugm/cell-factory-design-course/blob/main/colab-setup.ipynb)
and run its one cell. It copies the repository into `MyDrive/cell-factory-design-course`. Then open the
notebooks from Google Drive (right-click → *Open with* → *Google Colaboratory*), and your changes save
automatically. The setup cell still runs in every notebook, because each Colab notebook runs on its own fresh machine.

## Run locally

```bash
mamba env create -f environment.yml        # or: conda env create -f environment.yml
mamba activate cell-factory-design-course
jupyter lab                                 # open student/ or instructor/
```

`requirements-lock.txt` pins every package to the exact versions the notebooks were last tested with
(Python 3.12, linux-64): `pip install -r requirements-lock.txt`.

## Maintaining the course

```bash
make refs      # render [@key] citations in instructor/ from references.bib
make student   # refs + regenerate student/ from instructor/
make test      # execute all instructor and student notebooks (outputs go to a temp dir)
make check     # refs rendered, student/ in sync, no outputs committed (what CI checks)
make clean     # clear all outputs in place; commit notebooks without outputs
```

Edit only `instructor/`: tag solution cells with `solution`, cite with `[@key]` (keys from
`references.bib`; each citing notebook has one markdown cell tagged `references`), then run
`make student`. CI (`.github/workflows/notebooks.yml`) runs `make check` and executes every
notebook, instructor and student version, on each push, pull request and weekly.

### Compatibility notes

- **cameo** (used in notebooks 04, 08, 09, 10) had its last release in 2021. `cameo_compat.py`
  patches it for Python 3.12, cobra 0.32, pandas 2 and IPython 9; notebooks `import cameo_compat`
  before importing cameo. `requirements.txt` also pins `numpy<2.4` and `setuptools<81` for cameo.
- **Solver**: the notebooks use GLPK, which ships with optlang. The original course used CPLEX; the
  MILP-based methods (pathway prediction, OptKnock) are much slower with GLPK. Notebook 12 switches
  GLPK to dual simplex because the default primal simplex stalls on the enzyme-constrained model.
- **Dynamic FBA** (notebook 11) used the `dfba` package, which has no builds for current Python. It
  is re-implemented with cobra and `scipy.integrate.solve_ivp`; results match the original closely.

## Data

| File | Used in | Source |
|------|---------|--------|
| `iJO1366.xml.gz`, `e_coli_core.xml.gz`, `iMM904.xml.gz` | 01-10 | [BiGG Models](https://bigg.ucsd.edu), older exports (they differ from today's BiGG files) |
| `iJR904.xml.gz` | 11 | [BiGG Models](https://bigg.ucsd.edu/models/iJR904), downloaded 2026-09-30 |
| `eciML1515.xml.gz` | 12 | GECKO enzyme-constrained iML1515 |
| `ecoli_proteomics_schmidt2016_S5_ren.tsv`, `ecoli_details_schmidt2016_S23.tsv` | 12 | Schmidt et al. 2016, Nat Biotechnol 34:104, supplementary tables |

