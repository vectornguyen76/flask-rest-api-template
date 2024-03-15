import logging

from flask_smorest import abort

from app.db import db
from app.models.permission_model import PermissionModel
from app.models.role_model import RoleModel
from app.models.role_permission_model import RolePermissionModel

# Create logger for this module
logger = logging.getLogger(__name__)


def get_role_permission():
    results = RolePermissionModel.query.all()
    return results


def update_roles_to_permission(permission_data):
    for permission_id in permission_data["data_update"]:
        permission = PermissionModel.query.filter_by(id=int(permission_id)).first()

        permission.roles = []

        for role_id in permission_data["data_update"][permission_id]:
            role = RoleModel.query.filter_by(id=role_id).first()
            permission.roles.append(role)
        try:
            db.session.add(permission)
            db.session.commit()
        except Exception as ex:
            logger.error(f"An error occurred while inserting the roles. Error: {ex}")
            abort(
                500, message=f"An error occurred while inserting the roles. Error: {ex}"
            )
    return {"message": "Update successfully!"}
