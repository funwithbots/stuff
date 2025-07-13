#!/usr/bin/env python3
import os
import sys
import subprocess

EBOOK_CONVERT_PATH = os.getenv(
    "EBOOK_CONVERT_PATH", r"D:/bin/Calibre Portable/Calibre/ebook-convert.exe"
)


def convert_to_pdf(input_path: str) -> None:
    """
    Convert a single .epub or .mobi file to PDF using Calibre's ebook-convert.
    """
    # Make sure ebook-convert is available
    if not os.path.exists(EBOOK_CONVERT_PATH):
        print(
            "Error: 'ebook-convert' command not found. Please install Calibre.",
            file=sys.stderr,
        )
        sys.exit(1)

    base, ext = os.path.splitext(input_path)
    ext = ext.lower()
    if ext not in (".epub", ".mobi"):
        return

    output_path = f"{base}.pdf"
    if os.path.exists(output_path):
        print(f"{output_path} already exists. Skipping.")
        return
    print(f"Converting '{input_path}' → '{output_path}'…")
    try:
        subprocess.run([EBOOK_CONVERT_PATH, input_path, output_path], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Conversion failed for '{input_path}': {e}", file=sys.stderr)


def main(directory: str) -> None:
    if not os.path.isdir(directory):
        print(f"Error: '{directory}' is not a valid directory.", file=sys.stderr)
        sys.exit(1)

    for filename in os.listdir(directory):
        full_path = os.path.join(directory, filename)
        if os.path.isfile(full_path):
            convert_to_pdf(full_path)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <directory>", file=sys.stderr)
        sys.exit(1)
    main(sys.argv[1])
