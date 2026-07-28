# PDF Processing Toolkit
A collection of Python scripts and utilities for automating common PDF processing tasks — built for internal workflows (document handling, reporting, and file management).

# Features
This repository includes the following tools:
| Script | Description |
|---|---|
| ```merge_pdf.py``` | Merge two PDF files by entering their file paths manually |
| ```merge_pdf_batch.py``` | Merge multiple PDF pairs in bulk, based on a list defined in an Excel file |
| ```merge_pdf_gui.py``` | GUI app (Tkinter) to merge multiple PDF files |
| ```duplicate_pdf.py``` | Duplicate a PDF file into multiple copies |
| ```pdf_2_text.py``` | Extract text content from a PDF into a ```.txt``` file |
| ```rename_pdf_by_title.pdf``` | Auto-rename PDF files in a folder based on a title extracted from their content (regex-based) |
| ```word_2_pdf_split.py``` | Convert Word (```.docx```) document to PDF, then split the result into one PDF file per page |
| ```split_pdf.py``` | Split a PDF into separate files, one per page |
| ```pdf_2_docx.py``` | Convert a PDF file into an editable Word (```.docx```) document |
| ```compress_pdf_ghostscript.py``` | Compress a PDF using Ghostscript (```gswin64c.exe```) for stringer file-size reduction |

# Requirements
- Python 3.10+
- Install dependencies:
  ```pip install -r requirements.txt```
- For ```compress_pdf_ghostscript.py```, Ghostscript must be installed separately, and the GS_PATH variable adjusted to match your local installation path.
- For ```word_to_pdf_split.py``` (docx2pdf), Microsoft Word must be installed (Windows/macOS only).

# Notes
- Some scripts reference personal/local file paths (e.g. ```C:\Users\...```) as examples — update these paths before running.
- ```rename_pdf_by_title.py``` uses a regex pattern tuned for a specific report format (competency recap / IPASN); adjust the pattern for other document formats.
- This is a personal automation toolkit; scripts may need adjustment depending on the target file structure or use case.
