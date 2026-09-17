#!/bin/bash

echo "Starting TURING..."

# Check Python
if ! command -v python3 &> /dev/null; then
    echo "Error: Python3 is not installed."
    exit 1
fi

# Check Ollama
if ! command -v ollama &> /dev/null; then
    echo "Error: Ollama is not installed."
    exit 1
fi

# Check Ollama service
if ! curl -s http://127.0.0.1:11434/api/tags > /dev/null; then
    echo "Starting Ollama..."
    ollama serve > /dev/null 2>&1 &
    sleep 2
fi

echo "Environment OK."
echo "Launching TURING..."

python3 main.py