from flask import Blueprint
from service import View,Insert,Update,Delete

crud_blueprint = Blueprint('crud',__name__)

@crud_blueprint.route('/view', methods=['GET'])
def Get():
    data = View()
    return data

@crud_blueprint.route('/insert', methods=['POST'])
def Post():
    data = Insert()
    return data

@crud_blueprint.route('/update', methods=['PUT'])
def Updatee():
    data = Update()
    return data

@crud_blueprint.route('/delete', methods=['DELETE'])
def Del():
    data = Delete() 
    return data
