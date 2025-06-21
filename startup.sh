#!/bin/bash

cd "$(dirname "$0")"

echo "activating venv..."
source venv/bin/activate

echo "starting API..."
echo "starting application"
python3 main.py
