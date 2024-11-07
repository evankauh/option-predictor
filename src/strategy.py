def covered_call_strategy(option_data, target_delta=0.3):
    """Selects covered call options based on target delta."""
    return [opt for opt in option_data if opt["delta"] <= target_delta]

def put_sell_strategy(option_data, target_delta=0.2):
    """Selects put options to sell based on target delta."""
    return [opt for opt in option_data if opt["delta"] >= target_delta]

def filter_by_risk(contracts, max_delta=0.3, max_vega=0.2):
    """Filters contracts based on delta and vega limits."""
    return [c for c in contracts if abs(c["delta"]) <= max_delta and abs(c["vega"]) <= max_vega]
