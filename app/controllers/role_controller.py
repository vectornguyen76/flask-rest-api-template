from app.services import role_service
from flask.views import MethodView
from flask_smorest import Blueprint
from flask_principal import Permission, RoleNeed
from flask_jwt_extended import jwt_required
from app.schemas.user_schema import RoleSchema, UpdateRolePermissionSchema

blp = Blueprint("Role", __name__, description="Role API")

@blp.route("/role")
class RoleList(MethodView):  
    @jwt_required()
    @blp.response(200, RoleSchema(many=True))
    def get(self):
        result = role_service.get_all_role()
        return result
    
    @jwt_required()
    @blp.arguments(UpdateRolePermissionSchema)
    def post(self, qa_history_data):
        result = role_service.post_role(qa_history_data)
        return result
    
@blp.route("/role/<int:role_id>")
class Role(MethodView):   
    @jwt_required()
    @blp.response(200, RoleSchema)
    def get(self, role_id):
        result = role_service.get_role(role_id)
        return result
    
    @jwt_required()
    @blp.arguments(UpdateRolePermissionSchema)
    def put(self, role_data, role_id):
        result = role_service.update_role(role_data, role_id)
        return result
    
    @jwt_required()
    def delete(self, role_id):
        result = role_service.delete_role(role_id)
        return result