from flask import jsonify, request, make_response
from app.utils.common import isEmpty
from app.models.deviceUserModels import DeviceUsers
from app.middleware.authJwt import Verifytoken
from app.utils.api_response import *


class DeviceUserController(DeviceUsers):

    def __init__(self):
        super().__init__()

    @Verifytoken
    def getDeviceAll(self):
        try:
            return make_response(self.get(), 200)
        except Exception as e:
            return make_response(jsonify({'message': "Server Error. " + str(e)}), 500)

    def getDeviceById(self,id):
        pass

    def putDeviceById(self,id):
        pass

    def postDevice(self):
        pass

    def deleteDeviceById(self,id):
        pass

deviceUserController = DeviceUserController()
deviceUserController.load()
