# from app.models.user_model import UserModel
# from flask_principal import Principal, identity_loaded, RoleNeed
# from app import app

# # Initialize Flask-Principal
# principal = Principal(app)

# # Define a function to load the user's identity
# @identity_loaded.connect_via(app)
# def on_identity_loaded(sender, identity):
#     # Get User
#     user = UserModel.query.filter_by(id=identity.id).first()
    
#     # Get all unique permissions
#     for role in user.roles:
#         # get permission
#         for permission in role.permissions:
#             # Add the user's roles to the identity object
#             identity.provides.add(RoleNeed(permission.route))
