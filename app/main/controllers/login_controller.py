from flask_restful import Resource
from flask import Response, render_template

from main.services import login_service

class LoginController(Resource):
    def get(self):
        return Response(render_template("login.html"))
    
    def post(self):
        result = login_service.post_login()
        return result