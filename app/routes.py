from flask import Blueprint, Flask, render_template, url_for, flash, redirect, request, send_file, send_from_directory, send_file, session
from app import app, db, bcrypt, mail
from app.models import User
from flask_login import login_user, current_user, logout_user, login_required
from flask_mail import Mail, Message
from werkzeug.utils import secure_filename
from wtforms.fields.html5 import DateField
from app.forms import RegistrationForm
import os
import datetime
from config import Config

APP_ROOT = os.path.dirname(os.path.abspath(__file__))

main_bp = Blueprint(
	"main_bp", __name__,
	template_folder='templates',
	static_folder='static'
)

@main_bp.route('/')
def home():
	form = RegistrationForm()

	if form.validate_on_submit():
		user = User(email = form.email.data)
		db.session.add(user)
		db.session.commit()
		return redirect(url_for('/contact/paloalto'))

	return render_template('index.html', title='Home Page', form=form)

@main_bp.route('/about')
def about():
	return render_template('about.html', title='About Page')

@main_bp.route('/services')
def services():
	return render_template('services.html', title='Our Services')

@main_bp.route('/attorneys')
def attorneys():
	return render_template('attorneys.html', title='Meet the Attorneys')

@main_bp.route('/contact/paloalto', methods=['GET', 'POST'])
def contactpaloalto():
	form = RegistrationForm()

	if form.validate_on_submit():
		user = User(email = form.email.data, name = form.name.data, description = form.description.data, issue = form.issue.data, phone = form.phone.data)
		db.session.add(user)
		db.session.commit()

		#msg = Message('Thank You for Contacting Lun & Associates', sender = 'bensdrive89@gmail.com', recipients = [form.email.data])
		#msg.body = Body =  'Thank you for reaching out to us ' + form.name.data + ',\n\nSomeone from Lun & Associates will contact you shortly to set up a consultation. If you feel that your issue needs urgent attention, please call us at (408)903-9799. \n\nLun & Associates'
		#mail.send(msg)

		#notification = Message('A New Client Has Contacted Lun & Associates', sender = 'bensdrive89@gmail.com',
						#recipients = ['brand335@yahoo.com'])
		#notification.body = Body =  'A potential client has reached out to us,\n \n Name: ' + form.name.data + '\n Email: ' + form.email.data + '\nPhone Number: ' + form.phone.data + '\n Issue: ' + form.issue.data + '\n Description: ' + form.description.data
		#mail.send(notification)

		return redirect(url_for('main_bp.contactpaloalto'))
	else:
		print(form.errors)

	return render_template('contactpaloalto.html', title='Contact Page', form=form)

@main_bp.route('/contact/sanjose', methods=['GET', 'POST'])
def contactsanjose():
	form = RegistrationForm()

	if form.validate_on_submit():
		user = User(email = form.email.data, name = form.name.data, description = form.description.data, issue = form.issue.data, phone = form.phone.data)
		db.session.add(user)
		db.session.commit()

		msg = Message('Thank You for Contacting Lun & Associates', sender = 'bensdrive89@gmail.com', recipients = [user.email])
		msg.body = Body =  'Thank you for reaching out to us ' + user.name + ',\n\nSomeone from Lun & Associates will contact you shortly to set up a consultation. If you feel that your issue needs urgent attention, please call us at (408)903-9799. \n\nLun & Associates'
		mail.send(msg)

		notification = Message('A New Client Has Contacted Lun & Associates', sender = 'bensdrive89@gmail.com', 
						recipients = ['joseph@lunlaw.com', 'wendy@lunlaw.com'])
		notification.body = Body =  'A potential client has reached out to us,\n \n Name: ' + user.name + '\n Email: ' + user.email + '\nPhone Number: ' + user.phone + '\n Issue: ' + user.issue + '\n Description: ' + user.description
		mail.send(notification)

		return redirect(url_for('main_bp.contactsanjose'))

	return render_template('contactsanjose.html', title='Contact Page', form=form)

@main_bp.route('/contact/newark', methods=['GET', 'POST'])
def contactnewark():
	form = RegistrationForm()

	if form.validate_on_submit():
		user = User(email = form.email.data, name = form.name.data, description = form.description.data, issue = form.issue.data, phone = form.phone.data)
		db.session.add(user)
		db.session.commit()

		msg = Message('Thank You for Contacting Lun & Associates', sender = 'bensdrive89@gmail.com', recipients = [user.email])
		msg.body = Body =  'Thank you for reaching out to us ' + user.name + ',\n\nSomeone from Lun & Associates will contact you shortly to set up a consultation. If you feel that your issue needs urgent attention, please call us at (408)903-9799. \n\nLun & Associates'
		mail.send(msg)

		notification = Message('A New Client Has Contacted Lun & Associates', sender = 'bensdrive89@gmail.com', 
						recipients = ['joseph@lunlaw.com', 'wendy@lunlaw.com'])
		notification.body = Body =  'A potential client has reached out to us,\n \n Name: ' + user.name + '\n Email: ' + user.email + '\nPhone Number: ' + user.phone + '\n Issue: ' + user.issue + '\n Description: ' + user.description
		mail.send(notification)

		return redirect(url_for('main_bp.contactnewark'))

	return render_template('contactnewark.html', title='Contact Page', form=form)

@main_bp.route('/blog')
def blog():
	return render_template('blog.html', title='Contact Page')

@main_bp.route('/services/familylaw')
def familylaw():
	return render_template('familyservices.html', title='Family Law Services')

@main_bp.route('/services/bankruptcy')
def bankruptcy():
	return render_template('bankruptcyservices.html', title='Bankruptcy Services')

@main_bp.route('/services/personalinjury')
def personalinjury():
	return render_template('personalinjuryservices.html', title='Immigration Services')
