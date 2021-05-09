# -*- coding: utf-8 -*-
"""Application configuration.
Most configuration is set via environment variables.
For local development, use a .env file to set
environment variables.
"""
import os
from starlette.config import Config
from loguru import logger
import secrets

# get environment variables
config = Config(".env")
USE_ENV = config("USE_ENV", default="docker")
# Access Token Settings
SECRET_KEY = secrets.token_urlsafe(64)

# Application information
if USE_ENV.lower() == "dotenv":
    logger.info(f"external configuration is for use with {USE_ENV.lower()}")
    # dotenv variables
    APP_VERSION = config("APP_VERSION", default="1.0.0")
    OWNER = config("OWNER", default="Mike Ryan")
    WEBSITE = config("WEBSITE", default="https://devsetgo.com")
    LICENSE_TYPE = config("LICENSE_TYPE", default="MIT")
    LICENSE_LINK = config(
        "LICENSE_LINK", default="https://github.com/devsetgo/starlette-SRTDashboard"
    )

    # Application Configurations
    HOST_DOMAIN = config("HOST_DOMAIN", default="https://devsetgo.com")
    SQLALCHEMY_DATABASE_URI = config(
        "SQLALCHEMY_DATABASE_URI", default="sqlite:///sqlite_db/starlette_ui.db"
    )

    # set release environment settings
    RELEASE_ENV = config("RELEASE_ENV", default="prd")

    # Safety check to prevent debug mode or mocking in production
    if RELEASE_ENV == "prd":
        DEBUG = False
        MOCK_GITHUB = False
    else:
        DEBUG = config("DEBUG", default=False)
        MOCK_GITHUB = config("MOCK_GITHUB", cast=bool, default=False)

    # Loguru settings
    LOGURU_RETENTION = config("LOGURU_RETENTION", default="10 days")
    LOGURU_ROTATION = config("LOGURU_ROTATION", default="10 MB")

    # GitHub API
    GITHUB_CLIENT_ID = config("GITHUB_CLIENT_ID", cast=str, default="no-id")
    GITHUB_CLIENT_SECRET = config("GITHUB_CLIENT_SECRET", cast=str, default="no-secret")

    # Github variables
    # if using docker env variables, you can pass them here and not include in .env file
    if GITHUB_CLIENT_ID == "no-id":
        logger.info(f"getting Github Client ID from Docker ENV variable")

    if GITHUB_CLIENT_SECRET == "no-secret":
        logger.info(f"getting Github Client Secret from Docker ENV variable")

else:
    logger.info(f"external configuration is for use with {USE_ENV.lower()}")
    # docker variables
    APP_VERSION = os.environ["APP_VERSION"]

    OWNER = os.environ["OWNER"]
    WEBSITE = os.environ["WEBSITE"]
    LICENSE_TYPE = os.environ["LICENSE_TYPE"]
    LICENSE_LINK = os.environ["LICENSE_LINK"]

    # Application Configurations
    HOST_DOMAIN = os.environ["HOST_DOMAIN"]
    SQLALCHEMY_DATABASE_URI = os.environ["SQLALCHEMY_DATABASE_URI"]

    # set release environment settings
    RELEASE_ENV = os.environ["RELEASE_ENV"]

    # Safety check to prevent debug mode or mocking in production
    if RELEASE_ENV == "prd":
        DEBUG = False
        MOCK_GITHUB = False
    else:
        DEBUG = os.environ["DEBUG"]
        MOCK_GITHUB = os.environ["MOCK_GITHUB"]

    # Loguru settings
    LOGURU_RETENTION = os.environ["LOGURU_RETENTION"]
    LOGURU_ROTATION = os.environ["LOGURU_ROTATION"]

    # GitHub API
    GITHUB_CLIENT_ID = os.environ["GITHUB_CLIENT_ID"]
    GITHUB_CLIENT_SECRET = os.environ["GITHUB_CLIENT_SECRET"]

    # Github variables
    # if using docker env variables, you can pass them here and not include in .env file
    # if GITHUB_CLIENT_ID == "no-id":
    #     logger.info(f"getting Github Client ID from Docker ENV variable")

    # if GITHUB_CLIENT_SECRET == "no-secret":
    #     logger.info(f"getting Github Client Secret from Docker ENV variable")
    #     GITHUB_CLIENT_SECRET = os.getenv("GITHUB_CLIENT_SECRET", "not-provded")
    #     if GITHUB_CLIENT_ID == "not-provded":
    #         logger.error(f"Github Client ID was not found")
