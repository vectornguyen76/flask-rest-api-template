import datetime
import os
import secrets

basedir = os.path.abspath(os.path.dirname(__file__))

class DefaultConfig:
    """
    Default Configuration
    """
    # Configuracion Flask
    APP_NAME = os.environ.get('APP_NAME')
    SECRET_KEY = secrets.token_urlsafe(64)
    PROPAGATE_EXCEPTIONS = True
    DEBUG = False
    TESTING = False

    # Configuracion de Flask-JWT-Extend
    JWT_SECRET_KEY = secrets.token_urlsafe(64)
    # Determina los minutos que permanece activo el access token
    JWT_ACCESS_TOKEN_EXPIRES = datetime.timedelta(minutes=30)
    # Determina los dias que permanece activo el refresh token
    JWT_REFRESH_TOKEN_EXPIRES = datetime.timedelta(days=30)
    # Algoritmo usado para generar el token
    JWT_ALGORITHM = 'HS256'
    # Algoritmo usado para decodificar el token
    JWT_DECODE_ALGORITHMS = 'HS256'
    # Header que debe contener el JWT en una request
    JWT_HEADER_NAME = "Authorization"
    # Palabra que va delante del token en la cabecera Authorization en este caso vacia
    JWT_HEADER_TYPE = 'Bearer'
    # Dónde buscar un JWT al procesar una solicitud.
    JWT_TOKEN_LOCATION = 'headers'
    
    API_TITLE = "Template REST API"
    API_VERSION = "v1"
    OPENAPI_VERSION = "3.0.3"
    OPENAPI_URL_PREFIX = "/"
    OPENAPI_SWAGGER_UI_PATH = "/swagger-ui"
    OPENAPI_SWAGGER_UI_URL = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"

    # Configuracion de BBDD
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SHOW_SQLALCHEMY_LOG_MESSAGES = False

    # Entornos App
    APP_ENV_LOCAL = 'local'
    APP_ENV_TESTING = 'testing'
    APP_ENV_DEVELOP = 'develop'
    APP_ENV_PRODUCTION = 'production'
    APP_ENV = ''

    # Logging
    FTM = '[%(asctime)s.%(msecs)d]\t %(levelname)s \t[%(name)s.%(funcName)s:%(lineno)d]\t %(message)s'
    DATE_FMT = '%d/%m/%Y %H:%M:%S'
    LOG_FILE_API = f'{basedir}/logs/api.log'


class DevelopConfig(DefaultConfig):
    # Entorno App
    APP_ENV = DefaultConfig.APP_ENV_DEVELOP

    # Activa el modo debug
    DEBUG = True

    # Configuracion de BBDD
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')


class TestingConfig(DefaultConfig):
    # Entorno App
    APP_ENV = DefaultConfig.APP_ENV_TESTING

    # Flask deshabilita la captura de errores durante el manejo de peticiones para obtener mejores
    # informes de error en los tests
    TESTING = True
    # Activa el modo debug
    DEBUG = True  # Antes era False
    # False para deshabilitar la protección CSRF durante los tests
    WTF_CSRF_ENABLED = False

    # Logging
    LOG_FILE_API = f'{basedir}/logs/api_tests.log'

    # Configuracion de BBDD
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_TEST_URL')


class LocalConfig(DefaultConfig):
    # Entorno App
    APP_ENV = DefaultConfig.APP_ENV_LOCAL

    # Activa el modo debug
    DEBUG = False

    # Configuracion de BBDD
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')


class ProductionConfig(DefaultConfig):
    # Entorno App
    APP_ENV = DefaultConfig.APP_ENV_PRODUCTION

    # Activa el modo debug
    DEBUG = False

    # Configuracion de BBDD
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')

    # SQLAlchemy 1.4.x has removed support for the postgres:// URI scheme, which is used by Heroku Postgres.
    # To maintain compatibility, perform the following before setting up connections with SQLAlchemy:
    if SQLALCHEMY_DATABASE_URI.startswith("postgres://"):
        SQLALCHEMY_DATABASE_URI = SQLALCHEMY_DATABASE_URI.replace("postgres://", "postgresql://", 1)
