from config import settings
from piccolo.conf.apps import AppRegistry
from piccolo.engine.postgres import PostgresEngine


DB = PostgresEngine(config={
    'database': settings.postgres_db,
    'user': settings.postgres_user,
    'password': settings.postgres_user,
    'host': settings.postgres_host,
    'port': settings.postgres_port,
})


# A list of paths to piccolo apps
# e.g. ['blog.piccolo_app']
APP_REGISTRY = AppRegistry(apps=['piccolo_admin.piccolo_app', 'api.library.piccolo_app'])
