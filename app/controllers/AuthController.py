from flask import jsonify, request, make_response
import jwt
from app import app
from datetime import datetime, timezone, timedelta
from app.utils.common import isEmpty
from app.models.deviceUserModels import deviceUsers


class AuthController():

    def getJWTClaims(self, request):
        deviceid = request.headers.get('jwtdeviceid')
        password = request.headers.get('jwtpassword')
        language = request.headers.get('jwtlanguage')
        if isEmpty(deviceid) and isEmpty(password) and isEmpty(language):
            if not request.is_json:
                return jsonify({'error': True})
            data = request.get_json()

            deviceid = data.get("jwtdeviceid")
            password = data.get("jwtpassword")
            language = data.get("jwtlanguage")
            if isEmpty(deviceid):
                return jsonify({'error': True})
            if isEmpty(password):
                return jsonify({'error': True})
            if isEmpty(language):
                return jsonify({'error': True})
            return jsonify({'error': False, 'deviceid': deviceid, 'password': password, 'language': language})
        else:
            if isEmpty(deviceid):
                return jsonify({'error': True})
            if isEmpty(password):
                return jsonify({'error': True})
            if isEmpty(language):
                return jsonify({'error': True})
            return jsonify({'error': False, 'deviceid': deviceid, 'password': password, 'language': language})

    def login(self):
        try:
            result = self.getJWTClaims(request).get_json()
            if result.get('error'):
                return make_response(jsonify({'message': 'deviceid,password,language required must be Header or Body'}), 401)
            auth = deviceUsers.authDevice(
                result.get('deviceid'), result.get('password'))
            if not auth:
                return make_response(jsonify({'message': 'Forbidden'}), 403)
            token = jwt.encode({
                'deviceid': result.get('deviceid'),
                'language': result.get('language'),
                "exp": datetime.now(tz=timezone.utc) + timedelta(seconds=30000),
                "iat": datetime.now(tz=timezone.utc)
            },
                app.config['SECRET_KEY'])
            return jsonify({'token': token})
        except Exception as e:
            return make_response(jsonify({'message': "Server Error. " + str(e)}), 500)
