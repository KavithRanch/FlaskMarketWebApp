from market import app, db
from flask import render_template, redirect, url_for
from market.models import Item, User
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

@app.route('/register', methods=['GET', 'POST'])
def register_page():
    form = RegisterForm()
    if form.validate_on_submit():
        user_to_create = User(username=form.username.data,
                              email=form.email_address.data,
                              password_hash=form.password.data)
        db.session.add(user_to_create)
        db.session.commit()
        return redirect(url_for('market_page'))

    # Checking is there are errors in validations
    if form.errors != {}:
        for err_msg in form.errors.values():
            print(f'There was an error with creating a user: {err_msg}')
    return render_template('register.html', form=form)