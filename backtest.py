"""Backtest implementation for SPY strategy: Does a simple trend rule beat buy-and-hold?"""
import pandas as pd

def load_prices(csv_path="data/spy.csv"):
    """Daily dividend-adjusted SPY closes, indexed by date."""
    df = pd.read_csv(csv_path, index_col="Date", parse_dates=True)
    return df["Close"].sort_index().dropna()

if __name__ == "__main__":
    prices = load_prices()
    print(f"Loaded {len(prices)} days: {prices.index[0].date()} to {prices.index[-1].date()}")