#!/bin/bash
set -e
set -x

# run dev
autoflake --in-place --remove-all-unused-imports -r .
