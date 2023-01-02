from flask import jsonify, request, make_response
from app.middleware.authJwt import Verifytoken
from app.utils.api_response import *
from app.models.verifyModels import users


class VerifyController():

    @Verifytoken
    def verifyUid(self):
        pass

    @Verifytoken
    def verifyBio(self):
        pass

    @Verifytoken
    def verifyQR(self):
        pass

    @Verifytoken
    def getUserAll(self):
        pass

    @Verifytoken
    def getUserById(self, id):
        pass

    @Verifytoken
    def putUserById(self, id):
        pass

    @Verifytoken
    def postUser(self):
        pass

    @Verifytoken
    def deleteUserById(self, id):
        pass


verifyController = VerifyController()
