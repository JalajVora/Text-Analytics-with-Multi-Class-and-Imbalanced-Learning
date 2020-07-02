import pandas as pd

def load_features():
    try:
        return pd.read_csv('feature_collection.csv')
    except:
        print('Could not load feature collection') 