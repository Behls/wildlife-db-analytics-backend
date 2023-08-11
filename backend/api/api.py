
from flask import Blueprint, jsonify, json
from ..model import Users, Species, Donation, Patient, Notes, Treatment, Medicine   

api = Blueprint('api', __name__)

@api.route('/users', methods=['GET'])
def getAllUsers():
    getAllUsers = Users.query.all()
    data = []
    response = ""
    if(getAllUsers):
        for user in getAllUsers:
            response = user.serialize()
            data.append(response)
            alist = jsonify(data)
        return alist
    else:
        response = {"users": "no_users_found"}
        return response

@api.route('/users/<int:id>', methods=['GET'])
def getUserByID(id):
    getUser = Users.query.get(id)
    if(getUser):
        response = jsonify(getUser.serialize())
        return response;   
    else:
        response = {"user": "user_not_found"}
        return response


@api.route('/patients/<int:id>', methods=['GET'])
def getPatientByID(id):
    getPatient = Patient.query.get(id)
    if(getPatient):
        response = jsonify(getPatient.serialize())
        return response;
    else:
        response = {"patient": "patient_not_found"}
        return response
    
@api.route('/patients', methods=['GET'])
def getAllPatients():
    getAllPatients = Patient.query.all()
    data = []
    response = ""
    if(getAllPatients):
        for patient in getAllPatients:
            response = patient.serialize()
            data.append(response)
            alist = jsonify(data)
        return alist
    else:
        response = {"users": "no_patients_found"}
        return response

@api.route('/species', methods=['GET'])
def getAllSpecies():
    getAllSpecies = Species.query.all()
    data = []
    response = ""
    if(getAllSpecies):
        for species in getAllSpecies:
            response = species.serialize()
            data.append(response)
            alist = jsonify(data)
        return alist
    else:
        response = {"species": "no_species_data_found"}
        return response

@api.route('/species/<int:id>', methods=['GET'])
def getSpeciesByID(id):
    getspecies = Species.query.get(id)
    if(getspecies):
        response = jsonify(getspecies.serialize())
        return response
    else:
        response = {"species": "species_not_found"}
        return response

@api.route('/treatment/<int:id>', methods=['GET'])
def getTreatmentByID(id):
    getTreatment = Treatment.query.get(id)
    if(getTreatment):
        response = jsonify(getTreatment.serialize())
        return response
    else:
        response = {"treatments": "treatments_not_found"}
        return response
    

@api.route('/treatments', methods=['GET'])
def getAllTreatments():
    getAllTreatments = Treatment.query.all()
    data = []
    response = ""
    if(getAllTreatments):
        for treatment in getAllTreatments:
            response = treatment.serialize()
            data.append(response)
            alist = jsonify(data)
        return alist
    else:
        response = {"treatments": "no_treatments_data_found"}
        return response
    
@api.route('/donation/<int:id>', methods=['GET'])
def getDonationsByID(id):
    getDonations = Donation.query.get(id)
    if(getDonations):
        response = jsonify(getDonations.serialize())
        return response
    else:
        response = {"donations": "no_donations_not_found"}
        return response
    

@api.route('/donations', methods=['GET'])
def getAllDonations():
    getDonations = Donation.query.all()
    data = []
    response = ""
    if(getDonations):
        for donation in getDonations:
            response = donation.serialize()
            data.append(response)
            alist = jsonify(data)
        return alist
    else:
        response = {"donations": "no_donations_data_found"}
        return response
    
@api.route('/notes/<int:id>', methods=['GET'])
def getNotesByID(id):
    getNotes = Notes.query.get(id)
    if(getNotes):
        response = jsonify(getNotes.serialize())
        return response
    else:
        response = {"notes": "notes_not_found"}
        return response
    

@api.route('/notes', methods=['GET'])
def getAllNotes():
    getNotes = Notes.query.all()
    data = []
    response = ""
    if(getNotes):
        for note in getNotes:
            response = note.serialize()
            data.append(response)
            alist = jsonify(data)
        return alist
    else:
        response = {"notes": "notes_not_found"}
        return response