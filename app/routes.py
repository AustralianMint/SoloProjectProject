#render_template = Renders template and according arguments (e.g Name of person)
#Uses Jinja2 for substitution of {{...}}

from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm
from flask_login import current_user, login_user
from app.models import User

#All decorators which invoke the function when called.
@app.route('/')
@app.route('/index')

#Define what methods are accepted.
@app.route('/login', methods=['GET', 'POST'])

def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()

    #Checks if user exists & Password matches
    #If correct, remembers usr, serves index.html
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('index'))
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
