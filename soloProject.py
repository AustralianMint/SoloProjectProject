#Imports the 'app' variable which is part of 'app package'.
from app import app, db
from app.models import User, Post

#After 'flask shell', shell calls & loads all things in function
@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post}

