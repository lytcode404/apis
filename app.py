from flask import Flask, jsonify
from flask_cors import CORS
import pandas as pd
import json

app = Flask(__name__)
CORS(app)

# Load data from the 'sample.json' file in the root directory
with open('day_stats.json', 'r') as json_file:
    sample_data = json.load(json_file)


@app.route('/', methods=['GET'])
def get_data():
    return jsonify(sample_data)


if __name__ == '__main__':
    app.run(debug=True)
