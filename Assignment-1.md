---
jupyter:
  kernelspec:
    display_name: Python 3 (ipykernel)
    language: python
    name: python3
  language_info:
    codemirror_mode:
      name: ipython
      version: 3
    file_extension: .py
    mimetype: text/x-python
    name: python
    nbconvert_exporter: python
    pygments_lexer: ipython3
    version: 3.10.9
  nbformat: 4
  nbformat_minor: 5
---

::: {#017ddab9 .cell .code execution_count="1"}
``` python
import yfinance as yf
import pandas as pd
from tabulate import tabulate

ticker_symbols = ['AAPL', 'AMZN', 'GOOGL', 'META', 'TSLA']
index_symbols = ['SPY', 'QQQ', 'UKX', '^N225', '^GDAXI']
start_date = '2010-01-01'
end_date = '2023-05-01'

stock_data = yf.download(ticker_symbols, start=start_date, end=end_date)['Adj Close']
index_data = yf.download(index_symbols, start=start_date, end=end_date)['Adj Close']

stock_metrics = []
for ticker in ticker_symbols:
    cumulative_returns = (1 + stock_data[ticker].pct_change()).cumprod().iloc[-1]

    rf_rate = 0.01  
    annualized_returns = (cumulative_returns ** (252 / len(stock_data))) - 1
    annualized_volatility = stock_data[ticker].pct_change().std() * (252 ** 0.5)

    downside_returns = stock_data[ticker].pct_change().copy()
    downside_returns[downside_returns > 0] = 0
    downside_volatility = downside_returns.std() * (252 ** 0.5)

    sharpe_ratio = (annualized_returns - rf_rate) / annualized_volatility
    sortino_ratio = (annualized_returns - rf_rate) / downside_volatility

    rolling_max = stock_data[ticker].cummax()
    daily_drawdown = stock_data[ticker] / rolling_max - 1
    max_drawdown = daily_drawdown.cummin().iloc[-1]

    stock_metrics.append([ticker, cumulative_returns, sharpe_ratio, annualized_volatility, sortino_ratio, max_drawdown])

index_metrics = []
for index in index_symbols:
    
    cumulative_returns = (1 + index_data[index].pct_change()).cumprod().iloc[-1]

    rf_rate = 0.01  
    annualized_returns = (cumulative_returns ** (252 / len(index_data))) - 1
    annualized_volatility = index_data[index].pct_change().std() * (252 ** 0.5)

    downside_returns = index_data[index].pct_change().copy()
    downside_returns[downside_returns > 0] = 0
    downside_volatility = downside_returns.std() * (252 ** 0.5)

    sharpe_ratio = (annualized_returns - rf_rate) / annualized_volatility
    sortino_ratio = (annualized_returns - rf_rate) / downside_volatility

    rolling_max = index_data[index].cummax()
    daily_drawdown = index_data[index] / rolling_max - 1
    max_drawdown = daily_drawdown.cummin().iloc[-1]

    index_metrics.append([index, cumulative_returns, sharpe_ratio, annualized_volatility, sortino_ratio, max_drawdown])

stock_df = pd.DataFrame(stock_metrics, columns=['Ticker', 'Cumulative Return', 'Sharpe Ratio', 'Volatility', 'Sortino Ratio', 'Max Drawdown'])
index_df = pd.DataFrame(index_metrics, columns=['Ticker', 'Cumulative Return', 'Sharpe Ratio', 'Volatility', 'Sortino Ratio', 'Max Drawdown'])

stock_df = stock_df.set_index('Ticker').T.reset_index()
index_df = index_df.set_index('Ticker').T.reset_index()

print("Stocks Metrics:")
stock_table = tabulate(stock_df, headers='keys', tablefmt='fancy_grid')
print(stock_table)

print("-" * 80)

print("Indices Metrics:")
index_table = tabulate(index_df, headers='keys', tablefmt='fancy_grid')
print(index_table)
```

::: {.output .stream .stdout}
    [*********************100%***********************]  5 of 5 completed
    [*********************100%***********************]  5 of 5 completed
    Stocks Metrics:
    ╒════╤═══════════════════╤═══════════╤═══════════╤═══════════╤═══════════╤════════════╕
    │    │ index             │      AAPL │      AMZN │     GOOGL │      META │       TSLA │
    ╞════╪═══════════════════╪═══════════╪═══════════╪═══════════╪═══════════╪════════════╡
    │  0 │ Cumulative Return │ 26.0834   │ 15.7506   │  6.84373  │  6.28616  │ 103.167    │
    ├────┼───────────────────┼───────────┼───────────┼───────────┼───────────┼────────────┤
    │  1 │ Sharpe Ratio      │  0.936217 │  0.663731 │  0.533089 │  0.338834 │   0.709075 │
    ├────┼───────────────────┼───────────┼───────────┼───────────┼───────────┼────────────┤
    │  2 │ Volatility        │  0.286002 │  0.331799 │  0.272976 │  0.407763 │   0.573807 │
    ├────┼───────────────────┼───────────┼───────────┼───────────┼───────────┼────────────┤
    │  3 │ Sortino Ratio     │  1.56389  │  1.1254   │  0.892236 │  0.556595 │   1.2297   │
    ├────┼───────────────────┼───────────┼───────────┼───────────┼───────────┼────────────┤
    │  4 │ Max Drawdown      │ -0.437972 │ -0.561453 │ -0.443201 │ -0.767361 │  -0.736322 │
    ╘════╧═══════════════════╧═══════════╧═══════════╧═══════════╧═══════════╧════════════╛
    --------------------------------------------------------------------------------
    Indices Metrics:
    ╒════╤═══════════════════╤═══════════╤═══════════╤═══════════════╤═══════════╤═══════════╕
    │    │ index             │       SPY │       QQQ │           UKX │     ^N225 │    ^GDAXI │
    ╞════╪═══════════════════╪═══════════╪═══════════╪═══════════════╪═══════════╪═══════════╡
    │  0 │ Cumulative Return │  4.72015  │  7.86627  │   1.17514     │  2.70831  │  2.63254  │
    ├────┼───────────────────┼───────────┼───────────┼───────────────┼───────────┼───────────┤
    │  1 │ Sharpe Ratio      │  0.633221 │  0.741676 │   0.000523207 │  0.322405 │  0.314389 │
    ├────┼───────────────────┼───────────┼───────────┼───────────────┼───────────┼───────────┤
    │  2 │ Volatility        │  0.172773 │  0.204592 │   3.43898     │  0.201934 │  0.200038 │
    ├────┼───────────────────┼───────────┼───────────┼───────────────┼───────────┼───────────┤
    │  3 │ Sortino Ratio     │  0.975694 │  1.16718  │   0.00513008  │  0.514    │  0.495851 │
    ├────┼───────────────────┼───────────┼───────────┼───────────────┼───────────┼───────────┤
    │  4 │ Max Drawdown      │ -0.337173 │ -0.351187 │ nan           │ -0.317989 │ -0.387794 │
    ╘════╧═══════════════════╧═══════════╧═══════════╧═══════════════╧═══════════╧═══════════╛
:::
:::

::: {#3d4b94d5 .cell .code}
``` python
```
:::
