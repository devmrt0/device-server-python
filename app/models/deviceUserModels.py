import json
import os
from app.utils.api_response import *


class DeviceUsers():

    def __init__(self):
        self.list = dict()
        self.filename = os.getcwd() + "/app/data/devices.json"

    def load(self):
        try:
            with open(self.filename) as json_file:
                json_data = json.load(json_file)
            for JsonObj in json_data:
                self.list[JsonObj.get('id')] = JsonObj
        except Exception as e:
            print(str(e))

    def authDevice(self, id, password):
        userFound = self.list.get(id)
        if userFound != None:
            return (userFound.get(password, '') == password)
        else:
            return False

    def get(self):
        if len(self.list) == 0:
            return warning(10007)
        else:
            return success(list(self.list.values()))


deviceUsers = DeviceUsers()
deviceUsers.load()
