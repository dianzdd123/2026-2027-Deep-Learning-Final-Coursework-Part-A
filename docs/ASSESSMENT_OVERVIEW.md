# 2026–2027 Deep Learning Final Project: assessment overview

[Repository home](../README.md) · [Part A guide](COURSEWORK_GUIDE.md) · [Part B guide](PART_B_GUIDE.md) · [Handbook wording notes](HANDBOOK_NOTES.md)

This page summarises the supplied **2026/27 Final Project Handbook**. Its cover labels the document **“released Tuesday 10 November 2026”**; that is the handbook's version label. The linked PDF is the complete source, and its page links below use **PDF page numbers**, including the cover. This repository distributes the Part A dataset and supporting guidance. Assessed work is submitted through **Canvas**. [Handbook cover, PDF p. 1](../resources/2026_2027_DL_Final_Project_Handbook_Shared.pdf#page=1); [§9, PDF p. 32](../resources/2026_2027_DL_Final_Project_Handbook_Shared.pdf#page=32).

## 1. The two assessed parts

| Part | Work | Required marks | Main deliverables |
|---|---|---:|---|
| **A — individual** | Shape classification and three-axis force estimation from the released GelSight images | **60** | IEEE report, reproducible code and trained models with the specified `predict.py` interface |
| **B — group of 5–6** | An advanced tactile perception project grounded in the reading list, with a trained proof of concept | **40** | Video of at most 5 minutes, proof-of-concept code, contributions and AI-use form, confirmation email, and individual peer assessments |

Part B marks can be adjusted through peer moderation. Up to **15 bonus marks in total** are available, and the final mark cannot exceed **100**. Part A's shape and force tasks are both required; they are not the two assessed coursework parts. [§§1.1–1.2, PDF p. 5](../resources/2026_2027_DL_Final_Project_Handbook_Shared.pdf#page=5); [§2, PDF pp. 6–8](../resources/2026_2027_DL_Final_Project_Handbook_Shared.pdf#page=6).

## 2. Dates and times

The handbook defines Week 1 as the week commencing **Monday 9 November 2026** and states that deadlines are **23:59 UK time (GMT)**. The progress check is a meeting within the stated date window; no appointment time is specified. [§2.2, PDF p. 8](../resources/2026_2027_DL_Final_Project_Handbook_Shared.pdf#page=8).

| Milestone | Date | What is required |
|---|---|---|
| Handbook release date stated in the document | Tuesday **10 November 2026** | Handbook, slides, dataset and example submission |
| Group list confirmed | Monday **23 November 2026** | Registered Canvas groups of 5–6; groups fixed from this date, subject to the handbook's problem-resolution process |
| Group charter and Part B direction | Sunday **29 November 2026, 23:59 GMT** | Signed charter and one paragraph naming the direction, paper(s), dataset and stakeholder; required, for feedback rather than marks |
| Part B progress check | **30 November–4 December 2026** | Ten-minute meeting with the TA, showing a proof-of-concept result and storyline |
| **Part A submission** | **Sunday 13 December 2026, 23:59 GMT** | Individual ZIP on Canvas and notebook-sharing arrangements below |
| **Part B submission** | **Sunday 20 December 2026, 23:59 GMT** | Group video, code ZIP and contributions form on Canvas, plus confirmation email |
| **Peer assessment closes** | **Wednesday 23 December 2026, 23:59 GMT** | Every student completes the Canvas form |

Sources: [§2.2, PDF p. 8](../resources/2026_2027_DL_Final_Project_Handbook_Shared.pdf#page=8); [§8.1, PDF p. 30](../resources/2026_2027_DL_Final_Project_Handbook_Shared.pdf#page=30); [§8.3, PDF p. 31](../resources/2026_2027_DL_Final_Project_Handbook_Shared.pdf#page=31).

## 3. Required work and mark allocation

### Part A: 60 marks

| Required task | Marks | Essential evidence |
|---|---:|---|
| **Task 1: data preparation** | **10** | Loading and label associations (4); exploratory analysis (3); normalisation and correct splits (3) |
| **Task 2: shape classification** | **20** | At least **three CNN architectures** and an accuracy/efficiency comparison (10); accuracy, macro precision/recall/F1 and confusion matrix (5); discussion and failure analysis (5) |
| **Task 3: force estimation** | **20** | At least **two architectures** with continuous `fx, fy, fz` outputs (10); per-axis and overall RMSE, required tangential analysis and comparison (5); discussion and failure analysis (5) |
| **Task 5: report and visualisation** | **10** | Clear IEEE-format report, methods, results, figures and tables |

The force analysis must separate press and shear observations, compare models with a **training-split mean-force baseline**, plot predicted versus true `fx` and `fy` for shear images, and explain the worst tangential predictions. Report force errors in **newtons**. Hidden-test results support the marking of Tasks 2 and 3; the handbook does not allocate a separate additional block of hidden-test marks. [§§3.4–3.5, PDF pp. 13–15](../resources/2026_2027_DL_Final_Project_Handbook_Shared.pdf#page=13); [§5.3, PDF p. 20](../resources/2026_2027_DL_Final_Project_Handbook_Shared.pdf#page=20); [§10.1, PDF pp. 36–37](../resources/2026_2027_DL_Final_Project_Handbook_Shared.pdf#page=36).

Use **60/20/20 training/validation/test splits**, stratified by shape class and grouped by `contact_id` for force data. Fit normalisation using training data only. Train and validate using **only the released coursework data**: no additional TacVerse data or other tactile datasets. General-purpose pretrained weights such as ImageNet are allowed if identified. This follows the explicit rule in §11.3; see the [wording notes](HANDBOOK_NOTES.md) about the shorter, conflicting wording in §6.5. [§3.3, PDF pp. 11–12](../resources/2026_2027_DL_Final_Project_Handbook_Shared.pdf#page=11); [§11.3, PDF p. 41](../resources/2026_2027_DL_Final_Project_Handbook_Shared.pdf#page=41).

### Part B: 40 marks

| Criterion | Marks | Breakdown |
|---|---:|---|
| Problem and stakeholder | **10** | Clarity and relevance (5); stakeholder analysis (5) |
| Proposed solution overview | **10** | Feasibility (5); creativity and innovation in methods (5) |
| Novelty | **10** | Originality of the overall idea, framing or insight, positioned against the reading-list papers and an obvious alternative |
| Presentation quality | **10** | Clarity and structure, including timing (5); engagement and delivery, with every member presenting (5) |

A trained proof of concept and its code are **mandatory**. The supplementary code is **not separately graded**; it lets markers verify the work shown in the video. Read at least **two** reading-list papers as a group and build the idea on at least **one**, named in the video. Part B may use neither the Part A coursework dataset nor the **GelSight subsets of TacVerse**. [§6.3, PDF pp. 23–24](../resources/2026_2027_DL_Final_Project_Handbook_Shared.pdf#page=23); [§6.6, PDF p. 26](../resources/2026_2027_DL_Final_Project_Handbook_Shared.pdf#page=26); [§10.2, PDF p. 37](../resources/2026_2027_DL_Final_Project_Handbook_Shared.pdf#page=37); [§11.3, PDF p. 41](../resources/2026_2027_DL_Final_Project_Handbook_Shared.pdf#page=41).

### Optional work and bonuses

| Optional work | Maximum bonus | Evidence required |
|---|---:|---|
| Part A data augmentation | **+2** | Effective, physically justified augmentation |
| Part A shape optimisation and regularisation | **+4** | Techniques applied and their effects evidenced |
| Part A force optimisation and regularisation | **+4** | Techniques applied and their effects evidenced |
| Part A Task 4: hyperparameter tuning | **+5** | Systematic search and experimentally justified choices |
| Part A novel approach | **+5** | Creative approach, documented and justified |
| Early submission | **+3 or +5 per part** | Complete submission within the relevant window below |

All bonus sources together are capped at **15 marks**, awarded against the criteria at the instructors' discretion; the final mark is capped at **100**. Collecting new tactile data for Part B is optional and requires prior agreement. [§2.3, PDF p. 8](../resources/2026_2027_DL_Final_Project_Handbook_Shared.pdf#page=8); [§6.7, PDF p. 26](../resources/2026_2027_DL_Final_Project_Handbook_Shared.pdf#page=26); [§9.3, PDF p. 35](../resources/2026_2027_DL_Final_Project_Handbook_Shared.pdf#page=35); [§10.4, PDF p. 38](../resources/2026_2027_DL_Final_Project_Handbook_Shared.pdf#page=38).

## 4. What to submit

### Part A: one individual ZIP on Canvas

Name the ZIP **`DL_Coursework_YourName_CID.zip`**, where `CID` is your eight-digit College ID. Include the following. [§2.1, PDF pp. 7–8](../resources/2026_2027_DL_Final_Project_Handbook_Shared.pdf#page=7); [§9.1, PDF p. 33](../resources/2026_2027_DL_Final_Project_Handbook_Shared.pdf#page=33).

| Item | Filename or location | Requirements |
|---|---|---|
| Report | `DL_Coursework_YourName_CID.pdf` | IEEE conference template, double column, **3–6 pages** through Conclusions and Future Work; references and the AI-use declaration may extend beyond page 6 |
| Code | `code/` | Preprocessing, training, evaluation and any tuning; commented, reproducible, error-free notebooks/scripts; save notebook outputs |
| Model folder | Eight-digit CID folder, e.g. `01234567/` | `predict.py`, all required weights, helper modules and optional pinned `requirements.txt`; **under 200 MB** |

The report's required sections are Abstract, Introduction, Objectives, Methodology, Experiments, Evaluation, Conclusions and Future Work, followed by References and the AI-use declaration. Preserve the IEEE layout. [§§4.1–4.2, PDF pp. 16–18](../resources/2026_2027_DL_Final_Project_Handbook_Shared.pdf#page=16).

`predict.py` must support both specified tasks, return one row per image with the required columns, use images alone, work on CPU and use a GPU when available, make **no downloads during prediction**, and complete **each task within 10 minutes on a Colab GPU runtime**. Test the final extracted model folder in a fresh runtime. Share a Colab notebook with **`l.wei24@imperial.ac.uk`** with viewer access; for a local Jupyter notebook, the copy in `code/` covers this requirement. The ZIP copy is marked. [§§5.2–5.6, PDF pp. 20–22](../resources/2026_2027_DL_Final_Project_Handbook_Shared.pdf#page=20); [§9.1, PDF p. 33](../resources/2026_2027_DL_Final_Project_Handbook_Shared.pdf#page=33).

### Part B: the coordinator submits for the group

| Item | Required filename or action |
|---|---|
| Video | `GroupXX_TactileDL_Video.mp4`; at most **5:00**, including opening and closing cards; **under 1 GB** |
| Captions | Burned in, or matching `GroupXX_TactileDL_Video.srt` |
| Proof-of-concept code | `GroupXX_TactileDL_Code.zip`: `GroupXX_TactileDL.ipynb`, README, optional requirements and model weights; **no raw dataset** |
| Contributions and AI-use form | `GroupXX_TactileDL_Contributions.pdf`, agreed by all members; evidenced shares of effort total **100%** |
| Confirmation email | To **`l.wei24@imperial.ac.uk`**, copying every member; subject **`[DeepLearning] Final Assessment PartB Submission - GroupXX`** |
| Peer assessment | Completed individually on Canvas by the peer-assessment deadline |

`XX` is the two-digit group number. The Part B notebook must run top to bottom in a fresh session, with **`TRAIN = False`** near the top to load saved weights. If a weight file exceeds **100 MB**, put its link in the README. The email includes the group number, title, direction, papers, members, Colab link with viewer access, and video/weights links when needed. If Canvas cannot accept the video, use College OneDrive with module-team view access and submit a text file containing the link on Canvas before the deadline. Do not change the video afterwards. [§7.2, PDF p. 27](../resources/2026_2027_DL_Final_Project_Handbook_Shared.pdf#page=27); [§9.2, PDF pp. 33–35](../resources/2026_2027_DL_Final_Project_Handbook_Shared.pdf#page=33).

## 5. Early submissions, lateness and technical problems

| Part | **+5**: more than two weeks early | **+3**: at least one week early, when the +5 window is not met |
|---|---|---|
| A | **Before 23:59 GMT, Sunday 29 November 2026** | **By 23:59 GMT, Sunday 6 December 2026** |
| B | **Before 23:59 GMT, Sunday 6 December 2026** | **By 23:59 GMT, Sunday 13 December 2026** |

For Part B, **all group files** must be submitted by the cut-off; the bonus goes to each member, and replacing a file afterwards removes it. Early bonuses count within the overall 15-mark bonus cap. [§9.3, PDF p. 35](../resources/2026_2027_DL_Final_Project_Handbook_Shared.pdf#page=35).

The handbook states **5 marks deducted per day late, for up to 7 days**; after more than 7 days, the item receives **zero**. Late Part B files affect the whole group. Extensions require exceptional circumstances, an advance request and appropriate documentation through the College process. **Where College policy differs, College policy applies.** The handbook does not specify partial-day rounding or the order of late deductions relative to moderation and caps; no extra rule is introduced here. [§9.3, PDF p. 35](../resources/2026_2027_DL_Final_Project_Handbook_Shared.pdf#page=35).

If Canvas fails near the deadline, email the TA **before the deadline** with a share link and screenshot of the error; the handbook treats this as on time if the files remain unchanged. Only the coordinator uploads Part B, and the last upload before the deadline is marked. [§9.4, PDF p. 35](../resources/2026_2027_DL_Final_Project_Handbook_Shared.pdf#page=35).

## 6. Peer assessment and moderation

Each student rates **every group member, including themselves**, from **1 to 5** on attendance/communication, technical contribution, video contribution, research/stakeholder/novelty work, and reliability. Ratings are confidential. A rating of **1 or 2** needs a brief reason supported by evidence. [§8.6, PDF p. 32](../resources/2026_2027_DL_Final_Project_Handbook_Shared.pdf#page=32).

The peer score is the average total received across those five criteria. Divide a student's peer score by the group's average to obtain the peer factor, `PF`. If **0.90 ≤ PF ≤ 1.10**, it is set to **1**. Otherwise it is used subject to the usual **0.50–1.10** bounds, with the moderated Part B mark capped at **40**. Documented non-contribution can reduce `PF` below 0.50, down to zero. The module team checks adjustments against the charter, minutes, logs and contributions form and can override unfair or coordinated ratings. [§10.3, PDF pp. 37–38](../resources/2026_2027_DL_Final_Project_Handbook_Shared.pdf#page=37).

The handbook's overall formula is `min(100, A + B × PF + Bonus)`, with `B × PF ≤ 40` and `Bonus ≤ 15`; its late-submission rules are stated separately. [§2, PDF p. 6](../resources/2026_2027_DL_Final_Project_Handbook_Shared.pdf#page=6); [§9.3, PDF p. 35](../resources/2026_2027_DL_Final_Project_Handbook_Shared.pdf#page=35); [§10.3, PDF pp. 37–38](../resources/2026_2027_DL_Final_Project_Handbook_Shared.pdf#page=37).

## 7. Academic integrity and AI use

Part A is individual: do not share its code, models, results or report, including with Part B teammates. Every Part B member is responsible for the whole group submission. Cite sources, adapted code, datasets, pretrained weights and media; report actual results and use validation rather than test data for model selection. [§11.1, PDF p. 40](../resources/2026_2027_DL_Final_Project_Handbook_Shared.pdf#page=40).

| AI-assisted activity | Handbook rule |
|---|---|
| Brainstorming, concept explanations or debugging | Allowed, declared |
| Generating/completing code | Allowed, declared; understand, test and be able to explain every line |
| Improving grammar/clarity of text you wrote | Allowed, declared |
| Video editing, captions or graphics | Allowed, declared; label AI-generated images |
| Writing whole sections of the Part A report | Not allowed; the ideas, analysis and wording must be yours |
| AI voices, avatars or deepfakes replacing presenters | Not allowed; §7.2 allows only a reasonable adjustment agreed with the module team |
| Generating/changing data, results or references | §11.2 uses a blanket prohibition; see the specific Direction E clarification below |

Declare the tool name/version, purpose, affected parts and how you checked the output. Put the declaration **after the Part A references** and in the **Part B contributions and AI-use form**; state explicitly if no AI was used. [§11.2, PDF p. 40](../resources/2026_2027_DL_Final_Project_Handbook_Shared.pdf#page=40); [§7.2, PDF p. 27](../resources/2026_2027_DL_Final_Project_Handbook_Shared.pdf#page=27).

**Check with the module team before choosing synthetic-data generation:** Direction E proposes GAN/diffusion generation, while the AI-use table uses broader prohibitory wording. The supplied PDF is preserved as provided; this summary does not invent an exception. See [Handbook wording notes](HANDBOOK_NOTES.md). [§6.4, PDF p. 25](../resources/2026_2027_DL_Final_Project_Handbook_Shared.pdf#page=25); [§11.2, PDF p. 40](../resources/2026_2027_DL_Final_Project_Handbook_Shared.pdf#page=40).

For questions, the handbook names **Dr Dandan Zhang**, module leader (`d.zhang17@imperial.ac.uk`), and **Ms Lan Wei**, teaching assistant (`l.wei24@imperial.ac.uk`). Clarifications affecting the class are announced on Canvas. [§1.3, PDF p. 5](../resources/2026_2027_DL_Final_Project_Handbook_Shared.pdf#page=5).
