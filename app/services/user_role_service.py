import logging

from flask_smorest import abort

from app.db import db
from app.models.role_model import RoleModel
from app.models.user_model import UserModel

# Create logger for this module
logger = logging.getLogger(__name__)


def link_roles_to_user(user_id, role_id):
    user = UserModel.query.filter_by(id=user_id).first()
    role = RoleModel.query.filter_by(id=role_id).first()

    user.roles.append(role)

    try:
        db.session.add(user)
        db.session.commit()
    except Exception as ex:
        logger.error(f"An error occurred while inserting the role. Error: {ex}")
        abort(500, message=f"An error occurred while inserting the role. Error: {ex}")

    return role


def delete_roles_to_user(user_id, role_id):
    user = UserModel.query.filter_by(id=user_id).first()
    role = RoleModel.query.filter_by(id=role_id).first()

    user.roles.remove(role)

    try:
        db.session.add(user)
        db.session.commit()
    except Exception as ex:
        logger.error(f"An error occurred while deleting the role. Error: {ex}")
        abort(500, message=f"An error occurred while deleting the role. Error: {ex}")

    return {"message": "User removed from role", "user": user, "role": role}
