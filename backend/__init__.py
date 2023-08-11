from flask import Flask, request ,render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from flask_login import LoginManager

db =SQLAlchemy()

def create_app():

    app = Flask(__name__)    
    app.config.from_object("backend.config.Config")
    db.init_app(app)
    
    @app.route('/')
    @app.route('/logs', methods=['GET', 'POST'])
    def login():
        hello = {"name": "sam", "age": "12"}
        return hello

    return app
