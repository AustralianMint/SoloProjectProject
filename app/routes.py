#render_template = Renders template and according arguments (e.g Name of person)
#Uses Jinja2 for substitution of {{...}}

from flask import render_template, flash, redirect, url_for, request
from app import app, db
from app.forms import LoginForm, RegistrationForm, editDbForm
from flask_login import current_user, login_user, logout_user, login_required
from app.models import User, Post, Primary_clothes, Other_clothes, High_clothes
from werkzeug.urls import url_parse
from .tables import Results, P_Items, Other_Items, high_clothes_table 

#Decorators which invoke the function when root is called called.
@app.route('/')
@app.route('/index')
@login_required

def index():
    #Query respective db Models
    all_users = User.query.all()
    primaryClothes = Primary_clothes.query.all()
    otherClothes = Other_clothes.query.all()
    highClothes = High_clothes.query.all()

    #Initialize already created table from tables.py
    init_Table = Results(all_users)
    init_Table_Primary = P_Items(primaryClothes)
    init_Table_Other = Other_Items(otherClothes)
    init_Table_High = high_clothes_table(highClothes)

    return render_template('index.html', title='Home', table=init_Table,
        table2=init_Table_Primary, table3=init_Table_Other, table4=init_Table_High)

#Define what methods are accepted.
@app.route('/login', methods=['GET', 'POST'])

def login():
    #Handles special case if usr already logged in.
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    #LoginForm class w/ defined features

    #Checks if user exists & Password matches
    #If correct, remembers usr, serves index.html
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        
        #Redirect to 'next' page (prior page be4 having 2 log in)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('login.html', title='Sign In', form=form)
    #Render template fills placeholder variables w/ actual data.


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        #Place form answers into db & set their password
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

#Shows user PP
#<username> being the argument provided eg. 'susan'
@app.route('/user/<username>')
@login_required
def user(username):
    #Will return 404 if user doesn't exist.
    user = User.query.filter_by(username=username).first_or_404()
    posts = [
        {'author': user, 'body': 'Test post #1'},
        {'author': user, 'body': 'Test post #2'}
    ]
    return render_template('user.html', user=user, posts=posts)

#dynamic route. When table2 is accessed and id of 'edit' is called
#@app.route('/table2/<int:id>') 
#def link():
#    return render_template('editDb.html', title='Edit Database')

@app.route('/editDb', methods=['GET', 'POST'])
def editDb():
    form = editDbForm()
    flash('Regardless')
    #if form.validate_on_submit():
    if form.is_submitted():
        flash('Congratulations, quantities have been updated!')
        edited_amount = Primary_clothes(clothingItem=form.clothingItem.data, quantity=form.quantity.data)
        db.session.add(edited_amount)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('editDb.html', title='Edit Database', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))