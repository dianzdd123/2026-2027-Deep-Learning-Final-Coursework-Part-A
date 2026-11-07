# Source alignment: course instructions, starter code and dataset

[Repository home](../README.md) · [Assessment overview](ASSESSMENT_OVERVIEW.md)

## Source materials reviewed

1. **Tactile_DL_2027.zip** : user-provided archive, 37,441,246 bytes, SHA-256 `1a1620e4695b220043318e7b209202940b930fcf82f69b4f761213255c6b4ca5`. Its original `README.md`, labels, image files and example-submission code remain unchanged.
2. **Deep Learning Final Project 2026/27 : Simplified Handbook**, 9 pages, dated 10 November 2026 : uploaded in this conversation.
3. **Deep Learning Final Project : Key Information Student Briefing**, 27 slides, dated 10 November 2026 : uploaded in this conversation.
4. **Earlier Final Project Handbook** (51-page PDF retained in `resources/`) : contains provisions that differ from documents (2) and (3).

The **new simplified handbook explicitly says the full handbook takes precedence if they differ** and that Canvas is the place for course-wide clarifications. Therefore repository text explains observed differences rather than declaring an unverified policy change. The newly supplied PDFs are the basis of the orientation pages, but **they are not currently bundled as GitHub release assets**; access official copies via Canvas.

## Changes and discrepancies requiring clarification

| Topic | New simplified handbook / briefing | Earlier full handbook | Repository treatment |
|---|---|---|---|
| Part B group size | **4–6** (simplified p. 1; briefing slides 6, 15–16) | **5–6** | Show new stated size and request final Canvas confirmation |
| Bonus marks | **Only Part A Task 4 tuning, up to +5** (simplified pp. 1, 3, 8; briefing slides 6–7) | **Multiple bonuses, capped at +15** | New scheme described as current orientation; old scheme not presented as available |
| Training-mean baseline for forces | **Recommended** (simplified p. 4) | **Required** as part of tangential analysis | Recommend using it, and flag the rule difference |
| Part B proof-of-concept protocol | New simplified minimum is a trained model, test results and demo; grouping/baseline are recommendations (pp. 6–7) | More detailed seven-item minimum | Do not misrepresent simplified recommendations as requirements |
| Data-generation direction | Generative direction E appears in both newer documents | Older AI table broadly forbids generating or changing data | Refer to Canvas for scope; do not invent an exception |
| Source distribution | Github distributes **Part A data and starter code**; Canvas holds handbook, briefing, registration, assessment and announcements (briefing slide 24) | Old repository mirrored a full handbook | Present GitHub/Canvas responsibilities separately |

## Stable requirements common to the reviewed materials

- Part A: individual, **60 marks**, **13 December 2026 at 23:59 GMT**.
- Part B: group, **40 marks**, **20 December 2026 at 23:59 GMT**, peer assessment **23 December**.
- Part A dataset: **4,000 RGB JPEGs, 320×240**, 2,000 shape and 2,000 force images.
- Shape: ten classes, **at least three CNNs**, macro metrics and confusion matrix.
- Force: **at least two architectures**, predictions `fx,fy,fz` in newtons, separate press/shear tangential analysis.
- Evaluation: **60/20/20**; shape stratified by class; force grouped by physical contact; training-only statistics.
- Part A submission: **3–6-page IEEE report**, code, weights and model-folder `predict.py`; one ZIP through Canvas; model folder below 200 MB; no downloads during inference.
- Part B: advanced task, cited research, working proof of concept, ≤5-minute video, no Part A data or TacVerse GelSight subsets.
- AI: declared assistance, genuine student analysis and results, no fabricated evidence.

## Repository preservation

- The dataset archive and its checksum are unchanged and still distributed in release **v1.0.2**.
- The download helper remains pinned to `v1.0.2` and checks file size and SHA-256 before extraction.
- Existing supplied weights and example script illustrate the prediction interface; training on all released data means they are **not** held-out evaluation results.
- The older full PDF is retained as an archival source in `resources/`, not silently edited or described as the newly uploaded simplified handbook.
- No assessed submissions should be pushed to this public repository.

**For the module team:** resolving the three grading differences (group size, bonus cap, force baseline) in a dated Canvas announcement would prevent students following contradictory requirements.
