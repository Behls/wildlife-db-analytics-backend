from flask import Blueprint
from flask import render_template, request, url_for, render_template, redirect, flash, session, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from ..model import Users
from backend import db
from datetime import datetime, timedelta, timezone

auth = Blueprint("auth", __name__)

@auth.route('/login', methods=['POST', 'GET'])
def login():

    # email = request.json.get("email", None)
    # password = request.json.get("password", None)

    email="smith@test.com"
    password="pass123"

    getUser = Users.query.filter_by(email=email).first()
    
    if not getUser or not getUser.checkPassword(password):
        response ={
            "msg": "Wrong email or password",
            "status": "user_not_found"
        }
        return response
    else:
        response = {
                    "status":"user_found",
                    "usertype": getUser.usertype,
                    "firstname": getUser.firstname,
                    "surname": getUser.surname,
                    "email": getUser.email,
                    "address": getUser.address,
                    "contact": getUser.contact
        }
        return response
    
@auth.route("/logout", methods=["POST"])
def logout():
    response = jsonify({"status": "user_logout"})
    return response