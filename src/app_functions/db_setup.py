# -*- coding: utf-8 -*-

import databases
from loguru import logger
import sqlalchemy

from settings import SQLALCHEMY_DATABASE_URI

engine = sqlalchemy.create_engine(
    SQLALCHEMY_DATABASE_URI,
    poolclass=sqlalchemy.pool.QueuePool,
    max_overflow=10,
    pool_size=100,
)
metadata = sqlalchemy.MetaData()
database = databases.Database(SQLALCHEMY_DATABASE_URI)


def create_db():
    metadata.create_all(engine)
    logger.info(f"Creating tables")


async def connect_db():
    await database.connect()
    logger.info(f"connecting to database")


async def disconnect_db():
    await database.disconnect()
    logger.info(f"disconnecting from database")


users = sqlalchemy.Table(
    "users",
    metadata,
    sqlalchemy.Column("pk", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("created_at", sqlalchemy.DateTime, index=True),
    sqlalchemy.Column("last_login", sqlalchemy.DateTime, index=True),
    sqlalchemy.Column("github_id", sqlalchemy.Integer, index=True),
    sqlalchemy.Column("username", sqlalchemy.String, index=True),
    sqlalchemy.Column("is_admin", sqlalchemy.Boolean, index=True),
    sqlalchemy.Column("name", sqlalchemy.String),
    sqlalchemy.Column("avatar_url", sqlalchemy.String),
)
