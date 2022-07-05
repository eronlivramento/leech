#!/bin/sh
echo ""
echo "Flake 8"
echo "======="
echo ""
python -m flake8 src/ && echo "src module success"
python -m flake8 tests/ && echo "tests module success"
echo ""