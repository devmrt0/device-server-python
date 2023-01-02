import websocket
import json
import http.client

# Ayarları buradan yap
host = "localhost"
http_port = 8080
ws_port = 8080
deviceid = "IRT28123456"
password = "password"
language = "tr"
# Ayarları buradan yap

def cmd_get_device_info(requestid, req_data):
    resp = {}
    resp['status'] = 1
    resp['code'] = 0
    resp['detail'] = "OK"
    resp['requestid'] = requestid
    device_info = '{"model":"IRT28M","communication":{"rs232":1,"ethernet":true,"wifi":false},"SAM":false,"display":{"type":0},"keyboard":{"type":null},"audio":{"type":0},"outputs":{"relay":1,"MOSFET":1},"inputs":{"digitalinput":2}}'
    data = json.loads(device_info)
    resp['data'] = data
    return json.dumps(resp)


def on_message(ws, message):
    print(message)
    command = json.loads(message)
    if ("method" in command):
        if (command.get('method') == "get_device_info"):
            res = cmd_get_device_info(command.get('requestid'), command.get('command.data'))
        else:
            res = "Invalid Command"
        ws.send(res)


def on_error(ws, error):
    print(error)


def on_close(ws, close_status_code, close_msg):
    print("Disconnected")


def on_open(ws):
    print("Connected")

conn = http.client.HTTPConnection(host, http_port)
payload = ''
headers = {
    'jwtdeviceid': deviceid,
    'jwtpassword': password,
    'jwtlanguage': language
}
    
conn.request("POST", "/api/login", payload, headers)
res = conn.getresponse()
if res.status == 200:
    data = json.loads(res.read())
    print(data)
websocket.enableTrace(False)
ws = websocket.WebSocketApp("ws://" + host + ":" + str(ws_port) + "?token=" + data['token'],
                            on_open=on_open,
                            on_message=on_message,
                            on_error=on_error,
                            on_close=on_close)

ws.run_forever(reconnect=5)
