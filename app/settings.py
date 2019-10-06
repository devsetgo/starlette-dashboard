# -*- coding: utf-8 -*-
"""Application configuration.
Most configuration is set via environment variables.
For local development, use a .env file to set
environment variables.
"""
import os

from starlette.config import Config

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
RELEASE_ENV = config("RELEASE_ENV", default="prd")
SQLALCHEMY_DATABASE_URI = config(
    "SQLALCHEMY_DATABASE_URI", default="sqlite:///sqlite_db/starlette_ui.db"
)

# Loguru settings
LOGURU_RETENTION = config("LOGURU_RETENTION", default="10 days")
LOGURU_ROTATION = config("LOGURU_ROTATION", default="10 MB")

# Access Token Settings
SECRET_KEY = config("SECRET_KEY", default="secret-key")
ALGORITHM = config("ALGORITHM", default="HS256")
ACCESS_TOKEN_EXPIRE_MINUTES = config("ACCESS_TOKEN_EXPIRE_MINUTES", default=10080)
