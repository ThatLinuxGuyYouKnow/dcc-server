from auth.signup import signUpUser
from flask import Flask, request, jsonify, send_file

app = Flask(__name__)



@app.route('/signup', methods=['POST'])
def createUser():
    status = signUpUser(request=request)
    if status == true:
        return jsonify({'Successful'}),200
    else:
        return jsonify({'error':status}),400
