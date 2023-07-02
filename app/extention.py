from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from flask_cors import CORS

migrate = Migrate()
jwt = JWTManager()
cors = CORS()
