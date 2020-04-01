from flask import Flask
from .config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(Config)
#Referencing Config class in config module.

#Represents Database and Migration engine
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import routes, models
#'models' defines structure of db