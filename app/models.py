from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from datetime import datetime
from hashlib import md5
from app import db, login

#User class inherits from db.Model (base class)
class User(UserMixin, db.Model):
    #fields created as instances of db.Column
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    posts = db.relationship('Post', backref ='author', lazy='dynamic')
    #db.relationship declares one in 'one-to-many'

    #__repr__ tells python how to print objects
    def __repr__(self):
        return '<User {}>'.format(self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    #returns user's avatar image, scaled 2 requested size in px
    def avatar(self, size):
        #generate MD5 hash w/ email. Lowerecased, str turne 2 bytes, hash func.
        digest = md5(self.email.lower().encode('utf8')).hexdigest()
        return 'https://www.gravatar.com/avatar/{}?d=identicon&s={}'.format(
            digest,size)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    #'default' will set to whatever 'datetime.utcnow' func returns.
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Post {}>'.format(self.body)

class Primary_clothes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    clothingItem = db.Column(db.String(64))
    quantity = db.Column(db.Integer)

class Other_clothes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    clothingItem = db.Column(db.String(64))
    quantity = db.Column(db.Integer)

class High_clothes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    clothingItem = db.Column(db.String(64))
    quantity = db.Column(db.Integer)

#Keep track of logged in user
@login.user_loader
def load_user(id):
    return(User.query.get(int(id)))