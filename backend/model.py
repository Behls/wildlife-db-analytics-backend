from flask_login import UserMixin
from sqlalchemy import Column, Integer, ForeignKey, String, Float
from sqlalchemy.orm import relationship
from sqlalchemy.sql.expression import false, null
from sqlalchemy.sql import func
from sqlalchemy.ext.declarative import declarative_base
from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash
from . import db

class User(UserMixin, db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    usertype = db.Column(db.String(255))
    firstname = db.Column(db.String(255))
    surname = db.Column(db.String(255))
    email = db.Column(db.String(255), nullable=False)
    address = db.Column(db.String(255))
    password_hash = db.Column(db.String(255))
    contact = db.Column(db.String(255))
    user = db.relationship('User', backref='user')

    def checkPassword(self, password):
       return check_password_hash(self.password_hash, password)

    def setPassword(self, password):
        self.password_hash = generate_password_hash(password)

class Medicine(db.Model):
    __tablename__ = 'medicine'

    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    medication_name = db.Column(db.String(255))
    dosage = db.Column(db.Integer())
    medicine = db.relationship('Medicine', backref='medicine')

class Donation(db.Model):
    __tablename__ = 'donation'

    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    type = db.Column(db.String(255))
    amount = db.Column(db.Float())
    date = db.Column(db.DateTime(), server_default=func.now())

class Notes(db.Model):
    __tablename__ = 'notes'

    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    note = db.Column(db.String(255))
    date_added = db.Column(db.DateTime(), nullable=False, server_default=func.now())
    added_by = db.Column(db.Integer(), db.ForeignKey('user.id'))


class Patient(db.Model):
    __tablename__ = 'patient'

    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    type = db.Column(db.String(255))
    name = db.Column(db.String(255))
    weight = db.Column(db.Float())
    status = db.Column(db.String(255), nullable=False)
    admitted = db.Column(db.DateTime(), nullable=False, server_default=func.now())
    # discharge = db.Column(db.DateTime(), server_default=func.now())
    patient = db.relationship('Patient', backref='patient')


class Treatment(db.Model):
    __tablename__ = 'treatment'

    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    future_treatment = db.Column(db.String(255), nullable=False)
    current_treatment = db.Column(db.String(255), nullable=False)
    patient_id = db.Column(db.Integer(), db.ForeignKey('patient.id'))
    medication_id = db.Column(db.Integer(), db.ForeignKey('medicine.id'))
    created_by = db.Column(db.Integer(), db.ForeignKey('user.id'))
    note_id = db.Column(db.Integer(), db.ForeignKey('note.id'))

class Species(db.Model):
    __tablename__ = 'species'

    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), nullable=False)
    type = db.Column(db.String(255), nullable=False)
