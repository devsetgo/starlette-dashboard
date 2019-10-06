# -*- coding: utf-8 -*-
# from sqlalchemy.orm import scoped_session, sessionmaker
from datetime import datetime, timedelta

import databases
from loguru import logger
from sqlalchemy import (
    Boolean,
    Column,
    Date,
    DateTime,
    Float,
    ForeignKey,
    Integer,
    MetaData,
    String,
    Table,
    create_engine,
)
from sqlalchemy.pool import QueuePool
from starlette.config import Config

from settings import (
    APP_VERSION,
    HOST_DOMAIN,
    LICENSE_LINK,
    LICENSE_TYPE,
    OWNER,
    RELEASE_ENV,
    SQLALCHEMY_DATABASE_URI,
    WEBSITE,
)

engine = create_engine(
    SQLALCHEMY_DATABASE_URI, poolclass=QueuePool, max_overflow=10, pool_size=100
)
metadata = MetaData()
database = databases.Database(SQLALCHEMY_DATABASE_URI)


def create_db():
    metadata.create_all(engine)
    logger.info("Create: {info}", info="Creating tables")


async def connect_db():
    await database.connect()
    logger.info("Create: {info}", info="connecting to database")


async def disconnect_db():
    await database.disconnect()
    logger.info("Create: {info}", info="disconnecting database")


users = Table(
    "users",
    metadata,
    # Column('Id', Integer, primary_key=True),
    Column("userId", String(length=100), primary_key=True),
    Column("firstName", String(length=150)),
    Column("lastName", String(length=150)),
    Column("title", String(length=200)),
    Column("company", String(length=200)),
    Column("address", String(length=300)),
    Column("city", String(length=200)),
    Column("country", String(length=200)),
    Column("postal", String(length=50)),
    Column("email", String(length=200)),
    Column("website", String(length=500)),
    Column("password", String(length=50)),
    Column("description", String(length=2000)),
    Column("dateCreate", DateTime()),
    Column("dateUpdated", DateTime()),
    Column("isActive", Boolean(), default=True),
    Column("isSuperuser", Boolean(), default=True),
)
