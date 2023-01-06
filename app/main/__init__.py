from flask import Flask, jsonify, request, render_template, flash
import json
from dataclasses import dataclass
from datetime import datetime
from flask_jwt_extended import JWTManager 
import secrets
from passlib.hash import pbkdf2_sha256
from main.config import Config
from main.models.models import db
from main.models.blocklist_model import BlocklistModel 

app = Flask(__name__)

# Config
app.config.from_object(Config)

# Connect with db
db.init_app(app)

# Config JWT
jwt = JWTManager(app)

@jwt.token_in_blocklist_loader
def check_if_token_in_blocklist(jwt_header, jwt_payload):
    print(jwt_payload['jti'])
    return BlocklistModel.query.filter_by(block_list=jwt_payload['jti']).first()

@jwt.revoked_token_loader
def revoked_token_callback(jwt_header, jwt_payload):
    return jsonify({"description": "The token has been revoked", "error": "token_revoked"}), 401

@jwt.additional_claims_loader
def add_claims_to_jwt(identity):
    # Look in admin in database
    if identity == 1:
        return {"is_admin": True}
    return {"is_admin": False}

@jwt.expired_token_loader
def expired_token_callback(jwt_header, jwt_payload):
    return jsonify({"message": "Token has expired.", "error": "token_expired"}), 401

@jwt.invalid_token_loader
def invalid_token_callback(error):
    return jsonify({"message": "Signature verification failed.", "error": "invalid_token"}), 401

@jwt.unauthorized_loader
def miss_token_callback(error):
    return jsonify({"description": "Request does not contain an access token", "error": "authorization_required"}), 401

def create_app():
    global app
    return app