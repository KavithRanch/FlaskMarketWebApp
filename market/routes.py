from market import app
from flask import render_template
from market.models import Item
from market.forms import RegisterForm


# Route URLs for home page
@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')  # Pointing to the html home page


@app.route('/market')
def market_page():
    items = Item.query.all()
    return render_template('market.html', items=items)  # Pointing to the market home page

@app.route('/register')
def register_page():
    form = RegisterForm()
    return render_template('register.html', form=form)