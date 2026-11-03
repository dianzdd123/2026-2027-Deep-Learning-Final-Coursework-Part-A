# Handbook version and wording notes

[Correct handbook](../resources/2026_2027_DL_Final_Project_Handbook_Shared.pdf) · [Assessment overview](ASSESSMENT_OVERVIEW.md) · [Part A guide](COURSEWORK_GUIDE.md) · [Part B guide](PART_B_GUIDE.md)

The repository uses the **51-page 2026/27 Final Project Handbook** supplied by the module leader. The PDF is preserved unchanged. These notes distinguish source wording from requirements that can be stated unambiguously; they do not create new assessment permissions or rules. Module-team clarifications are announced on Canvas, as described in [Section 1.3, PDF page 5](../resources/2026_2027_DL_Final_Project_Handbook_Shared.pdf#page=5).

## 1. Which TacVerse data may be used?

The table in [Section 6.5, PDF page 25](../resources/2026_2027_DL_Final_Project_Handbook_Shared.pdf#page=25) says “never use any TacVerse data in Part A”. Taken literally, this conflicts with the required Part A dataset being a curated TacVerse subset.

The explicit rule in [Section 11.3, PDF page 41](../resources/2026_2027_DL_Final_Project_Handbook_Shared.pdf#page=41) is more specific: **Part A uses only the released coursework data; no other TacVerse data and no other tactile dataset may be added.** The repository guides reproduce that explicit rule. General-purpose pretrained weights such as ImageNet are permitted if acknowledged.

For **Part B**, Section 11.3 excludes both the Part A coursework dataset and the GelSight subsets of TacVerse. Refer questions about a proposed dataset to the module team.

## 2. Synthetic-data research and the AI-use table

Direction E in [Section 6.4, PDF page 25](../resources/2026_2027_DL_Final_Project_Handbook_Shared.pdf#page=25) proposes diffusion/GAN generation of tactile data. The risk guidance in [Section 7.6, PDF page 30](../resources/2026_2027_DL_Final_Project_Handbook_Shared.pdf#page=30) discusses evaluating synthetic-data approaches on real data. However, the AI-use table in [Section 11.2, PDF page 40](../resources/2026_2027_DL_Final_Project_Handbook_Shared.pdf#page=40) gives a broad prohibition on generating or changing data, results or references.

**Ask the module team to clarify the permitted scope before choosing a synthetic-data direction.** This repository does not invent an exception. Fabricating experiments, reporting generated samples as real measurements, or inventing results or references is not permitted.

## 3. Inference timing and late-submission details

[Section 5.4, PDF page 21](../resources/2026_2027_DL_Final_Project_Handbook_Shared.pdf#page=21) requires each task to finish within ten minutes on a Colab GPU runtime. The hidden-test image count and exact GPU model are not specified. A small self-check verifies the interface and loading path; it does not prove runtime on the complete hidden test set.

[Section 9.3, PDF page 35](../resources/2026_2027_DL_Final_Project_Handbook_Shared.pdf#page=35) states the late penalty, maximum late window and extension process. It does not specify partial-day rounding or every ordering detail between penalties and caps. The repository does not infer these details. The handbook states that College policy applies where it differs.

## 4. Dates, versions and source preservation

- The cover states **2026/27, released Tuesday 10 November 2026**. This is the PDF's stated project date, not the GitHub repository creation date.
- **Dataset v1.0.0** retains the original archive, published on 2 November 2026. Images, labels, the original dataset README, example scripts and checkpoints are unchanged.
- **Guidance v1.0.1** replaces the mistaken handbook in the current repository and updates the student materials. Historical commits and the original dataset tag are retained.
- The original dataset README remains a provenance copy. Current instructions follow the correct handbook, including its mixed press/shear self-check sampling instead of the older every-100th-image example.
