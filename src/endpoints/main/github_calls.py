# -*- coding: utf-8 -*-
import httpx
import settings
from loguru import logger


github_api = httpx.AsyncClient(base_url="https://api.github.com")


async def get_repo_list(user_name: str) -> dict:
    url = f"/users/{user_name}/repos?client_id={settings.GITHUB_CLIENT_ID}\
        &client_secret={settings.GITHUB_CLIENT_SECRET}&archived=false&per_page=100"
    response = await github_api.get(url)
    # response.raise_for_status()
    logger.info(f"fetching repo list for {user_name}")
    results = response.json()
    return results


async def get_repo_info(user_name: str) -> dict:
    # /repos/octocat/Hello-World
    url = f"/users/{user_name}/repos?client_id={settings.GITHUB_CLIENT_ID}\
        &client_secret={settings.GITHUB_CLIENT_SECRET}"
    response = await github_api.get(url)
    # response.raise_for_status()
    results: dict = response.json()
    logger.info(f"fetching repos for {user_name}")
    return results


async def get_user_info(user_name: str) -> dict:
    url = f"/users/{user_name}"
    response = await github_api.get(url)
    logger.info(f"fetching information for {user_name}")
    results: dict = response.json()
    return results


async def get_user_events(user_name: str) -> dict:
    url = f"/users/{user_name}/events/public?per_page=100"
    response = await github_api.get(url)
    logger.info(f"fetching information for {user_name}")
    results = response.json()
    return results
