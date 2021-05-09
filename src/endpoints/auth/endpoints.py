# -*- coding: utf-8 -*-
from app_functions.crud_ops import fetch_one_db, execute_one_db
from starlette.responses import RedirectResponse
from starlette.datastructures import URL
from loguru import logger
from app_functions.db_setup import users
import settings
import datetime


async def login(request):
    from main import GITHUB_AUTH_URL

    logger.info(f"loggin request")
    query = {
        "client_id": settings.GITHUB_CLIENT_ID,
        "redirect_url": request.url_for("auth:callback"),
    }
    url = URL(GITHUB_AUTH_URL).include_query_params(**query)
    return RedirectResponse(url, status_code=303)


async def logout(request):
    logger.info(f'logout request {request.session["username"]}')
    request.session.clear()
    url = request.url_for("dashboard")
    return RedirectResponse(url, status_code=303)


async def callback(request):
    from main import github_client, github_api_client

    # Obtain an access token.
    code = request.query_params.get("code", "")
    url = "/login/oauth/access_token"
    data = {
        "client_id": settings.GITHUB_CLIENT_ID,
        "client_secret": settings.GITHUB_CLIENT_SECRET,
        "code": code,
    }
    headers = {"accept": "application/json"}
    response = await github_client.post(url, data=data, headers=headers)
    logger.debug(response.request.url)
    response.raise_for_status()
    data = response.json()
    #  Make a request to the API.
    url = "/user"
    headers = {
        "authorization": f'token {data["access_token"]}',
    }
    response = await github_api_client.get(url, headers=headers)
    logger.debug(response.request.url)
    response.raise_for_status()
    data = response.json()

    # Log the user in, and redirect back to the homepage.
    query = users.select().where(users.c.github_id == data["id"])
    user = await fetch_one_db(query=query)
    if user is None:

        query = users.insert()
        values = {
            "created_at": datetime.datetime.now(),
            "last_login": datetime.datetime.now(),
            "username": data["login"],
            "github_id": data["id"],
            "is_admin": False,
            "name": data["name"],
            "avatar_url": data["avatar_url"],
        }
    else:
        query = users.update().where(users.c.github_id == data["id"])
        values = {
            "last_login": datetime.datetime.now(),
            "username": data["login"],
            "name": data["name"],
            "avatar_url": data["avatar_url"],
        }
    await execute_one_db(query=query, values=values)

    request.session["username"] = data["login"]
    request.session["realname"] = data["name"]
    request.session["avatar_url"] = data["avatar_url"]
    url = request.url_for("profile", username=data["login"])
    logger.info(f'logging {request.session["username"]} and send to profile page')
    return RedirectResponse(url, status_code=303)
