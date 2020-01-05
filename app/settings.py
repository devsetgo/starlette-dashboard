# -*- coding: utf-8 -*-
"""Application configuration.
Most configuration is set via environment variables.
For local development, use a .env file to set
environment variables.
"""

from starlette.config import Config

# get environment variables
config = Config(".env")

# Application information
DEBUG = config("DEBUG", default=False)
APP_VERSION = config("APP_VERSION", default="1.0.0")
OWNER = config("OWNER", default="Mike Ryan")
WEBSITE = config("WEBSITE", default="https://devsetgo.com")
LICENSE_TYPE = config("LICENSE_TYPE", default="MIT")
LICENSE_LINK = config(
    "LICENSE_LINK", default="https://github.com/devsetgo/starlette-SRTDashboard"
)

# Demo Data
CREATE_SAMPLE_DATA = config("CREATE_SAMPLE_DATA", default=False)
NUMBER_CONFIG = config("NUMBER_CONFIG", default=10)
NUMBER_USERS = config("NUMBER_USER", default=10)

# Application Configurations
HOST_DOMAIN = config("HOST_DOMAIN", default="https://devsetgo.com")
RELEASE_ENV = config("RELEASE_ENV", default="prd")
SQLALCHEMY_DATABASE_URI = config(
    "SQLALCHEMY_DATABASE_URI", default="sqlite:///sqlite_db/api.db"
)

# Loguru settings
LOGURU_RETENTION = config("LOGURU_RETENTION", default="10 days")
LOGURU_ROTATION = config("LOGURU_ROTATION", default="10 MB")

# Access Token Settings
SECRET_KEY = config("SECRET_KEY", default="secret-key-1234567890")
ALGORITHM = config("ALGORITHM", default="HS256")
ACCESS_TOKEN_EXPIRE_MINUTES = config("ACCESS_TOKEN_EXPIRE_MINUTES", default=10080)

# GitHub API
GITHUB_CLIENT_ID = config("GITHUB_CLIENT_ID", cast=str, default="")
GITHUB_CLIENT_SECRET = config("GITHUB_CLIENT_SECRET", cast=str, default="")
MOCK_GITHUB = config("MOCK_GITHUB", cast=bool, default=False)
