import pandas as pd


def utilWeek(data):
    mean_values = []
    dates = []
    reversed_df = data.iloc[2:].reset_index(drop=True)
    reversed_df['Date'] = pd.to_datetime(reversed_df['Date'])

    for i in range(0, len(reversed_df)-1, 7):
        mean_values.append(reversed_df.iloc[i:i+7, 1:].mean())
        dates.append(reversed_df['Date'].iloc[i] + pd.Timedelta(days=7))

    # Create a new DataFrame for mean values
    mean_df = pd.DataFrame(mean_values)
    mean_df['Date'] = dates
    mean_df

    return mean_df


def utilMonth(data):
    mean_values = []
    dates = []
    reversed_df = data.iloc[2:].reset_index(drop=True)
    reversed_df['Date'] = pd.to_datetime(reversed_df['Date'])

    for i in range(0, len(reversed_df)-1, 30):
        mean_values.append(reversed_df.iloc[i:i+30, 1:].mean())
        dates.append(reversed_df['Date'].iloc[i] + pd.Timedelta(days=30))

    # Create a new DataFrame for mean values
    mean_df = pd.DataFrame(mean_values)
    mean_df['Date'] = dates
    mean_df

    return mean_df


def utilYear(data):
    mean_values = []
    dates = []
    reversed_df = data.iloc[2:].reset_index(drop=True)
    reversed_df['Date'] = pd.to_datetime(reversed_df['Date'])

    step = 365
    if 2*len(reversed_df)-1 <= 365*2:
        step = (len(reversed_df)-1)//2

    for i in range(0, len(reversed_df)-1, step):
        mean_values.append(reversed_df.iloc[i:i+step, 1:].mean())
        dates.append(reversed_df['Date'].iloc[i] + pd.Timedelta(days=step))

    # Create a new DataFrame for mean values
    mean_df = pd.DataFrame(mean_values)
    mean_df['Date'] = dates
    mean_df

    return mean_df
