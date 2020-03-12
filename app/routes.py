#render_template = Renders template and according arguments (e.g Name of person)
#Uses Jinja2 for substitution of {{...}}

from flask import render_template
from app import app

#Decorators which invoke the function when called.
@app.route('/')
@app.route('/index')

def index():
    #Fake user to greet. 
    user = {'username': 'Miguel'}
    #Returns template from /templates
    return render_template('index.html', title='Home', user=user)

