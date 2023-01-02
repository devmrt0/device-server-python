from app.utils.common import isEmpty, JSONstringify

errors = {10001: "Token must have a value for auth", 10002: "Expired", 10003: "Invalid Token", 10004: "Başka bir cihaz bağlanmaya çalıştığı için bağlantı kapatıldı",
          10005: "This device already connected.", 10006: "Cihaz bağlı olmadığı için komut cihaza gönderilemedi.", 10007: "no data found.", 10008: "Token Not Found in device list.", 10009: "Invalid requestid.", 10010: "Invalid device response.", 10011: "Command timeout response.", 10012: "invalid method.", 10013: "Schema Validaiton Error.", 10014: "Json body must have value.", 20015: "Dosya bulunamadı."
          }


def errlist():
    return "Listelendi"


def error(code, detail='', data=None, requestid=''):
    msg = ""
    if isEmpty(detail):
        msg = errors.get(code)
    else:
        msg = detail
    if not isEmpty(data):
        if not isEmpty(requestid):
            return {'status': -1, 'code': code, 'detail': msg, 'data': data, 'requestid': requestid}
        else:
            return {'status': -1, 'code': code, 'detail': msg, 'data': data}
    else:
        if not isEmpty(requestid):
            return {'status': -1, 'code': code, 'detail': msg, 'requestid': requestid}
        else:
            return {'status': -1, 'code': code, 'detail': msg}


def warning(code, detail=''):
    msg = ''
    if isEmpty(detail):
        msg = errors.get(code)
    else:
        msg = detail
    return {'status': 0, 'code': code, 'detail': detail}


def success(data=None, requestid=''):
    if not isEmpty(data):
        if not isEmpty(requestid):
            return {'status': 1, 'code': 0, 'detail': "OK", 'data': data, 'requestid': requestid}
        else:
            return {'status': 1, 'code': 0, 'detail': "OK", 'data': data}
    else:
        if not isEmpty(requestid):
            return {'status': 1, 'code': 0, 'detail': "OK",  'requestid': requestid}
        else:
            return {'status': 1, 'code': 0, 'detail': "OK"}


def error_str(code, detail='', data=None, requestid=''):
    return JSONstringify(error(code, detail, data, requestid))


def warning_str(code, detail=''):
    return JSONstringify(warning(code, detail))


def success_str(data, requestid=''):
    return JSONstringify(success(data, requestid))
