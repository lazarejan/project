#!/bin/bash

cd "$(dirname "$0")"

echo "activating venv..."
source venv/bin/activate

echo ============================================
echo "starting API..."
echo "starting application..."
echo ============================================
python3 main.py
