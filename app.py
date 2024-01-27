from flask import Flask, request, jsonify
import pandas as pd
from helper import change_in_day, change_in_month, change_in_week, change_in_year

app = Flask(__name__)


def all_data(name):
    try:
        results_list = []
        data = pd.read_csv('./crypto-db/' + name + '.csv')
        del data['Unnamed: 0']
        coin_name = name
        change_day = change_in_day(data)
        change_week = change_in_week(data)
        change_month = change_in_month(data)
        change_year = change_in_year(data)
        results_list.append({
            'coin_name': coin_name,
            'change_day': change_day,
            'change_week': change_week,
            'change_month': change_month,
            'change_year': change_year
        })
        return results_list

    except Exception as e:
        error_message = f"Error processing data for {name}: {e}"
        print(error_message)
        return {'error': error_message}


def dayStats(name):
    day_stats = []
    try:
        data = pd.read_csv('./crypto-db/' + name+'.csv')
        del data['Unnamed: 0']
        coin_name = name
        data_list = data.to_dict(orient='records')
        day_stats.append({
            'coin_name': coin_name,
            'day_stats': data_list,
        })
        return day_stats
    except Exception as e:
        print(data)
        return


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


if __name__ == '__main__':
    app.run(debug=True)
