# Part A: Simplified Handbook

[Home](../README.md) · [Setup](GETTING_STARTED.md) · [Dataset labels](DATASET_CARD.md)

**Individual coursework · 60 marks**  
**Deadline: 13 December 2026, 23:59 GMT · Submit on Canvas**

Build models for shape classification and 3D contact-force estimation from tactile images.

## 1. Download the data

[Download Tactile_DL_2027.zip](https://github.com/dianzdd123/2026-2027-Deep-Learning-Final-Coursework-Part-A/releases/download/v1.0.2/Tactile_DL_2027.zip) and extract it.

| Task | Data | Target |
|---|---|---|
| Shape classification | 2,000 images; ten classes | Class ID 0–9 |
| Force estimation | 2,000 images; 1,000 press/shear pairs | `fx,fy,fz` in newtons |

All images are RGB, 320 × 240 pixels. [Label paths and class IDs](DATASET_CARD.md).

Use only the released coursework tactile data. General-purpose pretrained weights, such as ImageNet, are permitted with citation.

## 2. Prepare the data — 10 marks

- Inspect sample images, label associations, class counts and force distributions.
- Use **60% training, 20% validation and 20% test**.
- Stratify shape splits by class.
- Split force data **by `contact_id`**, keeping both images of each contact together.
- Fit normalisation and force-target standardisation using **training data only**.
- Save the splits and random seed. Select models on validation data; use the test set for final evaluation.

Keep splits and evaluation conditions fixed across models. For force images, use flips or rotations only if you can justify the corresponding force-label transformation.

## 3. Shape classification — 20 marks

Compare **at least three distinct CNN architectures**, including a baseline.

Report:

- Accuracy and macro precision, recall and F1.
- Confusion matrix and examples of misclassified images.
- Model size, training and inference times, and hardware.
- A brief explanation of architecture choices, common errors and generalisation limits.

## 4. Force estimation — 20 marks

Compare **at least two models** predicting `fx,fy,fz` from one image.

Report:

- Per-axis and overall RMSE in **newtons**, after reversing target standardisation.
- Tangential RMSE separately for press (`is_shear=0`) and shear (`is_shear=1`):

```python
rmse_t = np.sqrt(np.mean((pred_fx - true_fx)**2 + (pred_fy - true_fy)**2))
```

- Predicted-versus-true `fx` and `fy` plots for shear images, with a `y=x` reference.
- Normal versus tangential errors and examples of the largest failures.

A model that always predicts the **training-set mean force** is a recommended baseline.

Use image pixels only for prediction. Do not use `contact_id`, `is_shear`, filenames or test labels as input features. Negative `fz` indicates pressing into the sensor.

## 5. Optional hyperparameter tuning — up to 5 bonus marks

Define a search space and budget, select settings using validation results, and report the trials and resulting improvement.

## 6. Technical report — 10 marks

Write a **3–6-page IEEE conference-format, double-column report** covering:

- Abstract, Introduction and Objectives.
- Methodology: splits, preprocessing, architectures and training.
- Experiments and Evaluation: model comparisons, learning curves, required metrics and plots, and error analysis.
- Conclusions and Future Work.
- References and an AI-use declaration.

Cite the dataset, reused code, architectures and pretrained weights. Explain your results using evidence from your own experiments.

Dataset citation: Wei, L. *et al.* (2026), TacVerse, *Advanced Robotics Research*, e70169. [doi:10.1002/adrr.70169](https://doi.org/10.1002/adrr.70169).

## 7. Submit your work

Upload **`DL_Coursework_YourName_CID.zip`** to Canvas.

| Path inside ZIP | Contents |
|---|---|
| `DL_Coursework_YourName_CID.pdf` | Technical report |
| `code/` | Training and evaluation code or notebooks |
| `01234567/` | Model folder named with your eight-digit CID |
| `01234567/predict.py` | Prediction script |
| `01234567/shape_model.pt` | Shape weights, or your model's equivalent |
| `01234567/force_model.pt` | Force weights, or your model's equivalent |
| `01234567/requirements.txt` | Additional pinned dependencies, if needed |

Run both commands from the model folder:

```bash
python predict.py --task shape --images <IMAGE_DIR> --out <OUT_CSV>
python predict.py --task force --images <IMAGE_DIR> --out <OUT_CSV>
```

Input is a flat folder of anonymous JPEGs. Write one row per image:

| Task | CSV columns |
|---|---|
| Shape | `filename,class_id` |
| Force | `filename,fx,fy,fz` — newtons, original sign |

The model folder must be **under 200 MB**, support CPU and GPU, download nothing during inference, and finish each task within **10 minutes on a Colab GPU**. Load weights with paths relative to the script. List only additional pinned packages in `requirements.txt`; exclude `torch` and `torchvision`.

Test both commands in a clean environment. Share your notebook with `l.wei24@imperial.ac.uk` as **Viewer**.

The [example submission](../example_submission/README.md) demonstrates the interface. Train and evaluate your own models using the required splits; the supplied checkpoints were trained on all released images.

## 8. Academic integrity

Part A is individual work. Do not share assessed code, weights, reports or results. Declare AI assistance; do not use AI to write entire report sections or fabricate data, results or references.

Use Canvas for submission and course announcements. Contact `d.zhang17@imperial.ac.uk` or `l.wei24@imperial.ac.uk` for coursework questions.
