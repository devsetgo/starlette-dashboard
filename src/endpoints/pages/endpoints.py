# -*- coding: utf-8 -*-
from loguru import logger
from starlette.applications import Starlette
from starlette.exceptions import HTTPException
from starlette.staticfiles import StaticFiles
from resources import templates

app = Starlette()
app.mount("/static", StaticFiles(directory="statics"), name="static")

detail = "page note found"


async def example_pages(request):
    try:
        html_page = request.path_params["page"]
        print(html_page)
        template = f"/pages/{html_page}.html"
        context = {"request": request}
        logger.info(f"page accessed: {template}")
        return templates.TemplateResponse(template, context)
    except Exception as e:
        logger.critical(
            f"Error: Page accessed: /{html_page} , but HTML page {e} does not exist"
        )
        raise HTTPException(404, detail=detail)


async def example_pages_charts(request):
    html_page = request.path_params["page"]
    try:

        template = f"/pages/charts/{html_page}.html"
        context = {"request": request}
        logger.info(f"page accessed: {template}")
        return templates.TemplateResponse(template, context)
    except Exception as e:
        logger.critical(
            f"Error: Page accessed: /{html_page} , but HTML page {e} does not exist"
        )
        raise HTTPException(404, detail=detail)


async def example_pages_forms(request):
    html_page = request.path_params["page"]
    logger.info(f"page requested: {html_page}")
    try:

        template = f"/pages/forms/{html_page}.html"
        context = {"request": request}
        logger.info(f"page accessed: {template}")
        return templates.TemplateResponse(template, context)
    except Exception as e:
        logger.critical(
            f"Error: Page accessed: /{html_page} , but HTML page {e} does not exist"
        )
        raise HTTPException(404, detail=detail)


async def example_pages_examples(request):
    html_page = request.path_params["page"]
    logger.info(f"page requested: {html_page}")
    try:

        template = f"/pages/examples/{html_page}.html"
        context = {"request": request}
        logger.info(f"page accessed: {template}")
        return templates.TemplateResponse(template, context)
    except Exception as e:
        logger.critical(
            f"Error: Page accessed: /{html_page} , but HTML page {e} does not exist"
        )
        raise HTTPException(404, detail=detail)


async def example_pages_mailbox(request):
    html_page = request.path_params["page"]
    logger.info(f"page requested: {html_page}")
    try:

        template = f"/pages/mailbox/{html_page}.html"
        context = {"request": request}
        logger.info(f"page accessed: {template}")
        return templates.TemplateResponse(template, context)
    except Exception as e:
        logger.critical(
            f"Error: Page accessed: /{html_page} , but HTML page {e} does not exist"
        )
        raise HTTPException(404, detail=detail)


async def example_pages_tables(request):
    html_page = request.path_params["page"]
    logger.info(f"page requested: {html_page}")
    try:

        template = f"/pages/tables/{html_page}.html"
        context = {"request": request}
        logger.info(f"page accessed: {template}")
        return templates.TemplateResponse(template, context)
    except Exception as e:
        logger.critical(
            f"Error: Page accessed: /{html_page} , but HTML page {e} does not exist"
        )
        raise HTTPException(404, detail=detail)


async def example_pages_ui(request):
    html_page = request.path_params["page"]
    logger.info(f"page requested: {html_page}")
    try:

        template = f"/pages/UI/{html_page}.html"
        context = {"request": request}
        logger.info(f"page accessed: {template}")
        return templates.TemplateResponse(template, context)
    except Exception as e:
        logger.critical(
            f"Error: Page accessed: /{html_page} , but HTML page {e} does not exist"
        )
        raise HTTPException(404, detail=detail)
