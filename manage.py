import unittest

import click
import coverage
from passlib.hash import pbkdf2_sha256

from app.db import db
from app.models import (
    PermissionModel,
    RoleModel,
    RolePermissionModel,
    UserModel,
    UserRoleModel,
)


@click.option(
    "--pattern", default="tests_*.py", help="Test search pattern", required=False
)
def cov(pattern):
    """
    Run the unit tests with coverage
    """
    cov = coverage.coverage(branch=True, include="app/*")
    cov.start()
    tests = unittest.TestLoader().discover("tests", pattern=pattern)
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        cov.stop()
        cov.save()
        print("Coverage Summary:")
        cov.report()
        cov.erase()
        return 0
    return 1


@click.option(
    "--pattern", default="tests_*.py", help="Test search pattern", required=False
)
def cov_html(pattern):
    """
    Run the unit tests with coverage and generate an HTML report.
    """
    cov = coverage.coverage(branch=True, include="app/*")
    cov.start()

    tests = unittest.TestLoader().discover("tests", pattern=pattern)
    result = unittest.TextTestRunner(verbosity=2).run(tests)

    if result.wasSuccessful():
        cov.stop()
        cov.save()

        print("Coverage Summary:")
        cov.report()
        cov.html_report(directory="report/htmlcov")
        cov.erase()
        return 0

    return 1


@click.option("--pattern", default="tests_*.py", help="Test pattern", required=False)
def tests(pattern):
    """
    Run the tests without code coverage
    """
    tests = unittest.TestLoader().discover("tests", pattern=pattern)
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1


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
    read_perrmission = PermissionModel(name="read", description="Read data")
    write_perrmission = PermissionModel(name="write", description="Write data")
    delete_perrmission = PermissionModel(name="delete", description="Delete data")
    db.session.add_all([read_perrmission, write_perrmission, delete_perrmission])
    db.session.commit()

    # Insert Role
    admin_role = RoleModel(name="Admin", description="Full Permission")
    user_role = RoleModel(name="User", description="Can read, write data")
    guest_role = RoleModel(name="Guest", description="Just read data")
    db.session.add_all([admin_role, user_role, guest_role])
    db.session.commit()

    # Insert Role_Permission
    role_permission_admin1 = RolePermissionModel(role_id=1, permission_id=1)
    role_permission_admin2 = RolePermissionModel(role_id=1, permission_id=2)
    role_permission_admin3 = RolePermissionModel(role_id=1, permission_id=3)
    role_permission_user1 = RolePermissionModel(role_id=2, permission_id=1)
    role_permission_user2 = RolePermissionModel(role_id=2, permission_id=2)
    role_permission_guest = RolePermissionModel(role_id=3, permission_id=1)
    db.session.add_all(
        [
            role_permission_admin1,
            role_permission_admin2,
            role_permission_admin3,
            role_permission_user1,
            role_permission_user2,
            role_permission_guest,
        ]
    )
    db.session.commit()

    # Insert User
    password = pbkdf2_sha256.hash("123456")
    admin_user = UserModel(username="admin", password=password)
    normal_user = UserModel(username="user", password=password)
    guest_user = UserModel(username="guest", password=password)
    db.session.add_all([admin_user, normal_user, guest_user])
    db.session.commit()

    # Insert UserRole
    user_role1 = UserRoleModel(user_id=1, role_id=1)
    user_role2 = UserRoleModel(user_id=2, role_id=2)
    user_role3 = UserRoleModel(user_id=3, role_id=3)
    db.session.add_all([user_role1, user_role2, user_role3])
    db.session.commit()


def create_user_admin(username="admin"):
    """
    Create User Admin.
    """
    admin = UserModel.query.filter_by(username=username).first()

    if admin is None:
        print("user-admin is not created before!")
        init_db_user()
    else:
        print("user-admin is created!")


def init_app(app):
    if app.config["APP_ENV"] == "production":
        commands = [create_db, reset_db, drop_db, create_user_admin]
    else:
        commands = [
            create_db,
            reset_db,
            drop_db,
            create_user_admin,
            tests,
            cov_html,
            cov,
        ]

    for command in commands:
        app.cli.add_command(app.cli.command()(command))
