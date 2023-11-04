from app.db import db


class RolePermissionModel(db.Model):
    __tablename__ = "role_permission"

    id = db.Column(db.Integer, primary_key=True)
    role_id = db.Column(db.Integer, db.ForeignKey("role.id"))
    permission_id = db.Column(db.Integer, db.ForeignKey("permission.id"))
