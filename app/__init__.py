from flask_smorest import Blueprint
from main.controllers.user_controller import blp as UserBlueprint

# Register Blueprint
api_blueprint = Blueprint('api', __name__, template_folder='templates', static_url_path='', static_folder='static')
api_blueprint.register_blueprint(UserBlueprint)