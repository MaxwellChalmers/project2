#!/bin/bash

# Exit immediately if any command fails
set -e

echo "Running isort --check"
poetry run isort --check .

echo "Running black"
poetry run black --line-length 80 .

echo "Running flake8"
poetry run flake8 .

echo ""
echo "Everything is looking good!"
