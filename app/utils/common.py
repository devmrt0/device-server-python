import json
from types import NoneType


def isEmptyValue(val):
    if type(val) == NoneType or val is None:
        return True
    else:
        return False


def isEmptyString(val):
    if (type(val) == str and (val == "" or val == '')):
        return True
    else:
        return False


def isEmpty(val):
    if isEmptyValue(val) == True or isEmptyString(val) == True:
        return True
    else:
        return False


def JSONstringify(val):
    return json.dumps(val, separators=(',', ':'))
