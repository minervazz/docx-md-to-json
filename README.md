# docx/md to json parsing

## Intro 
This is a tool for converting docx/md files to json, while keeping the original scheme, such as different layers of heading and main body text.

Usage mainly lies in parsing docx/md files so they can be turned into database vectors that keeps the document structure information, and so be further used in RAG applications. 

### Structure
```
root/
├─ files/
│  ├─ doctest.docx
│  └─ mdtest.md
├─ output/
│  ├─ docx.json
│  └─ md.json
├─ src/
│  ├─ docx2json.py
│  └─ md2json.py
├─ README.md
└─ requirements.txt
```

The `files` directory contains the source `.docx` and `.md` files. The `output` directory contains the converted `.json` output files. The `src` directory contains the source code for format conversion.

## Install
This project runs in a virtual conda environment of python == 3.11, with a pip version <= 24.0 (recommended 24.0).

You can use  `requirements.txt` to install required packages after the appropriate environment has been set.

## Usage
### docx to json
The source `.docx` file is located at `files/docxtest.docx`. Run `/src/docx2json.py` to perform the conversion, and the result will be stored as `/output/docx.json`.

### md to json
The source `.md` file is located at `files/mdtest.md`. Run `/src/md2json.py` to perform the conversion, and the result will be stored as `/output/md.json`.