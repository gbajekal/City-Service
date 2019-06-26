from flask import Flask
from city.route import city;
from country.route import country;
from category.route import category;
from login.route import login;
from flask_cors import CORS;
from flask_mysqldb import MySQL
app = Flask(__name__)
CORS(app);

# Add Database Configuration
app.config["MYSQL_HOST"] = "127.0.0.1"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = ""
app.config["MYSQL_DB"] = "test"

mysql = MySQL(app);
app.config["DB_CONN"] = mysql;


app.register_blueprint(login);
app.register_blueprint(city);
app.register_blueprint(country);
app.register_blueprint(category);







if __name__ =="__main__":
        app.run();
        