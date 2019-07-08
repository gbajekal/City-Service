'''
Created on 20-Jun-2019
This module handles the login services for Event Engine
On a successful login, it generates a token that is
mandatory to access other services

@author: GAUTAM
'''

from flask import Blueprint, jsonify, request, make_response,session
import json;
import jwt;
import datetime;
from app.utils import utilities;

# Create a Blueprint Object
login = Blueprint('login', __name__);
secretKey = utilities.secretKey;
@login.route('/login')
def loginUser():
    msg = "In login Service";
    auth = request.authorization;
    if auth and auth.password == "password":
        token = jwt.encode({'user':auth.username,'exp':datetime.datetime.utcnow() + datetime.timedelta(minutes=2)}, secretKey);
        session["username"] = auth.username;
        return jsonify({'token':token.decode('UTF-8')})
    return make_response("Could not verify", 401, {'WWW-Authenticate':'Basic Realm="Login Required"'});

@login.route('/unprotected')
def unprotected():
    return jsonify({"msg": "Anyone can access"});

@login.route('/protected')
@utilities.token_required
def protected():
    return jsonify({"msg": "Access only with Token"});
