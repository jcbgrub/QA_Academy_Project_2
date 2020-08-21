from flask import request, Response
import requests
from application import app
import random

@app.route('/get_email', methods=['GET','POST'])
def get_email():
	emailname = request.data.decode('utf-8')
	if len(emailname) >= 5:
		emailname = emailname+"@sputnik.com"
	elif len(emailname) >= 7:
		emailname = emailname+"@cosmonaut.com"
	elif response.text == 10:
		emailname = emailname+"@spacerocket.com"
	else:
		'this should not be here'
	return Response(emailname,mimetype='text/plain ')

