import tools.document_reader as dr


def test_txt_reader():
    content = dr.txt_reader("documents/notes.txt")
    assert content == "This is my robotics study plan..."


def test_txt_reader_empty():
    content = dr.txt_reader("documents/empty.txt")
    assert content == ""


def test_txt_reader_missing():
    content = dr.txt_reader("documents/missing.txt")
    assert content == "Path does not exist!"


def test_md_reader():
    content = dr.md_reader("documents/notes.md")
    assert content == '# Robotics\n\n## Languages\n- Python\n- C++\n\n## Goals\nBuild autonomous robots.'


def test_md_reader_missing():
    content = dr.md_reader("documents/missing.md")
    assert content == "Path does not exist!"


def test_json_reader():
    content = dr.json_reader("documents/notes.json")
    assert content == {'name': 'TURING', 'tools': ['calculator', 'weather', 'memory'], 'version': 1}


def test_json_reader_missing():
    content = dr.json_reader("documents/missing.json")
    assert content == "Path doesn't exist"


def test_csv_reader():
    content = dr.csv_reader("documents/notes.csv")

    assert content == [{'name': 'TURING',
                        'type': 'AI Agent',
                        'language': 'Python',
                        'status': 'Active'},
                        {'name': 'RoboArm',
                        'type': 'Manipulator',
                        'language': 'C++',
                        'status': 'Development'},
                        {'name': 'VisionBot',
                        'type': 'Computer Vision',
                        'language': 'Python',
                        'status': 'Testing'},
                        {'name': 'Atlas',
                        'type': 'Humanoid',
                        'language': 'C++',
                        'status': 'Research'},
                        {'name': 'DroneX',
                        'type': 'Autonomous Drone',
                        'language': 'Python',
                        'status': 'Prototype'}]


def test_csv_reader_missing():
    content = dr.csv_reader("documents/missing.csv")
    assert content == "PATH DOES NOT EXIST!"


def test_pdf_reader():
    content = dr.pdf_reader("documents/notes.pdf")

    assert isinstance(content, list)
    assert any("robotics" in page.lower() for page in content)


def test_pdf_reader_missing():
    content = dr.pdf_reader("documents/missing.pdf")
    assert content == "PATH DOESN'T EXIST!!"


def test_docx_reader():
    content = dr.docx_reader("documents/notes.docx")

    assert isinstance(content, list)
    assert any("robotics" in paragraph.lower() for paragraph in content)


def test_docx_reader_missing():
    content = dr.docx_reader("documents/missing.docx")
    assert content == "PATH DOESN'T EXIST!!"