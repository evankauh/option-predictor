import src.data_fetch as data_fetch
import src.data_processing as data_processing
import src.feature_engineering as feature_engineering
import src.sentiment_analysis as sentiment_analysis
import src.strategy as strategy
import backtesting

def main():
    # Step 1: Fetch and clean data
    data = data_fetch.fetch_market_data("AAPL")
    clean_data = data_processing.clean_data(data)
    
    # Step 2: Feature engineering
    features = feature_engineering.generate_features(clean_data)
    
    # Step 3: Backtesting (example)
    results = backtesting.run_backtest(strategy.covered_call_strategy, features)
    metrics = backtesting.calculate_metrics(results)
    print("Backtest Results:", metrics)

if __name__ == "__main__":
    main()
