from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from piccolo.apps.user.tables import BaseUser
from piccolo.engine import engine_finder
from piccolo_admin.endpoints import create_admin
from piccolo_api.session_auth.middleware import SessionsAuthBackend
from piccolo_api.session_auth.tables import SessionsBase

from starlette.middleware.authentication import AuthenticationMiddleware
from starlette.routing import Mount


app = FastAPI(
    routes=[
        Mount(
            "/admin/",
            create_admin(
                tables=[BaseUser],
                site_name="Backend Admin",
                production=False),
        ),
    ],
)


# Don't allow all in production, only for testing purposes!
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


session_auth = (
    AuthenticationMiddleware(
        app,
        backend=SessionsAuthBackend(
            auth_table=BaseUser,
            session_table=SessionsBase,
            cookie_name="piccoloauth",
            admin_only=True,
            superuser_only=False,
            active_only=True,
        ),
    ),
)

# API Routers
# app.include_router(some_router)


@app.on_event("startup")
async def open_database_connection_pool():
    try:
        engine = engine_finder()
        await engine.start_connection_pool()
    except Exception:
        print("Unable to connect to the database")


@app.on_event("shutdown")
async def close_database_connection_pool():
    try:
        engine = engine_finder()
        await engine.close_connection_pool()
    except Exception:
        print("Unable to connect to the database")
