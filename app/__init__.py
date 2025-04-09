# app/__init__.py
from flask import Flask
from .routes import main

def create_app():
    app = Flask(__name__)
    app.secret_key = "safesathi_secret_key"
    app.register_blueprint(main)
    return app
