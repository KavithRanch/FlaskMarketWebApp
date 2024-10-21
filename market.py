from flask import Flask, render_template  # Importing Flask instance from flask package
app = Flask(__name__)  # Initializing Flask instance with parameter __name__ (


# # Route URL for home page
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
def hello_world():
    return render_template('home.html')  # Pointing to the html home page
