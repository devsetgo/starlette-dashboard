#!/bin/bash
set -e
set -x

# clear pycache files
find . | grep -E "(__pycache__|\.pyc|\.pyo$)" | xargs rm -rf