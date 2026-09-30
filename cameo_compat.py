"""Make cameo 0.13.6 (last release, 2021, unmaintained) import on Python 3.12 + cobra 0.32.

Import this *before* importing cameo:

    import cameo_compat  # noqa: F401
"""
import collections
import collections.abc

import cobra.manipulation.delete

# grako (cameo -> gnomic -> grako) still uses aliases removed in Python 3.10.
for _name in ("Mapping", "MutableMapping", "Sequence", "Iterable", "Callable"):
    setattr(collections, _name, getattr(collections.abc, _name))


def find_gene_knockout_reactions(model, gene_list):
    """Reactions whose GPR evaluates to False when `gene_list` is knocked out (removed in cobra 0.25)."""
    knockouts = {getattr(g, "id", g) for g in gene_list}
    reactions = {r for g in knockouts for r in model.genes.get_by_id(g).reactions}
    return [r for r in reactions if not r.gpr.eval(knockouts)]


cobra.manipulation.delete.find_gene_knockout_reactions = find_gene_knockout_reactions

# cameo/__init__.py calls `get_ipython().magic(...)`, removed in IPython 9.
try:
    from IPython.core.interactiveshell import InteractiveShell
except ImportError:
    pass
else:
    if not hasattr(InteractiveShell, "magic"):
        InteractiveShell.magic = lambda self, line: self.run_line_magic(*(line.split(" ", 1) + [""])[:2])

# Silence cameo's pandas-3 FutureWarning (ChainedAssignmentError) and pkg_resources notice, which students cannot act on.
import warnings

warnings.filterwarnings("ignore", category=FutureWarning, module="cameo")
warnings.filterwarnings("ignore", message="pkg_resources is deprecated", category=UserWarning)

# pandas 2 removed Series.iteritems and DataFrame.append, both used throughout cameo.
import pandas

pandas.Series.iteritems = pandas.Series.items
pandas.DataFrame.append = lambda self, other, ignore_index=False: (
    other.copy() if self.empty else pandas.concat([self, other], ignore_index=ignore_index))

# Upstream bug: DifferentialFVAResult.plot() without an index forgets to pass the plotter on.
import numpy
from cameo.strain_design.deterministic.flux_variability_based import DifferentialFVAResult

_differential_fva_plot = DifferentialFVAResult.plot


def _plot(self, plotter, index=None, *args, **kwargs):
    if index is not None:
        return _differential_fva_plot(self, plotter, index, *args, **kwargs)
    unique = numpy.logical_not(self.solutions.duplicated(["biomass", "production"]))
    points = list(self.solutions.loc[unique, ["biomass", "production"]].itertuples(index=False))
    self.phase_plane.plot(plotter, title=kwargs.get("title") or "DifferentialFVA Result", points=points,
                          points_colors=["red"] * len(points))


DifferentialFVAResult.plot = _plot

# Upstream bug: plot_production_envelopes() forgets to pass the plotter on.
from cameo.strain_design.pathway_prediction.pathway_predictor import PathwayPredictions


def _plot_production_envelopes(self, plotter, model, objective=None, title=None):
    for i, pathway in enumerate(self.pathways):
        pathway.production_envelope(model, objective=objective).plot(plotter, title="Pathway %i" % (i + 1))


PathwayPredictions.plot_production_envelopes = _plot_production_envelopes
