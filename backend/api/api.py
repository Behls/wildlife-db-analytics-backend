from flask import Blueprint


api = Blueprint('api', __name__)

@api.route('/patients', methods=['GET'])
def getAllPatients():
    something = {"name": "patient1", "date":"dunno"}
    return something

# @api.route('/users', methods=['GET'])
# def getAllUsers():
#     pass

# @api.route('/patients/<id>', methods=['GET'])
# def getAPatient(id):
#     pass

# @api.route('/users/<id>', methods=['GET'])
# def getAUser(id):
#     pass

# @api.route('/species', methods=['GET', 'POST'])
# def getAllSpecies():
#     pass