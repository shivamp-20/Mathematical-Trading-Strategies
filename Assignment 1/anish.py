import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Define the indices and equities
indices = ['^GSPC', '^IXIC', '^DJI', '^FTSE', '^N225']
equities = ['AAPL', 'AMZN', 'GOOGL', 'MSFT', 'TSLA']

# Download the data
data = yf.download(indices + equities, start='2010-01-01', end='2023-05-20')['Adj Close']

# Calculate daily returns
returns = data.pct_change()

# Calculate cumulative returns
cumulative_returns = (1 + returns).cumprod()

# Calculate maximum drawdowns
rolling_max = cumulative_returns.rolling(window=len(cumulative_returns), min_periods=1).max()
drawdowns = (cumulative_returns / rolling_max) - 1
max_drawdowns = drawdowns.min()

# Calculate annualized average returns
avg_returns = returns.mean() * 252

# Calculate annualized standard deviation
std_returns = returns.std() * np.sqrt(252)

# Calculate Sharpe ratio
risk_free_rate = 0.0  # Assuming no risk-free rate for simplicity
sharpe_ratio = (avg_returns - risk_free_rate) / std_returns

# Calculate Sortino ratio
downside_returns = returns.where(returns < 0, 0)
downside_std = downside_returns.std() * np.sqrt(252)
sortino_ratio = (avg_returns - risk_free_rate) / downside_std

# Print the results
print("Indices:")
print(f"{'Index':<8} {'Sharpe Ratio':<15} {'Sortino Ratio':<15}")
for i, index in enumerate(indices):
    print(f"{index:<8} {sharpe_ratio[i]:<15.4f} {sortino_ratio[i]:<15.4f}")

print("\nEquities:")
print(f"{'Equity':<8} {'Sharpe Ratio':<15} {'Sortino Ratio':<15}")
for i, equity in enumerate(equities):
    print(f"{equity:<8} {sharpe_ratio[i + len(indices)]:<15.4f} {sortino_ratio[i + len(indices)]:<15.4f}")

# Plot cumulative returns
plt.figure(figsize=(10, 6))
for col in cumulative_returns.columns:
    plt.plot(cumulative_returns.index, cumulative_returns[col], label=col)
plt.title('Cumulative Returns')
plt.xlabel('Date')
plt.ylabel('Cumulative Returns')
plt.legend(loc='upper left')
plt.grid(True)
plt.show()