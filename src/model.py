import numpy as np
import yaml

# Load config
with open("config/config.yaml", "r") as file:
    config = yaml.safe_load(file)

def objective_function(contract, weights, max_risk, risk_free_rate):
    """Objective function combining premium and risk with penalties."""
    premium, delta, vega = contract["premium"], contract["delta"], contract["vega"]
    alpha, beta, gamma = weights
    sharpe_penalty = 0
    if vega > max_risk["vega"] or delta > max_risk["delta"]:
        sharpe_penalty = (premium - risk_free_rate) / np.std([delta, vega])
    return alpha * premium - beta * abs(delta) - gamma * abs(vega) - sharpe_penalty

def gradient_descent(contracts, weights, max_risk, risk_free_rate, learning_rate=0.01, iterations=100):
    """Optimize contracts using gradient descent."""
    best_contract = contracts[0]
    best_score = objective_function(best_contract, weights, max_risk, risk_free_rate)
    for _ in range(iterations):
        for contract in contracts:
            current_score = objective_function(contract, weights, max_risk, risk_free_rate)
            grad_premium = weights[0]
            grad_delta = -weights[1] * np.sign(contract["delta"])
            grad_vega = -weights[2] * np.sign(contract["vega"])
            contract["premium"] += learning_rate * grad_premium
            contract["delta"] += learning_rate * grad_delta
            contract["vega"] += learning_rate * grad_vega
            new_score = objective_function(contract, weights, max_risk, risk_free_rate)
            if new_score > best_score:
                best_score = new_score
                best_contract = contract.copy()
    return best_contract
