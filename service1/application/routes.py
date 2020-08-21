from flask import request, Response, render_template
import requests
from application import app, db
import random
from application.models import email

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', title='Home Page')

# Getting Email from Service4
@app.route('/')
@app.route('/generate',methods=['GET'])
def generate():
    # Response request
	response_email = requests.get('http://api:5003/get/get_email',)

    #   commiting response to database
    db_email = email(gen_email=response_email.text)
    db.session.add(db_email)
    db.session.commit()

    return render_template('generate.html',title='Your Email',data=response_email.txt)

