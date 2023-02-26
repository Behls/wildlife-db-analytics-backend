from flask import Flask, request ,render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from flask_login import LoginManager

db =SQLAlchemy()

def create_app():

    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'sam' 
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
    # app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    # app.config['MYSQL_HOST'] = 'comp-server.uhi.ac.uk'
    # app.config['MYSQL_USER'] = 'pe19016467'
    # app.config['MYSQL_PASSWORD'] = 'alannazimbehl'
    # app.config['MYSQL_DB'] = 'pe19016467'
    engine = create_engine('sqlite:///db.sqlite')
    session = Session(bind=engine)
    
    db.init_app(app)

    @app.route('/')
    @app.route('/login')
    def home():
        return render_template('index.html', title='Login Page')

    return app
