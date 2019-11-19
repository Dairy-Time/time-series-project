import pandas as pd


# Bring in prepared data

def prepare_data(df):
    df = pd.read_csv('fitbit/tidy.csv')
    df['date'] = pd.to_datetime(df['date'])
    df = df.set_index(df['date'])
    df['calories_burned'] = df['calories_burned'].str.replace(',','')
    df['steps'] = df['steps'].str.replace(',','')
    df['minutes_sedentary'] = df['minutes_sedentary'].str.replace(',','')
    df['activity_calories'] = df['activity_calories'].str.replace(',','')
    df[['calories_burned', 'steps', 'minutes_sedentary', 'activity_calories']] = df[['calories_burned', 'steps', 'minutes_sedentary', 'activity_calories']].apply(pd.to_numeric)
    df['total_minutes_logged'] = df['minutes_sedentary'] + df['minutes_lightly_active'] + df['minutes_fairly_active'] + df['minutes_very_active']
    df['distance_per_step'] = df['distance'] / df['steps']
    return df
