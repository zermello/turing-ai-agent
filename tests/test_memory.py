import tools.memory_tool as mry

def test_memory_tool():
    result = mry.memory_tool("remember i am lerning python")
    assert result == "Memory saved successfully."

def test_get_memory_tool():
    mry.memory_tool("test_memory_123")
    result = mry.get_memory_tool()
    assert "test_memory_123" in result

def test_memory_tool_empty():
    result = mry.memory_tool("")
    assert result == "Memory saved successfully."
