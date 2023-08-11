from flask_login import UserMixin
from sqlalchemy import Column, Integer, ForeignKey, String, Float
from sqlalchemy.orm import relationship
from sqlalchemy.sql.expression import false, null
from sqlalchemy.sql import func
from sqlalchemy.ext.declarative import declarative_base
from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash
from . import db
from dataclasses import dataclass

@dataclass
class Users(UserMixin, db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    usertype = db.Column(db.String(255))
    firstname = db.Column(db.String(255))
    surname = db.Column(db.String(255))
    email = db.Column(db.String(255), nullable=False)
    address = db.Column(db.String(255))
    password_hash = db.Column(db.String(255))
    contact = db.Column(db.String(255))
    organisation = db.Column(db.String(255))
    treatment = db.relationship('Treatment', backref='users')
    treatment_id = db.Column(db.Integer(), db.ForeignKey('treatment.id'))
    notes = db.relationship('Notes', backref='notes')
    notes_id = db.Column(db.Integer(), db.ForeignKey('notes.id'))
    

    def __init__(self):
        db.create_all()

    def checkPassword(self, password):
       return check_password_hash(self.password_hash, password)

    def setPassword(self, password):
        self.password_hash = generate_password_hash(password)
    
    def __repr__(self):
        return f"id={self.id}, usertype={self.usertype}, firstname={self.firstname}, lastname={self.surname}, email={self.email}, address={self.address}, contact={self.contact}"

    def serialize(self):
        return {"id": self.id,
                "usertype": self.usertype,
                "firstname": self.firstname,
                "lastname": self.surname,
                "organisation": self.organisation,
                "email": self.email,
                "address": self.address,
                "contact": self.contact
                }
@dataclass    
class Donation(db.Model):
    __tablename__ = 'donations'
    
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    type = db.Column(db.String(255))
    amount = db.Column(db.Float())
    date = db.Column(db.DateTime(), server_default=func.now())

    def serialize(self):
        return {"id": self.id,
                "type": self.type,
                "amount": self.amount,
                "date": self.date,
                }

@dataclass
class Medicine(db.Model):
    __tablename__ = 'medicine'

    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    medication_name = db.Column(db.String(255))
    dosage = db.Column(db.Integer())
    treatment = db.relationship('Treatment', backref='medicine')
    treatment_id = db.Column(db.Integer(), db.ForeignKey('treatment.id'))
    
    def serialize(self):
        return {"id": self.id,
                "medication_name": self.medication_name,
                "dosage": self.dosage,
        }

@dataclass
class Notes(db.Model):
    __tablename__ = 'notes'

    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    note = db.Column(db.String(255))
    date_added = db.Column(db.DateTime(), nullable=False, server_default=func.now())
    added_by = db.Column(db.Integer(), db.ForeignKey('user.id'))
    treatment = db.relationship('Treatment', backref='notes')
    
    def serialize(self):
        return {"id": self.id,
                "note": self.note,
                "date_added": self.date_added,
                "added_by": self.added_by
    }

@dataclass
class Patient(db.Model):
    __tablename__ = 'patients'


    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    species_id = db.Column(db.Integer(), db.ForeignKey('species.id'))
    name = db.Column(db.String(255))
    weight = db.Column(db.Float())
    status = db.Column(db.String(255), nullable=False)
    admitted = db.Column(db.DateTime(), nullable=False, server_default=func.now())
    discharge = db.Column(db.String(255))
    firstname = db.Column(db.String(255))
    surname = db.Column(db.String(255))
    email = db.Column(db.String(255), nullable=False)
    address = db.Column(db.String(255))
    contact = db.Column(db.String(255))
    postcode = db.Column(db.String(255))
    city = db.Column(db.String(255))
    organisation = db.Column(db.String(255))
    rescue_note = db.Column(db.String(255))
    treatment = db.relationship('Treatment', backref='patient')
    

    def serialize(self):
            return {"id": self.id,
                    "species_id": self.species_id,
                    "name": self.name,
                    "weight": self.weight,
                    "status": self.status,
                    "admitted": self.admitted,
                    "discharged": self.discharge,
                    "firstname": self.firstname,
                    "surname": self.surname,
                    "email": self.email,
                    "address": self.address,
                    "contact": self.contact,
                    "postcode": self.postcode,
                    "city": self.city,
                    "recue_note": self.rescue_note
            }


@dataclass
class Species(db.Model):
    __tablename__ = 'species'
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), nullable=False)
    type = db.Column(db.String(255), nullable=False)

    def __init__(self, name, type):
        self.name = name
        self.type = type

    def serialize(self):
            return {"id": self.id,
                    "name": self.name,
                    "type": self.type
            }


@dataclass
class Treatment(db.Model):

    __tablename__ = 'treatments'

    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    future_treatment = db.Column(db.String(255), nullable=False)
    current_treatment = db.Column(db.String(255), nullable=False)
    patient_id = db.Column(db.Integer(), db.ForeignKey('patients.id'))
    medication_id = db.Column(db.Integer(), db.ForeignKey('medicine.id'))
    created_by = db.Column(db.Integer(), db.ForeignKey('users.id'))
    note_id = db.Column(db.Integer(), db.ForeignKey('notes.id'))

    def serialize(self):
            return {"id": self.id,
                    "future_treatment": self.future_treatment,
                    "current_treatment": self.current_treatment,
                    "patient_id": self.patient_id,
                    "medication_id": self.medication_id,
                    "created_by": self.created_by,
                    "note_id": self.note_id,
                }