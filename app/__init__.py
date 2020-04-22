from flask import Flask
from .config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.config.from_object(Config)
login = LoginManager(app)
#Referencing Config class in config module.

login.login_view = 'login'
#Flask-login nees 2 know what the login view func is.

#Represents Database and Migration engine
db = SQLAlchemy(app)
migrate = Migrate(app, db)

#Initializing bootstrap
bootstrap = Bootstrap(app)

from app import routes, models
#'models' defines structure of db