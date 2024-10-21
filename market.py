from flask import Flask  # Importing Flask instance from flask package
app = Flask(__name__)  # Initializing Flask instance with parameter __name__ (


# Route URL for home page
@app.route('/')  # Decorator is where this function's content will appear
def hello_world():  # Function which is used to display data on homepage
    return 'Hello, World!'
