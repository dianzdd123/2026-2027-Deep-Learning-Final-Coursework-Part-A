# Deep Learning: Final Project 2026–2027
### Part A: Shape Classification and 3D Force Estimation from Tactile Images

**Imperial College London | I-X MSc Artificial Intelligence Applications and Innovation (AIAI)**  
**Deep Learning module | Academic year 2026–2027**  
**Lecturer:** Dr Dandan Zhang · **Teaching assistant:** Ms Lan Wei

This repository supports the **Deep Learning** module within Imperial College London's [MSc Artificial Intelligence Applications and Innovation (AIAI)](https://www.imperial.ac.uk/study/courses/postgraduate-taught/2026/applications-innovation/), taught in the [I-X interdisciplinary AI environment](https://ix.imperial.ac.uk/masters-programme). In this part of the final coursework, students work with real tactile-sensor images rather than conventional object photographs. The images show how a soft sensor surface changes when an object presses or slides across it, providing evidence about shape and contact force.

Students use these observations to build and compare deep-learning models for two tasks: recognising ten contact shapes and estimating the three components of contact force. The project connects techniques from the Deep Learning module with the AIAI programme's emphasis on applying AI to real engineering problems. It asks students not only to train a model, but also to explain what the data can tell them, how to evaluate their results fairly and what the model might struggle with on unseen examples.

This is the **Part A dataset and starter-code repository**. Official handbooks, briefing slides, assessment announcements and submissions remain on Canvas. The GitHub materials help students begin the practical work without replacing those formal instructions.

**[Download the dataset (37.44 MB)](https://github.com/dianzdd123/2026-2027-Deep-Learning-Final-Coursework-Part-A/releases/download/v1.0.2/Tactile_DL_2027.zip)** · **[Getting started](docs/GETTING_STARTED.md)** · **[Part A assignment guide](docs/COURSEWORK_GUIDE.md)** · **[Assessment information](docs/ASSESSMENT_OVERVIEW.md)**

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/dianzdd123/2026-2027-Deep-Learning-Final-Coursework-Part-A/blob/main/notebooks/01_explore_dataset.ipynb)

## Course and programme links

- [MSc Artificial Intelligence Applications and Innovation (Imperial course page)](https://www.imperial.ac.uk/study/courses/postgraduate-taught/2026/applications-innovation/): programme overview and its teaching structure, including the Deep Learning module.
- [I-X Master's programme](https://ix.imperial.ac.uk/masters-programme): context for the interdisciplinary programme and its focus on practical applications of AI.
- [Part A dataset release](https://github.com/dianzdd123/2026-2027-Deep-Learning-Final-Coursework-Part-A/releases/latest): data for the shape and force tasks in this coursework.

## Where to find the course materials

| Platform | Materials and actions |
|---|---|
| **GitHub : this repository** | Part A dataset release, dataset documentation, exploration notebook, starter code, and download/verification tools |
| **Canvas : module site** | Current Final Project Handbook, simplified handbook, briefing slides, announcements and clarifications, Part B group registration, submissions and peer assessment |
| **GitHub release v1.0.2** | [Complete tactile dataset](https://github.com/dianzdd123/2026-2027-Deep-Learning-Final-Coursework-Part-A/releases/download/v1.0.2/Tactile_DL_2027.zip) |

**Source and version note:** The newly provided *Simplified Handbook 2026/27* and *Key Information Student Briefing* are dated **10 November 2026**. Earlier comprehensive repository guides and a previously uploaded full handbook disagree on some provisions, notably **Part B group size (4–6 versus 5–6)** and **bonus cap (+5 versus +15)**. This README follows the newly provided documents for orientation; the simplified handbook itself says the *full handbook* takes precedence where texts differ. **Use current Canvas announcements for any binding clarification.** See [Source alignment and discrepancies](docs/SOURCE_ALIGNMENT.md). We have not silently altered the original PDFs.

## Why tactile sensing?

Most image-classification examples ask a network to recognise something visible, such as a car or a cat. Tactile images pose a different question: what can a robot infer from the deformation of its fingertip? A shallow indentation can be difficult to distinguish from noise, while the small movements of printed markers carry information about sideways force. These features make the dataset a useful setting for learning how model architecture, preprocessing and evaluation choices affect a practical AI system.

## Learning objectives

Students should be able to frame image classification and force regression tasks; inspect images and labels; build non-leaking 60/20/20 splits; compare CNN architectures with controlled experimental conditions; interpret classification and physical-force errors; and package a reproducible inference pipeline that can operate on unseen anonymous images.

## Data at a glance

| | Shape classification | 3D force estimation |
|---|---|---|
| Sensor | GelSight without markers | GelSight with markers |
| Released images | 2,000 RGB JPEGs | 2,000 RGB JPEGs (1,000 contacts × press/shear pairs) |
| Resolution | 320 × 240 | 320 × 240 |
| Targets | Class ID 0–9; ten shape classes | `fx`, `fy` (tangential), `fz` (normal), in newtons |
| Split | 60/20/20, stratified by class | 60/20/20, grouped by `contact_id` |

![Representative shape-class images](docs/assets/shape_examples.jpg)

*One released example per shape class.*

![Paired press/shear images](docs/assets/force_pair.jpg)

*Two images from one physical contact; they must stay together in data splitting.*

The data archive's older internal labels “Task A” (shape) and “Task B” (force) are **both tasks within coursework Part A**; they are not the separate group project Part B.

## Coursework at a glance

| Component | Assessment | Marks | Deadline (23:59 GMT) |
|---|---|---:|---|
| **Part A : individual** | Data preparation (10), shape classification (20), force estimation (20), technical report (10) | 60 | **Sunday 13 December 2026** |
| **Part B : group** | Advanced tactile perception project with a working proof-of-concept and a video of at most five minutes | 40 | **Sunday 20 December 2026** |
| **Peer assessment** | Each Part B member completes the Canvas form | : | **Wednesday 23 December 2026** |

In the **newly supplied simplified handbook and briefing**, groups comprise **4–6 students** and the only listed bonus is up to **five marks for systematic hyperparameter tuning** (Part A Task 4). The earlier full handbook differs; follow module-team clarification on Canvas. [Assessment overview](docs/ASSESSMENT_OVERVIEW.md).

### Part A: required work

1. **Prepare and inspect data:** verify labels, analyse image/force distributions, normalise with training statistics only, and split without contact leakage.
2. **Classify shapes:** compare **at least three CNN architectures**, reporting accuracy, macro precision/recall/F1, confusion matrix, efficiency and failure examples.
3. **Estimate forces:** compare **at least two architectures**, report per-axis and overall RMSE in **newtons**, and examine normal press versus shear. The newly supplied simplified handbook requires press/shear tangential RMSE, shear prediction plots and discussion; it **recommends** the training-mean baseline (required by the older full handbook).
4. **Write the report:** an **IEEE double-column report, 3–6 pages**, with evidence-based analyses and correct citations. Task 4 hyperparameter tuning is optional.

**Part A must use the released coursework tactile images only.** General-purpose pretraining such as ImageNet is allowed with attribution. The Part A dataset and the GelSight subsets of TacVerse must **not** be used for Part B.

### Submission interface

Student model folders must contain a working `predict.py` with two commands:

```bash
python predict.py --task shape --images <IMAGE_DIR> --out <OUT_CSV>
python predict.py --task force --images <IMAGE_DIR> --out <OUT_CSV>
```

Output CSV fields: `filename,class_id` for shape; `filename,fx,fy,fz` for force. Models receive **image data only** at prediction time; no `contact_id`, `is_shear` or filename-derived labels. The simplified handbook requires a CID-named model folder **under 200 MB**, no inference-time downloads, CPU/GPU compatibility and **ten minutes per task on a Colab GPU**. See the [inference reference](example_submission/README.md) and [Part A guide](docs/COURSEWORK_GUIDE.md).

The example checkpoints and `train_example.py` demonstrate the inference format only: they were trained using all released images and are **not** valid held-out evaluation baselines.

## Start here

1. Read the **current simplified and full handbooks on Canvas**; review [assessment information](docs/ASSESSMENT_OVERVIEW.md).
2. Download [`Tactile_DL_2027.zip`](https://github.com/dianzdd123/2026-2027-Deep-Learning-Final-Coursework-Part-A/releases/download/v1.0.2/Tactile_DL_2027.zip) from the release, **not** GitHub’s *Code → Download ZIP*. Check its accompanying `README.md`.
3. Open the [exploration notebook](notebooks/01_explore_dataset.ipynb), or run `python scripts/download_dataset.py` followed by `python scripts/verify_dataset.py --data Tactile_DL_2027`.
4. Use [Getting started](docs/GETTING_STARTED.md) for Colab/VS Code setup; [dataset card](docs/DATASET_CARD.md) for schema and provenance; and [Part A guide](docs/COURSEWORK_GUIDE.md) for the required experiments.
5. Perform your own controlled experiments and submit assessed work to **Canvas**, not GitHub.

## Academic conduct, attribution and support

Part A is individual: do not publish or share assessed student code, weights, reports or results. Declare AI assistance; do not use AI to write entire report sections, generate or change experimental results or invent references. Part B presenters must use their own voices. Refer to the module’s current handbook and Canvas guidance.

Questions: **Dr Dandan Zhang** (`d.zhang17@imperial.ac.uk`) or **Ms Lan Wei** (`l.wei24@imperial.ac.uk`). Email subject: `[2026-Deep-Learning-Inquiry]-[Name]`. Use [GitHub Issues](https://github.com/dianzdd123/2026-2027-Deep-Learning-Final-Coursework-Part-A/issues) for repository access problems only; do not post assessed solutions or identifying information.

**Source:** TacVerse : Wei, L. *et al.* (2026), *Advanced Robotics Research*, e70169. [DOI: 10.1002/adrr.70169](https://doi.org/10.1002/adrr.70169). The supplied archive is preserved unchanged and does not include a new reuse licence. [Dataset card](docs/DATASET_CARD.md) · [Citation metadata](CITATION.cff) · [Latest public release](https://github.com/dianzdd123/2026-2027-Deep-Learning-Final-Coursework-Part-A/releases/latest).
