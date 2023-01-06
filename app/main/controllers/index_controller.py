from flask_restful import Resource
from flask import Response, render_template

class IndexController(Resource):
    def get(self):
        return Response(render_template("index.html"))