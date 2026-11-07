# Assessment and deadlines | Deep Learning Final Project 2026/27

[Course homepage](../README.md) · [Part A](COURSEWORK_GUIDE.md) · [Part B](PART_B_GUIDE.md) · [Source comparison](SOURCE_ALIGNMENT.md)

This page summarises the **newly uploaded 9-page Simplified Handbook and 27-slide Student Briefing (10 November 2026)**. Both describe a 100-mark assessment comprising individual Part A (60) and group Part B (40). The simplified handbook says that if its provisions differ from the full handbook, the full handbook applies. Because the older full handbook currently stored here contains differences, **confirm the effective policy on Canvas** rather than relying on an undocumented choice of version.

## Assessment structure

| Component | Value | Core deliverable | Deadline |
|---|---:|---|---|
| Part A — individual | 60 | 3–6-page IEEE report, code and CID-named model folder with `predict.py` in one ZIP | 13 December 2026, 23:59 GMT |
| Part B — group | 40 | ≤5-minute video, reproducible proof-of-concept code, contributions/AI-use form | 20 December 2026, 23:59 GMT |
| Peer assessment | Moderates Part B | Each group member submits the Canvas form | 23 December 2026, 23:59 GMT |

**Newer brief:** Part B groups of **4–6**; only bonus is up to **+5** for Part A Task 4 hyperparameter tuning; final result capped at 100. The older full handbook states groups of **5–6** and bonuses capped at **+15**. These require a single definitive Canvas clarification; do not apply the old +15 scheme solely because historical repository pages mention it.

## Dates

| Milestone | Date |
|---|---|
| Project material release stated in briefing | Tuesday 10 November 2026 |
| Part B group list confirmed | Monday 23 November 2026 |
| Group charter and proposed direction | Sunday 29 November 2026, 23:59 GMT |
| TA progress check | 30 November–4 December 2026 |
| Escalate unresolved group concerns | Ideally by Monday 7 December 2026 |
| Part A submission | Sunday 13 December 2026, 23:59 GMT |
| Part B submission | Sunday 20 December 2026, 23:59 GMT |
| Individual peer assessment closes | Wednesday 23 December 2026, 23:59 GMT |

## Part A grading (60 marks)

| Task | Marks | Evidence |
|---|---:|---|
| 1 — preparation | 10 | Image/label loading and association (4); exploratory data analysis (3); normalisation and leakage-free splits (3) |
| 2 — shape classification | 20 | ≥3 CNN architectures; meaningful accuracy/efficiency comparison; macro precision, recall, F1 and confusion matrix; failure analysis |
| 3 — force estimation | 20 | ≥2 architectures; RMSE per axis and overall in newtons; press/shear tangential analysis and interpretation |
| 5 — technical report | 10 | IEEE double-column, 3–6 pages; clear methods, figures, evaluation and limitations |
| 4 — optional tuning | Up to +5 | Systematic validation-based search with documented budget, comparisons and justification |

The **simplified handbook** describes a training-mean force baseline as **recommended**; the earlier full handbook treats it as required. The repository guide labels it accordingly and flags the discrepancy. No other bonus scheme is stated in the newer materials.

## Part A submission checklist

Submit `DL_Coursework_YourName_CID.zip` on Canvas with `DL_Coursework_YourName_CID.pdf`, `code/`, and an eight-digit `CID/` containing `predict.py`, weights and any helpers. Share the working Colab/Jupyter notebook with `l.wei24@imperial.ac.uk` (Viewer). The ZIP copy is assessed.

For shape: output `filename,class_id`. For force: output `filename,fx,fy,fz` in newtons and original sign. Inference uses anonymous images only; no metadata, filename patterns or downloads. Model folder below 200 MB; CPU and GPU compatible; each task within ten minutes on Colab GPU. See [example_submission](../example_submission/README.md).

## Part B overview

Groups propose a stakeholder-relevant advanced tactile problem, build a **working proof of concept** on permitted data, and present a video of at most **5:00**, with each member speaking in their own voice. Marking: problem/stakeholder 10; proposed solution 10; novelty 10; presentation 10. Proof-of-concept code is mandatory but not separately graded. No Part A data or TacVerse GelSight subsets in Part B. See [Part B guide](PART_B_GUIDE.md).

## Academic integrity and submission platform

All submissions, registration, peer assessment and official clarifications take place in **Canvas**. Part A is individual work; do not share assessed outputs. Cite borrowed code, models, datasets and papers. AI can assist with declared, checked brainstorming/debugging/code/language editing; it must not fabricate data/results/references, write entire Part A report sections, or present in place of a Part B group member. Include the specified four-line AI-use declaration.

The simplified handbook states a late penalty of five marks per day, up to seven days, with extensions through the College process. Consult Canvas and the full handbook for binding implementation and circumstances.

**Source locations:** Simplified Handbook pp. 1–9; Key Information Student Briefing slides 6–8, 11–14, 16–23, 24–26. See [source alignment](SOURCE_ALIGNMENT.md) for differences with the earlier full handbook retained in this repository.
