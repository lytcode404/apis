from ctypes import util
from email import utils
import pandas as pd

from utils import utilMonth, utilWeek, utilYear


def change_in_year(data):
    last_year = 0
    last_2ndyear = 0
    count = 0
    for i in range(0, (data.shape[0])//2):
        last_year += data.iloc[i]['Close']
        if i+(data.shape[0])//2 <= data.shape[0]:
            count += 1
            last_2ndyear += data.iloc[i+(data.shape[0])//2]['Close']
    last_year = last_year/365
    last_2ndyear = last_2ndyear/365
    year_change = ((last_year - last_2ndyear)/last_2ndyear) * 10
    return year_change


def change_in_month(data):
    last_month = 0
    last_2ndmonth = 0
    for i in range(0, 30):
        last_month += data.iloc[i]['Close']
        last_2ndmonth += data.iloc[i+30]['Close']

    # last_month/30, last_2ndmonth/30
    month_change = ((last_month - last_2ndmonth)/last_2ndmonth)*100
    return month_change


def change_in_week(data):
    last_week = 0
    last_2ndweek = 0
    for i in range(0, 7):
        last_week += data.iloc[i]['Close']
        last_2ndweek += data.iloc[i+7]['Close']
    week_change = ((last_week - last_2ndweek)/last_2ndweek)*100
    return week_change


def change_in_day(data):
    day_change = ((data.iloc[0]['Close'] - data.iloc[1]
                  ['Close'])/data.iloc[1]['Close'])*100
    return day_change


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


def weekStats(name):
    week_stats = []
    try:
        data = pd.read_csv('./crypto-db/' + name+'.csv')
        del data['Unnamed: 0']
        data2 = utilWeek(data)
        coin_name = name
        data_list = data2.to_dict(orient='records')
        week_stats.append({
            'coin_name': coin_name,
            'week_stats': data_list,
        })
        return week_stats
    except Exception as e:
        print(e)
        return


def monthStats(name):
    week_stats = []
    try:
        data = pd.read_csv('./crypto-db/' + name+'.csv')
        del data['Unnamed: 0']
        data2 = utilMonth(data)
        coin_name = name
        data_list = data2.to_dict(orient='records')
        week_stats.append({
            'coin_name': coin_name,
            'month_stats': data_list,
        })
        return week_stats
    except Exception as e:
        print(e)
        return


def yearStats(name):
    week_stats = []
    try:
        data = pd.read_csv('./crypto-db/' + name+'.csv')
        del data['Unnamed: 0']
        data2 = utilYear(data)
        coin_name = name
        data_list = data2.to_dict(orient='records')
        week_stats.append({
            'coin_name': coin_name,
            'year_stats': data_list,
        })
        return week_stats
    except Exception as e:
        print(e)
        return
