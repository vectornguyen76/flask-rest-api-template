from db import db

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


