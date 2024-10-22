# FlaskMarketWebApp
**_Learning Flask through creating a market web app_**

Learning Material: https://youtu.be/Qr4QMBUPxWo?si=uhDPh79dkLB_iInH

## Notes:
### Setup
Flask start code: flask.palletsprojects.com/en/1.1x/quickstart

### Running Program

```commandline
# Setting python file as Flask App to run
set FLASK_APP=market.py

# Sets debug mode on
# Changes can be made and seen without restarting App
# Once deployed, turn it off
set FLASK_DEBUG=1

# Runs app
python -m flask run
```

### Frontend Code
Bootstrap start code: https://getbootstrap.com/docs/5.0/getting-started/introduction/
```html
<!--Jinja used for dynamic content generation-->
{{ ... }} <!--Displaying variables or simple expressions (using | "pipe" symbol)-->
{% ... %} <!--Loops and Conditionals-->
{% end... %}
```

### Backend Code

```python
# Basic API route
@app.route("/path")
def function():
    return val

# Dynamic API route changing value on screen with path input
@app.route('/about/<username>')
def about_page(username):
     return f'<h1>This is the about page of {username}</h1>'

# Rendering html page
@app.route('/home')
def hello_world():
    return render_template('home.html')

# Rendering html page + passing through arguments to be displayed
@app.route('/home')
def hello_world():
    items = ["1", "2", "3"]
    return render_template('home.html', items=items)
```
