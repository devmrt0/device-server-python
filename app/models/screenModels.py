import json
import os
from app.utils.api_response import *


class Screens():

    def __init__(self):
        self.list = dict()
        self.filename = os.getcwd() + "/app/data/screen.json"

    def load(self):
        pass
        
        

screens = Screens()
screens.load()
