import os
import unittest

from passlib.hash import pbkdf2_sha256

from app import create_app, db
from app.models import UserModel


class UsersUnitTests(unittest.TestCase):
    def setUp(self):
        """
        This method runs once before any test in this class.
        It sets up the application context and creates the necessary database tables.
        """
        self.app = create_app(
            settings_module=os.environ.get("APP_TEST_SETTINGS_MODULE")
        )
        with self.app.app_context():
            db.create_all()

    def tearDown(self):
        """
        This method runs once after all tests in this class have been executed.
        It removes the database session and drops the database tables.
        """
        with self.app.app_context():
            db.session.remove()
            db.drop_all()

    def test_create_user(self):
        """
        Test case to check if creating a user is successful.
        """

        with self.app.app_context():
            username = "test_user"
            password = "123456"

            user = UserModel(username=username, password=pbkdf2_sha256.hash(password))

            # Add to database
            db.session.add(user)
            db.session.commit()

            # Assertions to check if the user object is created correctly
            self.assertEqual(username, user.username)
            self.assertTrue(pbkdf2_sha256.verify(password, user.password))


if __name__ == "__main__":
    unittest.main()
