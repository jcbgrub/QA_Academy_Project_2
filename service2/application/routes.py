from application import app
from flask import request, Response
import requests
import random

#generates a the name of a random name with 4 letters 
@app.route('/get_name',methods=['GET'])
def get_name():
	name = ['KEynes','Friedrich','LIebknecht','Vladimir','Rosa']
	name = name[random.randint(0,4)]
	# return Response(name,mimetype='text/plain')
	return name

	