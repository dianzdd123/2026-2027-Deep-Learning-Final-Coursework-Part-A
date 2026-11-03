# 2026–2027 Deep Learning Final Coursework — Part A

## Learning from touch: shape recognition and contact-force estimation

This repository provides the tactile dataset and practical guidance for **Part A of the 2026–2027 Deep Learning final coursework**, maintained by **Dandan Zhang, Imperial College London**. It contains a compact teaching subset of **TacVerse**, with two supervised learning tasks: recognising an object's shape from a tactile image and estimating a three-dimensional contact-force vector.

**[Download the complete dataset — 37.44 MB](https://github.com/dianzdd123/2026-2027-Deep-Learning-Final-Coursework-Part-A/releases/download/v1.0.0/Tactile_DL_2027.zip)** · **[Dataset card](docs/DATASET_CARD.md)** · **[Coursework and submission guide](docs/COURSEWORK_GUIDE.md)** · **[Complete project handbook](resources/2026_2027_DL_Final_Project_Handbook_Shared.pdf)** · **[Dates and assessment](docs/ASSESSMENT_OVERVIEW.md)** · **[Latest guidance release v1.0.1](https://github.com/dianzdd123/2026-2027-Deep-Learning-Final-Coursework-Part-A/releases/tag/v1.0.1)**

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/dianzdd123/2026-2027-Deep-Learning-Final-Coursework-Part-A/blob/main/notebooks/01_explore_dataset.ipynb)

> **Coursework naming:** The handbook uses **Part A** for the individual technical coursework and **Part B** for the separate group project. Within Part A, **Task 2 is shape classification** and **Task 3 is force estimation**. The original dataset README calls these two learning tasks “Task A” and “Task B”; those legacy labels do not refer to coursework Parts A and B.

### Start here

1. Read the [complete **Deep Learning Final Project Handbook**](resources/2026_2027_DL_Final_Project_Handbook_Shared.pdf), especially Sections 2–5 for Part A, and the [dates and assessment overview](docs/ASSESSMENT_OVERVIEW.md).
2. Use the [handbook reading map](resources/README.md) and [Part A coursework guide](docs/COURSEWORK_GUIDE.md) to plan the required experiments and submission.
3. Open the [exploration notebook](notebooks/01_explore_dataset.ipynb), download and verify the data, and inspect the images with their labels.
4. Create reproducible splits, compare the required architectures, write the report and test your model folder in a fresh runtime.
5. For the separate group project, read the [Part B guide](docs/PART_B_GUIDE.md) and handbook Sections 6–8. **Part B must not use this Part A dataset or the GelSight subsets of TacVerse.**

The correct handbook is the **51-page 2026/27 Final Project Handbook**, preserved unchanged. Its cover gives the planned project release date as **Tuesday 10 November 2026**; this is the document's stated version date. The PDF is the source of the assessment requirements below, with later module-team announcements on Canvas providing any updates. The [source wording notes](docs/HANDBOOK_NOTES.md) identify two passages whose scope should be checked with the module team.

### Assessment at a glance

| Part | Work | Marks | Deadline and submission |
|---|---|---:|---|
| **Part A** | Individual: shape classification and 3D force estimation | **60** | **Sunday 13 December 2026, 23:59 UK time (GMT)**; one ZIP on Canvas |
| **Part B** | Groups of **5–6**: advanced tactile perception, a working proof of concept and a video of **at most 5 minutes** | **40**, subject to peer moderation | **Sunday 20 December 2026, 23:59 UK time (GMT)**; group files on Canvas |

All students complete peer assessment by **Wednesday 23 December 2026, 23:59 UK time (GMT)**. Optional bonuses total at most **15 marks**, and the final mark is capped at **100**. See [handbook Sections 2 and 10](resources/2026_2027_DL_Final_Project_Handbook_Shared.pdf#page=6) and the [full overview](docs/ASSESSMENT_OVERVIEW.md) for the marking criteria, other milestones, early-submission rules and late penalties.

### Required Part A work

| Handbook task | Requirement | Required marks |
|---|---|---:|
| **Task 1 — Data preparation** | Load both datasets, explore images and distributions, normalise pixels, standardise forces and create valid 60/20/20 splits | **10** |
| **Task 2 — Shape classification** | Implement and compare **at least three CNN architectures**; report classification metrics, efficiency and failure analysis | **20** |
| **Task 3 — Force estimation** | Compare **at least two architectures**; report force errors in N and the required press/shear tangential analysis against the training-mean baseline | **20** |
| **Task 5 — Report** | A **3–6 page IEEE conference-format report**, double column; references and the AI-use declaration may continue beyond page 6 | **10** |

**Task 4 (systematic hyperparameter tuning) is optional**, worth up to 5 bonus marks. Augmentation, evidenced optimisation/regularisation and a novel approach are also optional bonus work, subject to the overall cap. Use [handbook Sections 3–5](resources/2026_2027_DL_Final_Project_Handbook_Shared.pdf#page=9) and the [Part A guide](docs/COURSEWORK_GUIDE.md) for the full requirements.

## 1. Dataset at a glance

| Property | Shape classification — handbook Task 2 | Force estimation — handbook Task 3 |
|---|---|---|
| Learning problem | Multiclass image classification | Three-output regression |
| Sensor described in the supplied dataset | GelSight without markers | GelSight with markers |
| Released images | 2,000 | 2,000 |
| Targets | One of 10 classes, encoded as `class_id` 0–9 | `fx`, `fy`, `fz`, in newtons (N) |
| Balance / grouping | 200 images per class | 1,000 contacts; one press image and one shear image per contact |
| Image format | RGB JPEG, 320 × 240 pixels (width × height) | RGB JPEG, 320 × 240 pixels (width × height) |
| Supplied split | Unsplit; students create 60% / 20% / 20% splits | Unsplit; students create 60% / 20% / 20% splits **by contact** |
| Label file after extraction | `Tactile_DL_2027/shape_classification/labels.csv` | `Tactile_DL_2027/force_regression/labels.csv` |

The downloadable archive contains **4,000 images, three CSV files, an original dataset README, two example Python scripts, an example dependency file and two example model checkpoints**: **4,009 files** in total. Its size is **37,441,246 bytes** (37.44 MB / 35.71 MiB); the files occupy **37,546,502 bytes** before filesystem overhead after extraction.

The complete image data is attached to the **GitHub release**. The repository itself holds documentation, browsable labels, the supplied submission example and access utilities. GitHub's green **Code → Download ZIP** downloads these repository files; use the **dataset download above** to obtain all images.

### What does a tactile image show?

A vision-based tactile sensor uses an internal camera to observe a deformable surface. Contact changes the surface's appearance, providing cues about contact geometry and loading. In the supplied dataset, the marker-free images support shape recognition, while the marked images support force estimation. These are images of sensor deformation, rather than conventional photographs of the objects.

![One released tactile image from each of the 10 shape classes, labelled with its class ID and name.](docs/assets/shape_examples.jpg)

*One actual image per class from this release. Display scaling is for illustration; the dataset images are unchanged. Class IDs come directly from `classes.csv`.*

![The normal-press and shear images for one force contact, with the measured force labels in newtons.](docs/assets/force_pair.jpg)

*Two observations of the same contact. These images must remain together when creating the training, validation and test sets.*

## 2. Download and start exploring

### Google Colab

Open the **Open in Colab** button above. The notebook downloads the versioned archive, checks its SHA-256 checksum, extracts the data, reads the labels and displays examples. Exploration and data verification work on CPU. A GPU is useful when you subsequently train your own models.

For a new Colab notebook, these two cells provide the same starting point:

```python
!git clone -q https://github.com/dianzdd123/2026-2027-Deep-Learning-Final-Coursework-Part-A.git /content/coursework-part-a
!python /content/coursework-part-a/scripts/download_dataset.py --output-dir /content
```

```python
from pathlib import Path
import pandas as pd

ROOT = Path('/content/Tactile_DL_2027')
shape = pd.read_csv(ROOT / 'shape_classification/labels.csv')
force = pd.read_csv(ROOT / 'force_regression/labels.csv')

print(shape.groupby(['class_id', 'class_name']).size())
print(force[['fx', 'fy', 'fz']].describe())
```

After a Colab runtime is reset, download the dataset again or restore a copy from your Google Drive. Choose **Runtime → Change runtime type → GPU** when you begin model training and a GPU is available.

### Local Python, VS Code or Jupyter

Use Python 3.10 or newer. From a terminal:

```bash
git clone https://github.com/dianzdd123/2026-2027-Deep-Learning-Final-Coursework-Part-A.git
cd 2026-2027-Deep-Learning-Final-Coursework-Part-A
python -m pip install -r requirements.txt
python scripts/download_dataset.py
python scripts/verify_dataset.py --data Tactile_DL_2027
```

Open [`notebooks/01_explore_dataset.ipynb`](notebooks/01_explore_dataset.ipynb) in VS Code with the Jupyter extension, or in your existing Jupyter environment. Select the Python environment where you installed the requirements. The exploration requirements do not install PyTorch; install PyTorch separately if you want to run the supplied inference example locally.

### Already downloaded the ZIP?

You can extract it with your usual ZIP utility, or use the helper to check its checksum before extraction:

```bash
python scripts/download_dataset.py --archive /path/to/Tactile_DL_2027.zip
```

The helper preserves an existing extracted data folder. Choose a different `--output-dir` to extract a fresh copy. The top-level folder inside the archive is always **`Tactile_DL_2027`**, even though the academic year is 2026–2027.

## 3. Files and labels

| Location | Purpose |
|---|---|
| [`docs/DATASET_CARD.md`](docs/DATASET_CARD.md) | Provenance, label definitions, measured statistics, limitations and integrity details |
| [`docs/COURSEWORK_GUIDE.md`](docs/COURSEWORK_GUIDE.md) | Splitting, evaluation, tangential-force analysis and submission requirements from the supplied brief |
| [`resources/README.md`](resources/README.md) | Section and page map for the complete project handbook |
| [`resources/2026_2027_DL_Final_Project_Handbook_Shared.pdf`](resources/2026_2027_DL_Final_Project_Handbook_Shared.pdf) | The correct 51-page final project handbook, preserved unchanged |
| [`docs/ASSESSMENT_OVERVIEW.md`](docs/ASSESSMENT_OVERVIEW.md) | Dates, marks, deliverables, bonuses, late rules and academic integrity |
| [`docs/PART_B_GUIDE.md`](docs/PART_B_GUIDE.md) | Separate advanced tactile perception group project, permitted data, video and group-work requirements |
| [`docs/HANDBOOK_NOTES.md`](docs/HANDBOOK_NOTES.md) | Source version, original links and passages requiring clarification |
| [`metadata/shape_classification/`](metadata/shape_classification/) | Unmodified copies of `classes.csv` and shape `labels.csv` for browsing |
| [`metadata/force_regression/labels.csv`](metadata/force_regression/labels.csv) | Unmodified force labels for browsing |
| [`example_submission/`](example_submission/) | Original inference script, demonstration training script and supplied weights |
| [`notebooks/01_explore_dataset.ipynb`](notebooks/01_explore_dataset.ipynb) | Guided loading, visualisation and data inspection |
| [`scripts/download_dataset.py`](scripts/download_dataset.py) | Versioned download, checksum verification and extraction |
| [`scripts/verify_dataset.py`](scripts/verify_dataset.py) | Validation of labels, image files and contact pairs |
| [`docs/validation.json`](docs/validation.json) | Machine-readable release audit and force statistics |
| [`docs/ORIGINAL_DATASET_README.md`](docs/ORIGINAL_DATASET_README.md) | The supplied README preserved verbatim for provenance; its original links refer to the upstream repository |
| [`checksums.sha256`](checksums.sha256) | SHA-256 for the released dataset ZIP |

**CSV paths are relative to the corresponding extracted task folder.** For example, `images/contact_0001.jpg` resolves to `Tactile_DL_2027/force_regression/images/contact_0001.jpg`, not a path inside `metadata/`.

### Shape classes

| ID | Class | Images | ID | Class | Images |
|---:|---|---:|---:|---|---:|
| 0 | `cylinder` | 200 | 5 | `rectangle` | 200 |
| 1 | `dots` | 200 | 6 | `ring` | 200 |
| 2 | `hexagon` | 200 | 7 | `small_sphere` | 200 |
| 3 | `line` | 200 | 8 | `triangle` | 200 |
| 4 | `moon` | 200 | 9 | `wave` | 200 |

### Force labels

`contact_id` identifies a physical contact. `is_shear=0` denotes its normal-press image; `is_shear=1` denotes the image after a lateral displacement. `fx` and `fy` are tangential force components and `fz` is the normal force. **Negative `fz` means pressing into the sensor**, according to the supplied sensor-frame convention.

All targets are in **newtons**. In this release, the measured ranges are `fx ∈ [−1.329635, 1.396376]`, `fy ∈ [−1.367870, 1.277017]` and `fz ∈ [−1.989753, −0.010382]` N. See the [dataset card](docs/DATASET_CARD.md#measured-force-statistics) for statistics by press/shear subset.

## 4. Experimental protocol

The supplied coursework guidance requires students to create reproducible **60% training / 20% validation / 20% test** splits.

| Task | Split unit | Training | Validation | Test |
|---|---|---:|---:|---:|
| Shape | Images, stratified by class | 1,200 images; 120/class | 400 images; 40/class | 400 images; 40/class |
| Force | Unique `contact_id` values | 600 contacts / 1,200 images | 200 contacts / 400 images | 200 contacts / 400 images |

**Keep both images of every force contact in the same split.** Randomly splitting force images can place one observation of a contact in training and its paired observation in testing, inflating the apparent generalisation performance.

Fit any data-derived preprocessing, such as force-target means and standard deviations, using the **training split only**. Use validation data for model selection. Keep the test split for final evaluation. Record the random seed and save the split membership so that the experiment can be reproduced.

- **Shape:** report accuracy, macro precision, macro recall, macro F1 and a confusion matrix.
- **Force:** report per-axis and overall RMSE in newtons. Include the required separate press/shear analysis, tangential vector RMSE, a training-mean baseline, shear prediction plots and discussion of the worst tangential errors.
- **Augmentation:** consider the physical meaning of each transformation. Rotating or flipping force images may require transforming force labels in a correctly established sensor coordinate convention; avoid such transforms when that correspondence is not established.

The [coursework guide](docs/COURSEWORK_GUIDE.md) follows the correct handbook, including its model-comparison requirements, exact RMSE definitions, reporting rules and submission interface. Dates and marking criteria are in the [assessment overview](docs/ASSESSMENT_OVERVIEW.md).

**Part A data rule:** train and validate only on the released coursework data. Other TacVerse images and other tactile datasets are not permitted for Part A; general-purpose pretrained weights such as ImageNet are allowed and must be cited. This follows [handbook Section 11.3](resources/2026_2027_DL_Final_Project_Handbook_Shared.pdf#page=41).

## 5. Submission interface and example code

The supplied instructions describe a **separate, unreleased test set** used by the teaching team. The inference script must accept a flat folder of anonymous JPEG images and run on CPU as well as use a GPU when available:

```bash
python predict.py --task shape --images <IMAGE_DIR> --out <OUT_CSV>
python predict.py --task force --images <IMAGE_DIR> --out <OUT_CSV>
```

| Task | Required CSV columns | Output conventions |
|---|---|---|
| Shape | `filename,class_id` | File name only; integer class ID 0–9 |
| Force | `filename,fx,fy,fz` | File name only; forces in newtons on the original scale |

Return exactly one row per input image. Hidden-test filenames provide no labels or press/shear indicators. Predict from the image alone. Keep weights relative to `predict.py`. The **CID-named model folder** must be under **200 MB**, run on CPU, and complete each task within **10 minutes on a Colab GPU**. **No downloads are allowed at prediction time.** These are the [handbook Section 5.4 requirements](resources/2026_2027_DL_Final_Project_Handbook_Shared.pdf#page=21).

Submit `DL_Coursework_YourName_CID.zip` on Canvas, containing `DL_Coursework_YourName_CID.pdf`, your `code/` folder and the model folder named with your eight-digit CID. Share the Colab notebook with the TA, **l.wei24@imperial.ac.uk**, with viewer access; for local Jupyter work the notebook copy in `code/` fulfils this role. Restart and run the notebook with outputs saved before submission. See [handbook Section 9.1](resources/2026_2027_DL_Final_Project_Handbook_Shared.pdf#page=33).

**The example is a submission-interface demonstration.** Its training script uses **all released images**, and the supplied weights were produced for that demonstration. Do not report those weights as a model evaluated on an independent coursework test split. Develop and evaluate your own model using the required split protocol. The original example scripts and checkpoints are included unchanged in both [`example_submission/`](example_submission/) and the dataset ZIP.

### Academic integrity and AI use

Part A is individual: do not share assessed code, weights, results or reports, including with your Part B group. The handbook allows declared AI assistance for explanations, debugging, code generation and editing your own text, provided you understand, test and can explain it. AI must not write whole sections of the Part A report. AI voices or avatars may not replace Part B members, except for a reasonable adjustment agreed with the module team under Section 7.2. Do not fabricate results or references. Include the four-line AI-use declaration even if no AI was used; see [handbook Section 11](resources/2026_2027_DL_Final_Project_Handbook_Shared.pdf#page=40) and the [assessment overview](docs/ASSESSMENT_OVERVIEW.md).

## 6. Provenance and citation

The supplied README identifies this package as a curated subset of **TacVerse**, using `Shape_Classification/GelSight (no marker)` and `Force_Regression/GelSight (with marker)` from the source dataset. The **coursework release has its own 10-class mapping and split requirements**; use its CSVs and guidance when completing this coursework.

Please acknowledge the original dataset:

> Lan Wei, Gurmeher Khurana, Sirine Bhouri, Wenhao Hong, Zeyuan Xin, Qingzheng Cong, Wen Fan, Yanzheng Xiang and Dandan Zhang. **TacVerse: A Multisensor Dataset and Benchmark for Cross-Sensor Vision-Based Tactile Perception.** *Advanced Robotics Research*, 2026, e70169. [doi:10.1002/adrr.70169](https://doi.org/10.1002/adrr.70169).

```bibtex
@article{wei2026tacverse,
  title   = {TacVerse: A Multisensor Dataset and Benchmark for Cross-Sensor Vision-Based Tactile Perception},
  author  = {Wei, Lan and Khurana, Gurmeher and Bhouri, Sirine and Hong, Wenhao and Xin, Zeyuan and Cong, Qingzheng and Fan, Wen and Xiang, Yanzheng and Zhang, Dandan},
  journal = {Advanced Robotics Research},
  year    = {2026},
  pages   = {e70169},
  doi     = {10.1002/adrr.70169}
}
```

- [Original coursework repository](https://github.com/LannWei/Deep-Learning-CourseWork-2027)
- [TacVerse source repository](https://github.com/LannWei/Tactile_Database)
- [Article](https://advanced.onlinelibrary.wiley.com/doi/10.1002/adrr.70169)

The uploaded dataset archive is republished **byte for byte**, with a filename normalised to `Tactile_DL_2027.zip`. Documentation, a visual overview and access/validation utilities have been added around it. No open-source or Creative Commons licence was included in the supplied package, and this repository does not assign a new licence to that source material. Contact the teaching team about uses beyond the coursework or permission to redistribute.

## 7. Integrity and support

**Dataset v1.0.0**, published **2 November 2026**, remains unchanged. **Guidance v1.0.1** replaces the mistaken handbook and aligns the student materials with the correct final-project handbook. The dataset download keeps its original URL and checksum:

```text
1a1620e4695b220043318e7b209202940b930fcf82f69b4f761213255c6b4ca5  Tactile_DL_2027.zip
```

The release audit decoded all 4,000 JPEGs, checked every label-to-file mapping, verified the class counts and all 1,000 contact pairs, and found no exact duplicate image files or decoded pixel arrays. The audit checks data consistency; it does not establish statistical independence between similar contacts or images.

For a download problem or documentation error, [open a repository issue](https://github.com/dianzdd123/2026-2027-Deep-Learning-Final-Coursework-Part-A/issues). Keep assessed solutions and student-identifying information in the module's designated submission channel.
