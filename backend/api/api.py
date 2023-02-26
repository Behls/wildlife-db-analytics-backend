from flask import Blueprint

api = Blueprint('api', __name__)

@api.route('/api/patients', methods=['GET'])
def getAllPatients():
    pass

@api.route('/api/users', methods=['GET'])
def getAllUsers():
    pass

@api.route('/api/patients/<id>', methods=['GET'])
def getAllPatients(id):
    pass

@api.route('/api/users/<id>', methods=['GET'])
def getAllUsers(id):
    pass