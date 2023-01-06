from flask_restful import Resource
from main.services import user_service
from flask_jwt_extended import jwt_required, get_jwt
from flask import Response, render_template

from flask.views import MethodView
from flask_smorest import Blueprint, abort

blp = Blueprint("user", __name__, description="User API")
from main.services import login_service

@blp.route("/leaves")
class UserController(Resource):
    @jwt_required()
    def get(self):
        result = user_service.get_user()
        return result
    
    @jwt_required()
    def put(self):
        result = user_service.put_user()
        return result
    
    @jwt_required()
    def patch(self, id):
        result = user_service.patch_user(id)
        return result
        
    @jwt_required()
    def delete(self, id):
        # Only admin can delete user
        jwt = get_jwt()
        if not jwt.get("is_admin"):
            abort(401, message="Admin privilege requierd.")
        
        result = user_service.del_user(id)
        return result

@blp.route("/login")
class LoginController(Resource):
    def get(self):
        return Response(render_template("login.html"))
    
    def post(self):
        result = login_service.post_login()
        return result
    
@blp.route("/register")
class RegisterController(Resource):
    def get(self):
        return Response(render_template("register.html"))
    
    def post(self):
        result = user_service.put_user()
        return result