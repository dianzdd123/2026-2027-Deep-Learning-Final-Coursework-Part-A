# 2026–2027 Deep Learning Final Coursework — Part A

## Individual project: shape and three-dimensional force from tactile images

[Repository overview](../README.md) · [Handbook and course resources](../resources/README.md) · [Part B guide](PART_B_GUIDE.md) · [Full final project handbook](../resources/2026_2027_DL_Final_Project_Handbook_Shared.pdf)

### Project description

Part A is an individual investigation of visual tactile perception. Students develop and compare models for ten-class shape classification and three-dimensional contact-force estimation from GelSight images, then evaluate their performance, computational cost and failure modes. A separate analysis of tangential force is required. Part A contributes 60 marks; the separate Part B group project contributes 40 marks.

This assignment guide connects the requirements of the 2026/27 Final Project Handbook to the dataset, exploration notebook and submission utilities. The handbook provides the full assessment specification; the module team publishes class-wide clarifications on Canvas. [Handbook §§1.1–1.3, PDF p. 5](../resources/2026_2027_DL_Final_Project_Handbook_Shared.pdf#page=5)

**Deadline: Sunday 13 December 2026, 23:59 UK time (GMT). Submission: Canvas.**

Submit one ZIP containing the report, reproducible code and a model folder named with the eight-digit College ID (CID). Share the Colab notebook with the teaching assistant (TA); for a local Jupyter notebook, the copy in `code/` fulfils this requirement. [Handbook §§2.2 and 9.1, PDF pp. 8 and 33](../resources/2026_2027_DL_Final_Project_Handbook_Shared.pdf#page=33)

### Learning outcomes

The required work develops the ability to:

- Prepare labelled tactile images and construct reproducible evaluation splits that respect physical contact groups.
- Compare classification and regression architectures using task-appropriate metrics and computational evidence.
- Interpret model errors in relation to contact geometry, sensor appearance and force components.
- Present supported conclusions in an academic report and provide a portable inference package.

These outcomes follow the required tasks and marking criteria in [Handbook §§3.3–3.7, PDF pp. 11–16](../resources/2026_2027_DL_Final_Project_Handbook_Shared.pdf#page=11) and [§10.1, PDF pp. 36–37](../resources/2026_2027_DL_Final_Project_Handbook_Shared.pdf#page=36).

### Guide navigation

| Stage | Sections |
|---|---|
| Assessment scope | [Task names and marks](#1-task-names-required-work-and-marks) |
| Data preparation | [Dataset access](#2-understand-and-access-the-dataset) · [Task 1: preparation and splits](#3-task-1-preparation-exploration-and-leakage-free-splits) |
| Model development | [Task 2: shape classification](#4-task-2-compare-at-least-three-cnns-for-shape-classification) · [Task 3: force estimation](#5-task-3-compare-at-least-two-force-estimation-architectures) · [Optional extensions](#6-optional-task-4-and-novel-approaches) |
| Report and submission | [Task 5: report](#7-task-5-write-the-ieee-report) · [Code and inference](#8-code-and-the-hidden-test-model-folder) · [Submission procedure](#9-package-and-submit-part-a) |
| Assessment policies | [Academic integrity, data and AI](#10-academic-integrity-permitted-data-and-ai-tools) · [Bonuses and late work](#11-bonus-marks-early-submission-and-late-work) |
| Final review | [Submission checklist](#12-final-part-a-checklist) |

Handbook version: 2026/27; stated release date: Tuesday 10 November 2026. Citations use PDF page numbers, counting the cover as page 1; printed page numbers are generally one lower.

## 1. Task names, required work and marks

The handbook divides Part A into five numbered tasks. The dataset archive retains the labels “Task A” for shape classification and “Task B” for force estimation; these correspond to handbook Tasks 2 and 3, respectively. Both learning tasks form part of the individual coursework.

| Handbook task | Dataset or workflow | Required work | Required marks |
|---|---|---|---:|
| Task 1: data preparation and preprocessing | Both dataset folders | Correct loading and label association; exploratory analysis; normalisation; 60/20/20 splits | 10 |
| Task 2: shape classification | `shape_classification/`, called “Task A” in the original dataset README | Compare at least three CNN architectures; report classification metrics, efficiency and error analysis | 20 |
| Task 3: force estimation | `force_regression/`, called “Task B” in the original dataset README | Compare at least two architectures; predict three forces; report RMSE and the required tangential analysis | 20 |
| Task 4: hyperparameter tuning | Validation-based model development | Optional systematic search, documented and justified | Bonus only |
| Task 5: evaluation and reporting | Both learning tasks | IEEE-format report, clear figures and tables, supported analysis and conclusions | 10 |
| Total required Part A work | Tasks 1, 2, 3 and 5 | Individual submission | 60 |

Task 1 allocates 4 marks to loading and label associations, 3 to exploratory analysis, and 3 to normalisation and splitting. Tasks 2 and 3 each allocate 10 marks to model design, 5 to metrics and 5 to discussion. Task 5 allocates 10 marks to reporting. Hidden-test results provide evidence of performance and generalisation for Tasks 2 and 3. No minimum accuracy or RMSE threshold is specified; assessment considers the quality of the method, evidence and analysis. The submitted model folder must run successfully. [Handbook §10.1, PDF pp. 36–37](../resources/2026_2027_DL_Final_Project_Handbook_Shared.pdf#page=36); [§15.1, PDF pp. 45–46](../resources/2026_2027_DL_Final_Project_Handbook_Shared.pdf#page=45)

## 2. Understand and access the dataset

GelSight records contact through an internal camera observing an illuminated, deformable gel. Changes in surface appearance provide information about contact geometry. In sensors with markers, marker movement also provides information about deformation and shear. Small, shallow or peripheral contacts can present subtle visual cues. The force-estimation model receives one image at inference, without an undeformed reference image. [Handbook §3.1, PDF pp. 9–10](../resources/2026_2027_DL_Final_Project_Handbook_Shared.pdf#page=9)

| Property | Shape classification | Force estimation |
|---|---|---|
| Released images | 2,000 | 2,000 |
| Sensor described in the handbook | GelSight without markers | GelSight with markers |
| Targets | Ten classes, 200 images each | `fx`, `fy`, `fz` in newtons |
| Grouping | Images of each class use the same physical indenter | 1,000 physical contacts, with one normal-press and one shear image per contact |
| Image format | RGB JPEG, 320 pixels wide × 240 pixels high | RGB JPEG, 320 pixels wide × 240 pixels high |
| Split supplied | None | None |

The coursework data is a curated TacVerse subset. The handbook's force-statistics table describes the full source recording. The [dataset card](DATASET_CARD.md) reports measured statistics for this release; the exploratory analysis should examine the released data directly. [Handbook §3.2 and Table 4, PDF pp. 10–12](../resources/2026_2027_DL_Final_Project_Handbook_Shared.pdf#page=10)

### Download and inspect

Use the [getting-started guide](GETTING_STARTED.md) or the [dataset exploration notebook](../notebooks/01_explore_dataset.ipynb). The complete image archive is distributed as a GitHub release asset. **Code → Download ZIP** retrieves the repository files; download the release archive to obtain the images. Extraction creates the directory `Tactile_DL_2027`.

| Extracted path inside `Tactile_DL_2027/` | Contents |
|---|---|
| `shape_classification/classes.csv` | Fixed class-name-to-ID mapping |
| `shape_classification/labels.csv` | `filename,class_name,class_id` |
| `shape_classification/images/<class_name>/` | Shape images |
| `force_regression/labels.csv` | `filename,contact_id,is_shear,fx,fy,fz` |
| `force_regression/images/` | Normal-press and shear images |
| `example_submission/` | Supplied inference example, example training script and weights |

CSV filenames are relative to their task folder. For example, a force filename `images/contact_0001.jpg` resolves under `Tactile_DL_2027/force_regression/`. In Colab, extracting to `/content` gives the root `/content/Tactile_DL_2027`. [Handbook §3.2, PDF p. 10](../resources/2026_2027_DL_Final_Project_Handbook_Shared.pdf#page=10)

### Class mapping and force conventions

| ID | Class | ID | Class |
|---:|---|---:|---|
| 0 | cylinder | 5 | rectangle |
| 1 | dots | 6 | ring |
| 2 | hexagon | 7 | small_sphere |
| 3 | line | 8 | triangle |
| 4 | moon | 9 | wave |

Retain the supplied class mapping throughout training, evaluation and submitted predictions. For force estimation, `fx` and `fy` are tangential components and `fz` is the normal component, all in the sensor coordinate frame. Negative `fz` means pressing into the sensor. `contact_id` links the two images of a contact; `is_shear = 0` identifies the normal press and `is_shear = 1` the image after lateral displacement. [Handbook §3.2 and Fig. 3, PDF pp. 10–11](../resources/2026_2027_DL_Final_Project_Handbook_Shared.pdf#page=10)

## 3. Task 1: preparation, exploration and leakage-free splits

### Required preparation

Load both label files and associate each image with its corresponding label. The exploratory data analysis (EDA) must include labelled samples, a force press/shear pair, class counts and the distributions of `fx`, `fy` and `fz` separated by press and shear. Interpret the observed patterns, including the relationship between normal force and visible contact. [Handbook §3.3, PDF pp. 11–12](../resources/2026_2027_DL_Final_Project_Handbook_Shared.pdf#page=11)

Normalise pixel intensities and standardise the force targets. Estimate data-derived normalisation parameters from the training split only and apply those fixed values to validation and test data. Retain the force means and standard deviations for conversion back to newtons during inference. Fix random seeds and preserve the split assignments or the code that reproduces them. [Handbook §3.3, PDF p. 12](../resources/2026_2027_DL_Final_Project_Handbook_Shared.pdf#page=12); [§5.7, PDF p. 22](../resources/2026_2027_DL_Final_Project_Handbook_Shared.pdf#page=22)

### Required 60% / 20% / 20% split

| Learning task | Split rule | Training | Validation | Test |
|---|---|---:|---:|---:|
| Shape classification | Stratified by class | 1,200 images, 120 per class | 400 images, 40 per class | 400 images, 40 per class |
| Force estimation | Grouped by `contact_id` | 600 contacts / 1,200 images | 200 contacts / 400 images | 200 contacts / 400 images |

Assign both images of each force contact to the same split and verify that the contact-ID sets do not overlap. Placing a press image in training and its paired shear image in testing would introduce information about the same physical contact into both sets. Report split sizes, class counts and force statistics for each split. The handbook provides `train_test_split` and `GroupShuffleSplit` examples. [Handbook §3.3, PDF p. 12](../resources/2026_2027_DL_Final_Project_Handbook_Shared.pdf#page=12); [Appendix A.1, PDF pp. 47–48](../resources/2026_2027_DL_Final_Project_Handbook_Shared.pdf#page=47)

Use validation data for model and hyperparameter selection, and reserve the test splits for final evaluation. Discuss the scope of the shape-classification evaluation: images within a class originate from the same physical indenter and can be visually similar. Performance on a random stratified split therefore needs to be interpreted within that acquisition setting. [Handbook §§3.3–3.4, PDF pp. 12–14](../resources/2026_2027_DL_Final_Project_Handbook_Shared.pdf#page=12)

### Preprocessing and optional augmentation

Justify the input resolution and treatment of the rectangular image geometry. Resizing, padding and cropping can alter small contact cues or marker detail. Augmentation is optional and may earn up to two bonus marks when its effectiveness and physical validity are demonstrated. Apply it to training data only and provide validation ablations with and without the augmentation. [Handbook §3.3, PDF pp. 12–13](../resources/2026_2027_DL_Final_Project_Handbook_Shared.pdf#page=12)

| Transformation | Physical considerations |
|---|---|
| Flips and rotations | Shape identity is usually preserved. For force images, tangential labels must transform consistently. The correspondence between image axes and force axes is not supplied and must be supported by evidence before applying label transformations. Rotation also changes the marker-grid orientation. |
| Translation or cropping | Keep the contact visible; consider its position relative to the marker grid and gel border. |
| Colour or brightness jitter | Shading carries depth and normal-force information; use physically justified changes and evaluate their effect. |
| Blur or noise | These can remove shallow contact cues or obscure marker positions. |

## 4. Task 2: compare at least three CNNs for shape classification

### Required comparison and assessment evidence

Implement and compare at least three meaningfully different convolutional neural network (CNN) architectures for the ten shape classes. The handbook suggests a small custom CNN, a deeper or residual model, and an efficient or pretrained model as one possible comparison. These examples do not prescribe the architectures. A comparison based only on filter counts provides limited architectural contrast. Non-CNN models, including vision transformers, may be added, but the comparison must still include at least three CNNs. [Handbook §3.4, PDF pp. 13–14](../resources/2026_2027_DL_Final_Project_Handbook_Shared.pdf#page=13); [§15.1, PDF p. 45](../resources/2026_2027_DL_Final_Project_Handbook_Shared.pdf#page=45)

For each model, report:

- Accuracy and macro-averaged precision, recall and F1-score.
- A confusion matrix, with clear class labels and interpretation of confused classes.
- Number of parameters, training time and inference time per image, stating the hardware.
- An analysis of failures, supported by misclassified examples with true and predicted labels.

### Recommended analysis

Interpret the trade-off between accuracy and computational efficiency. Where accuracies are similar, the handbook recommends an additional comparison such as input resolution, training-set size, robustness or a harder evaluation split. Variation across seeds can strengthen the evidence where feasible. Saliency maps or Grad-CAM may help examine whether a model attends to the contact or background. These extensions are recommendations; they supplement the required split and metrics. [Handbook §3.4, PDF pp. 13–14](../resources/2026_2027_DL_Final_Project_Handbook_Shared.pdf#page=13)

### Optional extension

Optimisation and regularisation may earn up to four bonus marks when their effects are demonstrated. The handbook gives dropout, weight decay, label smoothing, early stopping, learning-rate schedules and transfer-learning strategies as examples.

## 5. Task 3: compare at least two force-estimation architectures

### Required comparison and assessment evidence

Compare at least two architectures that predict three continuous force components. Justify the regression head and loss. The handbook describes a linear three-unit output layer trained on standardised targets, with mean squared error (MSE), mean absolute error (MAE) or Huber loss as possible objectives. Explain how the chosen model retains marker information and estimates normal and tangential force from a single frame. Press/shear pairs may supply a training signal; inference must operate on one image. [Handbook §3.5, PDF pp. 14–15](../resources/2026_2027_DL_Final_Project_Handbook_Shared.pdf#page=14); [§15.1, PDF p. 45](../resources/2026_2027_DL_Final_Project_Handbook_Shared.pdf#page=45)

### Exact required RMSE definitions

Convert predictions to the original force scale and sign before evaluation. Let `e = prediction − ground truth`, with `N` evaluated images and force axis `k`. Report root mean squared error (RMSE) in newtons using the following definitions:

$$
\mathrm{RMSE}_k = \sqrt{\frac{1}{N}\sum_{i=1}^{N} e_{ik}^{2}},\qquad k\in\{x,y,z\}.
$$

$$
\mathrm{RMSE}_t = \sqrt{\frac{1}{N}\sum_{i=1}^{N}\left(e_{ix}^{2}+e_{iy}^{2}\right)}.
$$

$$
\mathrm{RMSE}_{\mathrm{all}} = \sqrt{\frac{1}{3N}\sum_{i=1}^{N}\sum_{k\in\{x,y,z\}}e_{ik}^{2}}.
$$

Tangential RMSE measures the root mean squared length of the tangential error vector. Overall RMSE averages squared error across all three force components before taking the square root; it is not the arithmetic mean of the axis-wise RMSE values. MAE and R² are optional additional metrics. [Handbook §3.5, equations (2)–(4), PDF p. 15](../resources/2026_2027_DL_Final_Project_Handbook_Shared.pdf#page=15)

The following reproduces the metric definitions in Appendix A.1. `pred` must be an `(N, 3)` array in `fx, fy, fz` order, aligned with the rows of `df`, and expressed in newtons.

```python
import numpy as np

AX = ["fx", "fy", "fz"]

def tangential_metrics(df, pred):
    """Evaluate aligned predictions in newtons, separately for press and shear."""
    err = pred - df[AX].to_numpy()
    rows = {}
    for name, mask in [
        ("press", df.is_shear.eq(0).to_numpy()),
        ("shear", df.is_shear.eq(1).to_numpy()),
        ("all", np.ones(len(df), bool)),
    ]:
        e = err[mask]
        rows[name] = {
            "RMSE_fx": np.sqrt(np.mean(e[:, 0] ** 2)),
            "RMSE_fy": np.sqrt(np.mean(e[:, 1] ** 2)),
            "RMSE_fz": np.sqrt(np.mean(e[:, 2] ** 2)),
            "RMSE_t": np.sqrt(np.mean(e[:, 0] ** 2 + e[:, 1] ** 2)),
            "RMSE_all": np.sqrt(np.mean(e ** 2)),
        }
    return rows
```

[Handbook Appendix A.1, PDF pp. 47–48](../resources/2026_2027_DL_Final_Project_Handbook_Shared.pdf#page=47)

### Required tangential-force analysis

Half of the force images are normal presses, generally with small tangential components. Aggregate metrics can therefore obscure poor shear estimation. The required analysis has four components:

1. Press/shear table: report `RMSE_fx`, `RMSE_fy`, `RMSE_fz` and `RMSE_t` separately for press (`is_shear = 0`) and shear (`is_shear = 1`) images. Include both models and add the overall results.
2. Mean baseline: in the same table, evaluate a predictor that always returns the mean force vector calculated over all training images.
3. Shear scatter plots: plot predicted versus true `fx` and predicted versus true `fy`, with the `y = x` line.
4. Physical interpretation and failures: compare tangential and normal-force errors, explain the cues used to estimate shear, and show and discuss the worst tangential predictions.

Angular error for shear images with a true tangential magnitude above 0.2 N is optional. At inference, the model must not use `is_shear`, `contact_id` or filename patterns. [Handbook §3.5, PDF p. 15](../resources/2026_2027_DL_Final_Project_Handbook_Shared.pdf#page=15)

### Optional extension

Optimisation and regularisation for force estimation may earn up to four bonus marks when supported by evidence. The handbook suggests loss weighting, robust losses, separate heads, schedules and label-aware augmentation.

## 6. Optional Task 4 and novel approaches

Systematic hyperparameter tuning may earn up to five bonus marks. Document the search space and method, use validation data for selection, report the trials and sensitivity to important settings, and justify the selected configuration. Reporting only the best result from an undocumented sequence of trials does not meet this criterion. [Handbook §3.6, PDF pp. 15–16](../resources/2026_2027_DL_Final_Project_Handbook_Shared.pdf#page=15)

A novel approach may earn up to five bonus marks when clearly explained, evaluated and justified. Examples include combining marker features with learned features, using press/shear pairing during training, or incorporating marker-grid structure into the model. The permitted-data and inference rules apply to all optional work. [Handbook §3.8, PDF p. 16](../resources/2026_2027_DL_Final_Project_Handbook_Shared.pdf#page=16)

## 7. Task 5: write the IEEE report

### Format and length

Prepare a 3–6 page report using the official IEEE conference template in double-column format. Preserve the template's margins, column widths, line spacing and fonts. The page limit includes all content through Conclusions and Future Work; references and the AI-use declaration may extend beyond page 6. Replace the template placeholders and use the filename `DL_Coursework_YourName_CID.pdf`. [Handbook §4.1, PDF pp. 16–17](../resources/2026_2027_DL_Final_Project_Handbook_Shared.pdf#page=16)

### Required sections, in order

| Section | Evidence to include |
|---|---|
| Abstract | One paragraph covering the problem, approach, key numerical results and conclusion; include classification performance and force results, including shear tangential error |
| Introduction | Tactile-sensing background, motivation, challenges, related work and your contributions |
| Objectives | Specific aims against which your work can be assessed |
| Methodology | Data pipeline, EDA findings, normalisation, split, any augmentation, architectures, losses and training setup |
| Experiments | What you compared, why, and sufficient detail to reproduce it |
| Evaluation | Architecture comparisons, metrics, efficiency, required tangential analysis, interpretation and failure cases |
| Conclusions and Future Work | Answers to your objectives, key findings, limitations and concrete next steps; no new results |
| References | Sources in IEEE numbered style |
| AI-use declaration | The required disclosure after the references, including a statement if no AI tools were used |

[Handbook §§4.1–4.2, PDF pp. 16–18](../resources/2026_2027_DL_Final_Project_Handbook_Shared.pdf#page=16)

### Presentation of experimental evidence

The report provides the evidence used to assess Tasks 1–4. The handbook recommends organising that evidence around a split table; sample images and label distributions; training and validation curves; shape-architecture and efficiency comparisons; a confusion matrix and misclassified examples; force-architecture results; the required press/shear baseline comparison, scatter plots and tangential failures; and tuning results where applicable. Distinguish validation and test results explicitly. [Handbook §4.3, PDF p. 18](../resources/2026_2027_DL_Final_Project_Handbook_Shared.pdf#page=18)

Figures and tables must be legible at column width, cited in the text and consistent in terminology and units. Place informative figure captions below figures and table titles above tables. Label axes, use accessible colours and maintain consistent numerical precision.

Follow the handbook's template conventions: exclude symbols, special characters, footnotes and mathematics from the title and abstract; define abbreviations at first use in the main text; use SI units; number equations and define their symbols; and use IEEE citation style. [Handbook §§4.3–4.5, PDF pp. 18–19](../resources/2026_2027_DL_Final_Project_Handbook_Shared.pdf#page=18)

Cite the dataset, architectures, pretrained weights, libraries and adapted code. The literature review should engage with tactile sensing as well as relevant deep-learning methods. The [AI-use rules](#ai-use-rules) distinguish permitted language assistance from prohibited generation of whole report sections.

## 8. Code and the hidden-test model folder

Place preprocessing, training, evaluation and optional tuning notebooks or scripts in `code/`. The code must reproduce the reported results. Explain the architectures and task handling in comments, verify that the notebook runs without errors after a restart, and retain its plots, metrics and training logs. Print library versions, fix seeds and specify the data root in an accessible configuration variable. Frameworks pre-installed in Colab, including PyTorch and TensorFlow/Keras, are permitted. [Handbook §§5.1 and 5.7, PDF pp. 19–22](../resources/2026_2027_DL_Final_Project_Handbook_Shared.pdf#page=19)

### Model folder contents

Name the separate inference folder with the eight-digit CID, for example `01234567/`. Include `predict.py`, all trained weights required for inference, any imported helper modules and, where needed, a `requirements.txt` for additional packages. The model folder must be under 200 MB. [Handbook §§5.2–5.4, PDF pp. 20–21](../resources/2026_2027_DL_Final_Project_Handbook_Shared.pdf#page=20)

### Exact prediction interface

The grading script executes the following commands from inside the CID model folder:

```bash
python predict.py --task shape --images <IMAGE_DIR> --out <OUT_CSV>
python predict.py --task force --images <IMAGE_DIR> --out <OUT_CSV>
```

`<IMAGE_DIR>` is a flat directory of `.jpg` files without labels or class subdirectories. Hidden-test images have anonymous names, such as `test_0001.jpg`, and the same 320 × 240 RGB preprocessing as the release. Each output CSV must contain one row per image:

| Argument | Required CSV columns, in order | Required values |
|---|---|---|
| `--task shape` | `filename,class_id` | Image basename and integer ID 0–9 using `classes.csv` |
| `--task force` | `filename,fx,fy,fz` | Image basename and forces in newtons, on the original scale and sign |

The `filename` column contains the basename only, without a directory path. Hidden-test evaluation uses accuracy and macro F1 for shape classification, and axis-wise, overall and tangential RMSE for force estimation. Submissions that do not conform to the interface cannot be scored. [Handbook §5.3, PDF p. 20](../resources/2026_2027_DL_Final_Project_Handbook_Shared.pdf#page=20)

### Runtime and portability rules

- Include the model definition, preprocessing and weight-loading code in `predict.py` or your supplied helper files.
- Load weights relative to the script, for example `Path(__file__).parent / "shape_model.pt"`; do not use absolute paths to your computer or Drive.
- Use a GPU when available, and also support CPU execution.
- Download nothing at prediction time. Include every required weight file and prevent model construction from initiating a pretrained-weight download.
- Each task must finish within 10 minutes on a Colab GPU runtime.
- Use image content alone, without contact IDs, shear indicators or filename patterns.
- If needed, list only extra packages absent from Colab in the model folder's `requirements.txt`, one per line with pinned versions. Do not list `torch` or `torchvision` there: the Colab versions are used.

[Handbook §5.4, PDF p. 21](../resources/2026_2027_DL_Final_Project_Handbook_Shared.pdf#page=21)

Select the best checkpoint using validation data and retain the force-standardisation constants with the weights. For PyTorch, the handbook recommends tensors and plain Python lists compatible with `weights_only=True`, avoiding NumPy arrays or custom checkpoint objects. For Keras, use `.keras` with a consistent loading procedure. The FAQ permits final retraining on the combined training and validation data if disclosed; all reported results must still come from untouched test splits. [Handbook §5.5, PDF p. 21](../resources/2026_2027_DL_Final_Project_Handbook_Shared.pdf#page=21); [§15.1, PDF p. 45](../resources/2026_2027_DL_Final_Project_Handbook_Shared.pdf#page=45)

### Supplied example and self-check

The supplied [`example_submission/`](../example_submission/) demonstrates the required inference interface. Its training script uses all released images without a split. The example weights therefore do not provide an independent evaluation under the coursework protocol. Assessed models must be developed and evaluated using the required splits. [Handbook §5.2, PDF p. 20](../resources/2026_2027_DL_Final_Project_Handbook_Shared.pdf#page=20)

Verify the model folder in a fresh Colab runtime. The handbook's sample-copying procedure uses a stride of 99 to include both press and shear observations:

```python
import shutil
from pathlib import Path

data = Path("/content/Tactile_DL_2027")
for task, pattern in [
    ("shape", "shape_classification/images/*/*.jpg"),
    ("force", "force_regression/images/*.jpg"),
]:
    dst = Path(f"/content/check_{task}")
    dst.mkdir(exist_ok=True)
    for f in sorted(data.glob(pattern))[::99]:
        shutil.copy(f, dst)
```

From the CID folder, run both prediction commands using the sample folders and inspect the output CSVs. Install additional dependencies first if the optional requirements file is present. Verify row counts, filenames, columns, class IDs, force scale and reasonable agreement with the sample labels. Check CPU and GPU execution, then repeat the procedure after extracting the final ZIP to a new location. The self-check verifies the interface and loading procedure; held-out evaluation remains a separate requirement. [Handbook §5.6, PDF pp. 21–22](../resources/2026_2027_DL_Final_Project_Handbook_Shared.pdf#page=21); [§14.1, PDF p. 44](../resources/2026_2027_DL_Final_Project_Handbook_Shared.pdf#page=44)

## 9. Package and submit Part A

Submit one archive named `DL_Coursework_YourName_CID.zip`, with the following top-level contents:

| ZIP entry | Contents |
|---|---|
| `DL_Coursework_YourName_CID.pdf` | Your IEEE report |
| `code/` | Notebooks or scripts for preprocessing, training, evaluation and any tuning |
| `<your eight-digit CID>/` | `predict.py`, trained weights, helper modules and optional extra requirements |

For example, the filename for Jane Smith, CID `01234567`, is `DL_Coursework_JaneSmith_01234567.zip`. [Handbook §§2.1 and 9.1, PDF pp. 7–8 and 33](../resources/2026_2027_DL_Final_Project_Handbook_Shared.pdf#page=33)

Complete the following procedure before Sunday 13 December 2026 at 23:59 GMT:

1. Restart and run the notebook. Retain its outputs and verify that it reproduces the reported results.
2. Assemble and test the CID model folder in a fresh runtime.
3. Export the report, assemble the ZIP, extract it to a new location and repeat the inference self-check.
4. Upload the ZIP to the Part A assignment on Canvas.
5. For Colab, provide viewer access to the TA, Lan Wei (`l.wei24@imperial.ac.uk`). For local Jupyter work, include the notebook in `code/`. Do not edit the shared notebook after the deadline. The notebook copy in the submitted ZIP is the version assessed.

[Handbook §9.1, PDF p. 33](../resources/2026_2027_DL_Final_Project_Handbook_Shared.pdf#page=33)

If Canvas fails near the deadline, email the TA before the deadline with a share link to the submission files and a screenshot of the error. The handbook treats this as an on-time submission provided the files remain unchanged afterwards. [Handbook §9.4, PDF p. 35](../resources/2026_2027_DL_Final_Project_Handbook_Shared.pdf#page=35)

## 10. Academic integrity, permitted data and AI tools

### Individual work and permitted data

Part A is individual work. Do not share assessed code, models, results or reports with other students, including members of the Part B group. Cite adapted code in comments and the README, and ensure that it is understood. Acknowledge all other sources and assets. Report results faithfully: fabrication, alteration of results and test-set model selection are prohibited. The module team may ask a student to explain any part of the submission. [Handbook §11.1, PDF p. 40](../resources/2026_2027_DL_Final_Project_Handbook_Shared.pdf#page=40)

Part A training and validation must use only the released coursework data. Additional TacVerse data and other tactile datasets are not permitted. General-purpose pretrained weights, such as those trained on ImageNet, are allowed with attribution. Part B excludes both the Part A dataset and the GelSight subsets of TacVerse; its separate requirements are set out in the [Part B guide](PART_B_GUIDE.md). [Handbook §11.3, PDF p. 41](../resources/2026_2027_DL_Final_Project_Handbook_Shared.pdf#page=41)

These data restrictions follow the explicit rule in §11.3. The [handbook notes](HANDBOOK_NOTES.md) identify passages requiring clarification.

### AI-use rules

| Use | Handbook rule |
|---|---|
| Brainstorming, concept explanations or debugging | Allowed; declare it |
| Generating or completing code | Allowed; declare it, understand and test it, and be able to explain every line |
| Improving the grammar or clarity of text you wrote | Allowed; declare it |
| Video-editing, caption or graphics assistance | Allowed; declare it and label AI-generated images in the video |
| Writing whole sections of the Part A report | Not allowed; the ideas, analysis and wording must be yours |
| AI voices, avatars or deepfakes presenting instead of group members | Not allowed in Part B, except for a reasonable adjustment agreed with the module team under §7.2 |
| Generating or changing data, results or references | Never permitted; check that references exist and support the associated claims |

Include the following four-line AI-use declaration after the references. State explicitly if no AI tools were used:

```text
Tools used (name and version):
What we used them for:
Which parts of the submission they affected:
How we checked the output:
```

[Handbook §11.2, PDF p. 40](../resources/2026_2027_DL_Final_Project_Handbook_Shared.pdf#page=40); [presenter-adjustment provision in §7.2, PDF p. 27](../resources/2026_2027_DL_Final_Project_Handbook_Shared.pdf#page=27)

## 11. Bonus marks, early submission and late work

Optional work may receive the bonuses below, awarded against the stated criteria at the instructors' discretion. The combined bonus is capped at 15 marks per student, and the final project mark cannot exceed 100. [Handbook §10.4, PDF p. 38](../resources/2026_2027_DL_Final_Project_Handbook_Shared.pdf#page=38)

| Optional work | Maximum bonus |
|---|---:|
| Effective, physically justified data augmentation | +2 |
| Evidenced shape-model optimisation and regularisation | +4 |
| Evidenced force-model optimisation and regularisation | +4 |
| Systematic, justified hyperparameter tuning | +5 |
| Creative, well-documented and justified novel approach | +5 |
| Early submission | +3 or +5, subject to the cut-offs below |

For Part A, submission before 23:59 on Sunday 29 November 2026 qualifies for the +5 early-submission window. Submission by 23:59 on Sunday 6 December 2026 qualifies for +3 when the +5 window has not been met. These alternative levels count towards the overall bonus cap. [Handbook §9.3, PDF p. 35](../resources/2026_2027_DL_Final_Project_Handbook_Shared.pdf#page=35)

The late penalty is 5 marks per day for up to seven days. After seven days, the submitted item receives zero. Extensions require exceptional circumstances, an advance application and appropriate documentation through the College process. College policy applies where it differs from the handbook. [Handbook §9.3, PDF p. 35](../resources/2026_2027_DL_Final_Project_Handbook_Shared.pdf#page=35)

## 12. Final Part A checklist

Review the following before submission, together with the complete checklist in [Handbook §14.1, PDF pp. 43–44](../resources/2026_2027_DL_Final_Project_Handbook_Shared.pdf#page=43).

- [ ] Both tasks are included, with correct image-to-label associations and interpreted EDA.
- [ ] Shape splits are stratified 60/20/20; force splits are 60/20/20 by contact with no overlap.
- [ ] Normalisation parameters come from training data only; force standardisation is reversed for metrics and predictions.
- [ ] At least three CNN shape architectures and at least two force architectures are compared.
- [ ] Shape metrics, efficiency, confusion patterns and misclassified examples are analysed.
- [ ] Axis-wise and overall force RMSE are in newtons; the press/shear table, mean baseline, shear scatter plots and worst tangential cases are included and discussed.
- [ ] Model selection used validation data; reported final numbers use untouched test splits.
- [ ] The IEEE report meets the 3–6 page rule, required section order and figure/table requirements; sources and AI use are declared.
- [ ] The CID model folder is under 200 MB, contains all weights, downloads nothing during prediction, follows both command interfaces and runs on CPU and GPU.
- [ ] Each task meets the 10-minute Colab GPU limit; both CSVs have the required rows, columns, labels and units.
- [ ] The final ZIP was extracted and checked in a new location; the code is commented, runs cleanly and retains notebook outputs.
- [ ] The correctly named ZIP is submitted on Canvas before the deadline, with notebook access handled as in §9.1.

Contact Dr Dandan Zhang, module leader (`d.zhang17@imperial.ac.uk`), or Ms Lan Wei, teaching assistant (`l.wei24@imperial.ac.uk`), for assessment queries. The module team publishes class-wide clarifications on Canvas. [Handbook §1.3, PDF p. 5](../resources/2026_2027_DL_Final_Project_Handbook_Shared.pdf#page=5)

## Sources and dataset attribution

The [2026/27 Final Project Handbook](../resources/2026_2027_DL_Final_Project_Handbook_Shared.pdf) is the source of the assessment requirements, with section and page citations throughout this guide. The [original dataset README](ORIGINAL_DATASET_README.md) records the source package and its task labels.

The source dataset is TacVerse: L. Wei, G. Khurana, S. Bhouri, W. Hong, Z. Xin, Q. Cong, W. Fan, Y. Xiang and D. Zhang, “TacVerse: A Multisensor Dataset and Benchmark for Cross-Sensor Vision-Based Tactile Perception”, *Advanced Robotics Research*, 2026, [doi:10.1002/adrr.70169](https://doi.org/10.1002/adrr.70169). See the [dataset card](DATASET_CARD.md) for release-specific provenance, inventory, statistics and limitations.
