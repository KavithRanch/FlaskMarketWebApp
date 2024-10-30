from flask import Flask, render_template  # Importing Flask instance from flask package
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)  # Initializing Flask instance with parameter __name__
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'  # Config so App recognizes its databse
db = SQLAlchemy(app) # Initializing DB

class Item(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=30), nullable=False, unique=True)
    price = db.Column(db.Integer(), nullable=False)
    barcode = db.Column(db.String(length=12), nullable=False, unique=True)
    description = db.Column(db.String(length=1024), nullable=False, unique=True)

    def __repr__(self):
        return f'Item {self.name}'
# Route URL for home page
# @app.route('/')  # Decorator is where this function's content will appear
# def hello_world():  # Function which is used to display data on homepage
#     return '<h1>Hello World</h1>'
#
#
# # Dynamic Route URL for about page for any user
# @app.route('/about/<username>')
# def about_page(username):
#     return f'<h1>This is the about page of {username}</h1>'

# Route URLs for home page
@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')  # Pointing to the html home page


@app.route('/market')
def market_page():
    items = Item.query.all()
    return render_template('market.html', items=items)  # Pointing to the market home page
