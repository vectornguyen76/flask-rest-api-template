from flask.views import MethodView
from flask_jwt_extended import jwt_required
from flask_principal import Permission, RoleNeed
from flask_smorest import Blueprint

from app.schemas.user_schema import PermissionSchema, UpdatePermissionRoleSchema
from app.services import permission_service, role_permission_service

# Define permissions
read_permission = Permission(RoleNeed("read"))
write_permission = Permission(RoleNeed("write"))

blp = Blueprint("Permission", __name__, description="Permission API")


@blp.route("/permission")
class PermissionList(MethodView):
    @jwt_required()
    @read_permission.require(http_exception=403)
    @blp.response(200, PermissionSchema(many=True))
    def get(self):
        result = permission_service.get_all_permission()
        return result

    @jwt_required()
    @write_permission.require(http_exception=403)
    @blp.arguments(PermissionSchema)
    def post(self, qa_history_data):
        result = permission_service.post_permission(qa_history_data)
        return result


@blp.route("/permission/<int:permission_id>")
class Permission(MethodView):
    @jwt_required()
    @read_permission.require(http_exception=403)
    @blp.response(200, PermissionSchema)
    def get(self, permission_id):
        result = permission_service.get_permission(permission_id)
        return result

    @jwt_required()
    @write_permission.require(http_exception=403)
    @blp.arguments(PermissionSchema)
    def put(self, permission_data, permission_id):
        result = permission_service.update_permission(permission_data, permission_id)
        return result


@blp.route("/permission-role-update")
class PermissionRole(MethodView):
    @jwt_required()
    @write_permission.require(http_exception=403)
    @blp.arguments(UpdatePermissionRoleSchema)
    def put(self, permission_data):
        result = role_permission_service.update_roles_to_permission(permission_data)
        return result
