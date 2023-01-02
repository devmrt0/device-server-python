import jwt
from app import app
from app.utils.common import isEmpty
from app.utils.api_response import *


def getTokenWs(queryToken, headersToken):
    token = ""
    if not isEmpty(queryToken):
        token = queryToken
    else:
        if not isEmpty(headersToken):
            token = headersToken
    return token


def verifyTokenWs(token):
    if (token == ""):
        return error(10001, "", {'token': token})
    try:
        decoded = jwt.decode(token, app.config['SECRET_KEY'], algorithms=[
                             'RS256',], options={"verify_signature": False})
        deviceid = decoded.get('deviceid')
        language = decoded.get('language')
        return success({'deviceid': deviceid, 'language': language, 'token': token})
    except (RuntimeError, TypeError, NameError, ValueError) as err:
        if (err):
            if (err == 'TokenExpiredError'):
                return error(10002, "", {'token': token})
            else:
                return error(10003, "", {'token': token})
