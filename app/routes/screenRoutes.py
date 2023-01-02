from flask import Blueprint
from app.controllers.screenController import screenController

screen_api = Blueprint('screen_api', __name__, url_prefix='/api/app')

screen_api.add_url_rule('/screen',
                        view_func=screenController.getScreenAll, methods=['GET'])

screen_api.add_url_rule('/screen/<id>',
                        view_func=screenController.getScreenById, methods=['GET'])

screen_api.add_url_rule('/screen/<id>',
                        view_func=screenController.putScreenById, methods=['PUT'])