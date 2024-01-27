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
