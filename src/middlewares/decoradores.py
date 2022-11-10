from functools import wraps
from ..functions import functionUser
from flask_jwt_extended import verify_jwt_in_request
from flask_jwt_extended import get_jwt_identity
from flask import jsonify


def admin_required():
    def wrapper(fn):
        @wraps(fn)
        def decorator(*args, **kwargs):
            verify_jwt_in_request()
            claims = get_jwt_identity()
            if claims["rol"] == "ADMINISTRADOR":
                return fn(*args, **kwargs)
            else:
                return jsonify(msg="Role ADMIN only!"), 403
        return decorator
    return wrapper


def get_city():
    claims = get_jwt_identity()
    result = functionUser().findUserbyId(claims['id']).ciudad_id
    return result


def getUserId():
    claims = get_jwt_identity()
    return claims['id']
