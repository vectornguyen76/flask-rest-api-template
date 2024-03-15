from flask.views import MethodView
from flask_jwt_extended import jwt_required
from flask_smorest import Blueprint

from app.schemas.permission_schema import UpdatePermissionRoleSchema
from app.schemas.role_permission_schema import PermissionSchema
from app.services import permission_service, role_permission_service
from app.utils.decorators import permission_required

blp = Blueprint("Permission", __name__, description="Permission API")


@blp.route("/permission")
class PermissionList(MethodView):
    @jwt_required()
    @permission_required(permission_name="read")
    @blp.response(200, PermissionSchema(many=True))
    def get(self):
        result = permission_service.get_all_permission()
        return result

    @jwt_required()
    @permission_required(permission_name="write")
    @blp.arguments(PermissionSchema)
    def post(self, qa_history_data):
        result = permission_service.post_permission(qa_history_data)
        return result


@blp.route("/permission/<int:permission_id>")
class Permission(MethodView):
    @jwt_required()
    @permission_required(permission_name="read")
    @blp.response(200, PermissionSchema)
    def get(self, permission_id):
        result = permission_service.get_permission(permission_id)
        return result

    @jwt_required()
    @permission_required(permission_name="write")
    @blp.arguments(PermissionSchema)
    def put(self, permission_data, permission_id):
        result = permission_service.update_permission(permission_data, permission_id)
        return result


@blp.route("/permission-role-update")
class PermissionRole(MethodView):
    @jwt_required()
    @permission_required(permission_name="write")
    @blp.arguments(UpdatePermissionRoleSchema)
    def put(self, permission_data):
        result = role_permission_service.update_roles_to_permission(permission_data)
        return result
