# Setup

[Home](../README.md) · [Simplified handbook](COURSEWORK_GUIDE.md)

## Google Colab

Open the [exploration notebook](https://colab.research.google.com/github/dianzdd123/2026-2027-Deep-Learning-Final-Coursework-Part-A/blob/main/notebooks/01_explore_dataset.ipynb), save a copy and run the cells in order. Select a GPU runtime for training.

For a new notebook, run:

```python
!git clone -q https://github.com/dianzdd123/2026-2027-Deep-Learning-Final-Coursework-Part-A.git /content/coursework-part-a
!python /content/coursework-part-a/scripts/download_dataset.py --output-dir /content
```

Load the labels:

```python
from pathlib import Path
import pandas as pd

root = Path("/content/Tactile_DL_2027")
shape = pd.read_csv(root / "shape_classification/labels.csv")
force = pd.read_csv(root / "force_regression/labels.csv")
```

Save notebooks, splits and checkpoints to persistent storage before the runtime resets.

## Local Python / VS Code

Use Python 3.10 or newer:

```bash
git clone https://github.com/dianzdd123/2026-2027-Deep-Learning-Final-Coursework-Part-A.git
cd 2026-2027-Deep-Learning-Final-Coursework-Part-A
python -m pip install -r requirements.txt
python scripts/download_dataset.py
```

Open `notebooks/01_explore_dataset.ipynb` with your Python environment. Install PyTorch separately if using the supplied model example.

## Manual download

[Download Tactile_DL_2027.zip](https://github.com/dianzdd123/2026-2027-Deep-Learning-Final-Coursework-Part-A/releases/download/v1.0.2/Tactile_DL_2027.zip) and extract it. **Code → Download ZIP** does not contain the images.

Each label filename is relative to its task directory; see [dataset labels](DATASET_CARD.md). If the extracted folder already exists, use it or choose another output directory.

Next: create the splits and experiments in the [simplified handbook](COURSEWORK_GUIDE.md).
