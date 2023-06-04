#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import yfinance as yf
import matplotlib.pyplot as plt


# In[2]:


# Define the list of international indices and equities
indices = ['^XAX', '^FCHI', '^RUT', '^DJI', '^KS11']
equities = ['AAPL', 'GOOGL', 'MSFT', 'AMZN', 'RY']


# In[3]:


# Load data for indices and equities
index_data = yf.download(indices, start='2010-01-01', end='2023-05-01')['Adj Close']
equity_data = yf.download(equities, start='2010-01-01', end='2023-05-01')['Adj Close']
print(index_data)
print(equity_data)


# In[4]:


# Calculate daily returns
index_returns = index_data.pct_change()
equity_returns = equity_data.pct_change()
print(index_returns)
print(equity_returns)


# In[5]:


# Calculate cumulative returns
index_cum_returns = index_returns.add(1).cumprod()
equity_cum_returns = equity_returns.add(1).cumprod()


# In[6]:


# Calculate volatility (standard deviation of daily returns)
index_volatility = index_returns.std() * (252 ** 0.5)
equity_volatility = equity_returns.std() * (252 ** 0.5)


# In[7]:


# Calculate maximum drawdowns
index_drawdowns = (index_cum_returns.div(index_cum_returns.cummax()) - 1).min()
equity_drawdowns = (equity_cum_returns.div(equity_cum_returns.cummax()) - 1).min()


# In[8]:


# Calculate Sharpe ratio
risk_free_rate = 0.00
index_excess_returns = index_returns.sub(risk_free_rate)
index_sharpe_ratio = index_excess_returns.mean() / index_volatility

equity_excess_returns = equity_returns.sub(risk_free_rate)
equity_sharpe_ratio = equity_excess_returns.mean() / equity_volatility


# In[9]:


# Calculate Sortino ratio
index_downside_returns = index_returns.where(index_returns < 0, 0)
index_downside_volatility = index_downside_returns.std() * (252 ** 0.5)
index_sortino_ratio = index_excess_returns.mean() / index_downside_volatility

equity_downside_returns = equity_returns.where(equity_returns < 0, 0)
equity_downside_volatility = equity_downside_returns.std() * (252 ** 0.5)
equity_sortino_ratio = equity_excess_returns.mean() / equity_downside_volatility


# In[10]:


# Display the calculated metrics
index_metrics = pd.DataFrame({"Volatility": index_volatility, 
                              "Max Drawdown" : index_drawdowns,
                        'Sharpe Ratio': index_sharpe_ratio,
                        'Sortino Ratio': index_sortino_ratio})
index_metrics.columns = pd.MultiIndex.from_product([index_metrics.columns])
equity_metrics = pd.DataFrame({"Volatility": equity_volatility, 
                              "Max Drawdown" : equity_drawdowns,
                        'Sharpe Ratio': equity_sharpe_ratio,
                        'Sortino Ratio': equity_sortino_ratio})
equity_metrics.columns = pd.MultiIndex.from_product([ equity_metrics.columns])
print("Index Metrics:")
print(index_metrics)
index_cum_returns.plot(title='Cumulative Returns - Indices')
plt.show()

print()
print("Equity Metrics:")
print(equity_metrics)
equity_cum_returns.plot(title='Cumulative Returns - Equities')
plt.show()


# In[ ]:




