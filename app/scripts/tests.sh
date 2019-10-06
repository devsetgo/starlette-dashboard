#!/bin/bash
set -e
set -x

#run pre-commit
pre-commit run -a

# bash scripts/test.sh --cov-report=html ${@}
# python3 -m pytest
python3 -m pytest -v -s

# create coverage-badge
coverage-badge -o ../coverage.svg -f

# run of flake8 with report output
echo "flake8: start"
flake8 --tee . > flake8_report/flake8.txt
echo "flake8: report created"
