from flask import render_template
from application import app, db
from application.models import email
import requests

@app.route('/')
@app.route('/home',methods=['GET'])
def home():
	emailData = email.query.all()
	return render_template('home.html', title='Home',email=emailData)

# Getting Email from Service
@app.route('/')
@app.route('/generate',methods=['GET','POST'])
def generate():
	# Response request
	response_name = requests.get('http://service2:5001/get_name')
	response_number = requests.get('http://service3:5002/get_number')
	emailname = response_name.text+response_number.text

	email1 = requests.post('http://service4:5003/get_email',data=emailname)

	#   commiting response to database
	db_email = email(gen_email=email1.text)
	db.session.add(db_email)
	db.session.commit()

	return render_template('generate.html',title='Your Email',email1=email1)