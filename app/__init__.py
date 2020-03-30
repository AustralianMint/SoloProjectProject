from flask import Flask
from .config import Config

app = Flask(__name__)
app.config.from_object(Config)
#Referencing Config class in config module.

from app import routes