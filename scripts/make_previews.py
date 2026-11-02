"""Make the README figures from actual released images, without changing the data.

Run from the repository root after downloading the dataset:
    python scripts/make_previews.py --data Tactile_DL_2027
"""
from __future__ import annotations

import argparse
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd
from PIL import Image


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--data", type=Path, default=Path("Tactile_DL_2027"))
    parser.add_argument("--out", type=Path, default=Path("docs/assets"))
    args = parser.parse_args()
    args.out.mkdir(parents=True, exist_ok=True)
    blue = "#003e74"
    plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 11})

    shape_root = args.data / "shape_classification"
    shape = pd.read_csv(shape_root / "labels.csv")
    samples = shape.sort_values(["class_id", "filename"]).groupby("class_id").head(1)
    fig, axes = plt.subplots(2, 5, figsize=(16, 7.25), facecolor="white")
    fig.suptitle("TACTILE SHAPE CLASSIFICATION", fontsize=21, color=blue, fontweight="bold", y=0.98)
    fig.text(0.5, 0.92, "One released GelSight image per class · 200 images per class · RGB 320 × 240", ha="center", color="#505b65", fontsize=12)
    for ax, row in zip(axes.flat, samples.itertuples()):
        with Image.open(shape_root / row.filename) as image:
            ax.imshow(image)
        ax.set_title(f"{row.class_id}  |  {row.class_name}", color=blue, fontsize=12, fontweight="bold", pad=9)
        ax.set_xlabel(Path(row.filename).name, color="#56616d", fontsize=9)
        ax.set_xticks([])
        ax.set_yticks([])
        for spine in ax.spines.values():
            spine.set_visible(False)
    fig.subplots_adjust(left=0.02, right=0.98, top=0.85, bottom=0.065, hspace=0.40, wspace=0.10)
    fig.savefig(args.out / "shape_examples.jpg", dpi=120, facecolor="white", pil_kwargs={"quality": 90})
    plt.close(fig)

    force_root = args.data / "force_regression"
    force = pd.read_csv(force_root / "labels.csv")
    pair = force.loc[force.contact_id.eq(1)].sort_values("is_shear")
    fig, axes = plt.subplots(1, 2, figsize=(11, 5.7), facecolor="white")
    fig.suptitle("ONE CONTACT, TWO OBSERVATIONS", fontsize=21, color=blue, fontweight="bold", y=0.98)
    fig.text(0.5, 0.905, "Contact 0001 · Keep both observations in the same data split", ha="center", color="#505b65", fontsize=12)
    for ax, row in zip(axes, pair.itertuples()):
        with Image.open(force_root / row.filename) as image:
            ax.imshow(image)
        label = "Normal press · is_shear = 0" if row.is_shear == 0 else "After lateral displacement · is_shear = 1"
        ax.set_title(label, color=blue, fontsize=12, fontweight="bold", pad=10)
        ax.set_xlabel(f"fx = {row.fx:+.3f} N    fy = {row.fy:+.3f} N    fz = {row.fz:+.3f} N\n{Path(row.filename).name}", color="#33424f", fontsize=11, labelpad=10)
        ax.set_xticks([])
        ax.set_yticks([])
        for spine in ax.spines.values():
            spine.set_visible(False)
    fig.subplots_adjust(left=0.04, right=0.96, top=0.81, bottom=0.17, wspace=0.08)
    fig.savefig(args.out / "force_pair.jpg", dpi=120, facecolor="white", pil_kwargs={"quality": 90})
    plt.close(fig)
    print(f"Wrote shape_examples.jpg and force_pair.jpg to {args.out}")


if __name__ == "__main__":
    main()
