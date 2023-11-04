from app.db import db


class RoleModel(db.Model):
    __tablename__ = "role"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), unique=True, nullable=False)
    description = db.Column(db.String(), nullable=False)
    permissions = db.relationship(
        "PermissionModel", back_populates="roles", secondary="role_permission"
    )
    users = db.relationship("UserModel", back_populates="roles", secondary="user_role")
