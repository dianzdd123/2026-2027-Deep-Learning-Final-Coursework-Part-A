# 2026–2027 Deep Learning Final Coursework — Part A

## Individual project: shape and three-dimensional force from tactile images

[Repository overview](../README.md) · [Handbook and course resources](../resources/README.md) · [Part B guide](PART_B_GUIDE.md) · [Full final project handbook](../resources/2026_2027_DL_Final_Project_Handbook_Shared.pdf)

This guide organises the **Part A requirements in the 2026/27 Final Project Handbook** and connects them to the dataset and tools in this repository. Part A is individual coursework worth **60 marks**. It requires both shape classification and three-dimensional force estimation, including a separate analysis of tangential force. Part B is a separate group project worth 40 marks. Use the linked handbook for the complete assessment specification and check Canvas for any class-wide clarification from the module team. [Handbook §§1.1–1.3, PDF p. 5](../resources/2026_2027_DL_Final_Project_Handbook_Shared.pdf#page=5)

**Part A deadline: Sunday 13 December 2026, 23:59 UK time (GMT). Submit through Canvas.** Your submission is one ZIP containing your report, reproducible code and a model folder named with your eight-digit College ID (CID). Share your Colab notebook with the TA; for a local Jupyter notebook, the copy in `code/` covers this requirement. [Handbook §§2.2 and 9.1, PDF pp. 8 and 33](../resources/2026_2027_DL_Final_Project_Handbook_Shared.pdf#page=33)

The handbook cover identifies the version as **2026/27**, with the stated release date **Tuesday 10 November 2026**. Links below use **PDF page numbers**, counting the cover as page 1; the printed page numbers are generally one lower.

## 1. Task names, required work and marks

The archive's original README uses **Task A** for shape classification and **Task B** for force estimation. Both belong to **Part A of the final coursework**. The handbook uses numbered tasks:

| Handbook task | Dataset or workflow | Required work | Required marks |
|---|---|---|---:|
| **Task 1: data preparation and preprocessing** | Both dataset folders | Correct loading and label association; exploratory analysis; normalisation; 60/20/20 splits | 10 |
| **Task 2: shape classification** | `shape_classification/`, called “Task A” in the original dataset README | Compare **at least three CNN architectures**; report classification metrics, efficiency and error analysis | 20 |
| **Task 3: force estimation** | `force_regression/`, called “Task B” in the original dataset README | Compare **at least two architectures**; predict three forces; report RMSE and the required tangential analysis | 20 |
| **Task 4: hyperparameter tuning** | Validation-based model development | Optional systematic search, documented and justified | Bonus only |
| **Task 5: evaluation and reporting** | Both learning tasks | IEEE-format report, clear figures and tables, supported analysis and conclusions | 10 |
| **Total required Part A work** | Tasks 1, 2, 3 and 5 | Individual submission | **60** |

The detailed allocation is 4 + 3 + 3 marks for Task 1; 10 for model design, 5 for metrics and 5 for discussion in each of Tasks 2 and 3; and 10 for the report. Hidden-test results support the assessment of performance and generalisation in Tasks 2 and 3. There is **no minimum accuracy or RMSE threshold**: the handbook emphasises method, evidence and analysis, while requiring your model folder to run. [Handbook §10.1, PDF pp. 36–37](../resources/2026_2027_DL_Final_Project_Handbook_Shared.pdf#page=36); [§15.1, PDF pp. 45–46](../resources/2026_2027_DL_Final_Project_Handbook_Shared.pdf#page=45)

## 2. Understand and access the dataset

GelSight uses an internal camera to observe an illuminated, deformable gel. Contact changes the appearance of the gel. Marker-free images provide information about contact shape; in marked images, marker movement also carries information about deformation and shear. Contacts may be small, shallow or close to the edge. At prediction time, the force model sees **one image**, without an undeformed reference image. [Handbook §3.1, PDF pp. 9–10](../resources/2026_2027_DL_Final_Project_Handbook_Shared.pdf#page=9)

| Property | Shape classification | Force estimation |
|---|---|---|
| Released images | 2,000 | 2,000 |
| Sensor described in the handbook | GelSight without markers | GelSight with markers |
| Targets | Ten classes, 200 images each | `fx`, `fy`, `fz` in newtons |
| Grouping | Images of each class use the same physical indenter | 1,000 physical contacts, with one normal-press and one shear image per contact |
| Image format | RGB JPEG, 320 pixels wide × 240 pixels high | RGB JPEG, 320 pixels wide × 240 pixels high |
| Split supplied | None | None |

The coursework data is a curated TacVerse subset. The handbook's force-statistics table describes the **full source recording**, rather than an exact audit of this release. Use the [dataset card](DATASET_CARD.md) and your own exploration for the released subset's measured statistics. [Handbook §3.2 and Table 4, PDF pp. 10–12](../resources/2026_2027_DL_Final_Project_Handbook_Shared.pdf#page=10)

### Download and inspect

Follow the [repository download instructions](../README.md#2-download-and-start-exploring) or run [`notebooks/01_explore_dataset.ipynb`](../notebooks/01_explore_dataset.ipynb). The complete image archive is a **release asset**; GitHub's **Code → Download ZIP** downloads the repository files without that archive. After extraction, the dataset directory is `Tactile_DL_2027`.

| Extracted path inside `Tactile_DL_2027/` | Contents |
|---|---|
| `shape_classification/classes.csv` | Fixed class-name-to-ID mapping |
| `shape_classification/labels.csv` | `filename,class_name,class_id` |
| `shape_classification/images/<class_name>/` | Shape images |
| `force_regression/labels.csv` | `filename,contact_id,is_shear,fx,fy,fz` |
| `force_regression/images/` | Normal-press and shear images |
| `example_submission/` | Supplied inference example, example training script and weights |

CSV filenames are relative to **their task folder**. For example, a force filename `images/contact_0001.jpg` resolves under `Tactile_DL_2027/force_regression/`. In Colab, extracting to `/content` gives the root `/content/Tactile_DL_2027`. [Handbook §3.2, PDF p. 10](../resources/2026_2027_DL_Final_Project_Handbook_Shared.pdf#page=10)

### Class mapping and force conventions

| ID | Class | ID | Class |
|---:|---|---:|---|
| 0 | cylinder | 5 | rectangle |
| 1 | dots | 6 | ring |
| 2 | hexagon | 7 | small_sphere |
| 3 | line | 8 | triangle |
| 4 | moon | 9 | wave |

Use this mapping in every experiment and in the submitted predictions. For force estimation, `fx` and `fy` are tangential components and `fz` is the normal component, all in the sensor coordinate frame. **Negative `fz` means pressing into the sensor.** `contact_id` links the two images of a contact; `is_shear = 0` identifies the normal press and `is_shear = 1` the image after lateral displacement. [Handbook §3.2 and Fig. 3, PDF pp. 10–11](../resources/2026_2027_DL_Final_Project_Handbook_Shared.pdf#page=10)

## 3. Task 1: preparation, exploration and leakage-free splits

### Required preparation

Load both label files and associate every image with its correct label. Display labelled samples, including a force press/shear pair. Analyse the class counts and the distributions of `fx`, `fy` and `fz` separately for press and shear images; explain the patterns you observe and how normal force relates to visible contact. EDA needs interpretation as well as plots. [Handbook §3.3, PDF pp. 11–12](../resources/2026_2027_DL_Final_Project_Handbook_Shared.pdf#page=11)

Normalise pixel intensities and **standardise the force targets**. Fit any data-derived normalisation parameters on the **training split only**, then apply the same values to validation and test data. Save the force means and standard deviations so the inference script can return newtons. Fix your random seeds and save your split assignments or the code that recreates them. [Handbook §3.3, PDF p. 12](../resources/2026_2027_DL_Final_Project_Handbook_Shared.pdf#page=12); [§5.7, PDF p. 22](../resources/2026_2027_DL_Final_Project_Handbook_Shared.pdf#page=22)

### Required 60% / 20% / 20% split

| Learning task | Split rule | Training | Validation | Test |
|---|---|---:|---:|---:|
| Shape classification | **Stratified by class** | 1,200 images, 120 per class | 400 images, 40 per class | 400 images, 40 per class |
| Force estimation | **Grouped by `contact_id`** | 600 contacts / 1,200 images | 200 contacts / 400 images | 200 contacts / 400 images |

Keep both images of every force contact together. Check that no contact ID occurs in more than one split: a press in training and its paired shear image in testing would leak information about the same physical contact. The handbook supplies `train_test_split` and `GroupShuffleSplit` examples. Report split sizes, per-class counts and force statistics per split. [Handbook §3.3, PDF p. 12](../resources/2026_2027_DL_Final_Project_Handbook_Shared.pdf#page=12); [Appendix A.1, PDF pp. 47–48](../resources/2026_2027_DL_Final_Project_Handbook_Shared.pdf#page=47)

Choose models and settings using validation data. Keep the test splits for final evaluation. Discuss the scope of the shape test: images within a class can be very similar and come from the same physical indenter, so high performance on a random stratified split does not establish every kind of generalisation. [Handbook §§3.3–3.4, PDF pp. 12–14](../resources/2026_2027_DL_Final_Project_Handbook_Shared.pdf#page=12)

### Preprocessing and optional augmentation

Explain your resolution choice. The original images are rectangular; resizing, padding or cropping can affect small contacts and marker detail. Augmentation is optional, applies to **training data only**, and earns up to two bonus marks when effective and physically justified. Show validation ablations with and without the augmentations you claim. [Handbook §3.3, PDF pp. 12–13](../resources/2026_2027_DL_Final_Project_Handbook_Shared.pdf#page=12)

| Transformation | What needs checking |
|---|---|
| Flips and rotations | Shape identity is usually preserved. For force images, the tangential labels must transform consistently. The image-axis-to-force-axis mapping is **not supplied**: justify it with evidence rather than assuming which force component changes sign. Rotation also changes the marker-grid orientation. |
| Translation or cropping | Keep the contact visible; consider its position relative to the marker grid and gel border. |
| Colour or brightness jitter | Shading carries depth and normal-force information; use physically justified changes and evaluate their effect. |
| Blur or noise | These can remove shallow contact cues or obscure marker positions. |

## 4. Task 2: compare at least three CNNs for shape classification

Implement and compare **at least three meaningfully different CNN architectures**, tailored for the ten classes. The handbook gives a small custom CNN, a stronger/residual model and an efficient or pretrained model as examples, rather than prescribing those exact choices. Changing only the number of filters makes a weak architectural comparison. Non-CNN models, such as a vision transformer, may be additional comparisons, but do not replace the three required CNNs. [Handbook §3.4, PDF pp. 13–14](../resources/2026_2027_DL_Final_Project_Handbook_Shared.pdf#page=13); [§15.1, PDF p. 45](../resources/2026_2027_DL_Final_Project_Handbook_Shared.pdf#page=45)

For each model, report:

- Accuracy and **macro-averaged precision, recall and F1-score**.
- A confusion matrix, with clear class labels and interpretation of confused classes.
- Number of parameters, training time and inference time per image, stating the hardware.
- An analysis of failures, supported by misclassified examples with true and predicted labels.

Explain the accuracy–efficiency trade-off. If models have almost identical accuracy, make the comparison informative through another supported axis, such as resolution, data efficiency, robustness or a harder split. The handbook encourages variation across seeds where feasible. Saliency or Grad-CAM can support analysis of whether the model attends to the contact or background. These are suggestions for stronger evidence; the required baseline split and metrics remain as specified above. [Handbook §3.4, PDF pp. 13–14](../resources/2026_2027_DL_Final_Project_Handbook_Shared.pdf#page=13)

Optimisation and regularisation are optional bonus work, worth up to four additional marks for this task when their effects are evidenced. Examples in the handbook include dropout, weight decay, label smoothing, early stopping, schedules and transfer-learning strategies.

## 5. Task 3: compare at least two force-estimation architectures

Implement a model with **three continuous outputs** and compare **at least two architectures**. Explain the output head and loss. The handbook describes a linear three-unit output layer trained on standardised targets, with MSE, MAE or Huber loss as possible choices. Discuss how the model retains marker information and estimates normal and tangential force from one frame. The press/shear pairing may provide a training signal, but inference receives only a single image. [Handbook §3.5, PDF pp. 14–15](../resources/2026_2027_DL_Final_Project_Handbook_Shared.pdf#page=14); [§15.1, PDF p. 45](../resources/2026_2027_DL_Final_Project_Handbook_Shared.pdf#page=45)

### Exact required RMSE definitions

Convert predictions back to the **original force scale and sign** before evaluation. With error `e = prediction − ground truth`, report every RMSE in **newtons**:

$$
\mathrm{RMSE}_k = \sqrt{\frac{1}{N}\sum_{i=1}^{N} e_{ik}^{2}},\qquad k\in\{x,y,z\}.
$$

$$
\mathrm{RMSE}_t = \sqrt{\frac{1}{N}\sum_{i=1}^{N}\left(e_{ix}^{2}+e_{iy}^{2}\right)}.
$$

$$
\mathrm{RMSE}_{\mathrm{all}} = \sqrt{\frac{1}{3N}\sum_{i=1}^{N}\sum_{k\in\{x,y,z\}}e_{ik}^{2}}.
$$

Tangential RMSE is the root mean squared **length of the tangential error vector**, while overall RMSE averages squared error across all three components. Do not substitute a mean of the three axis-wise RMSE values. MAE and R² are optional extras. [Handbook §3.5, equations (2)–(4), PDF p. 15](../resources/2026_2027_DL_Final_Project_Handbook_Shared.pdf#page=15)

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

Half of the force images are normal presses, typically with small tangential components. Aggregate error can therefore conceal poor shear prediction. Include all four elements below:

1. **Press/shear table:** report `RMSE_fx`, `RMSE_fy`, `RMSE_fz` and `RMSE_t` separately for press (`is_shear = 0`) and shear (`is_shear = 1`) images. Include both models and add the overall results.
2. **Mean baseline:** in the same table, evaluate a predictor that always returns the mean force vector calculated over **all training images**.
3. **Shear scatter plots:** plot predicted versus true `fx` and predicted versus true `fy`, with the `y = x` line.
4. **Physical interpretation and failures:** compare tangential and normal-force errors, explain the cues used to estimate shear, and show and discuss the worst tangential predictions.

An optional extra is angular error for shear images whose true tangential magnitude exceeds 0.2 N. At prediction time, neither `is_shear`, `contact_id` nor filename patterns may be used. [Handbook §3.5, PDF p. 15](../resources/2026_2027_DL_Final_Project_Handbook_Shared.pdf#page=15)

Optimisation and regularisation for force estimation are optional, worth up to four bonus marks with evidence. The handbook suggests possibilities such as loss weighting, robust losses, separate heads, schedules or label-aware augmentation.

## 6. Optional Task 4 and novel approaches

Systematic tuning can earn up to five bonus marks. Define a search space, choose a search method, select using **validation data only**, report the trials and sensitivity, and justify the final settings. Reporting only the best result after informal trial and error does not satisfy the handbook's description of systematic tuning. [Handbook §3.6, PDF pp. 15–16](../resources/2026_2027_DL_Final_Project_Handbook_Shared.pdf#page=15)

A creative approach can earn up to five bonus marks if clearly explained, tested and justified. Handbook examples include combining marker features with learned features, exploiting the press/shear pairing during training, or designing around the marker grid. All optional work remains subject to the permitted-data and inference rules. [Handbook §3.8, PDF p. 16](../resources/2026_2027_DL_Final_Project_Handbook_Shared.pdf#page=16)

## 7. Task 5: write the IEEE report

### Format and length

Use the official **IEEE conference template**, in double-column format, without changing its margins, column widths, line spacing or fonts. The report is **3–6 pages through the end of Conclusions and Future Work**; references and the AI-use declaration may extend beyond page 6. Replace the template placeholders and name the PDF `DL_Coursework_YourName_CID.pdf`. [Handbook §4.1, PDF pp. 16–17](../resources/2026_2027_DL_Final_Project_Handbook_Shared.pdf#page=16)

### Required sections, in order

| Section | Evidence to include |
|---|---|
| **Abstract** | One paragraph covering the problem, approach, key numerical results and conclusion; include classification performance and force results, including shear tangential error |
| **Introduction** | Tactile-sensing background, motivation, challenges, related work and your contributions |
| **Objectives** | Specific aims against which your work can be assessed |
| **Methodology** | Data pipeline, EDA findings, normalisation, split, any augmentation, architectures, losses and training setup |
| **Experiments** | What you compared, why, and sufficient detail to reproduce it |
| **Evaluation** | Architecture comparisons, metrics, efficiency, required tangential analysis, interpretation and failure cases |
| **Conclusions and Future Work** | Answers to your objectives, key findings, limitations and concrete next steps; no new results |
| **References** | Sources in IEEE numbered style |
| **AI-use declaration** | The required disclosure after the references, including a statement if no AI tools were used |

[Handbook §§4.1–4.2, PDF pp. 16–18](../resources/2026_2027_DL_Final_Project_Handbook_Shared.pdf#page=16)

Use the report to show the evidence behind Tasks 1–4. The handbook recommends a split table; sample images and distributions; training/validation curves; shape architecture and efficiency comparisons; a confusion matrix and misclassified examples; force architecture results; the press/shear/mean-baseline table; shear scatter plots; worst tangential predictions; and tuning results if applicable. Label validation and test results clearly. [Handbook §4.3, PDF p. 18](../resources/2026_2027_DL_Final_Project_Handbook_Shared.pdf#page=18)

Figures and tables must be readable at column width, cited in the text and consistent in naming and units. Give figures informative captions below them and tables titles above them. Use labelled axes, accessible colours and consistent numerical precision. Follow the handbook's template rules: no symbols, special characters, footnotes or mathematics in the title or abstract; define abbreviations on first use in the main text; use SI units; number and define equations; and cite sources using IEEE style. [Handbook §§4.3–4.5, PDF pp. 18–19](../resources/2026_2027_DL_Final_Project_Handbook_Shared.pdf#page=18)

Cite the dataset, architectures, pretrained weights, libraries and adapted code you used. The handbook recommends starting from tactile literature as well as general deep-learning sources. Do not present generated text as your own report writing; the AI rules below apply.

## 8. Code and the hidden-test model folder

Put your preprocessing, training, evaluation and optional tuning notebooks or scripts in `code/`. The code must reproduce the report's numbers. Comment the architectures and task handling; restart and run the notebook without errors; save its plots, metrics and training logs. Print library versions, fix seeds and make the data root easy to change. Frameworks pre-installed in Colab, including PyTorch or TensorFlow/Keras, are permitted. [Handbook §§5.1 and 5.7, PDF pp. 19–22](../resources/2026_2027_DL_Final_Project_Handbook_Shared.pdf#page=19)

### Model folder contents

The separate inference folder is named with your **eight-digit CID**, for example `01234567/`. Include `predict.py`, all required trained weight files, any imported helper modules, and an optional `requirements.txt` for extra packages. Keep this folder **under 200 MB**. [Handbook §§5.2–5.4, PDF pp. 20–21](../resources/2026_2027_DL_Final_Project_Handbook_Shared.pdf#page=20)

### Exact prediction interface

The grader runs these commands **from inside your CID model folder**:

```bash
python predict.py --task shape --images <IMAGE_DIR> --out <OUT_CSV>
python predict.py --task force --images <IMAGE_DIR> --out <OUT_CSV>
```

`<IMAGE_DIR>` is a **flat folder of `.jpg` files**, without class folders or labels. Hidden-test images have anonymous names such as `test_0001.jpg` and the same 320 × 240 RGB preprocessing as the release. Write **one row per image**:

| Argument | Required CSV columns, in order | Required values |
|---|---|---|
| `--task shape` | `filename,class_id` | Image basename and integer ID 0–9 using `classes.csv` |
| `--task force` | `filename,fx,fy,fz` | Image basename and forces in newtons, on the original scale and sign |

`filename` means the basename only, without its directory. The hidden-set metrics are accuracy and macro F1 for shape, and axis-wise, overall and tangential RMSE for force. A folder that does not follow the interface cannot be scored. [Handbook §5.3, PDF p. 20](../resources/2026_2027_DL_Final_Project_Handbook_Shared.pdf#page=20)

### Runtime and portability rules

- Include the model definition, preprocessing and weight-loading code in `predict.py` or your supplied helper files.
- Load weights relative to the script, for example `Path(__file__).parent / "shape_model.pt"`; do not use absolute paths to your computer or Drive.
- Use a GPU when available, and **also support CPU execution**.
- **Download nothing at prediction time.** Ship all weights; do not trigger a pretrained-weight download when constructing the model.
- Each task must finish within **10 minutes on a Colab GPU runtime**.
- Use image content alone, without contact IDs, shear indicators or filename patterns.
- If needed, list only extra packages absent from Colab in the model folder's `requirements.txt`, one per line with pinned versions. Do not list `torch` or `torchvision` there: the Colab versions are used.

[Handbook §5.4, PDF p. 21](../resources/2026_2027_DL_Final_Project_Handbook_Shared.pdf#page=21)

Save the best checkpoint chosen on validation data, including the force standardisation constants. For PyTorch, the handbook recommends tensors and plain Python lists compatible with `weights_only=True`, rather than NumPy arrays or custom objects in checkpoints. For Keras, use `.keras` and load it consistently. The FAQ permits final retraining on training plus validation data if disclosed; all reported numbers must still come from untouched test splits. [Handbook §5.5, PDF p. 21](../resources/2026_2027_DL_Final_Project_Handbook_Shared.pdf#page=21); [§15.1, PDF p. 45](../resources/2026_2027_DL_Final_Project_Handbook_Shared.pdf#page=45)

### Supplied example and self-check

[`example_submission/`](../example_submission/) demonstrates the required interface. Its training script uses **all released images without a split**, so its supplied weights are not a valid coursework evaluation. Develop and evaluate your models using the required protocol. [Handbook §5.2, PDF p. 20](../resources/2026_2027_DL_Final_Project_Handbook_Shared.pdf#page=20)

Test your own model folder in a **fresh Colab runtime**. The handbook uses a stride of 99 when copying samples so the force folder includes press and shear images:

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

From your own CID folder, run the two commands with those flat folders as inputs and inspect both CSVs. Install the optional extra requirements file first if you have one. Check the row count, filenames, columns, class IDs and force scale, and whether predictions agree reasonably with the copied images' labels. Test CPU and GPU behaviour, then repeat the self-check on a fresh extraction of your final ZIP. These checks exercise the submission interface; they do not replace held-out evaluation. [Handbook §5.6, PDF pp. 21–22](../resources/2026_2027_DL_Final_Project_Handbook_Shared.pdf#page=21); [§14.1, PDF p. 44](../resources/2026_2027_DL_Final_Project_Handbook_Shared.pdf#page=44)

## 9. Package and submit Part A

Create **`DL_Coursework_YourName_CID.zip`** with the following top-level contents:

| ZIP entry | Contents |
|---|---|
| `DL_Coursework_YourName_CID.pdf` | Your IEEE report |
| `code/` | Notebooks or scripts for preprocessing, training, evaluation and any tuning |
| `<your eight-digit CID>/` | `predict.py`, trained weights, helper modules and optional extra requirements |

For example, Jane Smith with CID `01234567` uses `DL_Coursework_JaneSmith_01234567.zip`. [Handbook §§2.1 and 9.1, PDF pp. 7–8 and 33](../resources/2026_2027_DL_Final_Project_Handbook_Shared.pdf#page=33)

Before **Sunday 13 December 2026 at 23:59 GMT**:

1. Restart and run your notebook; keep its outputs and ensure it reproduces the reported numbers.
2. Build and test the CID model folder in a fresh runtime.
3. Export the report, assemble the ZIP, extract it somewhere new and repeat the inference self-check.
4. Upload the ZIP to the **Part A assignment on Canvas**.
5. For Colab, give **viewer access** to the TA, **Lan Wei, `l.wei24@imperial.ac.uk`**. A local Jupyter notebook is covered by its copy in `code/`. Do not edit the shared notebook after the deadline; **the copy inside the submitted ZIP is the version marked**.

[Handbook §9.1, PDF p. 33](../resources/2026_2027_DL_Final_Project_Handbook_Shared.pdf#page=33)

If Canvas fails near the deadline, the handbook instructs you to email the TA **before the deadline**, including a share link to the files and a screenshot of the error. It counts as on time if those files are not changed afterwards. [Handbook §9.4, PDF p. 35](../resources/2026_2027_DL_Final_Project_Handbook_Shared.pdf#page=35)

## 10. Academic integrity, permitted data and AI tools

### Individual work and permitted data

Part A is individual: do not share your Part A code, models, results or report with other students, including your Part B group. Cite adapted code in comments and your README, understand it, and cite other sources and assets you use. Report results faithfully; do not fabricate, alter or select test results through model tuning. The module team may ask you to explain any part of your submission. [Handbook §11.1, PDF p. 40](../resources/2026_2027_DL_Final_Project_Handbook_Shared.pdf#page=40)

For Part A, train and validate **only on the released coursework data**. Do not use additional TacVerse data or another tactile dataset. General-purpose pretrained weights such as ImageNet are allowed, with attribution. Part B must use separate data: the handbook excludes this Part A dataset **and the GelSight subsets of TacVerse** from Part B. See the [Part B guide](PART_B_GUIDE.md) for its distinct requirements. [Handbook §11.3, PDF p. 41](../resources/2026_2027_DL_Final_Project_Handbook_Shared.pdf#page=41)

This states the explicit permitted-subset rule in §11.3. See [Handbook notes](HANDBOOK_NOTES.md) for wording elsewhere in the PDF that needs clarification.

### AI-use rules

| Use | Handbook rule |
|---|---|
| Brainstorming, concept explanations or debugging | Allowed; declare it |
| Generating or completing code | Allowed; declare it, understand and test it, and be able to explain every line |
| Improving the grammar or clarity of text you wrote | Allowed; declare it |
| Video-editing, caption or graphics assistance | Allowed; declare it and label AI-generated images in the video |
| Writing whole sections of the Part A report | **Not allowed**; the ideas, analysis and wording must be yours |
| AI voices, avatars or deepfakes presenting instead of group members | **Not allowed** in Part B, except for a reasonable adjustment agreed with the module team under §7.2 |
| Generating or changing data, results or references | **Never permitted**; check that references exist and support the associated claims |

Use the handbook's four-line declaration **after the references** in the Part A report. If you used no AI tools, state that explicitly:

```text
Tools used (name and version):
What we used them for:
Which parts of the submission they affected:
How we checked the output:
```

[Handbook §11.2, PDF p. 40](../resources/2026_2027_DL_Final_Project_Handbook_Shared.pdf#page=40); [presenter-adjustment provision in §7.2, PDF p. 27](../resources/2026_2027_DL_Final_Project_Handbook_Shared.pdf#page=27)

## 11. Bonus marks, early submission and late work

The handbook offers the following optional bonuses; **all bonus marks together are capped at 15 per student**, and the final combined project mark cannot exceed 100. Bonuses are awarded against the stated criteria at the instructors' discretion. [Handbook §10.4, PDF p. 38](../resources/2026_2027_DL_Final_Project_Handbook_Shared.pdf#page=38)

| Optional work | Maximum bonus |
|---|---:|
| Effective, physically justified data augmentation | +2 |
| Evidenced shape-model optimisation and regularisation | +4 |
| Evidenced force-model optimisation and regularisation | +4 |
| Systematic, justified hyperparameter tuning | +5 |
| Creative, well-documented and justified novel approach | +5 |
| Early submission | +3 or +5, subject to the cut-offs below |

For **Part A**, the handbook specifies **+5** for submission **before 23:59 on Sunday 29 November 2026**, or **+3** for submission **by 23:59 on Sunday 6 December 2026**. These are alternative early-submission levels, within the overall bonus cap. [Handbook §9.3, PDF p. 35](../resources/2026_2027_DL_Final_Project_Handbook_Shared.pdf#page=35)

The handbook states a deduction of **5 marks for each day late**, up to seven days; after seven days the item receives zero. Extensions require exceptional circumstances, advance application and appropriate documentation through the College process. Where College policy differs, College policy applies. [Handbook §9.3, PDF p. 35](../resources/2026_2027_DL_Final_Project_Handbook_Shared.pdf#page=35)

## 12. Final Part A checklist

Use this alongside the complete checklist in [Handbook §14.1, PDF pp. 43–44](../resources/2026_2027_DL_Final_Project_Handbook_Shared.pdf#page=43).

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

Questions should go to the module team: **Dr Dandan Zhang**, module leader (`d.zhang17@imperial.ac.uk`), or **Ms Lan Wei**, teaching assistant (`l.wei24@imperial.ac.uk`). Clarifications that change the handbook are announced to the whole class on Canvas. [Handbook §1.3, PDF p. 5](../resources/2026_2027_DL_Final_Project_Handbook_Shared.pdf#page=5)

## Sources and dataset attribution

Assessment requirements in this guide are drawn from the supplied [2026/27 Final Project Handbook](../resources/2026_2027_DL_Final_Project_Handbook_Shared.pdf), with section and page links throughout. The [original dataset README](ORIGINAL_DATASET_README.md) is retained for provenance; its “Task A” and “Task B” labels refer to the two learning tasks within coursework Part A.

The source dataset is **TacVerse**: L. Wei, G. Khurana, S. Bhouri, W. Hong, Z. Xin, Q. Cong, W. Fan, Y. Xiang and D. Zhang, “TacVerse: A Multisensor Dataset and Benchmark for Cross-Sensor Vision-Based Tactile Perception”, *Advanced Robotics Research*, 2026, [doi:10.1002/adrr.70169](https://doi.org/10.1002/adrr.70169). See the [dataset card](DATASET_CARD.md) for release-specific provenance, inventory, statistics and limitations.
