import pandas as pd
from datetime import datetime
import acquire

def prepare_data(df):
    df['date'] = pd.to_datetime(df['date'])
    df = df.sort_values(by='date').set_index('date')
    df['calories_burned'] = df['calories_burned'].str.replace(',','')
    df['steps'] = df['steps'].str.replace(',','')
    df['minutes_sedentary'] = df['minutes_sedentary'].str.replace(',','')
    df['activity_calories'] = df['activity_calories'].str.replace(',','')
    df[['calories_burned', 'steps', 'minutes_sedentary', 'activity_calories']] = df[['calories_burned', 'steps', 'minutes_sedentary', 'activity_calories']].apply(pd.to_numeric)
    df['total_minutes_logged'] = df['minutes_sedentary'] + df['minutes_lightly_active'] + df['minutes_fairly_active'] + df['minutes_very_active']
    df['distance_per_step'] = (df['distance'] / df['steps'])
    return df


def impute_zeros(df):
    df.resample('D').mean()
    df['calories_burned'].replace(to_replace= 0, value= 3317, inplace=True)
    df['steps'].replace(to_replace= 0, value= 6916, inplace=True)
    df['distance'].replace(to_replace= 0, value= 3, inplace=True)
    df['floors'].replace(to_replace= 0, value= 6, inplace=True)
    df['minutes_sedentary'].replace(to_replace= 0, value= 920, inplace=True)
    df['minutes_lightly_active'].replace(to_replace= 0, value= 172, inplace=True)
    df['minutes_fairly_active'].replace(to_replace= 0, value= 17, inplace=True)
    df['minutes_very_active'].replace(to_replace= 0, value= 22, inplace=True)
    df['activity_calories'].replace(to_replace= 0, value= 1331, inplace=True)
    df['total_minutes_logged'].replace(to_replace= 0, value= 1131, inplace=True)
    df['distance_per_step'].replace(to_replace= 0, value= .000472, inplace=True)
    return df