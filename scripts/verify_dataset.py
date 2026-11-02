#!/usr/bin/env python3
"""Check the released coursework data without training a model or making splits.

Usage:
    python scripts/verify_dataset.py
    python scripts/verify_dataset.py --data /path/to/Tactile_DL_2027
    python scripts/verify_dataset.py --archive Tactile_DL_2027.zip

Requires Pillow (``python -m pip install Pillow``); all other imports are standard library.
"""

import argparse
import csv
import hashlib
import math
from collections import Counter, defaultdict
from pathlib import Path, PurePosixPath

from PIL import Image


CLASSES = {
    "cylinder": 0, "dots": 1, "hexagon": 2, "line": 3, "moon": 4,
    "rectangle": 5, "ring": 6, "small_sphere": 7, "triangle": 8, "wave": 9,
}
SCHEMAS = {
    "shape_classification/classes.csv": ["class_name", "class_id"],
    "shape_classification/labels.csv": ["filename", "class_name", "class_id"],
    "force_regression/labels.csv": ["filename", "contact_id", "is_shear", "fx", "fy", "fz"],
}


def sha256(path):
    """Read in small chunks so an archive does not have to fit in memory."""
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--data", type=Path, default=Path("Tactile_DL_2027"))
    parser.add_argument("--archive", type=Path, help="Optional archive whose SHA-256 is reported")
    parser.add_argument("--expected-sha256", help="Also require --archive to match this SHA-256")
    args = parser.parse_args()
    if args.expected_sha256 and not args.archive:
        parser.error("--expected-sha256 requires --archive")
    if args.expected_sha256 and (len(args.expected_sha256) != 64 or
                               any(c not in "0123456789abcdefABCDEF" for c in args.expected_sha256)):
        parser.error("--expected-sha256 must contain 64 hexadecimal characters")

    root = args.data.resolve()
    errors = []
    tables = {}
    for relative, columns in SCHEMAS.items():
        try:
            with (root / relative).open(newline="", encoding="utf-8-sig") as stream:
                reader = csv.DictReader(stream)
                if reader.fieldnames != columns:
                    errors.append(f"{relative}: expected columns {columns}, got {reader.fieldnames}")
                rows = list(reader)
                if any(None in row or any(value is None for value in row.values()) for row in rows):
                    errors.append(f"{relative}: row has missing or extra fields")
                tables[relative] = rows
        except (OSError, UnicodeError, csv.Error) as exc:
            errors.append(f"{relative}: {exc}")

    # Stop early if CSVs cannot be interpreted: subsequent checks depend on their schemas.
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1

    classes = tables["shape_classification/classes.csv"]
    expected_classes = {(name, str(identifier)) for name, identifier in CLASSES.items()}
    if len(classes) != 10 or {(r["class_name"], r["class_id"]) for r in classes} != expected_classes:
        errors.append("classes.csv does not contain the expected ten unique class mappings")

    shape = tables["shape_classification/labels.csv"]
    force = tables["force_regression/labels.csv"]
    if Counter(r["class_name"] for r in shape) != Counter({name: 200 for name in CLASSES}):
        errors.append("Shape data must contain exactly 200 rows for each of the ten classes")
    for index, row in enumerate(shape, start=2):
        if row["class_id"] != str(CLASSES.get(row["class_name"])):
            errors.append(f"Shape labels, row {index}: class name and ID disagree")
        if PurePosixPath(row["filename"]).parent.name != row["class_name"]:
            errors.append(f"Shape labels, row {index}: image folder and class name disagree")

    contacts = defaultdict(list)
    for index, row in enumerate(force, start=2):
        try:
            contact = int(row["contact_id"])
            shear = int(row["is_shear"])
            if shear not in (0, 1):
                raise ValueError("is_shear must be 0 or 1")
            if not all(math.isfinite(float(row[axis])) for axis in ("fx", "fy", "fz")):
                raise ValueError("force values must be finite numbers")
            expected = f"images/contact_{contact:04d}{'_shear' if shear else ''}.jpg"
            if row["filename"] != expected:
                raise ValueError("filename does not match contact_id and is_shear")
            contacts[contact].append(shear)
        except (ValueError, TypeError) as exc:
            errors.append(f"Force labels, row {index}: {exc}")
    if len(force) != 2000:
        errors.append(f"Expected 2,000 force rows; found {len(force):,}")
    if set(contacts) != set(range(1, 1001)) or any(sorted(v) != [0, 1] for v in contacts.values()):
        errors.append("Force contacts 1–1,000 must each have exactly one press and one shear image")

    image_count = 0
    image_hashes = {}
    for task, rows in (("shape_classification", shape), ("force_regression", force)):
        task_root = root / task
        names = [row["filename"] for row in rows]
        if len(names) != len(set(names)):
            errors.append(f"{task}: duplicate filename entries in labels.csv")
        present = {p.relative_to(task_root).as_posix() for p in (task_root / "images").rglob("*")
                   if p.is_file()}
        if set(names) != present:
            errors.append(f"{task}: {len(set(names) - present)} missing labelled files and "
                          f"{len(present - set(names))} unlabelled files")
        for name in sorted(set(names)):
            relative = PurePosixPath(name)
            path = task_root / relative
            if relative.is_absolute() or ".." in relative.parts or "\\" in name or \
                    not path.resolve().is_relative_to(task_root.resolve()):
                errors.append(f"{task}: unsafe image path {name!r}")
                continue
            try:
                with Image.open(path) as image:
                    image.load()  # Fully decode each file; checking its header alone is insufficient.
                    if image.format != "JPEG" or image.mode != "RGB" or image.size != (320, 240):
                        raise ValueError(f"expected RGB JPEG 320×240; got {image.format}, "
                                         f"{image.mode}, {image.size}")
                digest = sha256(path)
                if digest in image_hashes:
                    errors.append(f"Exact duplicate images: {image_hashes[digest]} and {task}/{name}")
                image_hashes[digest] = f"{task}/{name}"
                image_count += 1
            except (OSError, ValueError) as exc:
                errors.append(f"{task}/{name}: {exc}")

    archive_digest = None
    if args.archive:
        try:
            archive_digest = sha256(args.archive)
            if args.expected_sha256 and archive_digest != args.expected_sha256.lower():
                errors.append("Archive SHA-256 does not match --expected-sha256")
        except OSError as exc:
            errors.append(f"Archive: {exc}")

    if errors:
        for error in errors[:30]:
            print(f"ERROR: {error}")
        if len(errors) > 30:
            print(f"... and {len(errors) - 30} further errors")
        print(f"FAILED: {len(errors)} issue(s) found.")
        return 1

    print("PASS: Coursework dataset validation completed.")
    print(f"  {image_count:,} RGB JPEG images, all 320×240 pixels and fully decoded.")
    print("  Shape: 2,000 images; ten classes; 200 images per class; mapping verified.")
    print("  Force: 2,000 images; 1,000 complete press/shear pairs; all force values finite.")
    print("  Every CSV path exists; no unlabelled files, duplicate names or duplicate image bytes.")
    if archive_digest:
        print(f"  Archive SHA-256: {archive_digest}")
        if args.expected_sha256:
            print("  Archive checksum matches the expected value.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
