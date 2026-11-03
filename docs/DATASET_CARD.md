# Dataset Reference

2026–2027 Deep Learning Final Coursework · Part A

[Course overview](../README.md) · [Getting started](GETTING_STARTED.md) · [Part A guide](COURSEWORK_GUIDE.md) · [Project handbook](../resources/2026_2027_DL_Final_Project_Handbook_Shared.pdf) · [Validation record](validation.json)

This reference describes the released tactile images, label schemas and measured distributions used for Part A. It also sets out the dataset's provenance, verification results and limits on the conclusions that can be drawn from coursework experiments.

## Overview

| Field | Value |
|---|---|
| Coursework | 2026–2027 Deep Learning Final Coursework — Part A |
| Release | `v1.0.0`, 2 November 2026 |
| Repository maintainer | Dandan Zhang, Imperial College London |
| Archive | `Tactile_DL_2027.zip` |
| Extracted root | `Tactile_DL_2027/` |
| Source attribution | TacVerse; source information retained from the supplied README |
| Intended educational use | Supervised image classification and regression; experimental design, evaluation and reproducible inference |
| Labels supplied | All 4,000 released images; no train/validation/test membership supplied |
| Hidden evaluation data | Described in the supplied instructions; not included in this release |
| Licence | No licence file supplied; no new licence assigned to source data or example code |

Part A includes shape classification (handbook Task 2) and force estimation (handbook Task 3). The original archive uses the legacy names “Task A” and “Task B” for these two learning tasks. The latter is distinct from the separate Part B group project. The released data form a teaching subset of TacVerse; all counts, class IDs and statistics on this page describe this release.

## Assessment scope

The [Final Project Handbook](../resources/2026_2027_DL_Final_Project_Handbook_Shared.pdf) defines the assessment requirements. The [Part A guide](COURSEWORK_GUIDE.md) and [assessment overview](ASSESSMENT_OVERVIEW.md) provide companion summaries and links to the relevant sections.

For Part A, train and validate only on this released coursework subset; do not add other TacVerse data or another tactile dataset. General-purpose pretrained weights such as ImageNet are allowed and must be cited. For Part B, neither this Part A subset nor the GelSight subsets of TacVerse may be used. These rules are specified in [handbook Section 11.3, PDF page 41](../resources/2026_2027_DL_Final_Project_Handbook_Shared.pdf#page=41). The [handbook wording notes](HANDBOOK_NOTES.md) identify the conflicting shorthand in Section 6.5.

## Provenance and preparation

The supplied [original README](ORIGINAL_DATASET_README.md) states that the images come from two TacVerse subsets:

- `Shape_Classification/GelSight (no marker)`;
- `Force_Regression/GelSight (with marker)`.

The source README describes the images as RGB JPEGs resized to 320 × 240 pixels. The release audit independently confirmed those dimensions, colour mode and encoding for every image. The source README also states that each shape class uses the same physical indenter and that each force contact provides a press image and a subsequent shear image.

The source archive is preserved byte for byte. Images and labels are unchanged. The preview figures combine selected images for display, and the browsable CSVs and original submission files are identical to their counterparts in the archive.

The package does not include original high-resolution captures, raw video, acquisition timestamps, acquisition-session identifiers, the subset-selection script, calibration files, uncertainty estimates for the force labels or the unreleased test images. Do not infer those details from file numbering. For broader acquisition methodology, consult the [TacVerse paper](https://doi.org/10.1002/adrr.70169) and [source repository](https://github.com/LannWei/Tactile_Database).

## Data inventory

| Component | Files / rows | Description |
|---|---:|---|
| Shape images | 2,000 | 10 class folders; 200 JPEGs in each |
| Shape labels | 2,000 rows | `filename,class_name,class_id` |
| Class mapping | 10 rows | `class_name,class_id` |
| Force images | 2,000 | 1,000 contacts with two observations each |
| Force labels | 2,000 rows | `filename,contact_id,is_shear,fx,fy,fz` |
| Example submission | 5 files | Two Python scripts, dependency file and two `.pt` checkpoints |
| Original dataset README | 1 file | Source documentation and coursework interface |
| Total | 4,009 files | 37,546,502 uncompressed bytes |

The compressed archive is 37,441,246 bytes: approximately 37.44 MB using decimal units or 35.71 MiB using binary units. These figures exclude space used by filesystem allocation, repository documentation and software environments.

## Shape classification schema

Each row in `shape_classification/labels.csv` describes one image.

| Column | Type | Interpretation |
|---|---|---|
| `filename` | String | POSIX-style path relative to the extracted `shape_classification/` directory |
| `class_name` | String | Name from `classes.csv` |
| `class_id` | Integer | Stable coursework label from 0 through 9 |

For example, `images/cylinder/cylinder_0000.jpg,cylinder,0` resolves beneath `Tactile_DL_2027/shape_classification/`.

| Class ID | Class name | Number of images |
|---:|---|---:|
| 0 | `cylinder` | 200 |
| 1 | `dots` | 200 |
| 2 | `hexagon` | 200 |
| 3 | `line` | 200 |
| 4 | `moon` | 200 |
| 5 | `rectangle` | 200 |
| 6 | `ring` | 200 |
| 7 | `small_sphere` | 200 |
| 8 | `triangle` | 200 |
| 9 | `wave` | 200 |

Use the supplied class mapping throughout preprocessing, training and inference. Class counts are balanced, but this does not establish independence between physical objects or equal visual difficulty across classes.

## Force estimation schema

Each row in `force_regression/labels.csv` describes one image and its force vector.

| Column | Type | Interpretation |
|---|---|---|
| `filename` | String | Path relative to the extracted `force_regression/` directory |
| `contact_id` | Integer | Physical contact identifier, 1–1,000 in this release |
| `is_shear` | Binary integer | `0`: normal press; `1`: observation after lateral displacement |
| `fx` | Float | Tangential force along the source sensor's x axis, in N |
| `fy` | Float | Tangential force along the source sensor's y axis, in N |
| `fz` | Float | Normal force, in N; negative values denote pressing into the sensor |

Every contact has exactly two observations:

- `images/contact_NNNN.jpg`, with `is_shear=0`;
- `images/contact_NNNN_shear.jpg`, with `is_shear=1`.

The release contains 1,000 press images and 1,000 shear images. The labels for a press/shear pair need not be equal because lateral motion changes the measured loading. “Normal press” describes the acquisition condition; measured `fx` and `fy` values are not identically zero.

`contact_id` and `is_shear` support splitting and analysis. Hidden-test inference uses anonymous images without these metadata fields, so the model must predict from image content alone. The package does not provide a complete mapping from image axes to physical sensor axes. Any use of flips or rotations must therefore justify the corresponding force-label transformation.

## Measured force statistics

The following statistics were calculated directly from the 2,000 released label rows. They describe this coursework subset; the source-recording summary in the original README has a broader scope. Values are in newtons. “SD” denotes sample standard deviation with denominator `n−1`. Values are rounded for presentation; the CSVs retain their original precision.

| Subset | Images | `fx` mean ± SD | `fy` mean ± SD | `fz` mean ± SD |
|---|---:|---:|---:|---:|
| Normal press (`is_shear=0`) | 1,000 | −0.069391 ± 0.055699 | −0.005559 ± 0.031028 | −0.707167 ± 0.476133 |
| Shear (`is_shear=1`) | 1,000 | 0.000408 ± 0.364488 | −0.034880 ± 0.417863 | −0.671544 ± 0.463890 |
| All images | 2,000 | −0.034492 ± 0.262986 | −0.020220 ± 0.296576 | −0.689355 ± 0.470272 |

| Target | Minimum (N) | Maximum (N) |
|---|---:|---:|
| `fx` | −1.329635 | 1.396376 |
| `fy` | −1.367870 | 1.277017 |
| `fz` | −1.989753 | −0.010382 |

All force labels are finite. All `fz` values in this release are negative. The smaller tangential variation in press images explains why a pooled error alone may conceal poor shear estimation; the coursework therefore requires separate press/shear evaluation.

Estimate target standardisation and the required mean-force baseline from the **training subset only**. The full-release statistics above describe the dataset and must not be used as fitted preprocessing parameters.

## Splits, evaluation and scope of claims

The required split is 60% training, 20% validation and 20% test. Stratify shape splits by class. Split the force dataset by unique `contact_id` so that its two observations remain in the same subset. These proportions yield 600 / 200 / 200 force contacts and 1,200 / 400 / 400 force images.

A stratified image split for shapes evaluates held-out images of the represented class/indenter set. Because the source README states that one indenter provides each class, this does not establish generalisation to unseen physical objects. A contact-grouped force split prevents pair leakage, but does not by itself establish generalisation to new sensors, materials, sessions or loading ranges.

Use accuracy, macro precision/recall/F1 and a confusion matrix for shapes. Use per-axis and overall force RMSE in N, together with the required tangential analysis. The tangential vector RMSE specified in the source is:

$$\mathrm{RMSE}_t = \sqrt{\frac{1}{N}\sum_{i=1}^{N}\left[(\hat f_{x,i}-f_{x,i})^2+(\hat f_{y,i}-f_{y,i})^2\right]}.$$

This metric is the RMS length of the two-dimensional error vector, rather than the arithmetic average of the x- and y-axis RMSEs. See the [Part A guide](COURSEWORK_GUIDE.md) for the original metric code and complete reporting requirements.

## Quality checks and limitations

The release audit found:

- all 4,000 images decode as JPEG, RGB, 320 × 240;
- every label points to an existing image, and no image is unlabelled;
- all class IDs, names and class-folder assignments agree;
- all 1,000 force contacts have exactly one press and one shear observation;
- no duplicated CSV filenames, non-finite force values, exact duplicate image bytes or exact duplicate decoded pixel arrays;
- no EXIF or ICC blocks in the JPEGs inspected.

These checks do not rule out near duplicates, correlated acquisitions, systematic label error or distribution shift. Session identifiers are unavailable, which limits assessment of session-level independence. Image resizing and compression may reduce small contact details. The limited sensor variants and task-specific data do not support claims about unrestricted tactile sensing, unseen sensor hardware or general robotic manipulation without additional experiments.

The example training script uses all released data to produce checkpoints for interface verification. Those checkpoints cannot establish valid performance on a subsequently created held-out split of the same images. The source code and checkpoints are preserved without model-performance claims.

## Versioning, reproducibility and attribution

Release `v1.0.0` preserves the provided ZIP bytes, with a normalised download filename:

```text
1a1620e4695b220043318e7b209202940b930fcf82f69b4f761213255c6b4ca5  Tactile_DL_2027.zip
```

The [download helper](../scripts/download_dataset.py) uses a version-specific URL and verifies the checksum before extraction. The [validation script](../scripts/verify_dataset.py) can check a local copy. Retain the release version, random seed, split membership, environment versions, preprocessing and trained weights with your experiment records.

The [course overview](../README.md) and [citation record](../CITATION.cff) provide the dataset and source-paper acknowledgements. The package did not include a licence; public availability and scholarly citation do not assign new reuse terms to the data. Direct questions about reuse beyond the coursework to the teaching team or source rights holders.
