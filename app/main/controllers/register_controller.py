from flask_restful import Resource
from flask import Response, render_template

class RegisterController(Resource):
    def get(self):
        return Response(render_template("register.html"))