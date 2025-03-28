from auth.signup import signUpUser
from flask import Flask, request, jsonify, send_file
from flask_cors import CORS

app = Flask(__name__)

# Enable CORS for all routes
CORS(app)  # Allow all origins
# OR, to allow specific origins:


@app.route('/signup', methods=['POST'])
def createUser():
    status,data = signUpUser(request=request)
    if status:
        return jsonify({'message':'Successful','data':data}),200
    else:
        return jsonify({'error!':status}),400
