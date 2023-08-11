from flask import Flask, request, jsonify, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import json
from datetime import datetime, timedelta, timezone

db =SQLAlchemy()

def create_app():

    app = Flask(__name__)    
    app.config.from_object("backend.config.Config")
    db.init_app(app)
    
    @app.route('/')
    @app.route('/logs', methods=['GET', 'POST'])
    def home():
        return redirect(url_for('auth.login'))
    
    from backend.api.api import api 
    app.register_blueprint(api, url_prefix='/api')

    from backend.auth.auth import auth 
    app.register_blueprint(auth, url_prefix='/')

    return app
