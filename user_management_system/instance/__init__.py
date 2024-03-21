from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_pymongo import PyMongo

app = Flask(__name__)


#postgres
app.config.from_pyfile('config.py')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)

#mongo
app.config['MONGO_DBNAME'] = 'turbine_management'
app.config['MONGO_URI'] = 'mongodb://localhost:27017/turbine_management'
app.config['SECRET_KEY'] = 'some-secret-string'

mongo = PyMongo(app)