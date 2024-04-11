# contains main configurations of the application

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

# CORS - Cross Origin Request
# sends request to the backend from the different url

app = Flask(__name__)
CORS(app)  # to eliminate CORS error

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///mydatabase.db"
# specify  the location of the local Sqlite database that we are storing on the machine
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
# tracking the modifications to the DB is set False

db = SQLAlchemy(app) 
# instance of DB to accesss the database object








