from flask.views import MethodView
from flask_jwt_extended import jwt_required
from flask_smorest import Blueprint

from app.schemas.role_permission_schema import RoleSchema
from app.schemas.user_schema import UserAndRoleSchema
from app.services import user_role_service
from app.utils.decorators import permission_required

blp = Blueprint("User And Role", __name__, description="User And Role API")


@blp.route("/user/<int:user_id>/role/<int:role_id>")
class LinkRolesToUser(MethodView):
    @jwt_required()
    @permission_required(permission_name="write")
    @blp.response(201, RoleSchema)
    def post(self, user_id, role_id):
        result = user_role_service.link_roles_to_user(user_id, role_id)
        return result

    @jwt_required()
    @permission_required(permission_name="delete")
    @blp.response(200, UserAndRoleSchema)
    def delete(self, user_id, role_id):
        result = user_role_service.delete_roles_to_user(user_id, role_id)
        return result
