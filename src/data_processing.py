import pandas as pd

def load_data(filename):
    """Load data from a CSV or API."""
    return pd.read_csv(filename)

def clean_data(data):
    """Clean and preprocess raw data."""
    data.dropna(inplace=True)
    return data

def transform_features(data):
    """Applies feature engineering steps."""
    return generate_features(data)
