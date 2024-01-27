from flask import Flask, request, jsonify
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)

# Load data from the 'day_stats.json' file in the root directory
with open('day_stats.json', 'r') as json_file:
    sample_data = json.load(json_file)


@app.route('/', methods=['POST'])
def get_data():
    # Extracting JSON data from request body
    data = request.get_json()

    # Extracting 'name' from JSON data
    name = data.get('name')

    # Do something with the name if needed
    # For now, just returning the name
    return jsonify({'name': name})


if __name__ == '__main__':
    app.run()
