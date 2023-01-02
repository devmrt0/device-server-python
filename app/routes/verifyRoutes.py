from flask import Blueprint
from app.controllers.verifyController import verifyController

verify_api = Blueprint('verify_api', __name__, url_prefix='/api')

verify_api.add_url_rule('/verify/uid',
                        view_func=verifyController.verifyUid, methods=['POST'])

verify_api.add_url_rule('/verify/bio',
                        view_func=verifyController.verifyBio, methods=['POST'])

verify_api.add_url_rule('/verify/qr',
                        view_func=verifyController.verifyQR, methods=['POST'])

verify_api.add_url_rule('/app/user',
                        view_func=verifyController.getUserAll, methods=['GET'])

verify_api.add_url_rule('/app/user/<id>',
                        view_func=verifyController.getUserById, methods=['GET'])

verify_api.add_url_rule('/app/user/<id>',
                        view_func=verifyController.putUserById, methods=['PUT'])

verify_api.add_url_rule('/app/user',
                        view_func=verifyController.postUser, methods=['POST'])

verify_api.add_url_rule('/app/user/<id>',
                        view_func=verifyController.deleteUserById, methods=['DELETE'])