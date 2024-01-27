from flask import Flask, request, jsonify
import pandas as pd
from helper import all_data, change_in_day, change_in_month, change_in_week, change_in_year, dayStats, monthStats, weekStats, yearStats
from flask_cors import CORS
app = Flask(__name__)
CORS(app)


@app.route('/change-in-crypto', methods=['POST'])
def change_in_crypto():
    try:
        # Extract the name from JSON data
        name = request.json.get('name')

        # Get data for the provided name
        data = all_data(name)

        # Return the data as JSON response
        return jsonify({'data': data})

    except Exception as e:
        error_message = f"Error handling request: {e}"
        print(error_message)
        return jsonify({'error': error_message})


@app.route('/day-stats', methods=['POST'])
def day_stat():
    try:
        # Extract the name from JSON data
        name = request.json.get('name')

        # Get data for the provided name
        data = dayStats(name)

        # Return the data as JSON response
        return jsonify({'data': data})

    except Exception as e:
        error_message = f"Error handling request: {e}"
        print(error_message)
        return jsonify({'error': error_message})


@app.route('/week-stats', methods=['POST'])
def week_stat():
    try:
        # Extract the name from JSON data
        name = request.json.get('name')

        # Get data for the provided name
        data = weekStats(name)

        # Return the data as JSON response
        return jsonify({'data': data})

    except Exception as e:
        error_message = f"Error handling request: {e}"
        print(error_message)
        return jsonify({'error': error_message})


@app.route('/month-stats', methods=['POST'])
def month_stats():
    try:
        # Extract the name from JSON data
        name = request.json.get('name')

        # Get data for the provided name
        data = monthStats(name)

        # Return the data as JSON response
        return jsonify({'data': data})

    except Exception as e:
        error_message = f"Error handling request: {e}"
        print(error_message)
        return jsonify({'error': error_message})


@app.route('/year-stats', methods=['POST'])
def year_stats():
    try:
        # Extract the name from JSON data
        name = request.json.get('name')

        # Get data for the provided name
        data = yearStats(name)

        # Return the data as JSON response
        return jsonify({'data': data})

    except Exception as e:
        error_message = f"Error handling request: {e}"
        print(error_message)
        return jsonify({'error': error_message})


if __name__ == '__main__':
    app.run(debug=True)
