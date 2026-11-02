"""Example submission: inference script for both coursework tasks.

This file shows the required submission INTERFACE. The model itself is a deliberately
small baseline. Replace it with your own model, but keep the command line and the output
CSV format exactly as below.

    python predict.py --task shape --images <folder of .jpg> --out preds.csv
    python predict.py --task force --images <folder of .jpg> --out preds.csv

Output CSV columns
    shape : filename, class_id
    force : filename, fx, fy, fz   (newtons, original scale)

`filename` is the image file name only (e.g. test_0001.jpg). The images folder is flat
(no class sub-folders). Weights are loaded from files next to this script.
"""

from __future__ import annotations

import argparse
from pathlib import Path

import numpy as np
import pandas as pd
import torch
import torch.nn as nn
from PIL import Image

HERE = Path(__file__).resolve().parent
WEIGHTS = {"shape": HERE / "shape_model.pt", "force": HERE / "force_model.pt"}
OUTPUT_DIM = {"shape": 10, "force": 3}
INPUT_SIZE = (160, 120)  # (width, height) fed to the network


class SmallCNN(nn.Module):
    def __init__(self, out_dim: int):
        super().__init__()

        def block(c_in: int, c_out: int) -> nn.Sequential:
            return nn.Sequential(
                nn.Conv2d(c_in, c_out, 3, padding=1),
                nn.BatchNorm2d(c_out),
                nn.ReLU(inplace=True),
                nn.MaxPool2d(2),
            )

        self.features = nn.Sequential(block(3, 16), block(16, 32), block(32, 64), block(64, 128))
        self.head = nn.Sequential(nn.AdaptiveAvgPool2d(1), nn.Flatten(), nn.Linear(128, out_dim))

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        return self.head(self.features(x))


def load_image(path: Path) -> torch.Tensor:
    img = Image.open(path).convert("RGB").resize(INPUT_SIZE, Image.BILINEAR)
    x = torch.from_numpy(np.asarray(img, dtype=np.float32) / 255.0).permute(2, 0, 1)
    return (x - 0.5) / 0.5


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--task", choices=["shape", "force"], required=True)
    parser.add_argument("--images", type=Path, required=True, help="Flat folder of .jpg images")
    parser.add_argument("--out", type=Path, required=True, help="Where to write the predictions CSV")
    args = parser.parse_args()

    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    ckpt = torch.load(WEIGHTS[args.task], map_location=device)
    model = SmallCNN(OUTPUT_DIM[args.task]).to(device)
    model.load_state_dict(ckpt["state_dict"])
    model.eval()

    files = sorted(args.images.glob("*.jpg"))
    outputs = []
    with torch.no_grad():
        for i in range(0, len(files), 64):
            batch = torch.stack([load_image(p) for p in files[i : i + 64]]).to(device)
            outputs.append(model(batch).cpu())
    outputs = torch.cat(outputs).numpy()

    names = [p.name for p in files]
    if args.task == "shape":
        preds = pd.DataFrame({"filename": names, "class_id": outputs.argmax(axis=1)})
    else:
        # The network predicts standardised forces; convert back to newtons.
        forces = outputs * np.array(ckpt["target_std"]) + np.array(ckpt["target_mean"])
        preds = pd.DataFrame({"filename": names, "fx": forces[:, 0], "fy": forces[:, 1], "fz": forces[:, 2]})

    preds.to_csv(args.out, index=False)
    print(f"wrote {len(preds)} predictions to {args.out}")


if __name__ == "__main__":
    main()
