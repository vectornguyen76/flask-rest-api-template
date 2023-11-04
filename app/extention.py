from flask_cors import CORS
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate
from flask_principal import Principal

migrate = Migrate()
jwt = JWTManager()
cors = CORS()
principal = Principal()
