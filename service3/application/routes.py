from flask import request,Response
import requests
from application import app
import random

#generates a the name of a random author 
@app.route('/get_num2',methods=['GET'])
def get_name4():
    name_four = ['2','3','4','6','9']
    name_four = name_four[random.randrange(6)]
    return Response(author,mimetype='text/plain')

    @app.route('/get_num3',methods=['GET'])
def get_name5():
    name_five = ['Ellie','Sofia','Avery','James','Levy']
    name_five = name_five[random.randrange(6)]
    return Response(author,mimetype='text/plain')