from model import gradient_descent

def select_optimal_contracts(contracts, weights, max_risk, risk_free_rate):
    """Select optimal contract using gradient descent."""
    optimal_contract = gradient_descent(contracts, weights, max_risk, risk_free_rate)
    return optimal_contract
