from flask import Response, render_template

from flask.views import MethodView
from flask_smorest import Blueprint, abort

blp = Blueprint("Index", __name__, description="Index API")

@blp.route("/")
class Index(MethodView):
    def get(self):
        return Response(render_template("index.html"))