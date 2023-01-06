from main.models.user_model import UserModel, users_schema, db
from datetime import datetime
from flask_restful import reqparse
from passlib.hash import pbkdf2_sha256
from sqlalchemy import desc, asc

user_args = reqparse.RequestParser()
user_args.add_argument("username", type=str, required=True)
user_args.add_argument("password", type=str, required=True)
user_args.add_argument("time_created", type=str, required=False)

def get_user():
    results = UserModel.query.order_by(asc(UserModel.id)).all()
    output = users_schema.dump(results)

    return output, 200

def put_user():
    args = user_args.parse_args()
    username = args['username']
    password = args['password']
    time_created = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Hash password
    password = pbkdf2_sha256.hash(password)
    
    new_row = UserModel(username = username, password = password, time_created = time_created)
    
    try:
        db.session.add(new_row)
        db.session.commit()
    except:
        db.session.rollback()
        return {"message": "Bad request!"}, 400
    
    return {"message": "Add successfully!"}, 200

def patch_user(id):
    args = user_args.parse_args()
    result = UserModel.query.filter_by(id=id).first()
    if not result:
        return {"message": "User doesn't exist, cannot update!"}, 404

    try:
        if args['username']:
            result.username = args['username']
            
        if args['password']:
            # Hash password
            password = pbkdf2_sha256.hash(args['password'])
            result.password = password
            
        if args['time_created']:
            result.time_created = args['time_created']
            
        db.session.commit()
    except:
        db.session.rollback()
        return {"message": "Can not update!"}, 400

    return {"message": "Update successfully!"}, 200

def del_user(id):
    result = UserModel.query.filter_by(id=id).delete()
    if not result:
        return {"message": "User doesn't exist, cannot delete!"}, 404
    
    db.session.commit()
    return {"message": "Delete successfully!"}, 200
