import os
from memory import save_memory, get_memory
import logging

os.makedirs("data", exist_ok=True)

def memory_tool(content):
    try:
        save_memory(content)
        return "Memory saved successfully."
    except Exception as err:
        logging.error(f"ERROR: {err}")
        return "Cannot be saved to memory, connection error"

def get_memory_tool():
    try:
        memory = get_memory()
        return memory
    except Exception as err:
        logging.error(f"ERROR: {err}")
        return "Cannot fetch memory, connection error"

