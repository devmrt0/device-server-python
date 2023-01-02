import json
import os
import uuid
from app.utils.api_response import *
from app.utils.common import isEmpty, JSONstringify
from app.utils.json_schema import SchemaValidate
import time


class Commands():

    def __init__(self):
        self.list = dict()
        self.filename = os.getcwd() + "/app/data/commands.json"

    def add(self, command):
        url = command.get('url').strip()
        http_method = command.get('http_method').strip()
        method_type = command.get('method_type').strip()
        key = url + '_' + http_method + '_' + method_type
        self.list[key] = command

    def load(self):
        try:
            with open(self.filename) as json_file:
                json_data = json.load(json_file)
            for JsonObj in json_data:
                self.add(JsonObj)
        except Exception as e:
            print(str(e))

    def getCommand(self, url, http_method, method_type):
        return self.list.get(url + "_" + http_method + "_" + method_type)

    def checkDataIsArray(self, data):
        return (len(data) != 0) and (data != None) and (type(data) == list)
    # and isinstance(data,dict)

    def getCommandEx(self, url, http_method, id, data):
        if http_method == "post" and id == None:
            if self.checkDataIsArray(data):
                return self.getCommand(url, http_method, "all")
            else:
                return self.getCommand(url, http_method, "id")
        else:
            if id == None:
                return self.getCommand(url, http_method, "all")
            else:
                return self.getCommand(url, http_method, "id")


class Device():

    def __init__(self, id, language, token, ws):
        self.id = id
        self.language = language
        self.token = token
        self.ws = ws
        self.commands = dict()

    def sendCommand(self, method, data):
        command = {}
        command['status'] = 0
        command['code'] = 0
        command['detail'] = "OK"
        command['method'] = method
        command['requestid'] = str(uuid.uuid4())
        print(command['requestid'])
        #command['data'] = {}
        if not isEmpty(data):
            command['data'] = data
        self.commands[command['requestid']] = command
        if not isEmpty(data):
            self.ws.send(JSONstringify(
                {'method': command['method'], 'requestid': command['requestid'], 'data': command['data']}))
        else:
            self.ws.send(JSONstringify(
                {'method': command['method'], 'requestid': command['requestid']}))
        if 'data' in command:
            del command['data']
        return command['requestid']

    def addCommand(self, method, data):
        requestid = self.sendCommand(method, data)
        command = self.commands.get(requestid)
        for i in range(0, 300):
            time.sleep(0.010)
            if (command['status'] != 0):
                print('break')
                break
        if requestid in self.commands:
            del self.commands[requestid]
        return command

   #  async addCommand(method, data) {
   #      try {
   #          let requestid = this.sendCommand(method, data);
   #          let promise = new Promise((resolve, reject) => {
   #              const command = this.commands.get(requestid);
   #              let loopCnt = 0;
   #              let timer = setInterval(function (commands) {
   #                  loopCnt++;
   #                  //console.log("loopCnt : " + loopCnt + " command.status : " +  command.status);
   #                  if (command.status != 0) {
   #                      clearInterval(timer);
   #                      resolve(command);
   #                  } else
   #                      if (loopCnt > 300) {
   #                          clearInterval(timer);
   #                          resolve(api_resp.error(10011));
   #                      }
   #              }, 10);
   #          });
   #          let result = await promise;
   #          this.commands.delete(requestid);
   #          return result;
   #      } catch (error) {
   #          return { message: "Server Error. " + error.message };
   #      }
   #  }

    def parseResponseMessage(self, msg):
        try:
            command = json.loads(msg)
            if isEmpty(command["requestid"]):
                return False, None
            else:
                return True, command
        except Exception as e:
            return False, None

    def processCommand(self, msg):
        success, result = self.parseResponseMessage(msg)
        print(result)
        if success:
            command = self.commands.get(result['requestid'].strip(), None)
            if (command != None):
                command['status'] = result['status']
                command['code'] = result['code']
                command['detail'] = result['detail']
                if not (result['data'] is None):
                    command['data'] = result['data']
                self.commands[command['requestid']] = command
                return success_str()
            else:
                return error_str(10009, "", None, result['requestid'])
        else:
            return error_str(10010)


class Devices():

    def __init__(self):
        self.Tokenlist = dict()
        self.Devicelist = dict()
        self.commands = Commands()
        self.commands.load()

    def hasByToken(self, token):
        return token in self.Tokenlist

    def hasByDeviceid(self, deviceid):
        return deviceid in self.Devicelist

    def deleteByToken(self, token):
        device = self.Tokenlist.get(token, None)
        if (device != None):
            self.Devicelist.pop(device.id)
        return self.Tokenlist.pop(token)

    def deleteByDeviceid(self, deviceid):
        device = self.Devicelist.get(deviceid, None)
        if (device != None):
            self.Tokenlist.pop(device.token)
        return self.Devicelist.pop(deviceid)

    def deleteAndCloseByToken(self, token, msg):
        device = self.Tokenlist.get(token, None)
        if (device != None):
            device.ws.send(msg)
            device.ws.close()
            self.deleteByToken(token)
        return token

    def add(self, id, token, language, ws):
        device = Device(id, language, token, ws)
        self.Tokenlist[token] = device
        self.Devicelist[id] = device
        return True

    def checkDataIsNull(self, data):
        if (data == None or data == ''):
            return {}
        else:
            return data

    def AddToData(self, data, value, url):
        if (data == None):
            data = {}
        if (url == 'black_list'):
            data['uniqueid'] = value
        else:
            data['id'] = int(value)
        return data

    def queryStringIdToData(self, data, query, id, url):
        if len(query) == 0:
            # node (id != null)
            if (id != None):
                data = self.AddToData(data, id, url)
            return data
        else:
            data = self.checkDataIsNull(data)
            if (id != None) or (id != ''):
                data = self.AddToData(data, id, url)
                for param in query:
                    data[param] = query[param]
            return data

    def validate_schema(self, command, data):
        if (command['json_schema'] != None):
            if (len(data) == 0):
                return {'valid': False, 'error': "Body must have a value"}
            else:
                return SchemaValidate(data, command['json_schema'])
        else:
            return {'valid': True, 'error': ""}

    def addCommandToList(self, http_method, url, deviceid, query, data, id):
        command = self.commands.getCommandEx(url, http_method, id, data)
        if (command != None):
            device = self.Devicelist.get(deviceid, None)
            if (device != None):
                command_data = self.queryStringIdToData(data, query, id, url)
                vs = self.validate_schema(command, command_data)
                if vs['valid']:
                    return device.addCommand(command['method_name'], command_data)
                else:
                    return error(10013, "", vs['error'])
            else:
                return error(10006)
        else:
            return error(10012)

    def processCommand(self, token, msg):
        device = self.Tokenlist.get(token, None)
        if (device != None):
            return device.processCommand(msg)
        else:
            return error_str(10008, "Token not Found in Device List", {'token': token})


devices = Devices()
