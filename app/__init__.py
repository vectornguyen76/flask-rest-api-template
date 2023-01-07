from flask_smorest import Blueprint
from main.controllers.user_controller import blp as UserBlueprint
from main.controllers.index_controller import blp as IndexBlueprint

# Register Blueprint
api_blueprint = Blueprint('API', __name__, template_folder='templates', static_url_path='', static_folder='static')
api_blueprint.register_blueprint(UserBlueprint)
api_blueprint.register_blueprint(IndexBlueprint)