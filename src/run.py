from src import data_fetch, data_processing, feature_engineering, strategy
from predict import select_optimal_contracts
import yaml

# Load configuration
with open("config/config.yaml", "r") as file:
    config = yaml.safe_load(file)

def main():
    print("Starting the algorithm...")

    # Fetch and clean data
    raw_data = data_fetch.fetch_market_data(config["stock_symbol"], config["interval"])
    clean_data = data_processing.clean_data(raw_data)

    # Feature engineering
    features = feature_engineering.generate_features(clean_data)

    # Example contracts (for demonstration)
    contracts = [
        {"premium": 1.5, "delta": 0.3, "vega": 0.2},
        {"premium": 2.0, "delta": 0.25, "vega": 0.15},
        {"premium": 1.8, "delta": 0.35, "vega": 0.25}
    ]

    # Find optimal contract
    weights = (config["weights"]["alpha"], config["weights"]["beta"], config["weights"]["gamma"])
    max_risk = config["max_risk"]
    risk_free_rate = config["risk_free_rate"]
    
    optimal_contract = select_optimal_contracts(contracts, weights, max_risk, risk_free_rate)
    print("Optimal Contract:", optimal_contract)
    print("Algorithm completed successfully.")

if __name__ == "__main__":
    main()
