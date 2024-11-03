# Initializing market package
from flask import Flask, render_template  # Importing Flask instance from flask package
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)  # Initializing Flask instance with parameter __name__
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'  # Config so App recognizes its databse
db = SQLAlchemy(app) # Initializing DB

from market import routes
