# -*- coding: utf-8 -*-
"""Application configuration.
Most configuration is set via environment variables.
For local development, use a .env file to set
environment variables.
"""
import os
from starlette.config import Config
from loguru import logger

# get environment variables
config = Config(".env")

# Application information

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


DEBUG = config("DEBUG", default=False)
RELEASE_ENV = config("RELEASE_ENV", default="prd")
if RELEASE_ENV != "prd":
    DEBUG = False

# Loguru settings
LOGURU_RETENTION = config("LOGURU_RETENTION", default="10 days")
LOGURU_ROTATION = config("LOGURU_ROTATION", default="10 MB")

# Access Token Settings
SECRET_KEY = config("SECRET_KEY", default="secret-key-1234567890")

# GitHub API
GITHUB_CLIENT_ID = config("GITHUB_CLIENT_ID", cast=str, default="no-id")
GITHUB_CLIENT_SECRET = config("GITHUB_CLIENT_SECRET", cast=str, default="no-secret")

# Github variables
# if using docker env variables, you can pass them here and not include in .env file
if GITHUB_CLIENT_ID == "no-id":
    logger.info(f"getting Github Client ID from Docker ENV variable")
    GITHUB_CLIENT_ID = os.getenv("GITHUB_CLIENT_ID", "not-provded")
    if GITHUB_CLIENT_ID == "not-provded":
        logger.error(f"Github Client ID was not found")

if GITHUB_CLIENT_SECRET == "no-secret":
    logger.info(f"getting Github Client Secret from Docker ENV variable")
    GITHUB_CLIENT_SECRET = os.getenv("GITHUB_CLIENT_SECRET", "not-provded")
    if GITHUB_CLIENT_ID == "not-provded":
        logger.error(f"Github Client ID was not found")

MOCK_GITHUB = config("MOCK_GITHUB", cast=bool, default=False)
