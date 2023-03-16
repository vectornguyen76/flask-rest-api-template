from flask import Flask, jsonify
from flask_jwt_extended import JWTManager 
from config import Config
from db import db
from models.blocklist_model import BlocklistModel 
from blueprint import register_routing
from flask_cors import CORS
from flask_migrate import Migrate
from models.user_model import UserModel
from flask_principal import Principal, identity_loaded, RoleNeed

app = Flask(__name__)

# Config
app.config.from_object(Config)

# CORS - manage resource
CORS(app, supports_credentials='true' ,resources={r"*": { "origins": "*" }})

# Connect with db
db.init_app(app)

# Migrate db
migrate = Migrate(app, db)

# Register Blueprint
register_routing(app)

#################################################################################

# Initialize Flask-Principal
principal = Principal(app)

# Define a function to load the user's identity
@identity_loaded.connect_via(app)
def on_identity_loaded(sender, identity):
    # Get User
    user = UserModel.query.filter_by(id=identity.id).first()
    
    # Get all unique permissions
    for role in user.roles:
        # get permission
        for permission in role.permissions:
            # Add the user's roles to the identity object
            identity.provides.add(RoleNeed(permission.route))

#################################################################################

# Config JWT
jwt = JWTManager(app)

@jwt.token_verification_loader
def custom_token_verification_callback(jwt_header, jwt_data):    
    # Query in database
    user = UserModel.query.filter_by(id=jwt_data['sub']).first()
    
    # If user was blocked, user will not access.
    if user.block == True:
        return False
    
    return True

@jwt.token_in_blocklist_loader
def check_if_token_in_blocklist(jwt_header, jwt_payload):
    return BlocklistModel.query.filter_by(jti_blocklist=jwt_payload['jti']).first()

@jwt.revoked_token_loader
def revoked_token_callback(jwt_header, jwt_payload):
    return jsonify({"description": "The token has been revoked", "error": "token_revoked"}), 401

@jwt.needs_fresh_token_loader
def token_not_fresh_callback(jwt_header, jwt_payload):
    return jsonify({"description": "The token is not fresh", "error": "fresh_token_reqired"}), 401

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