from flask import request,Response
import requests
from application import app
import random

#generates a the name of a random author 
@app.route('/get_num_one',methods=['GET'])
def get_name1():
    name1 = ['2','3','4','6','9']
    name1= name1[random.randrange(6)]
    return Response(author,mimetype='text/plain')

@app.route('/get_num_two',methods=['GET'])
def get_name2():
    name2 = ['11','22','43','69','99']
    name2 = name2[random.randrange(6)]
    return Response(author,mimetype='text/plain')
