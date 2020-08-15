from flask import Flask, Response, request, jsonify
from faker import Faker

# Initialize a faker generator.
fake = Faker()

# Create the app object.
app = Flask(__name__)

@app.route('/text', methods=['GET'])
def get_text():
    return Response("whatevver", mimetype='text/plain')

@app.route('/upper/text', methods=['POST'])
def post_text():

    # fake to create random company and c
    company = fake.company()
    slogan = fake.catch_phrase()
    response = {
        "Company": company,
        "Slogan": slogan
    }
    # return name and email as a JSON httpresponse using jsonify
    return jsonify(response)

if __name__ == '__main__':
    app.run(port=5000, debug=True, host='0.0.0.0')