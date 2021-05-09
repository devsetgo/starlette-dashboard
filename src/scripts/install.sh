#!/bin/bash
set -e
set -x

# upgrade pip and setuptools
pip3 install --upgrade pip setuptools
# install requirements
pip3 install -r requirements/dev.txt