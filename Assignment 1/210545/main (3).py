import yfinance as yf
import numpy as np
import pandas as pd

# Define the list of tickers for international indices and equities
indices = ["^GSPC", "^FTSE", "^N225", "^GDAXI", "^HSI"]
equities = ["AAPL", "MSFT", "AMZN", "GOOGL", "FB"]

# Combine the lists of tickers
tickers = indices + equities

# Download the daily data since 2010-01-01
data = yf.download(tickers, start="2010-01-01")["Adj Close"]

# Separate the data for indices and equities
index_data = data[indices]
equity_data = data[equities]

# Calculate the daily returns for indices and equities
index_returns = index_data.pct_change().dropna()
equity_returns = equity_data.pct_change().dropna()

# Calculate the cumulative returns for indices and equities
index_cumulative_returns = (1 + index_returns).cumprod()
equity_cumulative_returns = (1 + equity_returns).cumprod()

# Calculate the maximum drawdowns for indices and equities
index_rolling_max = index_cumulative_returns.rolling(window=len(index_cumulative_returns), min_periods=1).max()
index_drawdown = index_cumulative_returns / index_rolling_max - 1

equity_rolling_max = equity_cumulative_returns.rolling(window=len(equity_cumulative_returns), min_periods=1).max()
equity_drawdown = equity_cumulative_returns / equity_rolling_max - 1

# Calculate the Sharpe ratio for indices and equities
risk_free_rate = 0.0  # Assuming risk-free rate is 0%

index_sharpe_ratio = (index_returns.mean() - risk_free_rate) / index_returns.std()
equity_sharpe_ratio = (equity_returns.mean() - risk_free_rate) / equity_returns.std()

# Calculate the Sortino ratio for indices and equities
index_downside_returns = index_returns.copy()
index_downside_returns[index_returns > 0] = 0  # Consider only downside returns
index_sortino_ratio = (index_returns.mean() - risk_free_rate) / index_downside_returns.std()

equity_downside_returns = equity_returns.copy()
equity_downside_returns[equity_returns > 0] = 0  # Consider only downside returns
equity_sortino_ratio = (equity_returns.mean() - risk_free_rate) / equity_downside_returns.std()

# Display the results
print("Indices Daily Returns:")
print(index_returns.tail())

print("\nEquities Daily Returns:")
print(equity_returns.tail())

print("\nIndices Cumulative Returns:")
print(index_cumulative_returns.tail())

print("\nEquities Cumulative Returns:")
print(equity_cumulative_returns.tail())

print("\nIndices Max Drawdowns:")
print(index_drawdown.min())

print("\nEquities Max Drawdowns:")
print(equity_drawdown.min())

print("\nIndices Sharpe Ratio:")
print(index_sharpe_ratio)

print("\nEquities Sharpe Ratio:")
print(equity_sharpe_ratio)

print("\nIndices Sortino Ratio:")
print(index_sortino_ratio)

print("\nEquities Sortino Ratio:")
print(equity_sortino_ratio)
