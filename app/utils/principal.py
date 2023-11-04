from flask_principal import RoleNeed, identity_loaded

from app.extention import principal
from app.models import UserModel


# Define a function to load the user's identity
@identity_loaded.connect
def on_identity_loaded(sender, identity):
    # Get User
    user = UserModel.query.filter_by(id=identity.id).first()

    # Get all unique permissions
    for role in user.roles:
        # get permission
        for permission in role.permissions:
            # Add the user's roles to the identity object
            identity.provides.add(RoleNeed(permission.name))
