"""Backtest implementation for SPY strategy: Does a simple trend rule beat buy-and-hold?"""
import pandas as pd
import numpy as np

TRADING_DAYS = 252  # Number of trading days in a year
COST_PER_TRADE = 0.0005  # 5 bps per trade

def load_prices(csv_path="data/spy.csv"):
    """Daily dividend-adjusted SPY closes, indexed by date."""
    df = pd.read_csv(csv_path, index_col="Date", parse_dates=True)
    return df["Close"].sort_index().dropna()

def run_strategy(prices, window):
    daily_ret = prices.pct_change().fillna(0)
    sma = prices.rolling(window).mean()
    signal = (prices > sma).astype(int)  # 1 if price > SMA, else 0
    position = signal.shift(1).fillna(0)  # no look-ahead bias
    trades = position.diff().abs().fillna(0)  # 1 if trade occurs, else 0
    strat_ret = position * daily_ret - trades * COST_PER_TRADE
    return pd.DataFrame({"buy_hold" : daily_ret, "strategy": strat_ret,
                         "position": position, "trades": trades})

if __name__ == "__main__":
    prices = load_prices()
    print(f"Loaded {len(prices)} days: {prices.index[0].date()} to {prices.index[-1].date()}")
