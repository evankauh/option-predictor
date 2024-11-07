import pandas as pd

def run_backtest(strategy_func, data):
    """Runs backtest using historical data and strategy."""
    results = []
    for index, row in data.iterrows():
        signal = strategy_func(row)
        if signal:
            results.append({"date": row["date"], "action": "Sell", "price": row["close"]})
    return pd.DataFrame(results)

def calculate_metrics(results):
    """Calculates performance metrics for backtest results."""
    total_trades = len(results)
    profit = results["price"].diff().sum()
    return {"total_trades": total_trades, "profit": profit}
    