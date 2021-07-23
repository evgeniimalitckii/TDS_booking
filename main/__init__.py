import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

app.config['SECRET_KEY'] = 'mykey'
app.config['SECURITY_PASSWORD_SALT'] = 'my_password_salt'

###############################
####### DATABASE SETUP ########
##############################

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app=app, db=db)

##############################
##### REGISTER BLUEPRINT #####
##############################

from main.booking.views import book

app.register_blueprint(book)
