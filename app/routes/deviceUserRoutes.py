from flask import Blueprint
from app.controllers.deviceUserController import deviceUserController

deviceUser_api = Blueprint('device_user_api', __name__, url_prefix='/api/app')

deviceUser_api.add_url_rule('/device', 
               view_func=deviceUserController.getDeviceAll, methods=['GET'])

deviceUser_api.add_url_rule('/device/<id>', 
               view_func=deviceUserController.getDeviceById, methods=['GET'])

deviceUser_api.add_url_rule('/device/<id>', 
               view_func=deviceUserController.putDeviceById, methods=['PUT'])

deviceUser_api.add_url_rule('/device', 
               view_func=deviceUserController.postDevice, methods=['POST'])

deviceUser_api.add_url_rule('/device/<id>', 
               view_func=deviceUserController.deleteDeviceById, methods=['DELETE'])