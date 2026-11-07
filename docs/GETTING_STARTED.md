# Getting started

[Course overview](../README.md) · [Dataset card](DATASET_CARD.md) · [Part A assignment guide](COURSEWORK_GUIDE.md) · [Assessment overview](ASSESSMENT_OVERVIEW.md)

This guide explains how to obtain the coursework dataset, verify its integrity and inspect the images and labels. Use either Google Colab or a local Python environment. Both routes use the same versioned archive and the same exploration notebook.

The released dataset contains 2,000 shape-classification images and 2,000 force-estimation images, together with labels and submission examples. The download is 37,441,246 bytes, approximately 37.44 MB. The extracted folder is named `Tactile_DL_2027`.

## 1. Review the coursework requirements

Read the current **Simplified Handbook, full handbook and briefing on Canvas** before starting. The older full handbook retained in this repository differs from the newly provided documents; consult [source alignment](SOURCE_ALIGNMENT.md) and official Canvas clarifications. The [Part A assignment guide](COURSEWORK_GUIDE.md) describes the experiments, while the [assessment overview](ASSESSMENT_OVERVIEW.md) consolidates dates and deliverables.

The exploration notebook supports data inspection. Model development, comparison and evaluation form the assessed work described in the handbook.

## 2. Choose a computing environment

### Google Colab

[![Open the exploration notebook in Google Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/dianzdd123/2026-2027-Deep-Learning-Final-Coursework-Part-A/blob/main/notebooks/01_explore_dataset.ipynb)

Open the notebook, save a working copy and run its cells in order. It downloads the dataset, checks the archive's SHA-256 checksum, extracts the files and displays labelled examples. Data loading and inspection run on CPU; a GPU is useful for the subsequent model-training work.

To use a new Colab notebook, run the following setup cell once in a fresh runtime:

```python
!git clone -q https://github.com/dianzdd123/2026-2027-Deep-Learning-Final-Coursework-Part-A.git /content/coursework-part-a
!python /content/coursework-part-a/scripts/download_dataset.py --output-dir /content
```

Set the dataset path in subsequent cells:

```python
from pathlib import Path
import pandas as pd

ROOT = Path('/content/Tactile_DL_2027')
shape = pd.read_csv(ROOT / 'shape_classification/labels.csv')
force = pd.read_csv(ROOT / 'force_regression/labels.csv')

print(shape.groupby(['class_id', 'class_name']).size())
print(force[['fx', 'fy', 'fz']].describe())
```

Files stored in the Colab runtime may be lost when the runtime resets. Preserve your own notebooks, split definitions, experiment records and model checkpoints in persistent storage. Download the dataset again, or restore a verified copy, when starting a new runtime.

### Local Python, VS Code or Jupyter

Use Python 3.10 or newer in a project environment. Run these commands from a terminal:

```bash
git clone https://github.com/dianzdd123/2026-2027-Deep-Learning-Final-Coursework-Part-A.git
cd 2026-2027-Deep-Learning-Final-Coursework-Part-A
python -m pip install -r requirements.txt
python scripts/download_dataset.py
python scripts/verify_dataset.py --data Tactile_DL_2027
```

Open [`01_explore_dataset.ipynb`](../notebooks/01_explore_dataset.ipynb) in VS Code with the Jupyter extension, or in an existing Jupyter environment. Select the Python environment in which you installed the requirements and run the notebook in order.

The repository requirements cover data exploration and integrity checks. PyTorch is a separate dependency for the supplied model example; consult [`example_submission/README.md`](../example_submission/README.md) before running it. An exploration environment and an assessed model environment serve different purposes, so record the dependencies required by your own submission.

### Use an existing archive

Download [`Tactile_DL_2027.zip`](https://github.com/dianzdd123/2026-2027-Deep-Learning-Final-Coursework-Part-A/releases/download/v1.0.2/Tactile_DL_2027.zip) directly, or use an existing copy. The helper verifies the archive before extraction:

```bash
python scripts/download_dataset.py --archive /path/to/Tactile_DL_2027.zip
```

The helper does not overwrite an existing extracted folder. To check that folder, run:

```bash
python scripts/verify_dataset.py --data Tactile_DL_2027
```

To create a separate extraction, provide a different parent directory with `--output-dir`. GitHub's **Code → Download ZIP** contains the repository files, while the complete image dataset is distributed through the release link above.

## 3. Locate the data and labels

Paths below are relative to the extracted `Tactile_DL_2027/` folder.

| Path | Contents |
|---|---|
| `shape_classification/images/` | Shape images organised in ten class folders |
| `shape_classification/classes.csv` | Authoritative mapping between class names and IDs |
| `shape_classification/labels.csv` | One row per shape image: `filename,class_name,class_id` |
| `force_regression/images/` | Press and shear images for 1,000 contacts |
| `force_regression/labels.csv` | One row per force image: `filename,contact_id,is_shear,fx,fy,fz` |

Each CSV's `filename` is relative to its task directory. For example, `images/contact_0001.jpg` resolves beneath `Tactile_DL_2027/force_regression/`. The copies in [`metadata/`](../metadata/) are provided for browsing; image files are in the extracted dataset.

For force data, `is_shear=0` denotes a press observation and `is_shear=1` denotes the paired shear observation. Forces are in newtons. In the supplied sensor convention, negative `fz` indicates pressing into the sensor. Use the [dataset card](DATASET_CARD.md) for the complete schema, class mapping, measured ranges and limitations.

## 4. Inspect the dataset before training

The verification utility checks image files, label mappings, class counts and contact pairing. The exploration notebook complements these checks with visual inspection and descriptive statistics.

Confirm that you can:

1. Load the ten-class mapping and associate each shape image with its label.
2. Display a press/shear pair with the same `contact_id` and interpret its force components.
3. Inspect class balance and the force distributions, including the separate press and shear subsets.
4. Resolve every image path from its label file and understand the distinction between an image and a physical contact.

These checks establish that the data can be used as intended. Successful loading alone does not establish that an experimental split is valid.

## 5. Establish the experimental protocol

Create the required 60% training, 20% validation and 20% test splits before fitting data-dependent preprocessing. Stratify shape images by class. For force estimation, split by `contact_id` so that both observations of each contact remain together.

Save the split membership and random seed. Fit preprocessing using training data, select models using validation data, and reserve the test set for final evaluation. The [Part A assignment guide](COURSEWORK_GUIDE.md) specifies the required architecture comparisons, evaluation measures and reporting evidence, including the permitted declared final refit after model selection.

The supplied training script uses all released images to demonstrate the submission interface. Its checkpoints therefore do not provide held-out coursework results. Use your own experiments and valid splits for the assessed analysis.

## Archive integrity

The downloader retrieves the archive from release `v1.0.2` and verifies both file size and SHA-256 before extraction. Its contents remain identical to dataset version `1.0.0`:

```text
1a1620e4695b220043318e7b209202940b930fcf82f69b4f761213255c6b4ca5  Tactile_DL_2027.zip
```

The checksum is also available in [`checksums.sha256`](../checksums.sha256). The [dataset card](DATASET_CARD.md) describes the release audit and the [machine-readable validation record](validation.json) reports its results.

## Common setup issues

| Observation | Resolution |
|---|---|
| Repository downloaded, but no image files are present | Download the separate dataset archive using the release link or helper script. |
| `Dataset folder already exists` | Verify the existing folder, or choose a new `--output-dir` for a separate extraction. |
| Checksum or archive-size mismatch | Obtain a fresh copy of the versioned release asset before extraction. |
| An image path cannot be resolved | Resolve the CSV filename beneath its extracted task directory. |
| A notebook cannot import an installed package | Select the kernel associated with the environment in which the package was installed. |
| Colab data is missing after a reset | Download the dataset again or restore a verified copy from persistent storage. |

Report access problems or documentation errors through [GitHub Issues](https://github.com/dianzdd123/2026-2027-Deep-Learning-Final-Coursework-Part-A/issues). Use the module's designated channels for assessment questions, and exclude assessed solutions and personal student information from public issues.
