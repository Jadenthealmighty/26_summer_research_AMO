"""
src/data_utils.py
-----------------
Utility functions for loading and saving experimental data.
"""

import numpy as np
import pandas as pd
from pathlib import Path
from datetime import datetime


REPO_ROOT = Path(__file__).resolve().parent.parent
DATA_RAW = REPO_ROOT / "data" / "raw"
DATA_PROCESSED = REPO_ROOT / "data" / "processed"
FIGURES = REPO_ROOT / "results" / "figures"



def save_npy(array: np.ndarray, name: str, processed: bool = False) -> Path:
    """Save a numpy array with a datestamped filename.

    Parameters
    ----------
    array : np.ndarray
    name  : str   Descriptive name, e.g. 'cavity_transmission_run3'
    processed : bool  If True, save to data/processed instead of data/raw

    Returns
    -------
    Path  The full path where the file was saved.
    """
    folder = DATA_PROCESSED if processed else DATA_RAW
    folder.mkdir(parents=True, exist_ok=True)
    date = datetime.today().strftime("%Y-%m-%d")
    path = folder / f"{date}_{name}.npy"
    np.save(path, array)
    print(f"Saved → {path}")
    return path


def save_csv(df: pd.DataFrame, name: str, processed: bool = False) -> Path:
    """Save a DataFrame as a datestamped CSV."""
    folder = DATA_PROCESSED if processed else DATA_RAW
    folder.mkdir(parents=True, exist_ok=True)
    date = datetime.today().strftime("%Y-%m-%d")
    path = folder / f"{date}_{name}.csv"
    df.to_csv(path, index=False)
    print(f"Saved → {path}")
    return path



def load_npy(filename: str, processed: bool = False) -> np.ndarray:
    """Load a .npy file from data/raw or data/processed."""
    folder = DATA_PROCESSED if processed else DATA_RAW
    path = folder / filename
    return np.load(path)


def load_csv(filename: str, processed: bool = False, **kwargs) -> pd.DataFrame:
    """Load a CSV from data/raw or data/processed."""
    folder = DATA_PROCESSED if processed else DATA_RAW
    path = folder / filename
    return pd.read_csv(path, **kwargs)


def list_data_files(folder: str = "raw", extension: str = "*") -> list[Path]:
    """List all data files in a folder matching an extension glob.

    Examples
    --------
    list_data_files("raw", "*.csv")
    list_data_files("processed", "*.npy")
    """
    base = DATA_RAW if folder == "raw" else DATA_PROCESSED
    return sorted(base.glob(extension))
