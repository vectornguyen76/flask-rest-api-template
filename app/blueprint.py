from flask_smorest import Api
from controllers.user_controller import blp as UserBlueprint
from controllers.role_controller import blp as RoleBlueprint
from controllers.permission_controller import blp as PermissionBlueprint
from controllers.user_role_controller import blp as UserRoleBlueprint
from controllers.role_permission_controller import blp as RolePermissionBlueprint

# Register Blueprint
def register_routing(app):
    api = Api(app)
    api.register_blueprint(UserBlueprint)
    api.register_blueprint(RoleBlueprint)
    api.register_blueprint(PermissionBlueprint)
    api.register_blueprint(UserRoleBlueprint)
    api.register_blueprint(RolePermissionBlueprint)