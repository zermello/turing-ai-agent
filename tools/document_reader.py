from pathlib import Path
import logging

#filelib
import json
import csv
import pymupdf
from docx import Document

# text file (.txt) reader
def txt_reader(file_path):
    path = Path(file_path)
    if path.exists():
        try:
            if path.is_file() and path.suffix.lower() == ".txt":
                content = path.read_text(encoding="utf-8")
                return content
            else:
                return "provide .txt file"
        except Exception as err:
            logging.error(f"ERROR: error occured due to {err}")
            return "error occured"
    if not path.exists():
        return "Path does not exist!"

# markdown file (.md) reader
def md_reader(file_path):
    path = Path(file_path)
    if path.exists():
        try:
            if path.is_file() and path.suffix.lower() == ".md":
                content = path.read_text(encoding="utf-8")
                return content
            else:
                return "provide .md file"
        except Exception as err:
                logging.error(f"ERROR: error occured due to {err}")
                return "error occured"
    if not path.exists():
        return "Path does not exist!"

# json file (.json) reader
def json_reader(file_path):
    path = Path(file_path)
    if path.exists():
        try:
            if path.is_file() and path.suffix.lower() == ".json":
                with open(path, "r", encoding="utf-8") as file:
                    content = json.load(file)
                    return content
            else:
                return "provide .json file"
        except Exception as err:
            logging.error(f"ERROR: error occured due to {err}")
            return "error occured"
    if not path.exists():
        return "Path doesn't exist"

# csv file (.csv) reader
def csv_reader(file_path):
    path = Path(file_path)
    if path.exists():
        try:
            if path.is_file() and path.suffix.lower() == ".csv":
                with path.open("r", encoding="utf-8") as file:
                    content = list(csv.DictReader(file))
                    return content
            else:
                return "PROVIDE .CSV FILE!"
        except Exception as err:
            logging.error(f"ERROR: {err}")
            return "Error occured"
    if not path.exists():
        return "PATH DOES NOT EXIST!"

# pdf file (.pdf) reader
def pdf_reader(file_path):
    path = Path(file_path)
    if path.exists():
        try:
            if path.is_file() and path.suffix.lower() == ".pdf":
                content = pymupdf.open(file_path)
                page_text = []
                for page in content:
                    text = page.get_text()
                    page_text.append(text)

                #CLOSE PDF DOCUMENT
                content.close()
                return page_text
            else:
                return "provide .pdf file!!"
        except Exception as err:
            logging.error(f"ERROR : {err}")
            return "Error occured"
    if not path.exists():
        return "PATH DOESN'T EXIST!!"
    
# docx file (.docx) reader
def docx_reader(file_path):
    path = Path(file_path)
    if path.exists():
        try:
            if path.is_file() and path.suffix.lower() == ".docx":
                content = Document(path)
                content = content.paragraphs
                content_text = []
                for paragraph in content:
                    text = paragraph.text
                    content_text.append(text)
                return content_text
            else:
                return "provide .docx file!!"
        except Exception as err:
            logging.error(f"ERROR : {err}")
            return "Error occured"
    if not path.exists():
        return "PATH DOESN'T EXIST!!"

DOCUMENT_READERS = {
    ".txt": txt_reader,
    ".md": md_reader,
    ".json": json_reader,
    ".csv": csv_reader,
    ".pdf": pdf_reader,
    ".docx": docx_reader,
}

def read_document(file_path):
    path = Path(file_path)

    reader = DOCUMENT_READERS.get(path.suffix.lower())

    if reader is None:
        return "Unsupported file type"

    return reader(file_path)