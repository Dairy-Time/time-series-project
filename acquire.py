import pandas as pd

def acquire_data():
    df = pd.read_csv('fitbit/tidy.csv')
    return df

