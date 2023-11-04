from flask import jsonify

from app.extention import jwt
from app.models import BlocklistModel, UserModel


@jwt.token_verification_loader
def custom_token_verification_callback(jwt_header, jwt_data):
    # Query in database
    user = UserModel.query.filter_by(id=jwt_data["sub"]).first()

    # If user was blocked, user will not access.
    if user.block is True:
        return False

    return True


@jwt.token_in_blocklist_loader
def check_if_token_in_blocklist(jwt_header, jwt_payload):
    return BlocklistModel.query.filter_by(jti_blocklist=jwt_payload["jti"]).first()


@jwt.revoked_token_loader
def revoked_token_callback(jwt_header, jwt_payload):
    return (
        jsonify(
            {"description": "The token has been revoked", "error": "token_revoked"}
        ),
        401,
    )


@jwt.needs_fresh_token_loader
def token_not_fresh_callback(jwt_header, jwt_payload):
    return (
        jsonify(
            {"description": "The token is not fresh", "error": "fresh_token_reqired"}
        ),
        401,
    )


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
    return (
        jsonify(
            {"message": "Signature verification failed.", "error": "invalid_token"}
        ),
        401,
    )


@jwt.unauthorized_loader
def miss_token_callback(error):
    return (
        jsonify(
            {
                "description": "Request does not contain an access token",
                "error": "authorization_required",
            }
        ),
        401,
    )
