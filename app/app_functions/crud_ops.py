# -*- coding: utf-8 -*-
"""
database simple functions. Pass query and where needed values and get result back
"""

from app_functions.db_setup import database


async def fetch_one_db(query):

    result = await database.fetch_one(query)
    return result


async def fetch_all_db(query):

    result = await database.fetch_all(query)
    return result


async def execute_one_db(query, values: dict):

    result = await database.execute(query, values)
    return result


async def execute_many_db(query, values: dict):

    result = await database.execute_many(query, values)
    return result
