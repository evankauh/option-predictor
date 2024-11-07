import numpy as np

def objective_function(contract, weights):
    """Objective function combining premium and risk.
    
    Args:
        contract (dict): Contract details with 'premium', 'delta', 'vega'.
        weights (tuple): Weights (alpha, beta, gamma) for premium, delta, and vega.
        
    Returns:
        float: Score representing the desirability of the contract.
    """
    premium, delta, vega = contract["premium"], contract["delta"], contract["vega"]
    alpha, beta, gamma = weights
    return alpha * premium - beta * abs(delta) - gamma * abs(vega)

def gradient_descent(contracts, weights, learning_rate=0.01, iterations=100):
    """Optimize contracts using gradient descent to find the best option contracts.

    Args:
        contracts (list): List of contract dictionaries with 'premium', 'delta', and 'vega' values.
        weights (tuple): Weights for objective function (alpha, beta, gamma).
        learning_rate (float): Step size for gradient updates.
        iterations (int): Number of iterations for the gradient descent loop.

    Returns:
        dict: Optimal contract with highest objective score.
    """
    # Initialize the best contract and score
    best_contract = contracts[0]
    best_score = objective_function(best_contract, weights)
    
    for _ in range(iterations):
        for contract in contracts:
            # Calculate the current score
            current_score = objective_function(contract, weights)
            
            # Compute gradients (using finite difference for simplicity)
            grad_premium = weights[0]
            grad_delta = -weights[1] * np.sign(contract["delta"])
            grad_vega = -weights[2] * np.sign(contract["vega"])
            
            # Adjust the contract parameters
            contract["premium"] += learning_rate * grad_premium
            contract["delta"] += learning_rate * grad_delta
            contract["vega"] += learning_rate * grad_vega
            
            # Evaluate new score
            new_score = objective_function(contract, weights)
            
            # Update the best contract if the new score is higher
            if new_score > best_score:
                best_score = new_score
                best_contract = contract.copy()
    
    return best_contract
