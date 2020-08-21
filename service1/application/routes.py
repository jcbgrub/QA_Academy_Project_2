from flask import request,Response
import requests
from application import app
import random

#generates a the name of a random author 
@app.route('/generate',methods=['GET'])
def generate():

    return Response(author,mimetype='text/plain')
