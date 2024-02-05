from flask import request, jsonify
from db_service import View,Delete,Update

 
def view():
    context = dict(request.args)
    table_name='books'
    result = View(table_name ,context)
    return jsonify(result)

def delete():
    context = dict(request.args)
    table_name='books'
    result = Delete(table_name,context)
    return result
    
def update():
    context = dict(request.args)
    table_name='books'
    result = Update(table_name,context)
    return jsonify(result)

    


