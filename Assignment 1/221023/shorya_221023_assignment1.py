import yfinance as yf
import pandas as pd

symbols = ['^GSPC', '^IXIC', '^FTSE', '^N225', '^GDAXI', 'AAPL', 'GOOGL', 'MSFT', 'AMZN']

data = yf.download(symbols, start='2010-01-01', end='2023-05-25')['Adj Close']

returns = data.pct_change()

cumulative_returns = (1 + returns).cumprod()

rolling_max = cumulative_returns.rolling(window=252, min_periods=1).max()
daily_drawdown = cumulative_returns / rolling_max - 1
max_drawdowns = daily_drawdown.rolling(window=252, min_periods=1).min()

risk_free_rate = 0
excess_returns = returns - risk_free_rate / 252
sharpe_ratio = excess_returns.mean() / excess_returns.std() * (252 ** 0.5)

downside_returns = returns.copy()
downside_returns[returns > 0] = 0
downside_std = downside_returns.std() * (252 ** 0.5)
sortino_ratio = excess_returns.mean() / downside_std

table = pd.DataFrame({'Returns': returns.mean(),
                      'Cumulative Returns': cumulative_returns.iloc[-1] - 1,
                      'Max Drawdown': max_drawdowns.min(),
                      'Sharpe Ratio': sharpe_ratio,
                      'Sortino Ratio': sortino_ratio})

print(table)