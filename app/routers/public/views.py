# -*- coding: utf-8 -*-
from starlette.applications import Starlette
from starlette.responses import (
    FileResponse,
    HTMLResponse,
    JSONResponse,
    PlainTextResponse,
    RedirectResponse,
    StreamingResponse,
)
from starlette.routing import Mount, Route, Router

from .private_routes import app as private_routes
from .public_routes import app as public_routes

public_routes = Starlette()

public_routes.mount("/{user_id:int}", app=private_routes)
public_routes.mount("/", app=public_routes)
