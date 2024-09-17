#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np
import yfinance as yf


# In[3]:


indices=["^GSPC", "^DJI", "^IXIC", "^NYA", "^XAX"]
equities=["AAPL", "GOOGL", "MSFT", "AMZN", "TSLA"]
data_i=yf.download(indices, start="2010-01-01", end="2023-05-01")['Adj Close']
data_e=yf.download(equities, start="2010-01-01", end="2023-05-01")['Adj Close']


# In[18]:


returns_i=data_i.pct_change()

cumulative_returns_i=(returns_i+1).cumprod()

volatility_i=returns_i.std()*np.sqrt(252)

rolling_max_i=cumulative_returns_i.rolling(window=len(cumulative_returns_i), min_periods=1).max()
drawdown_i=(cumulative_returns_i/rolling_max_i)-1
max_drawdown_i=drawdown_i.min()

sharpe_ratio_i=(returns_i.mean()-(0.02/252))*np.sqrt(252)/returns_i.std()

nreturns_i=returns_i.copy()
nreturns_i[nreturns_i>0]=0
sortino_ratio_i=(returns_i.mean()-(0.02/252))*np.sqrt(252)/nreturns_i.std()


# In[16]:


print(cumulative_returns_i.iloc[-1])
print(max_drawdown_i)
print(volatility_i)
print(sharpe_ratio_i)
print(sortino_ratio_i)


# In[6]:


returns_e=data_e.pct_change()

cumulative_returns_e=(returns_e+1).cumprod()

volatility_e=returns_e.std()*np.sqrt(252)

rolling_max_e=cumulative_returns_e.rolling(window=len(cumulative_returns_e), min_periods=1).max()
drawdown_e=(cumulative_returns_e/rolling_max_e)-1
max_drawdown_e=drawdown_e.min()

sharpe_ratio_e=(returns_e.mean()-(0.02/252))*np.sqrt(252)/returns_e.std()

nreturns_e=returns_e.copy()
nreturns_e[nreturns_e>0]=0
sortino_ratio_e=(returns_e.mean()-(0.02/252))*np.sqrt(252)/nreturns_e.std()


# In[14]:


print(returns_e)


# In[11]:


print(cumulative_returns_e.iloc[-1])
print(max_drawdown_e)
print(volatility_e)
print(sharpe_ratio_e)
print(sortino_ratio_e)

