# -*- coding: utf-8 -*-
# import json
# import os
# from pathlib import Path

import requests
import uvicorn
from loguru import logger

# from requests.exceptions import Timeout
from starlette.applications import Starlette
from starlette.config import Config
from starlette.exceptions import HTTPException

# from starlette.middleware.cors import CORSMiddleware
# from starlette.middleware.httpsredirect import HTTPSRedirectMiddleware
# from starlette.middleware.trustedhost import TrustedHostMiddleware
# from starlette.responses import HTMLResponse, JSONResponse
from starlette.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates

from com_lib.file_functions import open_json
from com_lib.logging_config import config_logging
from db_setup import create_db

config = Config(".env")
logger.info("Logging initiated")

app_env = config("RELEASE_ENV", default="prd")

debug_mode = False

if app_env == "dev":
    debug_mode = True

# initialize logging
config_logging()
# create database
create_db()
logger.info("Databasee initiated")

templates = Jinja2Templates(directory="templates")

app = Starlette(debug=debug_mode)
logger.info("Application initiated")

app.mount("/static", StaticFiles(directory="statics"), name="static")


@app.on_event("startup")
def startup():

    logger.info("Applicaton started")
    logger.info(f"Debug Mode set to {debug_mode}")


@app.on_event("shutdown")
async def shutdown():
    logger.info("Applicaton shutdown")


@app.route("/")
@app.route("/index")
async def homepage(request):
    try:
        logger.info(f"page accessed: /")
        template = "index.html"
        context = {"request": request}
        return templates.TemplateResponse(template, context)
    except HTTPException as e:
        logger.critical(e)


@app.route("/login")
async def login(request):
    try:
        # html_page = request.path_params["page"]
        logger.info(f"page accessed: login")

        context = {"request": request}

        template = f"login.html"
        return templates.TemplateResponse(template, context)
    except HTTPException as e:
        logger.critical(e)


@app.route("/example/report-task")
async def report_task(request):
    try:
        obj = open_json("task.json")
        logger.info(f"page accessed: login")

        context = {"request": request, "obj": obj}

        template = f"/example/report_task.html"
        return templates.TemplateResponse(template, context)
    except HTTPException as e:
        logger.critical(e)


@app.route("/example/{page}")
async def example_pages(request):
    try:
        html_page = request.path_params["page"]
        logger.info(f"page accessed: /example/{html_page}")

        if html_page == "datatable":
            obj = call_api()
            context = {"request": request, "obj": obj}
        else:
            context = {"request": request}

        template = f"/example/{html_page}.html"

        return templates.TemplateResponse(template, context)
    except HTTPException as e:
        logger.critical(e)


def call_api():
    """ call test-api to fetch fake users.  """
    # TODO: Consider changing to encode/httpx when stable https://github.com/encode/httpx

    try:
        r = requests.get("https://test-api.devsetgo.com/api/v1/users/list", timeout=2)
        logger.info(f"API Call Status Code: {r.status_code}")
        obj = r.json()
        logger.info(f"serving test-api response")
        return obj
    except Exception as e:
        logger.error(f"error: API was non-responsive: {e}")
        obj = open_json("sample.json")
        logger.info(f"serving sample.json due to API non-response")
        return obj


@app.route("/error")
async def error(request):
    """
    An example error. Switch the `debug` setting to see either tracebacks or 500 pages.
    """
    raise RuntimeError("Oh no")


@app.exception_handler(403)
async def not_found(request, exc):
    print(request, exc)
    """
    Return an HTTP 403 page.
    """
    template = "/error/403.html"
    context = {"request": request}
    return templates.TemplateResponse(template, context, status_code=403)


@app.exception_handler(404)
async def not_found(request, exc):
    print(request, exc)
    """
    Return an HTTP 404 page.
    """
    template = "/error/404.html"
    context = {"request": request}
    return templates.TemplateResponse(template, context, status_code=404)


@app.exception_handler(500)
async def server_error(request, exc):
    print(request, exc)
    """
    Return an HTTP 500 page.
    """
    template = "/error/500.html"
    context = {"request": request}
    return templates.TemplateResponse(template, context, status_code=500)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5000, log_level="info")
