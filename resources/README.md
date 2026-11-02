# Course resources

## Deep Learning Final Coursework, 2026–2027 — Part A

[Repository overview](../README.md) · [Coursework and submission guide](../docs/COURSEWORK_GUIDE.md) · [Dataset exploration notebook](../notebooks/01_explore_dataset.ipynb)

This page connects the general project handbook with the tactile dataset, practical
notebook and task-specific instructions in this repository.

## Read the handbook

**[Download or read Deep_Learning_in_Practice_HandBook.pdf](Deep_Learning_in_Practice_HandBook.pdf)**

*Deep Learning in Practice: A Handbook for Building, Evaluating and Reporting Projects*
accompanies the Deep Learning course for Imperial College London's MSc Artificial
Intelligence Applications and Innovation. The supplied PDF is dated **November 2026**.

**Status of this copy:** the original nine-page PDF is preserved as supplied. It contains
an introduction and a Quick Start section; Chapters 1–7 and Appendices A–B are explicitly
marked **“To Do”** and contain development outlines. Those outlines describe planned
coverage and checkpoints, rather than completed chapters. Use the available repository
materials below for the current tactile coursework workflow.

### Where to find each topic

Page numbers below count the PDF's cover as page 1. The document's own printed page
numbers are included to make navigation clear.

| Handbook topic | PDF page(s) / printed page(s) | Content in the supplied PDF | Current repository companion |
|---|---|---|---|
| How to Use This Handbook | 3 / 1 | Introduction to the project workflow and intended readership | [Repository overview](../README.md) and [coursework guide](../docs/COURSEWORK_GUIDE.md) |
| Quick Start | 4–5 / 2–3 | Instructions for a synthetic stripe-classification example; companion source files are not included in the supplied upload | [Dataset exploration notebook](../notebooks/01_explore_dataset.ipynb) is the runnable starting point available here; see the distinction below |
| Chapters 1–2: define the project; understand and split the data | 6 / 4 | “To Do” outlines | [Dataset card](../docs/DATASET_CARD.md) and [required data splits](../docs/COURSEWORK_GUIDE.md#3-create-reproducible-training-validation-and-test-splits) |
| Chapters 3–4: build a baseline; debug training | 7 / 5 | “To Do” outlines | [Supplied submission example](../example_submission/) and [guidance on using that example](../docs/COURSEWORK_GUIDE.md#7-use-the-example-submission-appropriately); these are interface examples, not completed handbook chapters |
| Chapter 5: improve through controlled experiments | 8 / 6 | “To Do” outline | [Coursework split requirements](../docs/COURSEWORK_GUIDE.md#3-create-reproducible-training-validation-and-test-splits) and [preprocessing considerations](../docs/COURSEWORK_GUIDE.md#8-preprocessing-choices-to-explain-in-your-report) provide task-specific constraints |
| Chapter 6: evaluate and analyse errors | 8 / 6 | “To Do” outline | [Shape evaluation](../docs/COURSEWORK_GUIDE.md#4-evaluate-shape-classification) and [force evaluation, including shear-error analysis](../docs/COURSEWORK_GUIDE.md#5-evaluate-force-estimation) |
| Chapter 7: report and hand over | 9 / 7 | “To Do” outline | [Submission interface and requirements](../docs/COURSEWORK_GUIDE.md#6-prepare-the-required-submission-interface) and [fresh-runtime self-check](../docs/COURSEWORK_GUIDE.md#check-your-submission-in-a-fresh-runtime) |
| Appendix A: Project Checklist | 9 / 7 | “To Do” outline | Review the [coursework guide](../docs/COURSEWORK_GUIDE.md) for the released dataset's requirements |
| Appendix B: Task Adaptation Cards | 9 / 7 | “To Do” outline for segmentation, text classification and time-series forecasting | This release provides tactile shape classification and force estimation; the planned adaptation cards are not included as completed resources |

## Start with the available notebook

Open **[`notebooks/01_explore_dataset.ipynb`](../notebooks/01_explore_dataset.ipynb)** in
Google Colab, VS Code or Jupyter. The [repository overview](../README.md#2-download-and-start-exploring)
provides the Colab link and local setup commands.

Run the notebook from top to bottom to download and verify the dataset, inspect labels,
view tactile images, compare press/shear pairs and examine the force distributions.
This exploration runs on CPU. It prepares you to design your own experiments; it does
not train a coursework model or provide a completed assessment solution.

The handbook's Quick Start describes a **different example**, using generated images of
vertical and horizontal stripes. It refers to these companion files:

- `examples/quickstart.py`
- `examples/smoke.json`
- `examples/requirements.txt`

Those files were not included with the supplied PDF and are not part of this repository
release. The PDF's Quick Start commands therefore cannot be run from this repository as
written. The root `requirements.txt` here installs the dataset-exploration dependencies;
it is not the missing handbook example's dependency file. The tactile exploration
notebook is the available runnable entry point, and does not implement the handbook's
stripe-training example.

## A practical reading sequence for Part A

1. **Orient yourself.** Read the repository overview and the handbook's introduction
   to understand the project workflow. Part A includes both tactile tasks.
2. **Inspect the data.** Run the exploration notebook and consult the dataset card for
   label definitions, contact grouping, units and release statistics.
3. **Plan your experiment.** Follow the coursework guide's 60%/20%/20% split
   requirements. Keep both force images from each contact in the same split.
4. **Develop your own models.** Use the available submission example to understand
   the inference interface. Its supplied weights were trained on all released images
   and do not constitute a valid coursework evaluation.
5. **Evaluate and prepare the submission.** Follow the classification and force metrics,
   required shear analysis, output formats and fresh-runtime checks in the coursework
   guide. Follow the current assignment brief for assessment policies, deadlines and
   submission arrangements.

## Source and scope

The handbook page map and status above refer to the supplied November 2026 PDF.
The [coursework guide](../docs/COURSEWORK_GUIDE.md) reorganises the instructions provided
with `Tactile_DL_2027.zip`; the [original dataset README](../docs/ORIGINAL_DATASET_README.md)
is retained for reference. This resource index adds navigation between those materials.
