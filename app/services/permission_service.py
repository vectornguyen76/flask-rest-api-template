import logging

from flask_smorest import abort
from sqlalchemy import asc

from app.db import db
from app.models.permission_model import PermissionModel

# Create logger for this module
logger = logging.getLogger(__name__)


def get_all_permission():
    results = PermissionModel.query.order_by(asc(PermissionModel.id)).all()
    return results


def post_permission(permission_data):
    name = permission_data["name"]
    description = permission_data["description"]

    try:
        new_row = PermissionModel(name=name, description=description)

        db.session.add(new_row)
        db.session.commit()
    except Exception as ex:
        db.session.rollback()
        logger.error(f"Can not add permission! Error: {ex}")
        abort(400, message=f"Can not add permission! Error: {ex}")

    return {"message": "Add successfully!"}


def get_permission(permission_id):
    results = PermissionModel.query.filter_by(id=permission_id).first()
    return results


def update_permission(permission_data, permission_id):
    permission = PermissionModel.query.filter_by(id=permission_id).first()

    if not permission:
        logger.error("permission doesn't exist, cannot update!")
        abort(400, message="permission doesn't exist, cannot update!")

    try:
        if permission_data["name"]:
            permission.name = permission_data["name"]

        if permission_data["description"]:
            permission.description = permission_data["description"]

        db.session.commit()
    except Exception as ex:
        db.session.rollback()
        logger.error(f"Can not update permission! Error: {ex}")
        abort(400, message=f"Can not update permission! Error: {ex}")

    return {"message": "Update successfully!"}
