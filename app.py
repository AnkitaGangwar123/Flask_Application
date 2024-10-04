import os
from flask import Flask, request, send_file
from application.config import LocalDevelopmentConfig

app = None
api = None

def create_app():
    app = Flask(__name__, template_folder='templates')
    if os.getenv('ENV', "development") == "production":
        raise Exception("Currently no production config is setup")
    else:
        print("starting local development")
        app.config.from_object(LocalDevelopmentConfig)

    app.secret_key == "this_is_a_secretkey"
    app.app_context().push()
    return app, api 

app, api = create_app()

from application.controllers import *

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True, port=8085)