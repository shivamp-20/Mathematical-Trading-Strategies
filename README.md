# Mathematical-Trading-Strategies
# Official repo for submission of assignments in Mathematical Trading Strategies

import yfinance as yf
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
indices = ["^HSI", "^FCHI", "^FTSE", "^N225", "^GDAXI"]
equities = ["NFLX", "JNJ", "GOOGL", "BABA", "TSLA"]

start_date = "2010-01-01"
end_date = "2023-05-01"

index_data = yf.download(indices, start=start_date, end=end_date)["Adj Close"]
equity_data =  yf.download(equities, start=start_date, end=end_date)["Adj Close"]

index_returns = index_data.pct_change()
equity_returns = equity_data.pct_change()

index_cumulative_returns = (1 + index_returns).cumprod() -1
equity_cumulative_returns = (1 + equity_returns).cumprod() -1

index_drawdowns = (index_cumulative_returns - index_cumulative_returns.cummax()) / index_cumulative_returns.cummax()
equity_drawdowns = (equity_cumulative_returns - equity_cumulative_returns.cummax()) /equity_cumulative_returns.cummax()

index_avg_returns = index_returns.mean()
index_volatility = index_returns.std()
equity_avg_returns = equity_returns.mean()
equity_volatility = equity_returns.std()

risk_free_rate = 0

index_sharpe_ratio = (index_avg_returns - risk_free_rate) / index_volatility
equity_sharpe_ratio = (equity_avg_returns - risk_free_rate) / equity_volatility
index_downside_returns = index_returns.where(index_returns < 0, 0)
index_downside_volatility = index_downside_returns.std()
index_sortino_ratio = (index_avg_returns - risk_free_rate) / index_downside_volatility
equity_downside_returns = equity_returns.where(equity_returns < 0, 0)
equity_downside_volatility = equity_downside_returns.std()
equity_sortino_ratio = (equity_avg_returns - risk_free_rate) / equity_downside_volatility


metrics_df = pd.DataFrame(index=['Cumulative returns', 'Volatility', 'Sharpe Ratio', 'Sortino Ratio', 'Max Drawdown'])
metrics_df2 = pd.DataFrame(index=['Cumulative returns', 'Volatility', 'Sharpe Ratio', 'Sortino Ratio', 'Max Drawdown'])
metrics_df[indices] = [
    index_cumulative_returns.iloc[-1],
    index_returns.std(),
    index_sharpe_ratio,
    index_sortino_ratio,
    indices_max_drawdowns]

metrics_df2[equities] = [
    equity_cumulative_returns.iloc[-1],
    equity_returns.std(),
    equity_sharpe_ratio,
    equity_sortino_ratio,
    equities_max_drawdowns
]    

print(metrics_df.to_string(header=True, index=True))
print(metrics_df2.to_string(header=True, index=True))

