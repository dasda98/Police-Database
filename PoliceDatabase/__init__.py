"""
The flask application package.
"""

from flask import Flask

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = ''
app.config['SECRET_KEY'] = 'secret'
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy(app)

from PoliceDatabase import views

