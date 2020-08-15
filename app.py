from flask import Flask, Response, request

app = Flask(__name__)

@app.route('/text', methods=['GET'])
def get_text():
    return Response("This is my first API", mimetype='text/plain')

@app.route('/upper/text', methods=['POST'])
def post_text():
    data_sent = request.data.decode('utf-8')
    upper_data = data_sent.upper()
    return Response("This is the data you sent to the API but in upper case: " + upper_data, mimetype='text/plain')

if __name__ == '__main__':
    app.run(port=5000, debug=True, host='0.0.0.0')