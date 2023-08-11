
from flask import Blueprint, jsonify, json
from ..model import Users

api = Blueprint('api', __name__)

@api.route('/patients', methods=['GET'])
def getAllPatients():
    something = {"name": "patient1", "date":"dunno"}
    return something

@api.route('/users', methods=['GET'])
def getAllUsers():
    getAllUsers = Users.query.all()
    response = []
    for user in getAllUsers:
        response.append(user)
    
    return json.dumps(response);

@api.route('/users/<int:id>', methods=['GET'])
def getUserByID(id):
    getUser = Users.query.get(id)
    # response = {"user:" : getUser.usertype}
    response = jsonify(getUser.serialize())
    return response;   


    

# @api.route('/patients/<id>', methods=['GET'])
# def getAPatient(id):
#     pass

# @api.route('/users/<id>', methods=['GET'])
# def getAUser(id):
#     pass

# @api.route('/species', methods=['GET', 'POST'])
# def getAllSpecies():
#     pass