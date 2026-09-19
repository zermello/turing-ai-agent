import tools.registry as reg

def test_reg_cal():
    result = reg.tools["calculate"]["function"]("8+8")
    assert result == 16

def test_reg_wtr():
    result = reg.tools["weather"]["function"]("tokyo")
    assert result 

def test_reg_time():
    result = reg.tools["time"]["function"]("tokyo")
    assert result 

def test_reg_memory():
    result = reg.tools["memory"]["function"]("remember i am learning ai")
    assert result == "Memory saved successfully."

def test_reg_web_search():
    result = reg.tools["web_search"]["function"]("who is brad pitt?")
    assert result 

def test_read_document():
    result = reg.tools["read_document"]["function"]("documents/notes.pdf")
    assert result
