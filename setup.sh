#!/bin/bash

set -e

echo "=============================="
echo "       TURING SETUP"
echo "=============================="

echo ""
echo "[1/5] Checking Python..."

if ! command -v python3 &> /dev/null
then
    echo "Python 3 is not installed."
    exit 1
fi

python3 --version

echo ""
echo "[2/5] Creating virtual environment..."

if [ ! -d ".venv" ]; then
    python3 -m venv .venv
    echo "Virtual environment created."
else
    echo "Virtual environment already exists."
fi

echo ""
echo "[3/5] Installing Python dependencies..."

source .venv/bin/activate

python -m pip install --upgrade pip
python -m pip install -r requirements.txt

echo ""
echo "[4/5] Checking Ollama..."

if ! command -v ollama &> /dev/null
then
    echo "WARNING: Ollama is not installed."
    echo "Install Ollama separately, then run setup again."
else
    echo "Ollama detected."

    echo ""
    echo "Checking Qwen model..."

    if ! ollama list | grep -q "qwen2.5:1.5b"
    then
        ollama pull qwen2.5:1.5b
    else
        echo "qwen2.5:1.5b already installed."
    fi

    echo ""
    echo "Checking embedding model..."

    if ! ollama list | grep -q "nomic-embed-text"
    then
        ollama pull nomic-embed-text
    else
        echo "nomic-embed-text already installed."
    fi
fi

echo ""
echo "[5/5] Setup complete."

echo ""
echo "Start TURING with:"
echo "./shell.sh"

echo ""