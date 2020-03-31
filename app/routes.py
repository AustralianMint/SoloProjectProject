#render_template = Renders template and according arguments (e.g Name of person)
#Uses Jinja2 for substitution of {{...}}

from flask import render_template
from app import app
from app.forms import LoginForm

#All decorators which invoke the function when called.
@app.route('/')
@app.route('/index')

#Define what methods are accepted.
@app.route('/login', methods=['GET', 'POST'])

def login():
    form = LoginForm()
    
    #Validate on submit does form heavy lifting
    if form.validate_on_submit():
        flash('Login request for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect('/index')
    return render_template('login.html', title='Sign In', form=form)

def index():
    #Fake user to greet. 
    user = {'username': 'Miguel'}

    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username:' 'Susan'},
            'body': 'The Avengers movie was so cool!' 
        },
        {
            'author': {'username:' 'Peezus'},
            'body': 'Damn Son That Movie Was Sooo super cooooooolll!'
        }
    ]

    #Returns template from /templates
    return render_template('index.html', title='Home', user=user, posts=posts)
