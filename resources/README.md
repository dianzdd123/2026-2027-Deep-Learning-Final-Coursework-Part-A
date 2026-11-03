# Project Handbook and Reading Guide

2026–2027 Deep Learning Final Coursework

[Course overview](../README.md) · [Getting started](../docs/GETTING_STARTED.md) · [Assessment overview](../docs/ASSESSMENT_OVERVIEW.md) · [Part A guide](../docs/COURSEWORK_GUIDE.md) · [Part B guide](../docs/PART_B_GUIDE.md)

## Course handbook

[Read or download the Final Project Handbook](2026_2027_DL_Final_Project_Handbook_Shared.pdf)

The 51-page handbook for 2026/27 sets out the technical briefs, assessment criteria, submission requirements and academic integrity rules for individual Part A and the Part B group project. It also includes reference code and group-work templates. The PDF supplied by the module leader is preserved unchanged.

The module leader is Dr Dandan Zhang, Department of Bioengineering, Imperial College London; the teaching assistant is Ms Lan Wei. Canvas is the platform for submissions and module-team announcements. Contacts and the clarification process are in [Section 1.3, PDF page 5](2026_2027_DL_Final_Project_Handbook_Shared.pdf#page=5).

The repository guides provide summaries and navigation without introducing additional assessment rules. The [handbook wording notes](../docs/HANDBOOK_NOTES.md) identify passages whose scope requires clarification from the module team.

## Handbook navigation

PDF pages below refer to the viewer's page counter, including the cover. After the cover, the printed page number is one lower: PDF page 8 is printed page 7.

| Topic | Handbook location | Companion resource |
|---|---|---|
| Overview, contacts and materials | [Sections 1–2, PDF page 5](2026_2027_DL_Final_Project_Handbook_Shared.pdf#page=5) | [Main overview](../README.md) |
| Deadlines, deliverables and required/optional work | [Sections 2.1–2.3, PDF page 7](2026_2027_DL_Final_Project_Handbook_Shared.pdf#page=7) | [Assessment overview](../docs/ASSESSMENT_OVERVIEW.md) |
| Sensor and dataset | [Sections 3.1–3.2, PDF page 9](2026_2027_DL_Final_Project_Handbook_Shared.pdf#page=9) | [Dataset card](../docs/DATASET_CARD.md) and [notebook](../notebooks/01_explore_dataset.ipynb) |
| Data preparation and valid splits | [Task 1, Section 3.3, PDF page 11](2026_2027_DL_Final_Project_Handbook_Shared.pdf#page=11) | [Part A guide](../docs/COURSEWORK_GUIDE.md) |
| At least three shape CNN architectures | [Task 2, Section 3.4, PDF page 13](2026_2027_DL_Final_Project_Handbook_Shared.pdf#page=13) | [Part A guide](../docs/COURSEWORK_GUIDE.md) |
| At least two force architectures and tangential analysis | [Task 3, Section 3.5, PDF page 14](2026_2027_DL_Final_Project_Handbook_Shared.pdf#page=14) | [Part A guide](../docs/COURSEWORK_GUIDE.md) |
| Optional tuning and novel approach | [Sections 3.6–3.8, PDF page 15](2026_2027_DL_Final_Project_Handbook_Shared.pdf#page=15) | [Assessment overview](../docs/ASSESSMENT_OVERVIEW.md) |
| IEEE report | [Section 4, PDF page 16](2026_2027_DL_Final_Project_Handbook_Shared.pdf#page=16) | [Part A report guide](../docs/COURSEWORK_GUIDE.md) |
| Model folder, inference interface and self-check | [Section 5, PDF page 19](2026_2027_DL_Final_Project_Handbook_Shared.pdf#page=19) | [Submission example](../example_submission/) and [Part A guide](../docs/COURSEWORK_GUIDE.md) |
| Part B directions, reading list and permitted data | [Section 6, PDF page 22](2026_2027_DL_Final_Project_Handbook_Shared.pdf#page=22) | [Part B guide](../docs/PART_B_GUIDE.md) |
| Five-minute video | [Section 7, PDF page 27](2026_2027_DL_Final_Project_Handbook_Shared.pdf#page=27) | [Part B guide](../docs/PART_B_GUIDE.md) |
| Group charter, records and peer assessment | [Section 8, PDF page 30](2026_2027_DL_Final_Project_Handbook_Shared.pdf#page=30) | [Part B guide](../docs/PART_B_GUIDE.md) |
| Part A submission | [Section 9.1, PDF page 33](2026_2027_DL_Final_Project_Handbook_Shared.pdf#page=33) | [Part A guide](../docs/COURSEWORK_GUIDE.md) |
| Part B submission | [Section 9.2, PDF page 33](2026_2027_DL_Final_Project_Handbook_Shared.pdf#page=33) | [Part B guide](../docs/PART_B_GUIDE.md) |
| Early bonus, late work and extensions | [Section 9.3, PDF page 35](2026_2027_DL_Final_Project_Handbook_Shared.pdf#page=35) | [Assessment overview](../docs/ASSESSMENT_OVERVIEW.md) |
| Marking and peer moderation | [Section 10, PDF page 36](2026_2027_DL_Final_Project_Handbook_Shared.pdf#page=36) | [Assessment overview](../docs/ASSESSMENT_OVERVIEW.md) |
| Academic integrity, AI use and permitted data | [Section 11, PDF page 40](2026_2027_DL_Final_Project_Handbook_Shared.pdf#page=40) | [Assessment overview](../docs/ASSESSMENT_OVERVIEW.md) and [wording notes](../docs/HANDBOOK_NOTES.md) |
| Timeline and pitfalls | [Sections 12–13, PDF page 41](2026_2027_DL_Final_Project_Handbook_Shared.pdf#page=41) | [Part A guide](../docs/COURSEWORK_GUIDE.md) and [Part B guide](../docs/PART_B_GUIDE.md) |
| Submission checklists | [Section 14, PDF page 43](2026_2027_DL_Final_Project_Handbook_Shared.pdf#page=43) | [Part A guide](../docs/COURSEWORK_GUIDE.md) and [Part B guide](../docs/PART_B_GUIDE.md) |
| Frequently asked questions | [Section 15, PDF page 45](2026_2027_DL_Final_Project_Handbook_Shared.pdf#page=45) | [Part A guide](../docs/COURSEWORK_GUIDE.md) and [Part B guide](../docs/PART_B_GUIDE.md) |
| Split/metric code and group-work templates | [Appendix A, PDF page 47](2026_2027_DL_Final_Project_Handbook_Shared.pdf#page=47) | Original templates in the PDF |

## Recommended sequence

For Part A:

1. Read Sections 2–3 to establish the scope, deliverables and technical tasks.
2. Follow [Getting started](../docs/GETTING_STARTED.md) and use the [exploration notebook](../notebooks/01_explore_dataset.ipynb) to inspect images and labels.
3. Create the required data splits before fitting preprocessing, then compare the specified model architectures.
4. Use Sections 4–5 to prepare the report and model folder.
5. Complete the checks in Sections 9.1 and 14 before submitting through Canvas.

For Part B, read Sections 6–8 with the group while Part A is under way. Select an advanced problem and reading-list paper, agree a permitted dataset, complete the group charter and develop a working proof of concept before recording. Neither the Part A coursework data nor TacVerse's GelSight subsets may be used for Part B.

### Role of the supporting code

The exploration notebook supports dataset inspection and validation. The original submission scripts and checkpoints demonstrate the prediction interface; their example training uses all released images and cannot establish held-out coursework performance. Students must develop the assessed models and report their own experiments.

## Document version and integrity

The handbook cover states Tuesday 10 November 2026 as the project release date. This is the document's stated date, distinct from the repository publication and correction dates. The supplied PDF is unchanged.

The handbook's materials table links to the upstream coursework repository. The same supplied dataset is available from [this repository's dataset release v1.0.0](https://github.com/dianzdd123/2026-2027-Deep-Learning-Final-Coursework-Part-A/releases/tag/v1.0.0), with unchanged bytes and checksum.

The handbook checksum is in [checksums.sha256](checksums.sha256):

```text
e855ea221dc15fe8ea17e634be32125cb47cb5ca568612ac427e5982695a8b0d  2026_2027_DL_Final_Project_Handbook_Shared.pdf
```
