from flask import jsonify, request, g
from functools import wraps
import jwt
import string
from app import app


def Verifytoken(func):
    # decorator factory which invoks update_wrapper() method and passes decorated function as an argument
    @wraps(func)
    def decorated(*args, **kwargs):
        authentication = request.headers.get('authentication')
        if authentication == None:
            return jsonify({'Message!': 'Authentication Required'}), 401
        token = authentication.split(" ")[1]
        if not token:
            return jsonify({'Message!': 'Authentication Required'}), 401
        try:
            decoded = jwt.decode(token, app.config['SECRET_KEY'], algorithms=[
                                 'RS256',], options={"verify_signature": False})
            g.userData = decoded
        except jwt.DecodeError:
            return jsonify({'Message': 'Invalid token'}), 401
        return func(*args, **kwargs)
    return decorated
