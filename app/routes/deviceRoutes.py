from flask import Blueprint
from app.controllers.deviceController import deviceController

device_api = Blueprint('device_api', __name__, url_prefix='/api')

device_api.add_url_rule('/device/<deviceid>/user/<user_id>/uniqueid',
                        view_func=deviceController.getUserUniqueIdCommand, methods=['GET'])

device_api.add_url_rule('/device/<deviceid>/user/<user_id>/uniqueid',
                        view_func=deviceController.postUserUniqueIdCommand, methods=['POST'])

device_api.add_url_rule('/device/<deviceid>/user/<user_id>/uniqueid',
                        view_func=deviceController.deleteUserUniqueIdCommand, methods=['DELETE'])

device_api.add_url_rule('/device/<deviceid>/user/<user_id>/uniqueid/<uniqueid>',
                        view_func=deviceController.deleteUserUniqueIdCommandById, methods=['DELETE'])

device_api.add_url_rule('/device/<deviceid>/user/<user_id>/photo/profile',
                        view_func=deviceController.getUserProfilePhotoCommand, methods=['GET'])

device_api.add_url_rule('/device/<deviceid>/user/<user_id>/photo/profile',
                        view_func=deviceController.postUserProfilePhotoCommand, methods=['POST'])

device_api.add_url_rule('/device/<deviceid>/user/<user_id>/photo/profile',
                        view_func=deviceController.deleteUserProfilePhotoCommand, methods=['DELETE'])

device_api.add_url_rule('/device/<deviceid>/user/<user_id>/time_zone/<date>',
                        view_func=deviceController.getUserTzCommandByDate, methods=['GET'])

device_api.add_url_rule('/device/<deviceid>/user/<user_id>/time_zone',
                        view_func=deviceController.postUserTzCommand, methods=['POST'])

device_api.add_url_rule('/device/<deviceid>/user/<user_id>/time_zone',
                        view_func=deviceController.getUserTzCommand, methods=['GET'])

device_api.add_url_rule('/device/<deviceid>/user/<user_id>/time_zone/:date',
                        view_func=deviceController.deleteUserTzCommandByDate, methods=['DELETE'])

device_api.add_url_rule('/device/<deviceid>/user/<user_id>/time_zone',
                        view_func=deviceController.deleteUserTzCommand, methods=['DELETE'])

device_api.add_url_rule('/device/<deviceid>/<command>/count',
                        view_func=deviceController.getCommandCount, methods=['GET'])

device_api.add_url_rule('/device/<deviceid>/<command>/list',
                        view_func=deviceController.getCommandList, methods=['GET'])

device_api.add_url_rule('/device/<deviceid>/<command>',
                        view_func=deviceController.getCommand, methods=['GET'])

device_api.add_url_rule('/device/<deviceid>/<command>/<id>',
                        view_func=deviceController.getCommandByid, methods=['GET'])

device_api.add_url_rule('/device/<deviceid>/<command>',
                        view_func=deviceController.postCommand, methods=['POST'])

device_api.add_url_rule('/device/<deviceid>/<command>/<id>',
                        view_func=deviceController.postCommandByid, methods=['POST'])

device_api.add_url_rule('/device/<deviceid>/<command>',
                        view_func=deviceController.deleteCommand, methods=['DELETE'])

device_api.add_url_rule('/device/<deviceid>/<command>/<id>',
                        view_func=deviceController.deleteCommandByid, methods=['DELETE'])
