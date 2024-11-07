import numpy as np

def calculate_greeks(option_data):
    """Calculate Greeks for each option."""
    option_data["delta"] = np.random.uniform(0, 1)
    option_data["vega"] = np.random.uniform(0, 1)
    return option_data

def generate_features(data):
    """Generate additional features like moving average and volatility."""
    data["moving_avg"] = data["close"].rolling(window=10).mean()
    data["volatility"] = data["close"].pct_change().rolling(window=10).std()
    return data
