#!/bin/bash
set -e

cd "$(dirname "$0")"

echo "setting up environment to run the program properly"
echo "1. virtual env in being created"
echo $( cat requirements.txt )
python3 -m venv venv
source venv/bin/activate

echo "Installing python dependencies... (requirements)"
pip install -r requirements.txt

echo "initializing database..."
python3 database.py

echo "generating data..."
python3 generator.py

echo "setup completed"
echo "to run the code use starup.sh"
