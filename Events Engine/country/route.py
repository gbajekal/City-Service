'''
Created on Jun 19, 2019

Description: This module is a REST service to do CRUD operations on City Entity
for both EventsNow and MeraEvents.

@author: gautam.b
'''

from flask import Blueprint
import json;
from utils.utilities import token_required


# Create a Blueprint Object
country = Blueprint('country', __name__);

@country.route('/country/')
@token_required
def getCountries():
    msg = "In Country Service";
    return json.dumps({"msg": msg});
    
    