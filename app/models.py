from app import db

#User class inherits from db.Model (base class)
class User(db.Model):
    #fields created as instances of db.Column
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    #__repr__ tells python how to print objects
    def __repr__(self):
        return '<User {}>'.format(self.username)