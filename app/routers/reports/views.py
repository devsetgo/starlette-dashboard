# -*- coding: utf-8 -*-
import json
import os
from pathlib import Path

import requests
import uvicorn
from loguru import logger
from requests.exceptions import Timeout
from starlette.applications import Starlette
from starlette.config import Config
from starlette.exceptions import HTTPException
from starlette.middleware.cors import CORSMiddleware
from starlette.middleware.httpsredirect import HTTPSRedirectMiddleware
from starlette.middleware.trustedhost import TrustedHostMiddleware
from starlette.responses import HTMLResponse, JSONResponse
from starlette.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates

from com_lib.file_functions import open_json


@app.route("/example/report-task")
async def report_task(request):
    try:
        # html_page = request.path_params["page"]
        logger.info(f"page accessed: login")

        context = {"request": request}

        template = f"/example/report_task.html"
        return templates.TemplateResponse(template, context)
    except HTTPException as e:
        logger.critical(e)
