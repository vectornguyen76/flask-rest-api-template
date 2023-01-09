from flask import Response, render_template
from flask_jwt_extended import jwt_required
from flask.views import MethodView
from flask_smorest import Blueprint, abort

blp = Blueprint("Index", __name__, description="Index API")

@blp.route("/")
class Index(MethodView):
    # @jwt_required()
    def get(self):
        return Response(render_template("index.html"))