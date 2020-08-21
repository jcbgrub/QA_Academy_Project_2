from flask import request, Response
import requests
from application import app
import random

#  generate random number 1-99
@app.route('/get_number',methods=['GET'])
def get_number():
    number= name_four[random.randint(0,100)]
    return Response(number,mimetype='text/plain')
 