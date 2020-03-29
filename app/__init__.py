from flask import Flask
#from config.py import Class Config
from config import Config

app = Flask(__name__)
#Reference Config Class
app.config.from_object(Config)

from app import routes