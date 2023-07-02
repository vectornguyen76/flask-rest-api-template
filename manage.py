from app import db
from app.models import UserModel, PermissionModel, RoleModel,  RolePermissionModel, UserRoleModel
from passlib.hash import pbkdf2_sha256

def create_db():
    """
    Create Database.
    """
    db.create_all()
    db.session.commit()


def reset_db():
    """
    Reset Database.
    """
    db.drop_all()
    db.create_all()
    db.session.commit()


def drop_db():
    """
    Drop Database.
    """
    db.drop_all()
    db.session.commit()

def init_db_user():
    # Insert Permission  
    new_perrmission1 = PermissionModel(name='User management', route='user_management')
    db.session.add_all([new_perrmission1])
    db.session.commit()
    
    # Insert Role  
    new_role1 = RoleModel(name='Super Admin', description='Full Permission')
    new_role2 = RoleModel(name='Admin', description='Manage user')
    new_role3 = RoleModel(name='Member', description='Member')
    new_role4 = RoleModel(name='Guest',description='Guest')
    db.session.add_all([new_role1, new_role2, new_role3, new_role4])
    db.session.commit()
    
    # Insert Role_Permission  
    new_permission1 = RolePermissionModel(role_id=1, permission_id=1)
    new_permission2 = RolePermissionModel(role_id=2, permission_id=1)
    db.session.add_all([new_permission1, new_permission2])
    db.session.commit()
    
    # Insert User  
    password = pbkdf2_sha256.hash("123456")
    new_user1 = UserModel(username='admin', password=password)
    db.session.add_all([new_user1])
    db.session.commit()
    
    # Insert UserRole  
    new_userrole1 = UserRoleModel(user_id=1, role_id = 1)
    new_userrole2 = UserRoleModel(user_id=1, role_id = 2)
    new_userrole3 = UserRoleModel(user_id=1, role_id = 3)
    db.session.add_all([new_userrole1, new_userrole2, new_userrole3])
    db.session.commit()

def create_user_admin(username='admin'):
    """
    Create User Admin.
    """
    admin = UserModel.query.filter_by(username=username).first()
    
    
    if admin is None:
        print("user-admin is not created!")
        init_db_user()
    else:
        print("user-admin is created!")
        
def init_app(app):
    if app.config['APP_ENV'] == 'production':
        commands = [create_db, reset_db, drop_db, create_user_admin]
    else:
        commands = [create_db, reset_db, drop_db, create_user_admin]

    for command in commands:
        app.cli.add_command(app.cli.command()(command))

