# Tactile Deep Learning Coursework 2027 — Dataset

This dataset accompanies the Deep Learning final project. It contains images from a
**GelSight** vision-based tactile sensor and supports two tasks:

| Task | Type | Sensor variant | Images | Target |
|---|---|---|---|---|
| **Task A – Shape classification** | Classification (10 classes) | GelSight **without** markers | 2,000 | Shape of the object pressed into the sensor |
| **Task B – Force estimation** | Regression (3 outputs) | GelSight **with** markers | 2,000 (1,000 contacts) | Contact force `fx, fy, fz` in newtons |

The data is a curated subset of the **TacVerse** multisensor tactile dataset (see
[Section 6](#6-data-source-and-citation)).
All images have been resized to **320 × 240 px (RGB, JPEG)**, so the full dataset fits
comfortably in Google Colab.

---

## 1. Background

A GelSight sensor is a soft, elastomeric gel pad that is illuminated from the inside and
filmed by a camera. When an object presses into the gel, the gel deforms and the camera
sees the shape and texture of the contact as a change in colour and shading.

- **Without markers** (Task A): the gel surface is plain, so the image shows the
  *geometry* of the contact — ideal for recognising shapes.
- **With markers** (Task B): a grid of black dots is printed on the gel. When the object
  pushes or drags the gel, the dots move. The dot displacement encodes the *shear* (in-plane)
  force, and the size and shading of the contact encode the *normal* force.

Most of each image is "empty" gel; the informative contact region is often small and can
appear anywhere on the pad. Keep this in mind when you choose a resolution, augmentations
and architectures.

---

## 2. Folder structure

```
Tactile_DL_2027/
├── README.md
├── example_submission/             # template showing the required submission format (Section 4.3)
├── shape_classification/
│   ├── classes.csv                 # class_name -> class_id mapping
│   ├── labels.csv                  # one row per image
│   └── images/
│       ├── cylinder/cylinder_0012.jpg
│       ├── dots/...
│       └── ... (10 class folders, 200 images each)
└── force_regression/
    ├── labels.csv                  # one row per image
    └── images/
        ├── contact_0001.jpg        # normal press
        ├── contact_0001_shear.jpg  # same contact, after a lateral (shear) move
        └── ...
```

### 2.1 `shape_classification/labels.csv`

| column | description |
|---|---|
| `filename` | Path relative to `shape_classification/`, e.g. `images/hexagon/hexagon_0042.jpg` |
| `class_name` | One of the 10 class names below |
| `class_id` | Integer label `0–9` (see `classes.csv`) |

Classes (200 images each, perfectly balanced):

| id | name | id | name |
|---|---|---|---|
| 0 | cylinder | 5 | rectangle |
| 1 | dots | 6 | ring |
| 2 | hexagon | 7 | small_sphere |
| 3 | line | 8 | triangle |
| 4 | moon | 9 | wave |

All images of a class come from the same indenter pressed into the sensor, so
many images within a class look very similar.

### 2.2 `force_regression/labels.csv`

| column | description |
|---|---|
| `filename` | Path relative to `force_regression/`, e.g. `images/contact_0001_shear.jpg` |
| `contact_id` | ID of the physical contact (`1–1000`). Each contact has **two** images. |
| `is_shear` | `0` = pure normal press, `1` = same press followed by a lateral (shear) displacement |
| `fx`, `fy` | Tangential (shear) force components, newtons |
| `fz` | Normal force, newtons. **Negative = pressing into the sensor** (sensor coordinate frame) |

Force ranges in the full source recording (your subset has a very similar distribution):

| | `fx` (N) | `fy` (N) | `fz` (N) |
|---|---|---|---|
| normal press (`is_shear=0`) | mean −0.07, std 0.06 | mean −0.01, std 0.03 | mean −0.73, std 0.47 |
| shear (`is_shear=1`) | mean 0.01, std 0.38 | mean −0.03, std 0.42 | mean −0.69, std 0.46 |
| overall min / max | −1.34 / 1.40 | −1.37 / 1.28 | −1.99 / 0.01 |

Note that for normal presses `fx` and `fy` are close to zero; large shear forces only
appear in the `_shear` images. The three targets also have different scales, so consider
standardising each target before training.

---

## 3. Getting started in Google Colab

`Tactile_DL_2027.zip` (about 37 MB) is attached to the **Releases** page of
<https://github.com/LannWei/Deep-Learning-CourseWork-2027/releases>. Put it into Colab
with **one** of the three options below.

**Option 1 – Download directly in Colab (quickest).** Nothing to upload, but you need to
run it again every time the Colab session restarts.

```python
!wget -q -O Tactile_DL_2027.zip https://github.com/LannWei/Deep-Learning-CourseWork-2027/releases/latest/download/Tactile_DL_2027.zip
!unzip -q -o Tactile_DL_2027.zip -d /content
```

**Option 2 – Google Drive.** Download the zip from the Releases page to your computer once,
then keep it in your Drive. You do not need to download it again after a restart.

1. Upload `Tactile_DL_2027.zip` to the top level of your Google Drive ("My Drive").
2. In Colab, run:

```python
from google.colab import drive
drive.mount('/content/drive')
!unzip -q -o /content/drive/MyDrive/Tactile_DL_2027.zip -d /content
```

**Option 3 – Upload directly to the Colab session.** This is quicker to set up, but the
files are deleted when the session ends.

```python
from google.colab import files
files.upload()   # select Tactile_DL_2027.zip in the dialog
!unzip -q -o Tactile_DL_2027.zip -d /content
```

Then read the labels:

```python
import pandas as pd
from pathlib import Path

ROOT = Path("/content/Tactile_DL_2027")
shape_df = pd.read_csv(ROOT / "shape_classification/labels.csv")
force_df = pd.read_csv(ROOT / "force_regression/labels.csv")
print(shape_df.class_name.value_counts())
print(force_df[["fx", "fy", "fz"]].describe())
```

A minimal PyTorch `Dataset`:

```python
import torch
from PIL import Image
from torch.utils.data import Dataset

class TactileDataset(Dataset):
    def __init__(self, df, root, targets, transform=None):
        self.df, self.root, self.targets, self.transform = df.reset_index(drop=True), Path(root), targets, transform

    def __len__(self):
        return len(self.df)

    def __getitem__(self, i):
        row = self.df.iloc[i]
        img = Image.open(self.root / row.filename).convert("RGB")
        if self.transform:
            img = self.transform(img)
        y = torch.tensor(row[self.targets].values.astype("float32"))
        return img, y

# Task A: targets=["class_id"]  (cast to long and squeeze for CrossEntropyLoss)
# Task B: targets=["fx", "fy", "fz"]
```

Remember to enable a GPU: *Runtime → Change runtime type → GPU*.

---

## 4. What you need to do with the data

### 4.1 Train / validation / test split — **you** create it

The released data is **not** pre-split. Split it yourself into **60 % training, 20 %
validation and 20 % test**, and fix the random seed so your results are reproducible.

- **Task A:** use a **stratified** split so that every class keeps the same proportion in
  all three sets (e.g. `sklearn.model_selection.train_test_split(..., stratify=y)`).
- **Task B:** split **by `contact_id`, not by image** (e.g. `GroupShuffleSplit`). The normal
  and shear images of one contact share the same press position and depth. If one ends up in
  training and the other in testing, your test score will be over-optimistic (data leakage).

Report the size of each split, and the class or force distribution in each split, in your
report.

### 4.2 Evaluation metrics

- **Task A:** Accuracy, Precision, Recall, F1-score (macro-averaged) and the confusion matrix.
- **Task B:** RMSE for **each** axis (`fx`, `fy`, `fz`) and the overall RMSE, in newtons.
  MAE and R² are optional extras. In addition, the **tangential-force analysis** below is
  **required**.

#### Required: tangential (shear) force error analysis

The tangential force `(fx, fy)` is the hardest part of Task B. In normal-press images it is
almost zero; in shear images it reaches about ±1.4 N. A model that ignores shear can still
look good on the overall RMSE, because half of the images have `fx ≈ fy ≈ 0`. You must
therefore analyse the tangential error **separately**:

1. **Per-subset table.** On your test split, report `RMSE_fx`, `RMSE_fy`, `RMSE_fz` and the
   tangential vector RMSE `RMSE_t` (defined below). Report them separately for normal-press
   images (`is_shear = 0`) and for shear images (`is_shear = 1`).
2. **Trivial baseline.** In the same table, report the same metrics for a baseline that always
   predicts the training-set mean force. This shows how much of the tangential force your
   model has actually learned.
3. **Prediction plots.** For the shear images, plot predicted vs. true `fx` and predicted vs.
   true `fy`, with the `y = x` line.
4. **Discussion.** Compare the tangential error with the normal-force error and explain the
   difference. Which visual cues (e.g. marker displacement) does your model need in order to
   estimate shear? Show and discuss your worst tangential predictions.

*Optional:* for shear images with a true tangential magnitude above 0.2 N, report the
angular error between the predicted and true tangential force directions.

Definitions (use exactly these so results are comparable):

```python
import numpy as np

def tangential_metrics(df, pred):
    """df: test rows with columns fx, fy, fz, is_shear; pred: array (N, 3) of fx, fy, fz in newtons."""
    true = df[["fx", "fy", "fz"]].to_numpy()
    err = pred - true
    rows = {}
    for name, mask in [("press", df.is_shear.eq(0).to_numpy()), ("shear", df.is_shear.eq(1).to_numpy()), ("all", np.ones(len(df), bool))]:
        e = err[mask]
        rows[name] = {
            "RMSE_fx": np.sqrt(np.mean(e[:, 0] ** 2)),
            "RMSE_fy": np.sqrt(np.mean(e[:, 1] ** 2)),
            "RMSE_fz": np.sqrt(np.mean(e[:, 2] ** 2)),
            # tangential vector error: length of the (fx, fy) error vector
            "RMSE_t": np.sqrt(np.mean(e[:, 0] ** 2 + e[:, 1] ** 2)),
        }
    return rows
```

### 4.3 Hidden test set

In addition to your own test split, the teaching team keeps a **separate, unreleased test
set** for each task, recorded with the same sensors and preprocessed in the same way
(320 × 240 RGB JPEG). Your submitted models will be evaluated on it.

Your models are graded **automatically** by a script. Submissions that do not follow the
interface below cannot be scored.

#### Submission folder

```
<your_student_id>/
├── predict.py          # REQUIRED – runs inference for both tasks
├── requirements.txt    # optional – extra pip packages not pre-installed in Colab
├── <weights files>     # e.g. shape_model.pt, force_model.pt (any names/format you like)
└── <helper modules>    # optional – any .py files that predict.py imports
```

#### `predict.py` interface

The grader runs these commands **from inside your submission folder**:

```bash
python predict.py --task shape --images <IMAGE_DIR> --out <OUT_CSV>
python predict.py --task force --images <IMAGE_DIR> --out <OUT_CSV>
```

- `<IMAGE_DIR>` is a **flat** folder of `.jpg` files: no class sub-folders and no labels.
  The files have anonymous names (`test_0001.jpg`, …) and are 320 × 240 RGB, exactly like
  the released data.
- `<OUT_CSV>` must contain **one row per image** with these columns:
  - `--task shape`: `filename, class_id` (integer `0–9`, see `classes.csv`)
  - `--task force`: `filename, fx, fy, fz` (newtons, **original scale**, not standardised)
  
  `filename` is the file name only, e.g. `test_0001.jpg`.
- `predict.py` must contain (or import from your own files) the model definition, all
  preprocessing, and the code that loads your weights. Load weights relative to the script,
  e.g. `Path(__file__).parent / "shape_model.pt"`. Do not use absolute paths such as
  `/content/drive/...`.
- Use a GPU if one is available, but the script must also run on CPU.
- Task B images are **not** marked as normal or shear. Your model must work from the image
  alone and must not rely on the filename, `contact_id` or `is_shear`.
- Keep the total submission size under **200 MB**.

#### `requirements.txt`

List only packages that are **not** already in Google Colab, one per line with a pinned
version (e.g. `timm==1.0.9`). They are installed with `pip install -r requirements.txt`
before your script runs. Do not list `torch` or `torchvision`: the Colab versions are used.

#### Example submission and self-check

[`example_submission/`](example_submission/) is a complete, working submission with a small
baseline CNN. Use it as a template.
- [`predict.py`](example_submission/predict.py) shows the required interface.
- [`train_example.py`](example_submission/train_example.py) shows how its weights were
  produced. It trains on all the data without a split, which is for demonstration only and
  is **not** acceptable in your coursework.

**Before you submit**, test your folder in a fresh Colab runtime:

```python
# copy a few released images into flat folders, the same layout the grader uses
import shutil
from pathlib import Path
data = Path("/content/Tactile_DL_2027")
for task, pattern in [("shape", "shape_classification/images/*/*.jpg"), ("force", "force_regression/images/*.jpg")]:
    dst = Path(f"/content/check_{task}")
    dst.mkdir(exist_ok=True)
    for f in sorted(data.glob(pattern))[::100]:   # every 100th image
        shutil.copy(f, dst)

%cd /content/<your_student_id>
!pip install -q -r requirements.txt
!python predict.py --task shape --images /content/check_shape --out /content/pred_shape.csv
!python predict.py --task force --images /content/check_force --out /content/pred_force.csv

import pandas as pd
print(pd.read_csv("/content/pred_shape.csv").head())
print(pd.read_csv("/content/pred_force.csv").head())
```

Both commands must finish without errors, and each CSV must have one row per image with the
columns listed above.

---

## 5. Tips

- 320 × 240 is not square. You can resize to 224 × 224, pad, crop or keep the aspect ratio,
  but justify your choice. Small contacts may vanish if you downsample too much.
- Think about which augmentations are *physically valid*:
  - **Task A:** flips and rotations are fine for most shapes.
  - **Task B:** flipping or rotating an image changes the direction of `fx`/`fy`, so the
    labels must be transformed too, or such augmentations avoided.
- Normalise pixel intensities (e.g. ImageNet mean/std if you use pretrained weights), and
  standardise the force targets for regression.

---

## 6. Data source and citation

This dataset is a subset of TacVerse. If you use it, please cite:

> L. Wei, G. Khurana, S. Bhouri, W. Hong, Z. Xin, Q. Cong, W. Fan, Y. Xiang and D. Zhang,
> "TacVerse: A Multisensor Dataset and Benchmark for Cross-Sensor Vision-Based Tactile
> Perception," *Advanced Robotics Research*, 2026. doi:
> [10.1002/adrr.70169](https://doi.org/10.1002/adrr.70169)

```bibtex
@article{wei2026tacverse,
  title   = {TacVerse: A Multisensor Dataset and Benchmark for Cross-Sensor Vision-Based Tactile Perception},
  author  = {Wei, Lan and Khurana, Gurmeher and Bhouri, Sirine and Hong, Wenhao and Xin, Zeyuan and Cong, Qingzheng and Fan, Wen and Xiang, Yanzheng and Zhang, Dandan},
  journal = {Advanced Robotics Research},
  year    = {2026},
  doi     = {10.1002/adrr.70169}
}
```

- Coursework repository: <https://github.com/LannWei/Deep-Learning-CourseWork-2027>
  (dataset zip under [Releases](https://github.com/LannWei/Deep-Learning-CourseWork-2027/releases))
- Dataset code: <https://github.com/LannWei/Tactile_Database>

Subsets used:

- Task A is a subset of `Shape_Classification/GelSight (no marker)`.
- Task B is a subset of `Force_Regression/GelSight (with marker)`.
