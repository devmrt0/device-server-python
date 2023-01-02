from flask import jsonify, request, make_response
from app.middleware.authJwt import Verifytoken
from app.utils.api_response import *
from app.models.deviceModels import devices


class DeviceController():

    @Verifytoken
    def getUserUniqueIdCommand(self,deviceid,user_id):
        pass

    @Verifytoken
    def postUserUniqueIdCommand(self,deviceid,user_id):
        pass

    @Verifytoken
    def deleteUserUniqueIdCommand(self,deviceid,user_id):
        pass

    @Verifytoken
    def deleteUserUniqueIdCommandById(self,deviceid,user_id,uniqueid):
        pass

    @Verifytoken
    def getUserProfilePhotoCommand(self,deviceid,user_id):
        pass

    @Verifytoken
    def postUserProfilePhotoCommand(self,deviceid,user_id):
        pass

    @Verifytoken
    def deleteUserProfilePhotoCommand(self,deviceid,user_id):
        pass

    @Verifytoken
    def getUserTzCommandByDate(self,deviceid,user_id,date):
        pass

    @Verifytoken
    def postUserTzCommand(self,deviceid,user_id):
        pass

    @Verifytoken
    def getUserTzCommand(self,deviceid,user_id):
        pass

    @Verifytoken
    def deleteUserTzCommandByDate(self,deviceid,user_id,date):
        pass

    @Verifytoken
    def deleteUserTzCommand(self,deviceid,user_id):
        pass

    @Verifytoken
    def getCommandCount(self,deviceid,command):
        pass

    @Verifytoken
    def getCommandList(self,deviceid,command):
        pass
    
    @Verifytoken
    def getCommand(self, deviceid, command):
        try:
            result = devices.addCommandToList(
                'get', command, deviceid, request.args, None, None)
            status = result.get('status', None)
            if status == None:
                return make_response(jsonify({'message': "Server Error. Undefinde Error"}), 500)
            elif (status == -1) and (result.get('code') in [10012, 10013, 10014]):
                return make_response(result, 400)
            else:
                return make_response(result, 200)
        except Exception as e:
            return make_response(jsonify({'message': "Server Error. " + str(e)}), 500)

    @Verifytoken
    def getCommandByid(self, deviceid, command,id):
        pass

    @Verifytoken
    def postCommand(self, deviceid, command):
        pass

    @Verifytoken
    def postCommandByid(self, deviceid, command,id):
        pass

    @Verifytoken
    def deleteCommand(self, deviceid, command):
        pass

    @Verifytoken
    def deleteCommandByid(self, deviceid, command,id):
        pass
        

deviceController = DeviceController()
