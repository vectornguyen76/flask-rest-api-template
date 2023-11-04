from flask_smorest import Api

from app.controllers.permission_controller import blp as PermissionBlueprint
from app.controllers.role_controller import blp as RoleBlueprint
from app.controllers.role_permission_controller import blp as RolePermissionBlueprint
from app.controllers.user_controller import blp as UserBlueprint
from app.controllers.user_role_controller import blp as UserRoleBlueprint


# Register Blueprint
def register_routing(app):
    api = Api(app)
    api.register_blueprint(UserBlueprint)
    api.register_blueprint(RoleBlueprint)
    api.register_blueprint(PermissionBlueprint)
    api.register_blueprint(UserRoleBlueprint)
    api.register_blueprint(RolePermissionBlueprint)
