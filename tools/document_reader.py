from pathlib import Path
import json

def txt_reader(file_path):
    path = Path(file_path)
    if path.exists():
        try:
            if path.suffix.lower() == ".txt":
                content = path.read_text(encoding="utf-8")
                return content
            else:
                return "provide .txt file"
        except Exception:
            return "error occured"
    if not path.exists():
        return "Path does not exist!"

txt_reader("../documents/notes.txt")

def md_reader(file_path):
    path = Path(file_path)
    if path.exists():
        try:
            if path.suffix.lower() == ".md":
                content = path.read_text(encoding="utf-8")
                return content
            else:
                return "provide .md file"
        except Exception:
                return "error occured"
    if not path.exists():
        return "Path does not exist!"

md_reader("../documents/robotics.md")

