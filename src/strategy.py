def covered_call_strategy(option_data, target_delta=0.3):
    """Selects covered call options based on target delta."""
    return [opt for opt in option_data if opt["delta"] <= target_delta]

def put_sell_strategy(option_data, target_delta=0.2):
    """Selects put options to sell based on target delta."""
    return [opt for opt in option_data if opt["delta"] >= target_delta]

def short_signal(stock_data):
    """Determines if a stock is a short candidate based on trend analysis."""
    if stock_data["moving_avg"].iloc[-1] < stock_data["close"].iloc[-1]:
        return True  # Example short condition
    return False
