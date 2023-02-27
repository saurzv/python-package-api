from flask import Flask
from os.path import join, dirname
from api.main.routes import main
from dotenv import load_dotenv

dotenv = join(dirname(__file__), '.env')
load_dotenv(dotenv)


def create_app():
    api = Flask(__name__)
    api.register_blueprint(main)
    return api
