from flask import request, Response
import requests
from application import app
import random

#  generate random number 1-99
@app.route('/get_number',methods=['GET'])
def get_number():
    number = random.randint(0,100)
    # return Response(number,mimetype='text/plain')
    return str(number)