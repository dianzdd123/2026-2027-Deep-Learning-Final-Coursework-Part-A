# Part B : Advanced tactile perception project

[Home](../README.md) · [Assessment](ASSESSMENT_OVERVIEW.md) · [Source comparison](SOURCE_ALIGNMENT.md)

**Group project · 40 marks · Due Sunday 20 December 2026, 23:59 GMT on Canvas**

The newly uploaded simplified handbook and briefing specify **groups of 4–6 students**. An earlier full handbook in the repository specifies 5–6; the simplified handbook says the full handbook controls discrepancies. **Confirm the final group-size rule through Canvas announcements.**

## Aim and assessed outputs

Propose an advanced tactile perception method for a clearly identified stakeholder, build and evaluate a **working proof-of-concept model**, and present the project in a video **no longer than five minutes**. Each student contributes to the technical work, reviews the final submission and presents in their **own voice**. The code demonstrates the proof of concept but does not earn separate marks.

| Criterion | Marks |
|---|---:|
| Problem and stakeholder | 10 |
| Proposed solution (feasibility, creativity) | 10 |
| Novelty relative to relevant research | 10 |
| Presentation quality and participation | 10 |

## Research and project directions

Read at least two relevant papers and build the proposed method on at least one from the course reading list on **Canvas**. State what your project adds. The simplified handbook identifies directions A–G:

| Direction | Starting references | Suggested eligible data |
|---|---|---|
| A. Explainable material, texture or hardness perception | TactEx; ViTacTip | Touch and Go; ObjectFolder Real |
| B. Graph-based learning on tactile markers | Tac-VGNN | Eligible marker-based TacVerse / TacTip-family data |
| C. Cross-sensor or self-supervised learning | TacVerse; SARL; Sparsh | Non-GelSight TacVerse; Touch-Slide |
| D. Visuo-tactile fusion / translation | Multimodality sensor; SARL | Touch and Go; ObjectFolder Real |
| E. Generative tactile approaches | MultiDiffSense | Real dataset and synthetic images; **seek clarification about AI/data-generation restrictions** |
| F. Slip and grasp-outcome detection | Feeling of Success; ViTacTip | Feeling of Success; YCB-Slide |
| G. Your own advanced research idea | Relevant reading-list paper | Requires module approval by 29 November |

**Data separation is strict:** the Part A coursework data and **TacVerse GelSight subsets** must not be used for Part B. Check dataset licence, cite its source and do not submit raw data.

## Proof of concept

The simplified handbook requires: one defined advanced task on an appropriate dataset, a model trained by the group, relevant held-out test results and a brief demonstration on test data. It recommends a split by **object/session/trial/sensor rather than individual frame**, a baseline comparison and at least one explained failure case.

## Schedule and group records

- **23 November:** group list confirmed on Canvas.
- **29 November, 23:59 GMT:** signed group charter and one-paragraph direction, paper(s), dataset and stakeholder.
- **30 November–4 December:** progress meeting with the TA.
- **20 December, 23:59 GMT:** project submission.
- **23 December, 23:59 GMT:** individual peer assessment closes.

Maintain weekly meeting minutes and individual contribution logs; raise group problems early.

## Video and submission

Video: **maximum 5:00**, each member appearing and presenting in their own voice; include paper citations, evaluation and an actual proof-of-concept demonstration. Captions required (burned in or corrected `.srt`), MP4 preferred, under 1 GB.

The group coordinator submits `GroupXX_TactileDL_Video.mp4`, `GroupXX_TactileDL_Code.zip` (notebook, README, trained weights; no raw data), and `GroupXX_TactileDL_Contributions.pdf` through Canvas. All group members complete the peer assessment. Ask the TA for the current confirmation-email procedure if needed.

**Academic integrity:** never fabricate data, metrics or references, never substitute AI voices/avatars for members, and include the prescribed AI-use declaration. Directions involving generated data must be clarified with the module team given the wording of the AI policy.

Sources: Simplified Handbook 2026/27 pp. 5–9; Student Briefing slides 16–23, 24–26. The binding full handbook and Canvas announcements take precedence where the provided versions conflict.
