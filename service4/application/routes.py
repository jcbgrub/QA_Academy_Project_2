from flask import request, Response
import requests
from application import app
import random

@app.route('/get_email', methods=['GET','POST'])
def get_email():
	response_name = requests.get('http://api:5001/get_name')
	response_number = requests.get('http://api:5002/get_number')
	emailname = response_name.text+response_number.text
	if len(emailname) >= 5:
		response_name+"@sputnik.com"
	elif len(emailname) >= 7:
		response_name+"@cosmonaut.com"
	elif response.text == 10:
		response_name+"@spacerocket.com"
	else:
		'this should not be here'
	return Response(emailname,mimetype='text/plain ')