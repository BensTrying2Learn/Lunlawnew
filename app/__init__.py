from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_mail import Mail
from config import Config

app = Flask(__name__, instance_relative_config=False)

db = SQLAlchemy()
bcrypt = Bcrypt(app)

app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'bensdrive89@gmail.com'
app.config['MAIL_PASSWORD'] = '335Benben'
SQLALCHEMY_TRACK_MODIFICATIONS = True

mail = Mail(app)

def create_app():
	app = Flask(__name__, instance_relative_config=False)
	app.config.from_object('config.Config')
	db.init_app(app)
	with app.app_context():
		from . import routes

		app.register_blueprint(routes.main_bp)
		#db.create_all()
	
		return app

from app import routes