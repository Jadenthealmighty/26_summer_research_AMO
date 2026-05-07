# Quantum Optics Research — Summer 2025

Undergraduate research repository for data analysis and simulation work in a quantum optics lab.

---

## Repository Structure

```
ROP_code/
│
├── data/
│   ├── csv_raw/      # csv files from recorded data
│   └── np_raw/      # numpy files for recorded data 
│
├── notebooks/        # Jupyter notebooks for analysis and exploration
│
├── src/              # Reusable Python modules and scripts
│
├── results/
│   ├── figures/      # Saved plots and figures (.png, .pdf, .svg)
│   └── reports/      # Written summaries, exports, or findings
│
├── environment/      # Environment and dependency files
│
├── README.md
├── .gitignore
└── requirements.txt
```

---

## Setup

### 1. Clone the repo
```bash
git clone <your-repo-url>
cd quantum-optics-research
```

### 2. Create and activate the virtual environment
```bash
python -m venv .venv
source .venv/bin/activate      # macOS / Linux
# .venv\Scripts\activate       # Windows
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Register the kernel with Jupyter
```bash
python -m ipykernel install --user --name=quantum-optics --display-name "Python (quantum-optics)"
```

### 5. Launch Jupyter
```bash
jupyter lab
```

---

## Data Conventions

- **Raw data is read-only.** Never modify files under `data/raw/`. If processing is needed, save results to `data/processed/`.
- **File naming:** use descriptive, date-prefixed names, e.g. `2025-06-01_cavity_transmission_run3.csv`.
- **Numpy arrays:** save with `np.save()` (`.npy`) or `np.savez_compressed()` (`.npz`) for multi-array files.
- **CSV files:** include a header row and document units in the filename or a companion `_meta.txt` file.

---

## Notebook Conventions

- One notebook per experiment or analysis topic.
- Keep notebooks reproducible: restart kernel and run all cells before saving.
- Use the `src/` modules for any logic reused across notebooks.

---

## Dependencies

See `requirements.txt` for the full list. Core packages:

| Package | Purpose |
|---|---|
| `numpy` | Array math and data storage |
| `scipy` | Signal processing, fitting, stats |
| `matplotlib` | Plotting |
| `pandas` | Tabular data / CSV handling |
| `jupyterlab` | Interactive notebooks |
| `ipykernel` | Jupyter kernel support |
| `lmfit` | Curve fitting with parameter bounds |
| `uncertainties` | Error propagation |
| `h5py` | HDF5 file support (large datasets) |

---

## Notes

- MicroPython / Arduino code will live in a future `firmware/` directory.
- Add large data files to `.gitignore` — use cloud storage or a data registry for anything over ~50 MB.
