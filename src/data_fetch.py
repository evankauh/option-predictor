import requests
import yaml

# Load configuration
with open("config/config.yaml", "r") as file:
    config = yaml.safe_load(file)

def fetch_market_data(symbol, interval="1min"):
    """Fetches real-time stock market data."""
    api_key = config["api_key"]
    url = f'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={symbol}&interval={interval}&apikey={api_key}'
    response = requests.get(url)
    return response.json()

def fetch_option_data(symbol):
    """Fetches options data (placeholder for actual options API)."""
    url = f'https://someoptionsapi.com/options?symbol={symbol}&apikey={config["api_key"]}'
    response = requests.get(url)
    return response.json()
