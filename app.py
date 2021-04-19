from flask import Flask
from flask import request
from mongo_client import Mongo_Client

Mongo_Object = Mongo_Client()

app = Flask(__name__)


@app.route('/upload_audio_track', methods=['GET', 'POST', 'UPDATE', 'DELETE'])
def find_parents():
    if request.method == 'GET':
        return "200 OK"

    if request.method == 'POST':
        payload = request.json
        print(payload)
        response = Mongo_Client().add_file(payload)
        print(response)
        return '200 ok'
    else:
        return "Error 405 Method Not Allowed"


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
