# Part A submission-interface example

[Correct handbook](../resources/2026_2027_DL_Final_Project_Handbook_Shared.pdf#page=19) · [Part A guide](../docs/COURSEWORK_GUIDE.md) · [Repository overview](../README.md)

The scripts, dependency file and checkpoints here are unchanged copies from `Tactile_DL_2027.zip`. They demonstrate the interface required for both Part A learning tasks:

```bash
python predict.py --task shape --images <IMAGE_DIR> --out <OUT_CSV>
python predict.py --task force --images <IMAGE_DIR> --out <OUT_CSV>
```

The shape CSV contains `filename,class_id`; the force CSV contains `filename,fx,fy,fz`, in newtons on the original scale. Use file names only and return one row per input JPEG. The hidden-test image folder is flat and anonymous.

**The supplied weights are interface demonstrations.** `train_example.py` uses all released images, so these weights cannot support held-out coursework performance claims. Students must create the required splits, compare at least three shape CNN architectures and at least two force architectures, and report their own experiments.

The submitted model folder is named with the student's eight-digit CID and must be under **200 MB**. Load bundled weights with relative paths, support CPU inference and avoid downloads at prediction time. Each task must finish within ten minutes on a Colab GPU runtime. See [Sections 5.3–5.4](../resources/2026_2027_DL_Final_Project_Handbook_Shared.pdf#page=20) and the [Part A guide](../docs/COURSEWORK_GUIDE.md) for exact requirements and the self-check.

The repository's exploration requirements are separate from the submission dependency file. The latter lists only extra packages not pre-installed in Colab, with pinned versions; the handbook says not to list `torch` or `torchvision`.
