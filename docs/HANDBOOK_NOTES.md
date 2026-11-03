# Handbook version and wording notes

[Handbook (PDF)](../resources/2026_2027_DL_Final_Project_Handbook_Shared.pdf) · [Assessment overview](ASSESSMENT_OVERVIEW.md) · [Part A guide](COURSEWORK_GUIDE.md) · [Part B guide](PART_B_GUIDE.md)

These notes accompany the 51-page 2026/27 Final Project Handbook and identify provisions that require careful interpretation or clarification. The PDF is retained unchanged. The notes introduce no additional assessment rules or permissions. Course-wide clarifications are issued by the module team on Canvas, as described in [Section 1.3, PDF page 5](../resources/2026_2027_DL_Final_Project_Handbook_Shared.pdf#page=5).

On this page: [TacVerse data](#1-permitted-use-of-tacverse-data) · [Synthetic data and AI](#2-synthetic-data-research-and-the-ai-use-table) · [Timing and submission policies](#3-inference-timing-and-late-submission-details) · [Document versions](#4-dates-versions-and-source-preservation)

<a id="1-which-tacverse-data-may-be-used"></a>

## 1. Permitted use of TacVerse data

The table in [Section 6.5, PDF page 25](../resources/2026_2027_DL_Final_Project_Handbook_Shared.pdf#page=25) says “never use any TacVerse data in Part A”. This wording is broader than the Part A dataset specification, which identifies the released coursework data as a curated TacVerse subset.

The specific restriction in [Section 11.3, PDF page 41](../resources/2026_2027_DL_Final_Project_Handbook_Shared.pdf#page=41) states that Part A uses only the released coursework data: no additional TacVerse data or other tactile dataset may be added. The repository guides follow this restriction. General-purpose pretrained weights such as ImageNet are permitted if acknowledged.

For Part B, Section 11.3 excludes both the Part A coursework dataset and the GelSight subsets of TacVerse. Refer questions about a proposed dataset to the module team.

## 2. Synthetic-data research and the AI-use table

Direction E in [Section 6.4, PDF page 25](../resources/2026_2027_DL_Final_Project_Handbook_Shared.pdf#page=25) proposes diffusion/GAN generation of tactile data. The risk guidance in [Section 7.6, PDF page 30](../resources/2026_2027_DL_Final_Project_Handbook_Shared.pdf#page=30) discusses evaluating synthetic-data approaches on real data. However, the AI-use table in [Section 11.2, PDF page 40](../resources/2026_2027_DL_Final_Project_Handbook_Shared.pdf#page=40) gives a broad prohibition on generating or changing data, results or references.

Seek clarification from the module team about the permitted experimental scope before choosing a synthetic-data direction. The generative-methods proposal and the AI-use prohibition remain unresolved in the source document. Fabricated experiments, generated samples presented as real measurements, and invented results or references are not permitted.

## 3. Inference timing and late-submission details

[Section 5.4, PDF page 21](../resources/2026_2027_DL_Final_Project_Handbook_Shared.pdf#page=21) requires each task to finish within ten minutes on a Colab GPU runtime. The hidden-test image count and exact GPU model are not specified. A small self-check establishes that the interface and model-loading process work. It cannot establish runtime on the complete hidden test set.

[Section 9.3, PDF page 35](../resources/2026_2027_DL_Final_Project_Handbook_Shared.pdf#page=35) states the late penalty, maximum late window and extension process. It does not specify partial-day rounding or the complete order of operations between penalties and mark caps. Those details require clarification. The handbook states that College policy applies where it differs.

## 4. Dates, versions and source preservation

- The cover states 2026/27, released Tuesday 10 November 2026. This is the PDF's stated project date, not the GitHub repository creation date.
- Dataset v1.0.0 retains the original archive, published on 2 November 2026. Images, labels, the original dataset README, example scripts and checkpoints are unchanged.
- Guidance v1.0.1 aligns the repository’s student materials with the 51-page handbook. Historical commits and the original dataset tag are retained.
- Guidance v1.0.2 refines the course descriptions, resource navigation and student guidance. The handbook and assessment requirements remain unchanged.
- The original dataset README is retained for provenance. Current instructions follow the 51-page handbook, including its mixed press/shear self-check sampling in place of the older every-100th-image example.
