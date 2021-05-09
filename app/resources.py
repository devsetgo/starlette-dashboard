# -*- coding: utf-8 -*-
from app_functions.db_setup import create_db
from com_lib.logging_config import config_logging
from loguru import logger
from app_functions import db_setup
from starlette.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates

# templates and static files
templates = Jinja2Templates(directory="templates")
statics = StaticFiles(directory="statics")


def init_app():

    config_logging()
    logger.info(f"Initiating application")
    create_db()
    logger.info(f"Initiating database")


async def startup():
    logger.info(f"starting up services")
    await db_setup.connect_db()

    return


async def shutdown():
    logger.info(f"shutting down services")
    await db_setup.disconnect_db()
    return
