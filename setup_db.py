from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app/main/database/database.db'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:070600@localhost/test_db'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.secret_key = 'secret string'

db = SQLAlchemy(app)

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
        
class BlocklistModel(db.Model):
    __tablename__ = "blocklist"
    
    blocklist = db.Column(db.String(), primary_key = True) 
        
if __name__ == '__main__':
    db.create_all()