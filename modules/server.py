from flask import Flask, jsonify
from flask_cors import CORS
from paste.translogger import TransLogger
from waitress import serve

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False # keep JSON in the order in which it is written

CORS(app)

@app.route('/', methods=['GET'])
def index():
    return jsonify({'name': 'FIFA Player Recommendation System', 'version': '0.0.1'})

def run_server():
    global app

    print('Server running on 0.0.0.0:8080')
    
    # TODO: change host/port configuration to read from a config file
    serve(TransLogger(app), host='0.0.0.0', port=8080)