#Imports the 'app' variable which is part of 'app package'.
from app import app, db
from app.models import User, Post, Primary_clothes

#After 'flask shell', shell calls & loads all things in function
@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post, 'Primary_clothes': Primary_clothes}

if __name__ == '__main__':
    app.run(host="0.0.0.0")
