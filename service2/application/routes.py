from application import app
from flask import request, Response
import requests

import random

# generates a random name  
@app.route('/get_name',methods=['GET'])
def get_name():
    name = ['Keynes','Friedrich','Liebknecht','Vladimir','Rosa']
    name = name[random.randint(0,4)]
    # return Response(name,mimetype='text/plain')
    return name

#generates a random name in capital
# @app.route('/get_name',methods=['GET'])
# def get_name():
#     name = ['KEYNES','FRIEDRICH','LIEBKNECHT','VLADIMIR','ROSA']
#     name = name[random.randint(0,4)]
    
#     # return Response(name,mimetype='text/plain')
#     return name
