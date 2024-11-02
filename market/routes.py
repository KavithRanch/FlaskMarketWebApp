from market import app
from flask import render_template
from market.models import Item

# Route URLs for home page
@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')  # Pointing to the html home page


@app.route('/market')
def market_page():
    items = Item.query.all()
    return render_template('market.html', items=items)  # Pointing to the market home page
