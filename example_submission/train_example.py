"""Train the example baseline and save weights in the format predict.py expects.

This script only exists so that the example submission has working weights. It trains on
ALL released images without a validation/test split, which is NOT an acceptable protocol
for your coursework. Use your own 60/20/20 split.

    python train_example.py --data /content/Tactile_DL_2027
"""

from __future__ import annotations

import argparse
from pathlib import Path

import pandas as pd
import torch
import torch.nn as nn
from torch.utils.data import DataLoader, TensorDataset

from predict import OUTPUT_DIM, WEIGHTS, SmallCNN, load_image

AXES = ["fx", "fy", "fz"]


def train(model: nn.Module, x: torch.Tensor, y: torch.Tensor, loss_fn, epochs: int, device) -> None:
    loader = DataLoader(TensorDataset(x, y), batch_size=64, shuffle=True)
    optimiser = torch.optim.Adam(model.parameters(), lr=1e-3)
    model.to(device).train()
    for epoch in range(1, epochs + 1):
        total = 0.0
        for xb, yb in loader:
            xb, yb = xb.to(device), yb.to(device)
            optimiser.zero_grad()
            loss = loss_fn(model(xb), yb)
            loss.backward()
            optimiser.step()
            total += loss.item() * len(xb)
        print(f"  epoch {epoch:2d}  loss {total / len(x):.4f}")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--data", type=Path, required=True, help="Path to Tactile_DL_2027/")
    parser.add_argument("--epochs", type=int, default=10)
    args = parser.parse_args()
    torch.manual_seed(0)
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

    print("shape classification")
    root = args.data / "shape_classification"
    df = pd.read_csv(root / "labels.csv")
    x = torch.stack([load_image(root / f) for f in df.filename])
    y = torch.tensor(df.class_id.values, dtype=torch.long)
    model = SmallCNN(OUTPUT_DIM["shape"])
    train(model, x, y, nn.CrossEntropyLoss(), args.epochs, device)
    torch.save({"state_dict": model.cpu().state_dict()}, WEIGHTS["shape"])

    print("force regression")
    root = args.data / "force_regression"
    df = pd.read_csv(root / "labels.csv")
    x = torch.stack([load_image(root / f) for f in df.filename])
    mean, std = df[AXES].mean().values, df[AXES].std().values
    y = torch.tensor((df[AXES].values - mean) / std, dtype=torch.float32)
    model = SmallCNN(OUTPUT_DIM["force"])
    train(model, x, y, nn.MSELoss(), args.epochs, device)
    torch.save(
        {"state_dict": model.cpu().state_dict(), "target_mean": mean.tolist(), "target_std": std.tolist()},
        WEIGHTS["force"],
    )
    print("saved", WEIGHTS["shape"].name, WEIGHTS["force"].name)


if __name__ == "__main__":
    main()
