#!/bin/bash
set -e
set -x

# run isort recursively
# isort -rc .

# Update pre-commit
pre-commit autoupdate
#run pre-commit
pre-commit run -a

# bash scripts/test.sh --cov-report=html ${@}
# python3 -m pytest
# python3 -m pytest -v -s # verbose
python3 -m pytest
sed -i "s/<source>\/home\/mike\/starlette-dashboard\/src<\/source>/<source>\/github\/workspace\/src<\/source>/g" /home/mike/starlette-dashboard/src/coverage.xml
# create coverage-badge
coverage-badge -o ../coverage.svg -f

# generate flake8 report
flake8 --tee . > flake8_report/report.txt

