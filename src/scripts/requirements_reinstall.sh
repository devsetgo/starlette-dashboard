#!/bin/bash
set -e
set -x

# remove current libraries
pip3 uninstall -r requirements/dev.txt -y

# upgrade pip and setuptools
pip3 install --upgrade pip setuptools

# install requirements
pip3 install -r requirements/dev.txt