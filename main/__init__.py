import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

app.config['SECRET_KEY'] = 'mykey_dvlmadlkcmdcal;c,'
app.config['SECURITY_PASSWORD_SALT'] = 'my_password_salt'

###############################
####### DATABASE SETUP ########
##############################

basedir = os.path.abspath(os.path.dirname(__file__))
# for localhost
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
# for heroku "tds-booking" project
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://wncgjwthdianhx:e49e7b3fd624473e22d1975d119e83efc9a525b8bbf9769a9401e65bac82c4b1@ec2-3-248-103-75.eu-west-1.compute.amazonaws.com:5432/d79j30n54ibobs'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app=app, db=db)

##############################
##### REGISTER BLUEPRINT #####
##############################

from main.booking.views import book

app.register_blueprint(book)
