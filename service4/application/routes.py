from flask import request, Response
import requests
from application import app
import random

@app.route('/get/email', methods=['GET'])
def email():
    response_name_four = requests.get('http://api:5001/get/get_name_four')
    response_name_five = requests.get('http://api:5001/get/get_name_five')
    response_num_one = requests.get('http://api:5002/get/get_num_one')
    response_num_two = requests.get('http://api:5002/get/get_num_two')

    if response.text == "1":
        return "Football"
    elif response.text == "2":
        return "Badminton"
    elif response.text == "3":
        return "Hockey"
    else:
        return "Out of Range"