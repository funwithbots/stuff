# Ebook to PDF Converter

This script converts `.epub` and `.mobi` ebook files to PDF format using Calibre's `ebook-convert` tool.

## Requirements

1. **Calibre**: Ensure that Calibre is installed, and the `ebook-convert` executable is available. You can download Calibre from [https://calibre-ebook.com/](https://calibre-ebook.com/).
2. **Python**: This script requires Python 3.x.
3. **Environment Setup**:
   - Update the `EBOOK_CONVERT_PATH` variable in the script to point to the location of `ebook-convert.exe` on your system.

## How It Works

The script:
1. Checks if the `ebook-convert` tool is available.
2. Scans a specified directory for `.epub` and `.mobi` files.
3. Converts each file to a PDF using `ebook-convert`.
4. Skips files that have already been converted (i.e., if a corresponding `.pdf` file exists).

## Usage

1. Open a terminal or command prompt.
2. Run the script with the directory containing the ebook files as an argument:

   ```bash
   python convert.py <directory>