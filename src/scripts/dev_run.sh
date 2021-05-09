#!/bin/bash
set -e
set -x

# run dev
uvicorn main:app --port 5000 --reload --log-level debug
