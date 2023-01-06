from main.models.user_model import UserModel, users_schema, db
from flask_restful import reqparse
from passlib.hash import pbkdf2_sha256
from flask_jwt_extended import create_access_token

login_args = reqparse.RequestParser()
login_args.add_argument("username", type=str, required=True)
login_args.add_argument("password", type=str, required=True)

def post_login():
    args = login_args.parse_args()
    user = UserModel.query.filter(UserModel.username == args['username']).first()
    
    # Verify
    if user and pbkdf2_sha256.verify(args['password'], user.password):
        access_token = create_access_token(identity=user.id)
        return {"access_token": access_token}, 200

    return {"message": "Invalid credentials."}, 400