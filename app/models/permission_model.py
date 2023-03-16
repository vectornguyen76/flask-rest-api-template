from db import db

class PermissionModel(db.Model):
    __tablename__ = 'permission'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), unique=True, nullable=False)
    route = db.Column(db.String(), unique=True, nullable=False)
    roles = db.relationship("RoleModel", back_populates="permissions", secondary="role_permission")
        