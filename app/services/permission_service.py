from app.db import db
from app.models.permission_model import PermissionModel
from sqlalchemy import asc
from flask_smorest import abort

def get_all_permission():
    results = PermissionModel.query.order_by(asc(PermissionModel.id)).all()
    return results

def post_permission(permission_data):
    name = permission_data['name']
    route = permission_data['route']

    try:
        new_row = PermissionModel(name=name, route=route)
    
        db.session.add(new_row)
        db.session.commit()
    except:
        db.session.rollback()
        abort(400, message="Can not add permission!")
    
    return {"message": "Add successfully!"}

def get_permission(permission_id):
    results = PermissionModel.query.filter_by(id=permission_id).first()
    return results

def update_permission(permission_data, permission_id):
    permission = PermissionModel.query.filter_by(id=permission_id).first()
    
    if not permission:
        abort(400, message="permission doesn't exist, cannot update!")

    try:                      
        if permission_data['name']:
            permission.name = permission_data['name']
            
        if permission_data['route']:
            permission.route = permission_data['route']
            
        db.session.commit()
    except:
        db.session.rollback()
        abort(400, message="Can not update permission!")

    return {"message": "Update successfully!"}

