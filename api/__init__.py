import os
from flask import Flask

app = Flask(__name__)
app.config['SECRET'] = os.getenv('SECRET_KEY')

from api import views