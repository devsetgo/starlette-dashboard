#!/bin/bash
set -e
set -x

# mkdocs
mkdocs build

# Copy Contribute to Github Contributing
cp ~/python-project-template/docs/index.md ~/python-project-template/README.md
cp ~/python-project-template/docs/contributing.md ~/python-project-template/CONTRIBUTING.md
cp ~/python-project-template/docs/changelog.md ~/python-project-template/CHANGELOG.md

mkdocs gh-deploy