import logging
import time
from functools import wraps

from flask_jwt_extended import get_jwt
from flask_smorest import abort

from app.models import UserModel

# Create logger for this module
logger = logging.getLogger(__name__)


def permission_required(permission_name):
    def decorator(func):
        def wrapper(*arg, **kwargs):
            jwt_data = get_jwt()
            user_id = jwt_data["sub"]
            user = UserModel.query.filter_by(id=user_id).first()
            for role in user.roles:
                for permission in role.permissions:
                    if permission.name == permission_name:
                        return func(*arg, **kwargs)
            logger.error("User does not have permission to access this API!")
            abort(403, message="User does not have permission to access this API!")

        return wrapper

    return decorator


def time_profiling(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        logger.info(f"Function {func.__name__} took {end_time-start_time:.4f}s.")
        return result

    return wrapper
