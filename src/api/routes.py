"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
from flask import Flask, request, jsonify, url_for, Blueprint
from api.models import db, User
from api.utils import generate_sitemap, APIException
from flask_cors import CORS

api = Blueprint('api', __name__)

# Allow CORS requests to this API
CORS(api)


@api.route('/hello', methods=['POST', 'GET'])
def handle_hello():

    response_body = {
        "message": "Hello! I'm a message that came from the backend, check the network tab on the google inspector and you will see the GET request"
    }

    return jsonify(response_body), 200

@api.route('/sign_up', methods=['POST'])
def handle_sign_up():

    body = request.json
    new_email = body["email"]
    new_password = body["password"]
    new_user = User(email = new_email, password = new_password)

    response_body = {
        "message": "New user successfully created!",
        "user": new_user.serialize()
    }
    db.session.add(new_user)
    db.session.commit()

    return jsonify(response_body), 200
