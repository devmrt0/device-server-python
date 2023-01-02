from flask import jsonify, request, make_response
from app.middleware.authJwt import Verifytoken
from app.utils.api_response import *
from app.models.screenModels import screens


class ScreenController():

    @Verifytoken
    def getScreenAll(self):
        pass

    @Verifytoken
    def getScreenById(self, id):
        pass

    @Verifytoken
    def putScreenById(self, id):
        pass


screenController = ScreenController()
