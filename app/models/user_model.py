from datetime import datetime

from app.db import db


class UserModel(db.Model):
    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(), nullable=False)
    block = db.Column(db.Boolean, default=False, nullable=False)
    time_created = db.Column(db.String(), default=datetime.now())
    roles = db.relationship("RoleModel", back_populates="users", secondary="user_role")
