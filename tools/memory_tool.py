import os
from memory import save_memory, get_memory

os.makedirs("data", exist_ok=True)

def memory_tool(content):
    save_memory(content)
    return "Memory saved successfully."

memory_tool("working in tools?")

