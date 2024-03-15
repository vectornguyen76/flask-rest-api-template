from flask.views import MethodView
from flask_jwt_extended import jwt_required
from flask_principal import Permission, RoleNeed
from flask_smorest import Blueprint

from app.schemas.role_schema import RoleSchema, UpdateRolePermissionSchema
from app.services import role_service

# Define permissions
read_permission = Permission(RoleNeed("read"))
write_permission = Permission(RoleNeed("write"))
delete_permission = Permission(RoleNeed("delete"))

blp = Blueprint("Role", __name__, description="Role API")


@blp.route("/role")
class RoleList(MethodView):
    @jwt_required()
    @read_permission.require(http_exception=403)
    @blp.response(200, RoleSchema(many=True))
    def get(self):
        result = role_service.get_all_role()
        return result

    @jwt_required()
    @write_permission.require(http_exception=403)
    @blp.arguments(UpdateRolePermissionSchema)
    def post(self, qa_history_data):
        result = role_service.post_role(qa_history_data)
        return result


@blp.route("/role/<int:role_id>")
class Role(MethodView):
    @jwt_required()
    @read_permission.require(http_exception=403)
    @blp.response(200, RoleSchema)
    def get(self, role_id):
        result = role_service.get_role(role_id)
        return result

    @jwt_required()
    @write_permission.require(http_exception=403)
    @blp.arguments(UpdateRolePermissionSchema)
    def put(self, role_data, role_id):
        result = role_service.update_role(role_data, role_id)
        return result

    @jwt_required()
    @delete_permission.require(http_exception=403)
    def delete(self, role_id):
        result = role_service.delete_role(role_id)
        return result
