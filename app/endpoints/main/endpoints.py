# -*- coding: utf-8 -*-
from loguru import logger
from starlette.exceptions import HTTPException
from resources import templates
from app_functions.db_setup import users, database
from endpoints.main import github_calls


async def homepage(request):

    template = "index.html"
    context = {"request": request}
    logger.info(f"page accessed: /")
    return templates.TemplateResponse(template, context)


async def homepage_page(request):
    try:
        html_page = request.path_params["page"]
        template = f"{html_page}.html"
        context = {"request": request}
        logger.info(f"page accessed: {template}")
        return templates.TemplateResponse(template, context)

    except Exception as e:
        logger.critical(
            f"Error: Page accessed: /{html_page} , but HTML page {e} does not exist"
        )
        raise HTTPException(404, detail="page note found")


async def profile(request):

    if "username" not in request.session:
        logger.error(
            f"user page access without being logged in from {request.client.host}"
        )
        raise HTTPException(status_code=403)

    username = request.path_params["username"]
    # can_edit = check_can_edit(request, username)

    query = users.select().where(users.c.username == username)
    profile_user = await database.fetch_one(query)
    if profile_user is None:
        raise HTTPException(status_code=403)

    repo_data = await github_calls.get_repo_list(username)
    user_data = await github_calls.get_user_info(username)
    user_events = await github_calls.get_user_events(username)
    status_code = 200
    template = "profile.html"
    context = {
        "request": request,
        "owner": username,
        "profile_user": profile_user,
        "repo_data": repo_data,
        "user_data": user_data,
        "user_events": user_events,
    }
    return templates.TemplateResponse(template, context, status_code=status_code)
