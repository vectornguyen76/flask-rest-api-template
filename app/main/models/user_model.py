
        
from .models import db
from .marshmallow import ma
from datetime import datetime

class UserModel(db.Model):
    __tablename__ = "user"
    
    id = db.Column(db.Integer, primary_key = True) 
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(), nullable=False)
    time_created = db.Column(db.String())
    
    # def __repr__(self):
    #     return '<Account %r>' % self.id
    
    def __init__(self, username, password, time_created):
        self.username = username
        self.password = password
        self.time_created = time_created

class User_Schema(ma.SQLAlchemySchema):
    class Meta:
        model = UserModel
    
    id = ma.auto_field()
    username = ma.auto_field()
    password = ma.auto_field()
    time_created = ma.auto_field()

users_schema = User_Schema(many=True)