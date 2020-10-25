# -*- coding: utf-8 -*-
"""
Configuration of Gunicorn to serve application utilizing Uvicorn
gunicorn config reference: https://github.com/benoitc/gunicorn/blob/master/examples/example_config.py
"""

import multiprocessing

# ip and port to bind
bind = "0.0.0.0:5000"
# max number of pending connections
# backlog = 2048
# define number of workers by cores times two plus one
workers = multiprocessing.cpu_count() * 2 + 1
# set worker class to uvicorn
worker_class = "uvicorn.workers.UvicornWorker"
# loglevel - The granularity of log output
# A string of "debug", "info", "warning", "error", "critical"
loglevel = "info"

"""
A dictionary containing headers and values that the front-end proxy uses to indicate HTTPS requests.
These tell Gunicorn to set wsgi.url_scheme to https, so your application can tell that the request is secure.
"""
secure_scheme_headers = {
    "X-FORWARDED-PROTOCOL": "ssl",
    "X-FORWARDED-PROTO": "https",
    "X-FORWARDED-SSL": "on",
}
# ips that are allowed to forward
FORWARDED_ALLOW_IPS = "127.0.0.1", "0.0.0.0"
