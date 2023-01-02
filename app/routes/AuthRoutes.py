from flask import Blueprint
from app.controllers.AuthController import AuthController

auth_api = Blueprint('auth_api', __name__, url_prefix='/api')

auth_api.add_url_rule(
    '/login', view_func=AuthController().login, methods=['POST'])
