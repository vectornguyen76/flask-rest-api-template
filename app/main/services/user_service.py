from main.models.models import db
from main.models.user_model import UserModel
from main.models.blocklist_model import BlocklistModel
from datetime import datetime
from passlib.hash import pbkdf2_sha256
from sqlalchemy import desc, asc
from flask_jwt_extended import create_access_token, create_refresh_token
from flask_smorest import abort

def get_all_user():
    results = UserModel.query.order_by(asc(UserModel.id)).all()
    return results

def get_user(user_id):
    results = UserModel.query.filter_by(id=user_id).first()
    return results

def update_user(user_data, user_id):
    result = UserModel.query.filter_by(id=user_id).first()
    if not result:
        abort(400, message="User doesn't exist, cannot update!")

    try:
        if user_data['username']:
            result.username = user_data['username']
            
        if user_data['password']:
            # Hash password
            password = pbkdf2_sha256.hash(user_data['password'])
            result.password = password
            
        if user_data['time_created']:
            result.time_created = user_data['time_created']
            
        db.session.commit()
    except:
        db.session.rollback()
        abort(400, message="Can not update!")

    return {"message": "Update successfully!"}

def delete_user(id):
    result = UserModel.query.filter_by(id=id).delete()
    if not result:
        abort(400, message="User doesn't exist, cannot delete!")
    
    db.session.commit()
    return {"message": "Delete successfully!"}

def login_user(user_data):
    user = UserModel.query.filter(UserModel.username == user_data['username']).first()
    
    # Verify
    if user and pbkdf2_sha256.verify(user_data['password'], user.password):
        access_token = create_access_token(identity=user.id, fresh=True)
        refresh_token = create_refresh_token(identity=user.id)
        return {"access_token": access_token, "refresh_token": refresh_token}

    abort(401, message="Invalid credentials.")

def register_user(user_data):
    username = user_data['username']
    password = user_data['password']
    time_created = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Hash password
    password = pbkdf2_sha256.hash(password)
    
    new_row = UserModel(username = username, password = password, time_created = time_created)
    
    try:
        db.session.add(new_row)
        db.session.commit()
    except:
        db.session.rollback()
        abort(400, message="Can not register!")
    
    return {"message": "Add successfully!"}

def add_jti_blocklist(jti):
    new_row = BlocklistModel(jti_blocklist = str(jti))
    try:
        db.session.add(new_row)
        db.session.commit()
    except:
        db.session.rollback()
        abort(400, message="Can not add jti!")