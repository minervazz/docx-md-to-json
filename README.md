# docx/md to json parsing

## Intro 
This is a tool for converting docx/md files to a structured json file, which is structured to show different layers of heading, main body text, and tables.

Usage mainly lies in parsing docx/md files so they can be turned into structured files, and so be further processed in RAG retrieval. 

### Structure
```
root/
├─ files/
│  ├─ [your input file].docx
│  └─ [your input file].md
├─ output/
│  ├─ [your input file-docx].txt
│  ├─ [your input file-docx].json
│  └─ [your input file-md].json
├─ src/
│  ├─ docx2txt.py
│  ├─ docx2json.py
│  └─ md2json.py
├─ README.md
├─ LICENSE
└─ requirements.txt
```

The `src` directory contains the source code for format conversion.

## Usage
This project runs in a virtual conda environment of python == 3.11, with a pip version <= 24.0 (recommended 24.0).

You can use  `requirements.txt` to install required packages after the appropriate environment has been set.

### docx to json
Change line 78 of `/src/docx2json.py` to `input_docx_path = "../files/[your input file].docx"` and run the file to perform the conversion, and the result will be stored as `output/[your input file-docx].json`.

### md to json
Change line 56 of `/src/md2json.py` to `input_docx_path = "../files/[your input file].md"` and run the file to perform the conversion, and the result will be stored as `output/[your input file-md].json`.

## Examples
Check the files already inside the files and output directory to see the parsing result. Headings with be separated from main body text, and tables and main body text will be placed under its corresponding heading level.