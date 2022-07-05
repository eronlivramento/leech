#!/bin/sh
echo ""
echo "Code Style"
echo "=========="
echo ""
python -m black --check -t py38 --exclude="build/|buck-out/|dist/|_build/|pip/|\.pip/|\.git/|\.hg/|\.mypy_cache/|\.tox/|\.venv/" . && echo "\n\nSuccess" || (echo "\n\nFailure\n\nRun \"make black\" to apply style formatting to your code"; return 2)
echo ""