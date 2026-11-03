# Submission Interface and Reference Implementation

2026–2027 Deep Learning Final Coursework · Part A

[Course overview](../README.md) · [Getting started](../docs/GETTING_STARTED.md) · [Part A guide](../docs/COURSEWORK_GUIDE.md) · [Handbook Section 5](../resources/2026_2027_DL_Final_Project_Handbook_Shared.pdf#page=19)

## Purpose

This example demonstrates the prediction interface used to evaluate the shape-classification and force-estimation models in Part A. The original scripts, dependency file and checkpoints are unchanged copies from `Tactile_DL_2027.zip`.

| File | Purpose |
|---|---|
| `predict.py` | Model definitions, preprocessing, weight loading and CSV prediction output for both learning tasks |
| `train_example.py` | Demonstration of how the supplied checkpoints were produced |
| `shape_model.pt` | Supplied shape-classification checkpoint |
| `force_model.pt` | Supplied force-estimation checkpoint |
| `requirements.txt` | Submission dependency-file example |

The checkpoints are provided for interface verification. The demonstration training script uses all released images, so these checkpoints cannot establish held-out coursework performance. Assessed experiments must use the required data splits and compare at least three shape CNN architectures and at least two force architectures.

## Command-line interface

The evaluator runs each command from inside the submitted model folder:

```bash
python predict.py --task shape --images <IMAGE_DIR> --out <OUT_CSV>
python predict.py --task force --images <IMAGE_DIR> --out <OUT_CSV>
```

`<IMAGE_DIR>` is a flat directory of anonymous JPEG files, without class subfolders or labels. Write one prediction row per input image to `<OUT_CSV>`.

| Learning task | Required CSV columns | Output convention |
|---|---|---|
| Shape classification | `filename,class_id` | File name only; integer class ID from the coursework mapping |
| Force estimation | `filename,fx,fy,fz` | File name only; forces in newtons, on the original scale and with the original sign convention |

## Model folder and execution requirements

Name the submitted model folder with the student's eight-digit College ID (CID). The folder must:

- remain below 200 MB;
- contain the required weights and any helper modules;
- load weights using paths relative to the script;
- support CPU inference and use a GPU when available;
- run without downloading files at prediction time;
- complete each task within ten minutes on a Colab GPU runtime.

See [handbook Sections 5.3–5.4](../resources/2026_2027_DL_Final_Project_Handbook_Shared.pdf#page=20) and the [Part A guide](../docs/COURSEWORK_GUIDE.md) for the full specification and submission self-check.

## Dependencies and reproducibility

The submission's `requirements.txt` must list only additional packages that are not pre-installed in Colab, with versions pinned. The handbook explicitly excludes `torch` and `torchvision` from this file. The repository's exploration dependencies serve a separate purpose and should not be copied into a submission without review.

Keep inference preprocessing consistent with training. Retain the training-derived force-standardisation constants needed to return predictions in newtons. Run both commands in a fresh environment before submission.
