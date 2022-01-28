from flask import Flask
from config import config_options
from .main import main as main_blueprint


def create_app(config_name):

    app = Flask(__name__)

    # Creating the app configurations
    app.config.from_object(config_options[config_name])

    # register blueprint
    app.register_blueprint(main_blueprint)


    # Will add the views and forms

    return app