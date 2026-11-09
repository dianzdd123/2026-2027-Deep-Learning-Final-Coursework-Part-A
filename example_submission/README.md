# Prediction Interface

[Home](../README.md) · [Simplified handbook](../docs/COURSEWORK_GUIDE.md#7-submit-your-work)

Use the supplied `predict.py` as an interface example. Train and evaluate your own models: the example checkpoints were trained on all released images.

## Commands

Run from your CID-named model folder:

```bash
python predict.py --task shape --images <IMAGE_DIR> --out <OUT_CSV>
python predict.py --task force --images <IMAGE_DIR> --out <OUT_CSV>
```

Input: a flat folder of anonymous JPEGs. Output: one row per image.

| Task | CSV columns |
|---|---|
| Shape | `filename,class_id` (integer 0–9) |
| Force | `filename,fx,fy,fz` (newtons, original sign) |

## Model folder

Include `predict.py`, weights and any helper modules in a folder named with your eight-digit CID.

- Keep the folder **under 200 MB**.
- Load local weights relative to the script; download nothing during inference.
- Support CPU and GPU.
- Finish each task within **10 minutes on a Colab GPU**.
- Use the same preprocessing as training and reverse force standardisation before output.
- If needed, list only additional pinned packages in `requirements.txt`; exclude `torch` and `torchvision`.

Test both commands in a clean environment before submission.
