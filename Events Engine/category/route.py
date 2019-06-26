'''
Created on Jun 19, 2019

@author: gautam.b
'''


from flask import Blueprint
import requests as req;
import json;
from utils.utilities import token_required

# Create a Blueprint Object
category = Blueprint('category', __name__);

@category.route('/category')
@token_required
def getCategories():
    msg = "In Categories Service";
    return json.dumps({"msg": msg});
    
    
    