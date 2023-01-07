from .models import db
from marshmallow import Schema, fields
class UserModel(db.Model):
    __tablename__ = "user"
    
    id = db.Column(db.Integer, primary_key = True) 
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(), nullable=False)
    time_created = db.Column(db.String())
    
    def __init__(self, username, password, time_created):
        self.username = username
        self.password = password
        self.time_created = time_created
class UserSchema(Schema):
    # Dump only: chỉ read
    id = fields.Str(dump_only=True)
    username = fields.Str(required=True)
    password = fields.Str(required=True)
    time_created = fields.Str(dump_only=True)
    
class UserUpdateSchema(Schema):
    username = fields.Str(allow_none=True)
    password = fields.Str(allow_none=True)
    time_created = fields.Str(allow_none=True)

