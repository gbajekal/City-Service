'''
Created on 20-Jun-2019

@author: GAUTAM
'''

from flask import Blueprint, jsonify, request, make_response
import jwt;


secretKey ="gingerIsAGoodBoy";
def token_required(f):
    def validateToken(*args, **kwargs):
        token = request.args.get("token");
        if not token:
            return jsonify({'msg':"Token missing"});
        try:
            data = jwt.decode(token, secretKey);
        except:
                return jsonify({"message": "Token Invalid"});
        return f(*args, **kwargs);
    
    return validateToken;