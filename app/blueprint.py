from flask_smorest import Api
from controllers.user_controller import blp as UserBlueprint

# Register Blueprint
def register_routing(app):
    api = Api(app)
    api.register_blueprint(UserBlueprint)