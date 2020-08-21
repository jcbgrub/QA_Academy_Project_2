from application import app
from flask import request, Response
import requests

import random

#generates a the name of a random name with 4 letters 
@app.route('/get_name_four',methods=['GET'])
def get_name4():
    name_four = ['Liam','Noah','Anna','Aimy','Levy']
    name_four = name_four[random.randint(0,4)]
    return Response(name_four,mimetype='text/plain')

#generates a the name of a random name with 5 letters
@app.route('/get_name_five',methods=['GET'])
def get_name5():
    name_five = ['Ellie','Sofia','Avery','James','Jacob']
    name_five = name_five[random.randrange(5)]
    return Response(name_five,mimetype='text/plain')