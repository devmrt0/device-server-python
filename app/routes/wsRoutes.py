from flask import request
from flask_sock import Sock, ConnectionClosed
from app.controllers.wsController import OnConnect, OnMessage, OnDisconnect

sock = Sock()


@sock.route('/')
def device_command_fws(ws):
    OnConnect(ws, request.args.get('token'), request.headers.get('token'))
    while True:
        try:
            data = ws.receive()
            OnMessage(ws, request.args.get('token'),
                      request.headers.get('token'), data)
        except ConnectionClosed:
            OnDisconnect(ws, request.args.get('token'),
                         request.headers.get('token'))
            break
