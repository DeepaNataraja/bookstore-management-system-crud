from flask import Blueprint
from service import View,Insert,Update,Delete

crud_blueprint = Blueprint('crud',__name__)

from flask import Blueprint
from Books.service import view,delete,update


crud_blueprint = Blueprint('crud',__name__)

@crud_blueprint.route('/view', methods=['GET'])

def Get():
    data = view()
    return data

# @crud_blueprint.add_url_rule(rule='/view',
#                           endpoint='view',
#                           view_func=View,
#                           methods=['GET'])

@crud_blueprint.route('/delete', methods=['DELETE'])
def Del():
    data = delete() 
    return data

@crud_blueprint.route('/update', methods=['PUT'])
def Updatee():
    data = update()
    return data

# @crud_blueprint.route('/insert', methods=['POST'])
# def Post():
#     data = Insert()
#     return data
