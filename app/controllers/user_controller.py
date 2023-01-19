from services import user_service
from flask_jwt_extended import jwt_required, get_jwt, get_jwt_identity, create_access_token
from flask.views import MethodView
from flask_smorest import Blueprint, abort

from schemas.user_schema import UserSchema, UserUpdateSchema

blp = Blueprint("User", __name__, description="User API")

@blp.route("/user")
class UserList(MethodView):  
    @jwt_required()
    @blp.response(200, UserSchema(many=True))
    def get(self):
        result = user_service.get_all_user()
        return result

@blp.route("/user/<int:user_id>")
class User(MethodView):   
    @jwt_required()
    @blp.response(200, UserSchema)
    def get(self, user_id):
        result = user_service.get_user(user_id)
        return result
    
    @jwt_required()
    @blp.arguments(UserUpdateSchema)
    def put(self, user_data, user_id):
        result = user_service.update_user(user_data, user_id)
        return result
        
    @jwt_required()
    def delete(self, user_id):
        # Only admin can delete user
        jwt = get_jwt()
        if not jwt.get("is_admin"):
            abort(401, message="Admin privilege requierd.")
        
        result = user_service.delete_user(user_id)
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
        jti = get_jwt()['jti']
        user_service.add_jti_blocklist(jti)
        
        return {"message": "Logout successfully!"}
    
@blp.route("/refresh")
class Refresh(MethodView):   
    @jwt_required(refresh=True)
    def post(self):
        # Get id current user
        current_user = get_jwt_identity()
        
        # Create new access token
        new_token = create_access_token(identity=current_user, fresh=False)
        
        # Block previous access_token
        jti = get_jwt()['jti']
        user_service.add_jti_blocklist(jti)
        
        return {"access_token": new_token}