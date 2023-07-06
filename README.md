# Mathematical-Trading-Strategies
Official repo for submission of assignments in Mathematical Trading Strategies
import yfinance as yf
import pandas as pd
import numpy as np
indices = ['^GSPC', '^FTSE', '^N225', '^GDAXI', '^HSI']
equities = ['AAPL', 'MSFT', 'AMZN', 'GOOGL', 'TSLA']
start_date = '2010-01-01'
end_date = '2023-05-17'
data = yf.download(indices + equities, start=start_date, end=end_date)['Adj Close']
returns = data.pct_change()
cumulative_returns = (1 + returns).cumprod() - 1
rolling_max = cumulative_returns.rolling(window=len(data), min_periods=1).max()
daily_drawdown = cumulative_returns / rolling_max - 1
max_drawdown = daily_drawdown.min()
risk_free_rate = 0.0  # Assuming risk-free rate of return as 0%
excess_returns = returns - risk_free_rate
sharpe_ratio = np.sqrt(252) * (excess_returns.mean() / excess_returns.std())
downside_returns = excess_returns.copy()
downside_returns[downside_returns > 0] = 0
sortino_ratio = np.sqrt(252) * (excess_returns.mean() / downside_returns.std())
print("Indices:")
print(cumulative_returns[indices])
print("\nEquities:")
print(cumulative_returns[equities])
print("\nMax Drawdowns:")
print(max_drawdown)
print("\nSharpe Ratios:")
print(sharpe_ratio)
print("\nSortino Ratios:")
print(sortino_ratio)
