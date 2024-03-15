from flask_smorest import Api

from app.routers.permission_router import blp as PermissionBlueprint
from app.routers.role_permission_router import blp as RolePermissionBlueprint
from app.routers.role_router import blp as RoleBlueprint
from app.routers.user_role_router import blp as UserRoleBlueprint
from app.routers.user_router import blp as UserBlueprint


# Register Blueprint
def register_routing(app):
    api = Api(app)
    api.register_blueprint(UserBlueprint)
    api.register_blueprint(RoleBlueprint)
    api.register_blueprint(PermissionBlueprint)
    api.register_blueprint(UserRoleBlueprint)
    api.register_blueprint(RolePermissionBlueprint)
