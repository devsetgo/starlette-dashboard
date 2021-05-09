#!/bin/bash
set -e
set -x

# run dev
# uvicorn main:app --workers 2 --port 5000
gunicorn -c gunicorn_cfg.py main:app
