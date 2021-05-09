#!/bin/bash
set -e
set -x

# Pip freeze current install libraries
pip3 freeze > remove_requirements.txt
# remove pkg-resources from filepython
sed -i '/pkg-resources==0.0.0/d' remove_requirements.txt
# uninstall libraries
pip3 uninstall -r remove_requirements.txt -y
# upgrade pip and setuptools
pip3 install --upgrade pip setuptools
# install requirements
pip3 install -r requirements/dev.txt

# remove file
rm -r remove_requirements.txt