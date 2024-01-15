from flask import Flask 
from routes import crud_blueprint

app = Flask(__name__)

app.register_blueprint(crud_blueprint, url_prefix='/crud')

@app.route('/home')
def Homepage():
    return " Home Page! "

if __name__=='__main__':
    app.run(debug=True)
