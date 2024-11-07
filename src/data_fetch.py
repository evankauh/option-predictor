import requests
import yaml
import os

# Load configuration
with open("config/config.yaml", "r") as file:
    config = yaml.safe_load(file)

def fetch_market_data(symbol, interval="1min"):
    """Fetches real-time stock market data."""
    api_key = config["api_key"]
    url = f'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={symbol}&interval={interval}&apikey={api_key}'
    response = requests.get(url)
    data = response.json()
    return data

def fetch_option_data(symbol):
    """Fetches options data (placeholder for actual options API)."""
    # Example URL for options data, modify according to actual API
    url = f'https://someoptionsapi.com/options?symbol={symbol}&apikey={config["api_key"]}'
    response = requests.get(url)
    data = response.json()
    return data

