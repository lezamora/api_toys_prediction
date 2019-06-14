import os
from flask import Flask
from flask_bcrypt import Bcrypt
from werkzeug.contrib.fixers import ProxyFix

from .config import config_by_name

if not os.path.exists('logs'):
    os.makedirs('logs')


flask_bcrypt = Bcrypt()


def create_app(config_name):
    app = Flask(__name__)
    app.wsgi_app = ProxyFix(app.wsgi_app)
    app.config.from_object(config_by_name[config_name])
    flask_bcrypt.init_app(app)

    return app
