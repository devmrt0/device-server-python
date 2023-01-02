from app.utils.common import isEmpty, JSONstringify
from app.utils.wstoken import getTokenWs, verifyTokenWs
from app.models.deviceModels import devices


def OnConnect(ws, query_token, header_token):
    try:
        result = verifyTokenWs(getTokenWs(
            query_token, header_token))
        token = result.get('data').get('token')
        if result.get('status', -1) == -1:
            if not isEmpty(token):
                devices.deleteByToken(token)
            ws.send(JSONstringify(result))
            ws.close()
        else:
            deviceid = result.get('data').get('deviceid')
            language = result.get('data').get('language')
            if devices.hasByToken(token):
                devices.deleteAndCloseByToken(token, JSONstringify(
                    {'status': -1, 'code': 10004, 'detail': "başka bir cihaz bağlanmaya çalıştığı için bağlantı kapatıldı.", 'data': {'deviceid': deviceid, 'language': language, 'token': token}}))
                print("WebSocket disconnetcted for decice already connected")
            else:
                devices.add(deviceid, token, language, ws)
                ws.send(JSONstringify(result))
                print("WebSocket connetcted()")
    except Exception as e:
        print(str(e))


def OnMessage(ws, query_token, header_token, data):
    try:
        token = getTokenWs(query_token, header_token)
        result = verifyTokenWs(token)
        if result.get('status', -1) == -1:
            if not isEmpty(token):
                devices.deleteByToken(token)
            ws.send(JSONstringify(result))
            ws.close()
        else:
            ws.send(devices.processCommand(token, data))
    except Exception as e:
        print(str(e))


def OnDisconnect(ws, query_token, header_token):
    try:
        token = getTokenWs(query_token, header_token)
        devices.deleteByToken(token)
        print("WebSocket was closed()")
    except Exception as e:
        print(str(e))
