'''
Created on Jun 19, 2019

Description: This module is a REST service to do CRUD operations on City Entity
for both EventsNow and MeraEvents.

@author: gautam.b
'''
from flask import Blueprint, jsonify, request
import json;
from utils import utilities;
from flask import current_app as app;
from flask_mysqldb import MySQL;
from mysql.connector import MySQLConnection, Error
from utils.utilities import token_required

# Create a Blueprint Object
city = Blueprint('city', __name__);



#****************************************************
# Checks whether it is a Get listing or addition
# via forms
#****************************************************

@city.route('/city', methods=["GET", "POST"])
@token_required
def cityHandler1():
    if request.method == "GET":
        return getCities();
    else:
        return setCity();

@city.route('/city/<cityName>', methods=["PUT", "DELETE"])
@token_required
def cityHandler2(cityName):
    if request.method == "DELETE":
        return deleteCity(cityName)
    else:
        return updateCity(cityName);


def getCities():
    msg = "In City Service";
    try:
        cityList = [];
        mysql = app.config["DB_CONN"];
        cur = mysql.connection.cursor();
        cur.execute('''Select name from city''');
        
        
        while True:
            row = cur.fetchone();
            if row == None:
                break;
            cityList.append(row[0]);
            msg = jsonify({"cityList":cityList});
        
        
    except Error as e :
        msg = jsonify({"msg":"Error in fetching cities"})

    finally:
        cur.close();
        return msg;
    
    
#***********************************************
# addCity() - The Add city method, adds a city 
# to the database
# The city to add is given in the city parameter
#***********************************************
#@city.route("/city/<cityName>", methods=["POST"])
def setCity():
    msg = "In setCity";
    try:
        #Retrieve the request parameters
        cityName = request.form["cityName"];
        
        print("In setCity() with city = " + cityName )
        
        
        mysql = app.config["DB_CONN"];
        cur = mysql.connection.cursor();
        query = 'INSERT INTO city (name) VALUES ("%s")' %(cityName);
        cur.execute(query);
        mysql.connection.commit();
        msg = jsonify({"msg": "City " + cityName + " added"});
    except Error as e:
        msg = jsonify({"msg": "Error in adding city "+ cityName });
    finally:
        cur.close();
        return msg;
        
    
#***********************************************
# deleteCity() - The Delete city method, deletes a city 
# from the database
# The city to delete is given in the city parameter
#***********************************************
def deleteCity(cityName):
    msg = "In deleteCity";
    try:
        #Retrieve the request parameters
            
        print("In deleteCity() with city = " + cityName )
        
        
        mysql = app.config["DB_CONN"];
        cur = mysql.connection.cursor();
        query = 'DELETE FROM city where name = ("%s")' %(cityName);
        cur.execute(query);
        mysql.connection.commit();
        msg = jsonify({"msg": "City " + cityName + " deleted"});
    except Error as e:
        msg = jsonify({"msg": "Error in adding city "+ cityName });
    finally:
        cur.close();
        return msg;
    
    
#***********************************************
# updateCity() - The update city method, updates a city 
# in database by toggling the case
# The city to update is given in the city parameter
#***********************************************
def updateCity(cityName):
    msg = "In updateCity";
    try:
        #Retrieve the request parameters
            
        print("In updateCity() with city = " + cityName )
        
        if cityName.isupper() == True:
            newName = cityName.lower();
        else:
            newName = cityName.upper();
        
        
        mysql = app.config["DB_CONN"];
        cur = mysql.connection.cursor();
        query = 'UPDATE city SET name = ("%s") where name =("%s")' %(newName, cityName);
        cur.execute(query);
        mysql.connection.commit();
        msg = jsonify({"msg": "City " + cityName + " updated"});
    except Error as e:
        msg = jsonify({"msg": "Error in adding city "+ cityName });
    finally:
        cur.close();
        return msg;