from db import db
from models.role_model import RoleModel
from models.role_permission_model import RolePermissionModel
from models.user_role_model import UserRoleModel
from models.permission_model import PermissionModel
from sqlalchemy import asc
from flask_smorest import abort

def get_all_role():
    results = RoleModel.query.order_by(asc(RoleModel.id)).all()
    return results

def post_role(role_data):
    name = role_data['name']
    description = role_data['description']
    
    try:
        new_row = RoleModel(name=name, description=description)

        # Add Permission
        for permission_id in role_data['permissions']:
            permission = PermissionModel.query.filter_by(id=permission_id).first()
            new_row.permissions.append(permission)
    
        db.session.add(new_row)
        db.session.commit()
    except:
        db.session.rollback()
        abort(400, message="Can not add role!")
    
    return {"message": "Add successfully!"}

def get_role(role_id):
    results = RoleModel.query.filter_by(id=role_id).first()
    return results

def update_role(role_data, role_id):
    role = RoleModel.query.filter_by(id=role_id).first()
    
    if not role:
        abort(400, message="role doesn't exist, cannot update!")

    # Updete role
    try:                      
        role.permissions = []
        
        for permission_id in role_data['permissions']:
            permission = PermissionModel.query.filter_by(id=permission_id).first()
            role.permissions.append(permission)
            
        if role_data['name']:
            role.name = role_data['name']
            
        if role_data['description']:
            role.description = role_data['description']
            
        db.session.add(role)
        db.session.commit()
    except:
        db.session.rollback()
        abort(400, message="Can not update role!")

    return {"message": "Update successfully!"}

def delete_role(role_id):
    role_permission = RolePermissionModel.query.filter_by(role_id=role_id).delete()
    user_role = UserRoleModel.query.filter_by(role_id=role_id).delete()
    role = RoleModel.query.filter_by(id=role_id).delete()
    
    if not role:
        abort(400, message="Role doesn't exist, cannot delete!")
    
    db.session.commit()
    return {"message": "Delete successfully!"}