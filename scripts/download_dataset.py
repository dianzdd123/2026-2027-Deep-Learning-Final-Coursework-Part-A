"""Download the pinned coursework dataset, check its SHA-256, and extract it.

Examples (run from the repository root):
    python scripts/download_dataset.py
    python scripts/download_dataset.py --output-dir /content
    python scripts/download_dataset.py --archive /path/to/Tactile_DL_2027.zip

Only Python's standard library is required. Existing dataset folders are never
overwritten: choose a fresh --output-dir if you want a second copy.
"""

from __future__ import annotations

import argparse
import hashlib
import shutil
import stat
import tempfile
import urllib.request
import zipfile
from pathlib import Path, PurePosixPath


DATASET_NAME = "Tactile_DL_2027"
ARCHIVE_NAME = f"{DATASET_NAME}.zip"
RELEASE_URL = (
    "https://github.com/dianzdd123/"
    "2026-2027-Deep-Learning-Final-Coursework-Part-A/"
    "releases/download/v1.0.2/Tactile_DL_2027.zip"
)
EXPECTED_BYTES = 37_441_246
EXPECTED_SHA256 = "1a1620e4695b220043318e7b209202940b930fcf82f69b4f761213255c6b4ca5"
CHUNK_BYTES = 1024 * 1024


def check_archive(path: Path) -> None:
    """Check the complete file before trusting or extracting its contents."""
    if not path.is_file():
        raise ValueError(f"Archive not found: {path}")
    if path.stat().st_size != EXPECTED_BYTES:
        raise ValueError(f"Wrong archive size: expected {EXPECTED_BYTES:,} bytes.")

    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(CHUNK_BYTES), b""):
            digest.update(chunk)
    if digest.hexdigest() != EXPECTED_SHA256:
        raise ValueError("SHA-256 mismatch. Download a fresh copy of the archive from release v1.0.2.")
    print(f"SHA-256 verified: {EXPECTED_SHA256}")


def download_archive(destination: Path) -> None:
    """Stream the download to a temporary file; retain it only after verification."""
    print(f"Downloading {ARCHIVE_NAME} ({EXPECTED_BYTES / 1_000_000:.2f} MB)...")
    request = urllib.request.Request(RELEASE_URL, headers={"User-Agent": "coursework-dataset-downloader"})
    temporary_path = None
    try:
        with tempfile.NamedTemporaryFile(dir=destination.parent, suffix=".part", delete=False) as output:
            temporary_path = Path(output.name)
            with urllib.request.urlopen(request, timeout=120) as response:
                shutil.copyfileobj(response, output, length=CHUNK_BYTES)
        check_archive(temporary_path)
        temporary_path.replace(destination)
    finally:
        if temporary_path is not None:
            temporary_path.unlink(missing_ok=True)


def extract_archive(archive: Path, output_dir: Path) -> Path:
    """Extract through a temporary directory after rejecting unsafe member paths."""
    target = output_dir / DATASET_NAME
    if target.exists():
        raise ValueError(f"Dataset folder already exists: {target}. Choose a new --output-dir.")

    with zipfile.ZipFile(archive) as source:
        for member in source.infolist():
            path = PurePosixPath(member.filename)
            if (
                path.is_absolute()
                or ".." in path.parts
                or "\\" in member.filename
                or not path.parts
                or path.parts[0] != DATASET_NAME
                or stat.S_ISLNK(member.external_attr >> 16)
            ):
                raise ValueError(f"Unexpected archive member: {member.filename}")

        # A partial extraction is discarded if the operation fails.
        with tempfile.TemporaryDirectory(dir=output_dir, prefix="tactile-extract-") as temporary:
            source.extractall(temporary)
            (Path(temporary) / DATASET_NAME).rename(target)
    return target


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--archive", type=Path, help="Use an existing ZIP instead of downloading.")
    parser.add_argument("--output-dir", type=Path, default=Path.cwd(), help="Parent directory for the dataset.")
    args = parser.parse_args()

    try:
        output_dir = args.output_dir.expanduser().resolve()
        output_dir.mkdir(parents=True, exist_ok=True)
        if (output_dir / DATASET_NAME).exists():
            raise ValueError(
                f"Dataset folder already exists: {output_dir / DATASET_NAME}. "
                "Run scripts/verify_dataset.py --data <that folder>, or choose a new --output-dir."
            )

        archive = args.archive.expanduser().resolve() if args.archive else output_dir / ARCHIVE_NAME
        if args.archive is not None or archive.exists():
            check_archive(archive)
        else:
            download_archive(archive)
        target = extract_archive(archive, output_dir)
    except (OSError, ValueError, zipfile.BadZipFile) as error:
        parser.exit(1, f"Dataset setup failed: {error}\n")

    print(f"Dataset ready: {target}")
    print("Contents: 2,000 shape images and 2,000 force images, labels and submission examples.")
    print(f'Next: python scripts/verify_dataset.py --data "{target}"')


if __name__ == "__main__":
    main()
