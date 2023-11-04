from flask.views import MethodView
from flask_jwt_extended import jwt_required
from flask_principal import Permission, RoleNeed
from flask_smorest import Blueprint

from app.schemas.user_schema import GetRolePermissionSchema
from app.services import role_permission_service

blp = Blueprint("Role And Permission", __name__, description="Role And Permission API")


@blp.route("/role-permission")
class GetRolePermission(MethodView):
    @jwt_required()
    @blp.response(200, GetRolePermissionSchema(many=True))
    def get(self):
        result = role_permission_service.get_role_permission()
        return result
