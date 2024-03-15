from flask.views import MethodView
from flask_jwt_extended import get_jwt, jwt_required
from flask_smorest import Blueprint

from app.schemas.user_schema import UpdateBlockUserSchema, UserSchema, UserUpdateSchema
from app.services import user_service
from app.utils.decorators import permission_required

blp = Blueprint("User", __name__, description="User API")


@blp.route("/user")
class UserList(MethodView):
    @jwt_required()
    @permission_required(permission_name="read")
    @blp.response(200, UserSchema(many=True))
    def get(self):
        result = user_service.get_all_user()
        return result


@blp.route("/user/<int:user_id>")
class User(MethodView):
    @jwt_required()
    @permission_required(permission_name="read")
    @blp.response(200, UserSchema)
    def get(self, user_id):
        result = user_service.get_user(user_id)
        return result

    @jwt_required()
    @permission_required(permission_name="write")
    @blp.arguments(UserUpdateSchema)
    def put(self, user_data, user_id):
        result = user_service.update_user(user_data, user_id)
        return result


@blp.route("/block-user/<int:user_id>")
class BlockUser(MethodView):
    @jwt_required()
    @permission_required(permission_name="delete")
    @blp.arguments(UpdateBlockUserSchema)
    def put(self, user_data, user_id):
        result = user_service.update_block_user(user_data, user_id)
        return result


@blp.route("/login")
class Login(MethodView):
    @blp.arguments(UserSchema)
    def post(self, user_data):
        result = user_service.login_user(user_data)
        return result


@blp.route("/register")
class Register(MethodView):
    @blp.arguments(UserSchema)
    def post(self, user_data):
        result = user_service.register_user(user_data)
        return result


@blp.route("/logout")
class Logout(MethodView):
    @jwt_required()
    def post(self):
        # Block access_token
        jti = get_jwt()["jti"]
        user_service.add_jti_blocklist(jti)

        return {"message": "Logout successfully!"}


@blp.route("/refresh")
class Refresh(MethodView):
    @jwt_required(refresh=True)
    def post(self):
        result = user_service.refresh_token()

        return result
