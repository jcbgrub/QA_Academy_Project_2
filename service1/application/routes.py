from flask import request,Response
import requests
from application import app
import random

#generates a the name of a random author 
@app.route('/get_name_four',methods=['GET'])
def get_name4():
    name_four = ['Liam','Noah','Anna','Aimy','Levy']
    name_four = name_four[random.randrange(6)]
    return Response(author,mimetype='text/plain')

@app.route('/get_name_five',methods=['GET'])
def get_name5():
    name_five = ['Ellie','Sofia','Avery','James','Jacob']
    name_five = name_five[random.randrange(6)]
    return Response(author,mimetype='text/plain')