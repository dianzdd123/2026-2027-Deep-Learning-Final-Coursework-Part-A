# 2026–2027 Deep Learning Final Coursework — Part A

## Student guide to the tactile learning tasks

[Return to the repository overview](../README.md)

For the accompanying project handbook and a map of its topics to the available notebook
and coursework guidance, see [Course resources](../resources/README.md).

This guide explains the tasks, evaluation protocol and submission interface supplied with
`Tactile_DL_2027.zip`. **Part A** is the name of this part of the final coursework. The
dataset itself contains **two tasks**, called Task A and Task B in the original package:

| Dataset task | Learning problem | Inputs | Outputs |
|---|---|---|---|
| **Task A: shape classification** | Classify the shape pressed into a tactile sensor | 2,000 GelSight images without markers | One integer class ID from 0 to 9 |
| **Task B: force estimation** | Estimate the contact force from a tactile image | 2,000 GelSight images with markers, from 1,000 contacts | Three force components: `fx`, `fy`, `fz`, in newtons |

Both tasks are included in this repository's Part A dataset release. The task letters do
not refer to separate parts of the final coursework.

The requirements below come from the README supplied inside the dataset archive. The
package does not specify a submission deadline, mark allocation or complete assessment
brief; consult the course's published assessment materials for those details.

## 1. Understand what the images represent

A GelSight sensor uses a camera to observe an illuminated, deformable gel pad. Pressing
an object into the pad changes the contact's appearance. In the shape task, the gel has
no markers: changes in shading and colour reveal contact geometry. In the force task,
black markers move as the gel deforms, providing information about lateral displacement
and shear.

All released images are **320 pixels wide × 240 pixels high**, stored as RGB JPEGs.
The contact may occupy only a small part of the frame and can appear at different
positions. Consider this when choosing image resolution and preprocessing.

For force estimation, `fx` and `fy` are tangential components, and `fz` is the normal
component. A **negative `fz` means pressing into the sensor**, in the supplied sensor
coordinate frame. Keep the sign and units of the labels.

Each force contact has two images: a normal press (`is_shear = 0`) and the same press
after lateral displacement (`is_shear = 1`). These paired images share a physical
contact and must stay together when creating data splits.

## 2. Locate and load the extracted data

Download the archive using the instructions in the [repository overview](../README.md),
then extract it. The top-level dataset directory is named `Tactile_DL_2027`.

| Path inside `Tactile_DL_2027/` | Contents |
|---|---|
| `shape_classification/classes.csv` | The fixed class-name-to-ID mapping |
| `shape_classification/labels.csv` | Image paths, class names and class IDs |
| `shape_classification/images/<class_name>/` | Shape images, organised by class |
| `force_regression/labels.csv` | Image paths, contact IDs, shear indicators and force labels |
| `force_regression/images/` | Normal-press and shear images |
| `example_submission/` | Example inference script, training script, requirements file and model weights |
| `README.md` | The original instructions supplied with the archive |

In Google Colab, extracting the archive into `/content` gives
`/content/Tactile_DL_2027`. On a local computer, use the corresponding path on your
machine. The following inspection code does not train a model:

```python
from pathlib import Path
import pandas as pd

ROOT = Path("/content/Tactile_DL_2027")  # Change this for a local installation.
shape_df = pd.read_csv(ROOT / "shape_classification/labels.csv")
force_df = pd.read_csv(ROOT / "force_regression/labels.csv")

print(shape_df["class_name"].value_counts().sort_index())
print(force_df[["fx", "fy", "fz"]].describe())
```

The `filename` column is relative to the **task directory**, not to `ROOT` itself.
For example, resolve a shape image using
`ROOT / "shape_classification" / shape_df.iloc[0]["filename"]`.
Resolve force image paths in the same way using `"force_regression"`.

In Colab, enable a GPU through **Runtime → Change runtime type → GPU** when needed.
Remember that files stored only in the Colab session need to be restored when the
session ends. The original package also describes keeping the archive in Google Drive
or uploading it directly into a session.

### Shape labels

Use the supplied mapping consistently in training, evaluation and inference:

| Class ID | Class name | Released images |
|---:|---|---:|
| 0 | cylinder | 200 |
| 1 | dots | 200 |
| 2 | hexagon | 200 |
| 3 | line | 200 |
| 4 | moon | 200 |
| 5 | rectangle | 200 |
| 6 | ring | 200 |
| 7 | small_sphere | 200 |
| 8 | triangle | 200 |
| 9 | wave | 200 |

All images of a class come from the same indenter according to the supplied README.
Many images within a class therefore look similar.

## 3. Create reproducible training, validation and test splits

The released data is **not pre-split**. You must create **60% training, 20% validation
and 20% test** splits, with a fixed random seed.

| Task | Required split method | Resulting sizes for this release |
|---|---|---|
| Shape classification | Stratify by class so each class retains the same proportions | 1,200 training, 400 validation and 400 test images; 120/40/40 per class |
| Force estimation | Split by `contact_id`, keeping both images of every contact in the same split | 600/200/200 contacts, corresponding to 1,200/400/400 images |

For shapes, the supplied README suggests stratified splitting with
`sklearn.model_selection.train_test_split`. For force data, it suggests a grouped
split such as `GroupShuffleSplit`.

Splitting the force data by individual image can place the normal image of a contact in
training and its shear image in testing. This leaks information about the same contact
across the split and can make the result appear better than it is.

Report the **size of each split** and the **class or force distribution within each
split**. Keep a record of your seed and selected rows so you can reproduce the experiment.

## 4. Evaluate shape classification

Report the following metrics on your test split:

- Accuracy.
- Macro-averaged precision, recall and F1-score.
- A confusion matrix using the supplied class IDs or class names.

Retain the fixed mapping in `classes.csv`; predicted IDs must match that mapping.

## 5. Evaluate force estimation

Report **RMSE for each axis** (`fx`, `fy`, `fz`) and **overall RMSE**, all in newtons.
MAE and R² are optional additional metrics. If you standardise targets during training,
convert predictions back to their original scale before reporting these metrics or
writing the submission CSV.

### Required tangential-force analysis

Normal-press images usually have small `fx` and `fy`. A model can consequently achieve
an apparently reasonable aggregate result while learning little about the shear images.
The supplied coursework instructions therefore require the following analysis:

1. **A table separated by contact state.** On the test split, report `RMSE_fx`,
   `RMSE_fy`, `RMSE_fz` and tangential vector RMSE `RMSE_t` separately for normal-press
   images (`is_shear = 0`) and shear images (`is_shear = 1`).
2. **A training-mean baseline.** In the same table, report those metrics for a baseline
   that always predicts the training-set mean force vector.
3. **Prediction plots for shear images.** Plot predicted versus true `fx` and predicted
   versus true `fy`, including the `y = x` line.
4. **An explanation of the errors.** Compare tangential and normal-force error, discuss
   the visual cues needed to estimate shear, and show and discuss the worst tangential
   predictions.

An optional extension is to report angular error between predicted and true tangential
force directions for shear images whose true tangential magnitude exceeds **0.2 N**.

### Exact tangential metric definition

For `N` evaluated images, the tangential vector error is

$$
\mathrm{RMSE}_t = \sqrt{\frac{1}{N}\sum_{i=1}^{N}
\left[(\hat f_{x,i}-f_{x,i})^2+(\hat f_{y,i}-f_{y,i})^2\right]}.
$$

It measures the root mean squared length of the two-dimensional tangential error
vector. Use the following function from the original package without changing the
metric definitions. Predictions must be aligned with the rows of `df`.

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

## 6. Prepare the required submission interface

The supplied instructions state that the teaching team has a separate, unreleased test
set for each task, recorded using the same sensors and preprocessing. The images are
320 × 240 RGB JPEGs. Submitted models are evaluated automatically, so the command-line
interface and output columns must match the specification below.

Your submission directory, named with your student ID, contains:

| File | Requirement |
|---|---|
| `predict.py` | Required; supports inference for both tasks |
| Model weight files | Include the trained weights needed by your code; filenames and formats may vary |
| Helper Python modules | Include any of your own modules imported by `predict.py` |
| `requirements.txt` | Optional; extra packages required beyond the existing Colab environment |

Keep the **total submission size under 200 MB**.

### Commands used by the grader

The grader runs these commands **from inside your submission directory**:

```bash
python predict.py --task shape --images <IMAGE_DIR> --out <OUT_CSV>
python predict.py --task force --images <IMAGE_DIR> --out <OUT_CSV>
```

`<IMAGE_DIR>` is a **flat directory of `.jpg` files** with no class subdirectories and
no labels. Files have anonymous names such as `test_0001.jpg`.

Write exactly one row for every image in the relevant output CSV:

| Task argument | Required CSV columns, in order | Values |
|---|---|---|
| `--task shape` | `filename,class_id` | Image basename and integer class ID 0–9 |
| `--task force` | `filename,fx,fy,fz` | Image basename and three forces in newtons, on their original scale |

The `filename` value is the **basename only**, such as `test_0001.jpg`, without the
directory path. Force-test images are not identified as normal-press or shear images.
The force model must operate from the image alone and must not depend on the filename,
`contact_id` or `is_shear`.

`predict.py` must include, or import from files you submit, the model definition,
preprocessing and weight-loading code. Load weights relative to the script, for example
with `Path(__file__).parent / "shape_model.pt"`. Avoid paths tied to your own computer
or Drive, such as `/content/drive/...`.

Use a GPU when one is available, and ensure the script **also runs on CPU**.

### Extra dependencies

In the submission's `requirements.txt`, list only packages not already installed in
Colab, one package per line with a pinned version. The original instructions give
`timm==1.0.9` as an example of the required format; it is not a required dependency.
The grader installs the file with `pip install -r requirements.txt`.

Do not list `torch` or `torchvision` in that submission file: the instructions specify
using the Colab versions.

## 7. Use the example submission appropriately

The extracted `Tactile_DL_2027/example_submission/` directory contains a small baseline
CNN and example weights. Its `predict.py` demonstrates the required interface, and
`train_example.py` shows how those example weights were produced.

**The example training script uses all released images without a validation/test
split.** This is an interface demonstration and is not an acceptable evaluation
protocol for the coursework. Your experiment must use the required splits described
above.

### Check your submission in a fresh runtime

Before submission, test your own directory in a fresh Colab runtime. The following
reproduces the original package's self-check: it copies a small selection of released
images into flat folders and exercises both prediction commands. This checks the
interface; it is not an estimate of model performance.

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

Replace `<your_student_id>` with the actual directory name. If your submission has
no optional `requirements.txt`, omit its installation line. Both prediction commands
must finish without errors. Check that each CSV has the required columns and one row
per image, with valid class IDs or forces on the original scale.

## 8. Preprocessing choices to explain in your report

The original dataset guide highlights the following considerations:

- **Image geometry.** The images are rectangular. You may resize, pad, crop or retain
  the aspect ratio, but justify the choice. Small contact regions may become difficult
  to see after substantial downsampling.
- **Augmentation.** For shape classification, flips and rotations can be suitable for
  most shapes. For force estimation, image flips or rotations change the interpretation
  of `fx` and `fy`; transform the force labels consistently or avoid those augmentations.
- **Normalisation.** Normalise pixel intensities appropriately; the supplied guide
  mentions ImageNet normalisation when using compatible pretrained weights. Consider
  standardising each force target because the axes have different scales, and return
  predictions to newtons for evaluation and submission.

## Source acknowledgement

This guide reorganises the instructions in `Tactile_DL_2027/README.md` supplied with
the dataset archive. The original coursework source is
[LannWei/Deep-Learning-CourseWork-2027](https://github.com/LannWei/Deep-Learning-CourseWork-2027).
The dataset is described there as a curated subset of **TacVerse**:

L. Wei, G. Khurana, S. Bhouri, W. Hong, Z. Xin, Q. Cong, W. Fan, Y. Xiang and D. Zhang,
“TacVerse: A Multisensor Dataset and Benchmark for Cross-Sensor Vision-Based Tactile
Perception”, *Advanced Robotics Research*, 2026.
[DOI: 10.1002/adrr.70169](https://doi.org/10.1002/adrr.70169).

The original package identifies the subsets as `Shape_Classification/GelSight (no marker)`
and `Force_Regression/GelSight (with marker)`, with dataset code at
[LannWei/Tactile_Database](https://github.com/LannWei/Tactile_Database).
