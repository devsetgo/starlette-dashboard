#!/bin/bash
set -e
set -x

# run of flake8 with report output
echo "flake8: start"
flake8 --tee . > flake8_report/report.txt
echo "flake8: report created"