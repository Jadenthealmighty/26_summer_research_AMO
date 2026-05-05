"""
src/plot_utils.py
-----------------
Matplotlib helpers for consistent, publication-ready figures.
"""

import matplotlib.pyplot as plt
import matplotlib as mpl
from pathlib import Path
from datetime import datetime

FIGURES = Path(__file__).resolve().parent.parent / "results" / "figures"


def set_style(font_size: int = 12, usetex: bool = False):
    """Apply a clean, publication-friendly style."""
    mpl.rcParams.update({
        "font.size": font_size,
        "axes.labelsize": font_size,
        "axes.titlesize": font_size + 1,
        "legend.fontsize": font_size - 1,
        "xtick.labelsize": font_size - 1,
        "ytick.labelsize": font_size - 1,
        "axes.spines.top": False,
        "axes.spines.right": False,
        "figure.dpi": 120,
        "savefig.dpi": 300,
        "text.usetex": usetex,
    })




def save_figure(fig: plt.Figure, name: str, fmt: str = "pdf") -> Path:
    """Save a figure with a datestamped filename to results/figures/.

    Parameters
    ----------
    fig  : matplotlib Figure
    name : str   Descriptive name, e.g. 'cavity_linewidth_fit'
    fmt  : str   File format: 'pdf', 'png', or 'svg'
    """
    FIGURES.mkdir(parents=True, exist_ok=True)
    date = datetime.today().strftime("%Y-%m-%d")
    path = FIGURES / f"{date}_{name}.{fmt}"
    fig.savefig(path, bbox_inches="tight")
    print(f"Figure saved → {path}")
    return path
