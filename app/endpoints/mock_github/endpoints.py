# -*- coding: utf-8 -*-
from resources import templates
from starlette.responses import JSONResponse
from loguru import logger


@logger.catch
async def authorize(request):
    redirect_url = request.query_params.get("redirect_url", "#")

    template = "mock_github/authorize.html"
    context = {"request": request, "redirect_url": redirect_url}
    return templates.TemplateResponse(template, context)


@logger.catch
async def access_token(request):
    response = {"access_token": "mock", "scope": "user:email", "token_type": "bearer"}
    return JSONResponse(response)


@logger.catch
async def user(request):
    return JSONResponse(
        {
            "login": "tomchristie",
            "id": 123,
            "name": "Tom Christie",
            "avatar_url": "https://avatars2.githubusercontent.com/u/647359?s=40&v=4",
        }
    )
    # {
    #     "login": "devsetgo",
    #     "id": 123,
    #     "name": "Mike Ryan",
    #     "avatar_url": "https://avatars3.githubusercontent.com/u/16019894?v=4",
    # }
    # )
