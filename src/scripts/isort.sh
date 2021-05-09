#!/bin/bash
set -e
set -x

# run isort recursively
isort -rc .

#run pre-commit
pre-commit run -a
