# Handbook provenance and current clarification notes

[Course homepage](../README.md) · [Source alignment](SOURCE_ALIGNMENT.md) · [Assessment](ASSESSMENT_OVERVIEW.md)

The previously uploaded **51-page Final Project Handbook** is preserved in [resources](../resources/2026_2027_DL_Final_Project_Handbook_Shared.pdf). Subsequently supplied course materials dated **10 November 2026** are the **9-page Simplified Handbook 2026/27** and **27-slide Key Information Student Briefing**. Both direct students to **Canvas** for current handbooks, announcements, groups and submissions. The new materials are not incorporated as PDF binaries in this repository.

## Differences that require official module clarification

- **Group size:** newer simplified handbook and briefing state **4–6**; earlier full handbook states **5–6**.
- **Maximum bonus:** newer documents specify **only up to +5 for Task 4 hyperparameter tuning**; earlier full handbook describes several bonuses with a +15 total cap.
- **Training-mean force baseline:** newer simplified handbook *recommends* it; earlier full handbook *requires* it.
- **Generative Part B direction:** appears in the reading/project directions, but general AI and data integrity restrictions prohibit generating/changing data without explicit distinction between legitimate generative experiments and fabricated evidence.

The newly supplied simplified handbook explicitly says the full handbook takes priority if inconsistent. Do not use this documentation as a substitute for a binding Canvas announcement identifying which full-handbook revision is current.

## Data and technical facts

The archive `Tactile_DL_2027.zip` is unchanged, with SHA-256 `1a1620e4695b220043318e7b209202940b930fcf82f69b4f761213255c6b4ca5`. Dataset contents include 2,000 shape and 2,000 force images. The sample script and checkpoints illustrate how to produce prediction files; they were trained on all released images, so they are not held-out test results.

Use only the supplied coursework dataset for Part A. The older handbook contains broader wording about TacVerse than its more specific dataset restriction: the released subset itself comes from TacVerse, but **extra** tactile data are excluded from Part A. Do not use this subset or TacVerse GelSight subsets for Part B.

## Verification and version status

The public distribution remains **v1.0.2** and the same verified archive is linked in the repository. The later revision of the `main` branch updates student guidance without changing the published dataset or creating another release. Earlier commits and tagged versions remain Git-history records.

For a detailed side-by-side comparison, consult [SOURCE_ALIGNMENT.md](SOURCE_ALIGNMENT.md).
