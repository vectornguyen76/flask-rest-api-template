from datetime import timedelta
import secrets

DEFAULT_ROLE = 3

class Config(object):
    SECRET_KEY = 'my-key'
    CORS_HEADERS = 'Content-Type'
    # SQLALCHEMY_DATABASE_URI = 'sqlite:///database/database.db'
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:070600@localhost/test_db'
    SQLALCHEMY_TRACK_MODIFICATION = False
    JWT_SECRET_KEY = str(secrets.SystemRandom().getrandbits(128))
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(minutes=5) 
    JWT_REFRESH_TOKEN_EXPIRES = timedelta(days=1)
    PROPAGATE_EXCEPTIONS = True,
    API_TITLE = "Template REST API"
    API_VERSION = "v1"
    OPENAPI_VERSION = "3.0.3"
    OPENAPI_URL_PREFIX = "/"
    OPENAPI_SWAGGER_UI_PATH = "/swagger-ui"
    OPENAPI_SWAGGER_UI_URL = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"
