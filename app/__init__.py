
from flask import Flask
app = Flask(__name__)
app.config.from_object('config')

# Setup Database
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy(app)

# Config Login Systems
import os 
from flask_login import LoginManager
from flask_openid import OpenID
from config import basedir

lm = LoginManager()
lm.init_app(app)
lm.login_view = 'login'
oid = OpenID(app, os.path.join(basedir, 'tmp'))

# Import Database
from app import views, models