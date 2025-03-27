from auth.signup import signUpUser
from flask import Flask, request, jsonify, send_file

app = Flask(__name__)



@app.route('/signup', methods='POST')
def createUser():
    signUpUser(request=request)
