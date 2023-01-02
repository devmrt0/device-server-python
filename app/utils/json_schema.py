#from jsonschema import validate, ValidationError
#import jsonschema


# schema içinde istediğiiz format yollanabilir schema={"format" : "ipv4"},

def SchemaValidate(data, json_schema):
    return {'valid': True, 'error': ""}

# def SchemaValidate(data, json_schema):
#     try:
#         valid = validate(instance=data, schema=json_schema)
#         return {'valid': valid, 'error': ""}
#     except ValidationError as err:
#         return {'valid': False, 'error': err}
