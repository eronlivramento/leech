#!/bin/sh
python src/cmd/leech.py
vim result_files/result.json
tail -f /dev/null