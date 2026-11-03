# Part B: advanced tactile perception project and video

[Repository home](../README.md) · [Assessment overview](ASSESSMENT_OVERVIEW.md) · [Part A guide](COURSEWORK_GUIDE.md) · [Complete handbook](../resources/2026_2027_DL_Final_Project_Handbook_Shared.pdf)

Part B develops an advanced tactile perception proposal supported by a trained proof-of-concept model. Groups of 5–6 students present their work for a defined stakeholder in a video of at most 5 minutes, with every member presenting. The component carries 40 marks and is due on Sunday 20 December 2026 at 23:59 UK time (GMT). Submit assessed work through Canvas. [§1.2, PDF p. 5](../resources/2026_2027_DL_Final_Project_Handbook_Shared.pdf#page=5); [§2.2, PDF p. 8](../resources/2026_2027_DL_Final_Project_Handbook_Shared.pdf#page=8); [§9.2, PDF pp. 33–35](../resources/2026_2027_DL_Final_Project_Handbook_Shared.pdf#page=33).

This guide accompanies the Part A dataset repository and summarises the 2026/27 Final Project Handbook. The cover’s “released Tuesday 10 November 2026” label identifies the source version. PDF page references include the cover. [Handbook cover, PDF p. 1](../resources/2026_2027_DL_Final_Project_Handbook_Shared.pdf#page=1).

On this page: [Project scope](#1-project-scope) · [Reading](#2-preparatory-reading) · [Directions](#3-project-directions) · [Data and evaluation](#4-data-choice-and-evaluation-protocol) · [Proof of concept](#5-proof-of-concept-requirements) · [Video](#6-video-and-assessment-criteria) · [Group work](#7-group-organisation-and-records) · [Submissions](#8-submission-requirements) · [AI and attribution](#9-ai-use-attribution-and-consent) · [Checklist](#10-submission-checklist)

<a id="1-what-you-are-proposing-and-what-you-must-build"></a>

## 1. Project scope

The proposed solution describes the complete system and its value to a stakeholder. The proof of concept is the smaller, implemented model used to demonstrate the central technical idea. A full system implementation is not required; a working proof of concept is mandatory. The stakeholder might need reliable grasping, material inspection, assistive touch or palpation, but the video must identify a specific user and their needs. [§6, PDF p. 22](../resources/2026_2027_DL_Final_Project_Handbook_Shared.pdf#page=22); [§7.3, PDF pp. 27–28](../resources/2026_2027_DL_Final_Project_Handbook_Shared.pdf#page=27).

“Advanced” means going beyond Part A's single-image shape classification and force regression in at least one way: a different model type, a harder setting, another sensing modality, or another tactile property or task. The handbook's examples include graph networks on markers, self-supervised or generative models, cross-sensor transfer, few-label learning, temporal slip prediction, vision–touch fusion, and material or hardness perception. Do not use the Part A coursework dataset in Part B. [§6.1, PDF pp. 22–23](../resources/2026_2027_DL_Final_Project_Handbook_Shared.pdf#page=22).

<a id="2-start-with-the-reading-list"></a>

## 2. Preparatory reading

Each group must read at least two papers before choosing a direction and develop its project from at least one paper in the handbook’s reading list. Identify the source paper in the video, display its reference on screen, cite it in the README and explain the group’s contribution beyond that work. Building the sensors described in the papers is not required. [§6.3, PDF pp. 23–24](../resources/2026_2027_DL_Final_Project_Handbook_Shared.pdf#page=23).

| Reading-list entry | Project relevance |
|---|---|
| TactEx | Explainable touch and hardness estimation; Direction A |
| ViTacTip | Visual and tactile cues, contact and force sensing; Directions A and F |
| Tac-VGNN | Marker graphs, Voronoi features and graph learning; Direction B |
| TacVerse | Within-sensor, cross-sensor and few-shot evaluation; Direction C |
| SARL | Spatially aware self-supervised visuo-tactile learning; Directions C and D |
| Sparsh | Self-supervised tactile representations and pretrained encoders; Direction C |
| Multi-modality sensor with GAN interpretation | Cross-modal translation; Direction D |
| MultiDiffSense | Diffusion-based tactile generation; Direction E, subject to the wording clarification below |
| The Feeling of Success | Grasp outcomes and tactile evidence; Direction F |
| MagicTac and CrystalTac | Sensor designs relevant if you propose to collect data |

The reading list and its relationship to the project directions are specified in [§6.3, PDF pp. 23–24](../resources/2026_2027_DL_Final_Project_Handbook_Shared.pdf#page=23). Full bibliographic entries appear in the [handbook references, PDF pp. 50–51](../resources/2026_2027_DL_Final_Project_Handbook_Shared.pdf#page=50).

<a id="3-choose-one-direction"></a>

## 3. Project directions

Submit a one-paragraph proposal by Sunday 29 November 2026, 23:59 GMT. Identify the direction, source paper or papers, dataset and stakeholder. This submission receives feedback and is not marked. Direction G requires approval at this stage. [§2.2, PDF p. 8](../resources/2026_2027_DL_Final_Project_Handbook_Shared.pdf#page=8); [§6.4, PDF pp. 24–25](../resources/2026_2027_DL_Final_Project_Handbook_Shared.pdf#page=24).

| Direction | Main technical focus | Starting papers | Dataset suggestions in the handbook |
|---|---|---|---|
| A. Material, texture or hardness with explanations | Classification and explainability | TactEx; ViTacTip | Touch and Go; ObjectFolder Real; eligible TacVerse grating data |
| B. Graph learning on tactile markers | Graph neural networks | Tac-VGNN | Eligible marker-based TacVerse or TacTip-family data |
| C. Cross-sensor generalisation and self-supervised pretraining | Transfer, few-shot or self-supervised learning | TacVerse; SARL; Sparsh | TacVerse sensors other than GelSight; Touch-Slide |
| D. Visuo-tactile fusion and cross-modal translation | Fusion or GAN translation | Multi-modality sensor with GAN interpretation; SARL | Touch and Go; ObjectFolder Real |
| E. Generative tactile data | Diffusion or GAN generation | MultiDiffSense | A small real dataset plus generated images, subject to clarification below |
| F. Slip and grasp-outcome detection | Temporal classification | The Feeling of Success; ViTacTip | Feeling of Success; YCB-Slide |
| G. Your own idea | An advanced setting meeting §6.1 | At least one reading-list paper | Dataset agreed with the module team by 29 November |

Source: [§6.4, PDF p. 25](../resources/2026_2027_DL_Final_Project_Handbook_Shared.pdf#page=25). The term “eligible” reflects the exclusion of the Part A dataset and all GelSight subsets of TacVerse. [§11.3, PDF p. 41](../resources/2026_2027_DL_Final_Project_Handbook_Shared.pdf#page=41).

Seek clarification from the module team before selecting synthetic-data generation. Direction E proposes GAN or diffusion methods, while §11.2 prohibits generating or changing data more broadly. The [handbook notes](HANDBOOK_NOTES.md#2-synthetic-data-research-and-the-ai-use-table) set out the unresolved scope of these provisions. [§6.4, PDF p. 25](../resources/2026_2027_DL_Final_Project_Handbook_Shared.pdf#page=25); [§11.2, PDF p. 40](../resources/2026_2027_DL_Final_Project_Handbook_Shared.pdf#page=40).

## 4. Data choice and evaluation protocol

The handbook permits a documented subset of a suitable dataset. Its dataset list includes TacVerse, Touch and Go, ObjectFolder Real, Feeling of Success, YCB-Slide and Touch-Slide. It describes Touch-Slide as an unlabelled resource for self-supervised pretraining, and permits pretrained tactile encoders such as Sparsh provided that you train and evaluate your own model. A different dataset can be proposed in your direction paragraph so the module team can check suitability. [§6.5, PDF pp. 25–26](../resources/2026_2027_DL_Final_Project_Handbook_Shared.pdf#page=25); [§15.2, PDF p. 46](../resources/2026_2027_DL_Final_Project_Handbook_Shared.pdf#page=46).

Apply the following data requirements:

- Exclude the Part A coursework dataset and the GelSight subsets of TacVerse from Part B.
- Follow the dataset's licence, cite it and document the subset. Do not redistribute raw data in your submission.
- Split by object, session, trial or sensor, never by individual frame. Use 60/20/20 or 70/15/15 training/validation/test proportions.
- Fit normalisation on the training set only.

Sources: [§§6.5–6.6, PDF pp. 25–26](../resources/2026_2027_DL_Final_Project_Handbook_Shared.pdf#page=25); [§11.3, PDF p. 41](../resources/2026_2027_DL_Final_Project_Handbook_Shared.pdf#page=41).

Collecting your own data is optional and must be agreed with the module team by the direction deadline. The handbook requires a safety induction and TA agreement before using laboratory robots or sensors; work involving people requires College ethical approval before collection. Keep collected data in College OneDrive or Teams and document collection and labelling. The creativity criterion primarily concerns innovation in methods rather than dataset novelty. [§6.7, PDF p. 26](../resources/2026_2027_DL_Final_Project_Handbook_Shared.pdf#page=26); [§11.3, PDF p. 41](../resources/2026_2027_DL_Final_Project_Handbook_Shared.pdf#page=41).

<a id="5-the-seven-proof-of-concept-requirements"></a>

## 5. Proof-of-concept requirements

Every group must meet all seven requirements below. [§6.6, PDF p. 26](../resources/2026_2027_DL_Final_Project_Handbook_Shared.pdf#page=26).

| Requirement | Required evidence |
|---|---|
| One advanced task and one dataset | State the task, dataset and documented subset |
| Leakage-free train/validation/test split | Group by object, session, trial or sensor; training-only normalisation |
| A model trained by your group | Training code and saved weights; fine-tuning a pretrained network is allowed |
| A reference point | A trivial baseline or simpler model; for cross-sensor work, a within-sensor score is a natural reference |
| Test-set results | Classification: accuracy, macro F1 and confusion matrix. Regression: RMSE, MAE and a predicted-versus-true plot |
| At least one failure case | A documented example and explanation of the failure |
| A short demonstration clip | Model predictions on test examples, shown by screen recording or with a live sensor |

Proof-of-concept code is required as supplementary material and is not separately graded. No minimum accuracy threshold is specified. Assessment considers the feasibility, reasoning and originality of the proposed solution, supported by credible experimental evidence. State the scope and limitations of that evidence. [§6.6, PDF p. 26](../resources/2026_2027_DL_Final_Project_Handbook_Shared.pdf#page=26); [§7.3, PDF p. 28](../resources/2026_2027_DL_Final_Project_Handbook_Shared.pdf#page=28); [§15.2, PDF p. 46](../resources/2026_2027_DL_Final_Project_Handbook_Shared.pdf#page=46).

<a id="6-build-the-video-around-the-marking-criteria"></a>

## 6. Video and assessment criteria

Address an imagined panel comprising a robotics engineer, a potential user and a funder. Each should understand the problem, stakeholder, proposed system, experimental evidence, novelty and operating limits. [§7.1, PDF p. 27](../resources/2026_2027_DL_Final_Project_Handbook_Shared.pdf#page=27).

| Criterion | Marks | Assessment evidence |
|---|---:|---|
| Problem and stakeholder | 10 | A clearly defined tactile problem and its relevance (5), plus the stakeholder's needs, objectives and potential impact (5) |
| Proposed solution | 10 | Realistic methods, data, metrics, risks and proof-of-concept evidence (5), plus innovation in methods rather than simply a new dataset (5) |
| Novelty | 10 | What is original about the overall idea, framing or insight compared with the reading-list work and the obvious approach |
| Presentation | 10 | Coherent structure within the limit (5), and clear, engaging delivery with every member presenting (5) |

Sources: [§7.3, PDF pp. 27–28](../resources/2026_2027_DL_Final_Project_Handbook_Shared.pdf#page=27); [§10.2, PDF p. 37](../resources/2026_2027_DL_Final_Project_Handbook_Shared.pdf#page=37).

### Video requirements

| Item | Requirement |
|---|---|
| Duration | 5:00 maximum including opening/closing cards; markers stop at 5:00. The handbook suggests aiming for 4:30–4:50 |
| Presenters | Every member is seen or heard presenting a segment, with their name shown on screen |
| Voice | Each member uses their own voice; AI voice clones, avatars or text-to-speech cannot replace presenters unless agreed as a reasonable adjustment |
| Evidence | Show the test result against its reference point, a short model demonstration on real test data, and the research connection |
| Opening card | Group number, project title and member names, approximately 5 seconds |
| Closing card | Contributions, datasets and third-party media with licences, approximately 10 seconds |
| Captions | Required: burned in or a matching `.srt`; correct automatic captions before submission |
| Encoding and size | MP4, H.264 video and AAC audio; 1920 × 1080 preferred, 1280 × 720 minimum; under 1 GB |

Source: [§7.2, PDF p. 27](../resources/2026_2027_DL_Final_Project_Handbook_Shared.pdf#page=27). Narrating over slides in your own voice is acceptable if a member cannot appear on camera; other adjustments should be discussed with the module team. [§15.2, PDF p. 46](../resources/2026_2027_DL_Final_Project_Handbook_Shared.pdf#page=46).

### Suggested running order

The suggested running order ends at 4:45, leaving a 15-second margin. These timings are advisory. In a group of six, each member may present one content segment; in a group of five, one member takes two shorter segments. [§7.4, PDF pp. 28–29](../resources/2026_2027_DL_Final_Project_Handbook_Shared.pdf#page=28).

| Time | Content |
|---|---|
| 0:00–0:05 | Opening card |
| 0:05–0:45 | Introduction, tactile problem and the role of touch |
| 0:45–1:25 | Stakeholder and what success means to them |
| 1:25–2:15 | Proposed solution, data, model, feasibility and key risks |
| 2:15–3:05 | Proof-of-concept result, reference point, demo and failure case |
| 3:05–3:55 | Novelty against the papers and obvious approach |
| 3:55–4:35 | Impact and summary |
| 4:35–4:45 | Closing card and credits |

Agree a storyboard before recording, time the narration, use a shared visual style and planned handovers, and watch the full video together. Address the one or two most important stakeholder risks, with concrete mitigations. Use media you have the right to use, cite paper figures on screen, obtain consent for people outside the group who appear, and keep personal data off screen. [§§7.5–7.7, PDF pp. 29–30](../resources/2026_2027_DL_Final_Project_Handbook_Shared.pdf#page=29).

<a id="7-organise-and-document-the-group-work"></a>

## 7. Group organisation and records

Form and register a group of 5–6 on Canvas in Weeks 1–2. The list is confirmed on Monday 23 November 2026. The module team places ungrouped students and may merge or add to groups smaller than five. Groups are fixed from that date except through the handbook's problem-resolution process. [§8.1, PDF p. 30](../resources/2026_2027_DL_Final_Project_Handbook_Shared.pdf#page=30).

Assign the six lead roles specified in the handbook: coordination and stakeholder analysis; research and novelty; data; modelling; evaluation and demonstration; and video production. A group of five combines two roles. Every member must contribute to technical work, present in the video and review the final video, code and contributions form. Video editing alone does not meet the technical-contribution requirement. Part A remains individual: do not share its code, models, results or reports within the group. [§§8–8.2, PDF pp. 30–31](../resources/2026_2027_DL_Final_Project_Handbook_Shared.pdf#page=30); [§11.1, PDF p. 40](../resources/2026_2027_DL_Final_Project_Handbook_Shared.pdf#page=40).

A ten-minute progress check with the TA takes place during 30 November–4 December 2026. Present a proof-of-concept result and the proposed video storyline. [§2.2, PDF p. 8](../resources/2026_2027_DL_Final_Project_Handbook_Shared.pdf#page=8).

### Charter, meetings and contribution records

| Record or activity | Required content |
|---|---|
| One-page signed charter, due 29 November, 23:59 GMT | Members/roles; communication and response expectations; weekly meeting; decision process; internal deadlines; handling missed work. Every member signs. Upload with the direction paragraph; required but not marked |
| At least one meeting each week, lasting 30–60 minutes | Progress and decisions; minutes containing date, attendance, actions, owners and due dates |
| Personal contribution log | Date, task, hours and evidence link for each member |
| Shared work location | Shared drive/Teams for files and GitHub or shared Colab for code |
| Contributions form | Agreed contributions, evidence and effort shares adding to 100%, plus AI-use declaration |

Sources: [§§8.3–8.4, PDF p. 31](../resources/2026_2027_DL_Final_Project_Handbook_Shared.pdf#page=31); [§9.2, PDF p. 34](../resources/2026_2027_DL_Final_Project_Handbook_Shared.pdf#page=34). Templates for the charter, minutes, contribution logs, storyboard and contributions form are provided in [Appendix A.2–A.6, PDF pp. 48–49](../resources/2026_2027_DL_Final_Project_Handbook_Shared.pdf#page=48).

Raise contribution concerns promptly in a group meeting and record them in the minutes. If unresolved within a week, any member should email the TA with the minutes, preferably before Monday 7 December 2026 so there is time to act. The module team may agree an action plan, issue a written warning and apply moderation or an alternative task for continuing non-contribution. Illness or other circumstances should be raised through the College process; one member's circumstances do not normally move the group deadline. [§8.5, PDF p. 32](../resources/2026_2027_DL_Final_Project_Handbook_Shared.pdf#page=32).

### Peer assessment

Every student completes the confidential Canvas peer-assessment form after the Part B deadline and by Wednesday 23 December 2026, 23:59 GMT. Rate all members, including yourself, on attendance/communication, technical work, video contribution, research/stakeholder/novelty work and reliability. Scores run from 1 to 5; scores of 1 or 2 need evidence. [§8.6, PDF p. 32](../resources/2026_2027_DL_Final_Project_Handbook_Shared.pdf#page=32).

Each member normally receives the group mark. Moderation uses the ratio of a student's average peer score to the group average; ratios in 0.90–1.10 are set to 1. Other ratios normally stay within 0.50–1.10, with the Part B mark capped at 40; documented non-contribution may reduce the factor further, to zero. The module team checks records before applying adjustments and can override unfair ratings. [§10.3, PDF pp. 37–38](../resources/2026_2027_DL_Final_Project_Handbook_Shared.pdf#page=37).

<a id="8-package-and-submit-the-work"></a>

## 8. Submission requirements

The coordinator submits the group’s work by Sunday 20 December 2026, 23:59 GMT, using the assigned two-digit group number in place of `XX`. [§9.2, PDF pp. 33–35](../resources/2026_2027_DL_Final_Project_Handbook_Shared.pdf#page=33).

| Deliverable | Required filename and contents |
|---|---|
| Video | `GroupXX_TactileDL_Video.mp4`; also `GroupXX_TactileDL_Video.srt` if captions are separate |
| Code ZIP | `GroupXX_TactileDL_Code.zip` containing `GroupXX_TactileDL.ipynb`, `README.md`, optional `requirements.txt`, and `models/` with the saved model |
| Contributions and AI-use form | `GroupXX_TactileDL_Contributions.pdf`, agreed by the whole group |
| Confirmation email | Coordinator emails the TA, copying every member and sharing the Colab notebook with viewer access |

The notebook must run top to bottom in a fresh session. Set `TRAIN = False` near the top to load saved weights, fix seeds and print library versions. The README identifies the dataset, subset and how to run. Include no raw dataset. If a model weight file exceeds 100 MB, provide its link in the README instead. [§9.2, PDF p. 34](../resources/2026_2027_DL_Final_Project_Handbook_Shared.pdf#page=34).

Send the confirmation to `l.wei24@imperial.ac.uk`, with subject `[DeepLearning] Final Assessment PartB Submission - GroupXX`. Include the group number, title, direction (A–G), source papers, member names and College emails, notebook viewer link, video link if not uploaded to Canvas, weights link if a file exceeds 100 MB, and any additional information relevant to assessment. [§9.2, PDF pp. 34–35](../resources/2026_2027_DL_Final_Project_Handbook_Shared.pdf#page=34).

If Canvas cannot accept the video, use College OneDrive with module-team view access and submit a text file containing the link on Canvas before the deadline; do not change it afterwards. If Canvas fails near the deadline, email the TA before the deadline with a share link and an error screenshot; the handbook accepts this as on time if the files do not change afterwards. Only the coordinator uploads Part B, and the last upload before the deadline is marked. [§§9.2–9.4, PDF pp. 34–35](../resources/2026_2027_DL_Final_Project_Handbook_Shared.pdf#page=34).

### Early and late submissions

For Part B, submitting all files before 23:59 GMT on Sunday 6 December 2026 qualifies for the +5 early window; submitting by 23:59 GMT on Sunday 13 December 2026 qualifies for +3 when the +5 window is not met. The bonus goes to every member, and later file replacement removes it. All bonuses across both parts are capped at 15, and the final mark at 100. [§9.3, PDF p. 35](../resources/2026_2027_DL_Final_Project_Handbook_Shared.pdf#page=35); [§10.4, PDF p. 38](../resources/2026_2027_DL_Final_Project_Handbook_Shared.pdf#page=38).

The late penalty is 5 marks per day for up to 7 days; after more than 7 days, the submission receives zero. Late Part B files affect the whole group. Exceptional extensions require an advance request with documentation; where College policy differs, College policy applies. The handbook does not specify partial-day rounding or the order of deductions. [§9.3, PDF p. 35](../resources/2026_2027_DL_Final_Project_Handbook_Shared.pdf#page=35).

## 9. AI use, attribution and consent

Declared AI assistance is permitted for brainstorming, conceptual explanations, debugging, generating or completing code that you understand and test, improving your own text, and supporting video editing, captions or graphics. Label AI-generated images in the video. Members must present in their own voices; replacements by AI voices, avatars or deepfakes are not allowed except for an agreed reasonable adjustment. Cite adapted code, papers, datasets, pretrained weights and media, and report the results your code actually produces. [§11.1–§11.2, PDF p. 40](../resources/2026_2027_DL_Final_Project_Handbook_Shared.pdf#page=40); [§7.2, PDF p. 27](../resources/2026_2027_DL_Final_Project_Handbook_Shared.pdf#page=27).

The group declaration must name the tools and versions, their purposes, affected submission parts and how outputs were checked; say explicitly if no AI was used. Include it in the agreed contributions form. The scope of the rule for experimental synthetic-data generation requires clarification, as noted under Direction E and in the [handbook notes](HANDBOOK_NOTES.md#2-synthetic-data-research-and-the-ai-use-table). [§11.2, PDF p. 40](../resources/2026_2027_DL_Final_Project_Handbook_Shared.pdf#page=40); [Appendix A.6, PDF p. 49](../resources/2026_2027_DL_Final_Project_Handbook_Shared.pdf#page=49).

Every member must agree before a video is shown to future cohorts; refusing has no effect on marks. Public posting after marks are released requires every member's agreement and permission for public sharing of every media item. [§7.7, PDF p. 30](../resources/2026_2027_DL_Final_Project_Handbook_Shared.pdf#page=30); [§15.2, PDF pp. 46–47](../resources/2026_2027_DL_Final_Project_Handbook_Shared.pdf#page=46).

<a id="10-final-check"></a>

## 10. Submission checklist

Use the following checks before the coordinator submits the work:

- Technical evidence: an advanced task, eligible dataset, grouped split, trained model, reference point, required test metrics, failure case and demonstration.
- Code package: a notebook that runs with `TRAIN = False`, a complete README, saved weights or the permitted link, and no raw data.
- Video: at most 5:00, every member presenting, corrected captions and complete media credits.
- Group administration: an agreed contributions form, completed upload and confirmation email, and awareness of the peer-assessment deadline.

The complete checklist appears in [§14.2, PDF pp. 44–45](../resources/2026_2027_DL_Final_Project_Handbook_Shared.pdf#page=44).
