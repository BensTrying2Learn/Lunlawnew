from os import environ, path
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_mail import Mail

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.env'))

class Config:
	app = Flask(__name__)
	SECRET_KEY = os.environ.get('SECRET_KEY')
	SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
	SQLALCHEMY_ECHO = False
	db = SQLAlchemy(app)
	bcrypt = Bcrypt(app)
	app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
	app.config['MAIL_PORT'] = 587
	app.config['MAIL_USE_TLS'] = True
	app.config['MAIL_USERNAME'] = 'bensdrive89@gmail.com'
	app.config['MAIL_PASSWORD'] = '335Benben'
	SQLALCHEMY_TRACK_MODIFICATIONS = True
	DEBUG=True
	TESTING=True