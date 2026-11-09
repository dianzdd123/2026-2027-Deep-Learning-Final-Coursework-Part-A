# Deep Learning Coursework 2026–2027: Part A

**Imperial College London · I-X MSc AIAI**  
**Lecturer:** Dandan Zhang · **Teaching assistant:** Lan Wei

Build and compare models for **ten-class shape classification** and **3D force estimation** from tactile images.

**Individual coursework · 60 marks · Due 13 December 2026, 23:59 GMT on Canvas**

## Start here

1. Read the [simplified handbook](docs/COURSEWORK_GUIDE.md).
2. [Download Tactile_DL_2027.zip](https://github.com/dianzdd123/2026-2027-Deep-Learning-Final-Coursework-Part-A/releases/download/v1.0.2/Tactile_DL_2027.zip) (37.44 MB). The images are in this archive, not **Code → Download ZIP**.
3. Open the [Colab notebook](https://colab.research.google.com/github/dianzdd123/2026-2027-Deep-Learning-Final-Coursework-Part-A/blob/main/notebooks/01_explore_dataset.ipynb) or follow [setup instructions](docs/GETTING_STARTED.md).
4. Train, evaluate and package your models using the [submission interface](example_submission/README.md).

| Task | Required work | Marks |
|---|---|---:|
| Data preparation | Inspect images and labels; create 60/20/20 splits | 10 |
| Shape classification | Compare at least three CNN architectures | 20 |
| Force estimation | Compare at least two models predicting `fx,fy,fz` | 20 |
| Technical report | 3–6 pages, IEEE double-column format | 10 |
| Optional tuning | Document a systematic validation-based search | Up to +5 |

Use only the released tactile data for Part A. Split force data by `contact_id`; keep each press/shear pair together.

![Shape examples](docs/assets/shape_examples.jpg)

[Dataset labels](docs/DATASET_CARD.md) · [Part B](docs/PART_B_GUIDE.md)

Submit assessed work on **Canvas**. Check Canvas for announcements and the current simplified handbook.

Questions: `d.zhang17@imperial.ac.uk` or `l.wei24@imperial.ac.uk`.  
Email subject: `[2026-Deep-Learning-Inquiry]-[Name]`.
