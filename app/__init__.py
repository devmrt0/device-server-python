from flask import Flask

# Init the Flask module
app = Flask(__name__)

# app configurations
app.config['SECRET_KEY'] = 'hebelehubele'
app.config['SOCK_SERVER_OPTIONS'] = {'ping_interval': 25}

# Init Sieve module for form validations
# Sieve(app)

# Register APIs
from app.routes.AuthRoutes import auth_api
app.register_blueprint(auth_api)
from app.routes.deviceRoutes import device_api
app.register_blueprint(device_api)
from app.routes.deviceUserRoutes import deviceUser_api
app.register_blueprint(deviceUser_api)
from app.routes.screenRoutes import screen_api
app.register_blueprint(screen_api)
from app.routes.verifyRoutes import verify_api
app.register_blueprint(verify_api)


# Register ws
#flask_sock
from app.routes.wsRoutes import sock
sock.init_app(app)
