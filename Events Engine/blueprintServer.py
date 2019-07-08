from flask import Flask
from app.blueprints.city.route import city;
from app.blueprints.country.route import country;
from app.blueprints.category.route import category;
from app.blueprints.login.route import login;
from flask_cors import CORS;
from flask_mysqldb import MySQL
import os;
app = Flask(__name__)
CORS(app);

#Register Blue prints


app.register_blueprint(login);
app.register_blueprint(city);
app.register_blueprint(country);
app.register_blueprint(category);




# Read configuration file based on 


print ("Env ="+ app.config['ENV']);
configFile = "";

#Read the appropriate Config File
if app.config['ENV'] == "production":
    configFile = "./config/prodConfig.py";
else:
    configFile = "./config/devConfig.py";

app.config.from_pyfile(configFile);
app.secret_key = os.urandom(24);

mysql = MySQL(app);
# set the connection to pass it to blueprints
app.config["DB_CONN"] = mysql;


@app.route("/")
def index():
    return "Welcome to Events Engine"










if __name__ =="__main__":
        app.run();
        