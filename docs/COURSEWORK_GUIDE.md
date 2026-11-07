# Part A : Individual technical coursework

[Home](../README.md) · [Getting started](GETTING_STARTED.md) · [Dataset card](DATASET_CARD.md) · [Assessment](ASSESSMENT_OVERVIEW.md)

**Shape classification and 3D contact-force estimation from GelSight images** · **60 marks** · **Due Sunday 13 December 2026 at 23:59 GMT via Canvas**.

This assignment forms the individual Part A component of Deep Learning within Imperial's [I-X MSc Artificial Intelligence Applications and Innovation](https://www.imperial.ac.uk/study/courses/postgraduate-taught/2026/applications-innovation/). The aim is to develop, compare and explain deep-learning models using physical tactile observations. It is not enough to present a high test score: document the data split, architecture decisions, fair experimental comparisons, error patterns and limits of generalisation.

## 1. Data and access

[Download `Tactile_DL_2027.zip`](https://github.com/dianzdd123/2026-2027-Deep-Learning-Final-Coursework-Part-A/releases/download/v1.0.2/Tactile_DL_2027.zip). The archive (37.44 MB) contains the original dataset `README.md`, 4,000 RGB 320×240 JPEG images and `example_submission/`. GitHub's **Code → Download ZIP** is *not* the data download.

| | Shape | Force |
|---|---|---|
| Images | 2,000: 200 per class across ten classes | 2,000: press and shear images for 1,000 contacts |
| Labels | `filename,class_name,class_id` | `filename,contact_id,is_shear,fx,fy,fz` |
| Sensor | GelSight without markers | GelSight with markers |
| Prediction target | Integer class ID, 0–9 | Three force components in newtons |

Shape classes: 0 cylinder; 1 dots; 2 hexagon; 3 line; 4 moon; 5 rectangle; 6 ring; 7 small_sphere; 8 triangle; 9 wave. `fx` and `fy` denote tangential force; `fz` denotes normal force, with negative `fz` indicating pressing into the sensor.

## 2. Required experimental design (Task 1 : 10 marks)

Inspect images and label associations; visualise class counts and force distributions, distinguishing press and shear. Make **60/20/20 train/validation/test splits**: stratify shape classes; for force split **by `contact_id`** so paired observations never cross sets. Fit any data-dependent normalisation on **training data only**. Store the split identifiers and random seed. Use the test set only for final evaluation.

A meaningful comparison holds splits and evaluation conditions fixed. Image flips or rotations may change force-vector labels and should not be applied without physical justification. Do not train on any extra tactile dataset: Part A uses only the released coursework data (general-purpose ImageNet pretraining is permitted with citation).

## 3. Shape classification (Task 2 : 20 marks)

Implement and compare **at least three distinct CNN architectures**, including a clear baseline and models that genuinely differ in design. For each, report model size, training/inference timings with hardware, accuracy, **macro precision, macro recall, macro F1**, and a confusion matrix. Inspect misclassified images, interpret shape confusions and discuss the generalisation limits of a random image split.

## 4. Force estimation (Task 3 : 20 marks)

Compare **at least two models** predicting `fx, fy, fz` from a **single anonymous image**. Standardise targets using training statistics and convert predictions back to **newtons** for evaluation. Report RMSE for each axis and overall. For both **press** (`is_shear=0`) and **shear** (`is_shear=1`) subsets, report tangential vector error:

```text
RMSE_t = sqrt(mean((pred_fx - true_fx)^2 + (pred_fy - true_fy)^2))
```

For shear images show predicted-versus-true `fx` and `fy` plots with the `y=x` reference. Discuss normal versus tangential error and the worst failures. **Recommended in the simplified handbook:** report a baseline that always predicts the **training-split mean force** (this is required in the earlier full handbook; see [source comparison](SOURCE_ALIGNMENT.md)).

**Never use `contact_id`, `is_shear`, image filenames or test labels as prediction features.**

## 5. Technical report (Task 5 : 10 marks)

Write a **3–6-page IEEE conference-format, double-column** report: Abstract, Introduction, Objectives, Methodology, Experiments, Evaluation, Conclusions and Future Work, followed by references and an AI-use declaration. Include the split protocol, sample images/label distributions, architecture comparisons, training curves, confusion matrix, force RMSE, press/shear tangential error, shear scatter plots and analysis of errors. Cite TacVerse and all reused architectures, pretrained weights and code.

Task 4 (optional) offers **up to five bonus marks** in the newer simplified handbook for systematic hyperparameter tuning: predefine a sensible search space/budget, select on the validation set and report trials. No additional bonuses are described in that newer document.

## 6. Reproducible model submission

Archive name: `DL_Coursework_YourName_CID.zip`.

```text
DL_Coursework_YourName_CID.zip
├── DL_Coursework_YourName_CID.pdf
├── code/                       # reproducible training/evaluation work
└── 01234567/                   # your own eight-digit CID
    ├── predict.py
    ├── shape_model.pt
    ├── force_model.pt
    └── requirements.txt        # optional, only extra pinned packages
```

The grader runs:

```bash
python predict.py --task shape --images <IMAGE_DIR> --out <OUT_CSV>
python predict.py --task force --images <IMAGE_DIR> --out <OUT_CSV>
```

Input: a flat folder of anonymous JPEGs. Output: CSV `filename,class_id` or `filename,fx,fy,fz` (newtons, original sign). Models must load local weights, run on CPU/GPU, download nothing during inference, use a model folder **under 200 MB**, and finish each task within **10 minutes** on a Colab GPU. Perform a clean-environment self-check and share your notebook with the TA at `l.wei24@imperial.ac.uk` as Viewer.

The supplied [example code](../example_submission/README.md) tests the *interface*, not legitimate held-out performance: its demonstration weights were trained on all released images. Do not cite their predictions as independent test results.

## 7. Sources and scope

This page follows the newly uploaded **Simplified Handbook 2026/27** (pp. 2–5) and **Key Information Student Briefing** (slides 10–14 and 23–26). The older full handbook in the repository differs on some bonus and baseline rules. Its authority relative to the new simplified document requires a Canvas clarification; see [source alignment](SOURCE_ALIGNMENT.md). Assessed submissions must go to Canvas, not GitHub.
