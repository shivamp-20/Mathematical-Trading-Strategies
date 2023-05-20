```python
import yfinance as yf
import pandas as pd
import numpy as np


indices = ['^GSPC', '^IXIC', '^DJI', '^FTSE', '^N225']
equities = ['AAPL', 'GOOGL', 'AMZN', 'MSFT', 'TSLA']


start_date = '2010-01-01'
end_date = '2023-05-01'


data = yf.download(indices + equities, start=start_date, end=end_date)['Adj Close']


returns = data.pct_change()


cumulative_returns = (returns + 1).cumprod()

rolling_max = cumulative_returns.rolling(window=252, min_periods=1).max()
drawdown = cumulative_returns / rolling_max - 1
max_drawdowns = drawdown.min()


annual_returns = returns.mean() * 252
annual_volatility = returns.std() * np.sqrt(252)

# Calculate risk-free rate (considered as 0% here)
risk_free_rate = 0


sharpe_ratio = (annual_returns - risk_free_rate) / annual_volatility


downside_returns = returns.copy()
downside_returns[returns > 0] = 0
downside_deviation = np.sqrt((downside_returns ** 2).mean() * 252)


sortino_ratio = (annual_returns - risk_free_rate) / downside_deviation


metrics = pd.DataFrame(index=['Cumulative Returns', 'Volatility', 'Sharpe Ratio', 'Sortino Ratio', 'Max Drawdown'])


for index, equity in enumerate(indices):
    metrics[equity] = [cumulative_returns[equity][-1], annual_volatility[equity], sharpe_ratio[index], sortino_ratio[index], max_drawdowns[equity]]


print(metrics)
```

    [*********************100%***********************]  10 of 10 completed
                           ^GSPC     ^IXIC      ^DJI     ^FTSE     ^N225
    Cumulative Returns  3.680068  5.296515  3.221683  1.430940  2.708307
    Volatility          0.174741  0.202732  0.169045  0.160128  0.202022
    Sharpe Ratio        0.984535  0.777468  0.654975  0.854683  0.901336
    Sortino Ratio       1.447919  1.156712  0.966143  1.265005  1.370797
    Max Drawdown       -0.339250 -0.357221 -0.370862 -0.350311 -0.312690
    


```python
import yfinance as yf
import pandas as pd
import numpy as np


indices = ['^GSPC', '^IXIC', '^DJI', '^FTSE', '^N225']
equities = ['AAPL', 'GOOGL', 'AMZN', 'MSFT', 'TSLA']


start_date = '2010-01-01'
end_date = '2023-05-01'


data = yf.download(indices + equities, start=start_date, end=end_date)['Adj Close']

returns = data.pct_change()


cumulative_returns = (returns + 1).cumprod()


rolling_max = cumulative_returns.rolling(window=252, min_periods=1).max()
drawdown = cumulative_returns / rolling_max - 1
max_drawdowns = drawdown.min()


annual_returns = returns.mean() * 252
annual_volatility = returns.std() * np.sqrt(252)


risk_free_rate = 0

sharpe_ratio = (annual_returns - risk_free_rate) / annual_volatility

downside_returns = returns.copy()
downside_returns[returns > 0] = 0
downside_deviation = np.sqrt((downside_returns ** 2).mean() * 252)


sortino_ratio = (annual_returns - risk_free_rate) / downside_deviation


metrics = pd.DataFrame(index=['Cumulative Returns', 'Volatility', 'Sharpe Ratio', 'Sortino Ratio', 'Max Drawdown'])


for equity in equities:
    metrics[equity] = [cumulative_returns[equity][-1], annual_volatility[equity], sharpe_ratio[equity], sortino_ratio[equity], max_drawdowns[equity]]


print(metrics)

```

    [*********************100%***********************]  10 of 10 completed
                             AAPL     GOOGL       AMZN       MSFT        TSLA
    Cumulative Returns  26.083424  6.843728  15.750559  13.006321  103.166575
    Volatility           0.281397  0.268572   0.326449   0.257183    0.564560
    Sharpe Ratio         0.984535  0.654975   0.777468   0.854683    0.901336
    Sortino Ratio        1.447919  0.966143   1.156712   1.265004    1.370797
    Max Drawdown        -0.437972 -0.443201  -0.518826  -0.371485   -0.716880
    


```python

```
