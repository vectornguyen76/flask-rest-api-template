import logging

from flask_jwt_extended import (
    create_access_token,
    create_refresh_token,
    get_jwt,
    get_jwt_identity,
)
from flask_smorest import abort
from passlib.hash import pbkdf2_sha256
from sqlalchemy import asc

from app.db import db
from app.models.blocklist_model import BlocklistModel
from app.models.role_model import RoleModel
from app.models.user_model import UserModel
from app.services import user_role_service

# Create logger for this module
logger = logging.getLogger(__name__)


def get_all_user():
    results = UserModel.query.order_by(asc(UserModel.id)).all()
    return results


def get_user(user_id):
    results = UserModel.query.filter_by(id=user_id).first()
    return results


def update_user(user_data, user_id):
    user = UserModel.query.filter_by(id=user_id).first()
    if not user:
        logger.error("User doesn't exist, cannot update!")
        abort(400, message="User doesn't exist, cannot update!")

    try:
        if user_data["username"]:
            user.username = user_data["username"]

        if user_data["password"]:
            # Hash password
            password = pbkdf2_sha256.hash(user_data["password"])
            user.password = password

        # Update roles
        user.roles = []

        for role_id in user_data["roles"]:
            role = RoleModel.query.filter_by(id=role_id).first()
            user.roles.append(role)

        db.session.commit()
    except Exception as ex:
        db.session.rollback()
        logger.error(f"Can not update! Error: {ex}")
        abort(400, message=f"Can not update! Error: {ex}")

    return {"message": "Update successfully!"}


def update_block_user(user_data, user_id):
    # Only admin can delete user
    jwt = get_jwt()
    if not jwt.get("is_admin"):
        logger.error("Admin privilege requierd.")
        abort(401, message="Admin privilege requierd.")

    if user_id == 1:
        logger.error("Can not block Super Admin!")
        abort(401, message="Can not block Super Admin!")

    user = UserModel.query.filter_by(id=user_id).first()

    if not user:
        logger.error("User doesn't exist, cannot update!")
        abort(400, message="User doesn't exist, cannot update!")

    try:
        # Update status block
        user.block = user_data["block"]

        db.session.add(user)
        db.session.commit()
    except Exception as ex:
        db.session.rollback()
        logger.error(f"Can not update status block User! Error: {ex}")
        abort(400, message=f"Can not update status block User! Error: {ex}")

    return {"message": "Block successfully!"}


def delete_user(id):
    # Only admin can delete user
    jwt = get_jwt()
    if not jwt.get("is_admin"):
        logger.error("Admin privilege requierd.")
        abort(401, message="Admin privilege requierd.")

    result = UserModel.query.filter_by(id=id).delete()
    if not result:
        logger.error("User doesn't exist, cannot delete!")
        abort(400, message="User doesn't exist, cannot delete!")

    db.session.commit()
    return {"message": "Delete successfully!"}


def login_user(user_data):
    # Check user name
    user = UserModel.query.filter(UserModel.username == user_data["username"]).first()

    # Verify
    if user and pbkdf2_sha256.verify(user_data["password"], user.password):
        # Create access_token
        access_token = create_access_token(identity=user.id, fresh=True)

        # Create refresh_token
        refresh_token = create_refresh_token(identity=user.id)

        logger.info(f"User login successfully! user_name: {user_data['username']}")

        return {"access_token": access_token, "refresh_token": refresh_token}

    logger.error("Invalid credentials.")
    abort(401, message="Invalid credentials.")


def register_user(user_data):
    username = user_data["username"]
    password = user_data["password"]

    # Check user name exist
    user = UserModel.query.filter(UserModel.username == user_data["username"]).first()
    if user:
        logger.error("Username already exists.")
        abort(400, message="Username already exists.")

    # Hash password
    password = pbkdf2_sha256.hash(password)

    new_user = UserModel(username=username, password=password)

    try:
        db.session.add(new_user)
        db.session.commit()

    except Exception as ex:
        db.session.rollback()
        logger.error(f"Can not register! Error: {ex}")
        abort(400, message=f"Can not register! Error: {ex}")

    try:
        # Add default role for user
        user_role_service.link_roles_to_user(user_id=new_user.id, role_id=3)

    except Exception as ex:
        logger.error(f"Can not register! - Can not add role default. Error: {ex}")
        abort(400, message=f"Can not register! - Can not add role default. Error: {ex}")

    return {"message": "Register successfully!"}


def refresh_token():
    # Get id current user
    current_user_id = get_jwt_identity()

    # Create access_token
    access_token = create_access_token(identity=current_user_id, fresh=True)

    # Create refresh_token
    refresh_token = create_refresh_token(identity=current_user_id)

    # Block previous access_token
    jti = get_jwt()["jti"]

    # Block access token
    add_jti_blocklist(jti)

    return {"access_token": access_token, "refresh_token": refresh_token}


def add_jti_blocklist(jti):
    # Add to blockist when remove jti
    new_row = BlocklistModel(jti_blocklist=str(jti))

    try:
        db.session.add(new_row)
        db.session.commit()
    except Exception as ex:
        db.session.rollback()
        logger.error(f"Can not add jti! Error: {ex}")
        abort(400, message=f"Can not add jti! Error: {ex}")
