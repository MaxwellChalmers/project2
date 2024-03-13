#!/bin/bash

# Exit immediately if any command fails
set -e

echo "Running isort --check"
poetry run isort --check *.py

echo "Running black"
poetry run black --line-length 80  *.py

echo "Running flake8"
poetry run flake8 *.py

echo ""
echo "Everything is looking good!"