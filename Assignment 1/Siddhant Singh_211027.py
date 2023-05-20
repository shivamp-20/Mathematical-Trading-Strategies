#!/usr/bin/env python
# coding: utf-8

# In[79]:


import yfinance as yf 
import pandas as pd
import datetime as dt
import matplotlib.pyplot as plt
import numpy as np


# In[80]:


start=dt.datetime(2010,1,1)
end=dt.datetime(2023,5,1)
tickers=['FL','KO','NKE','GOOGL','SPY','^BFX','^N100','^FCHI','^VIX','^XAX']
data=yf.download(tickers,start,end)
df=data['Adj Close']
df.head()


# In[81]:


daily_return=df/df.shift(1)-1


# In[82]:


daily_return.head()


# In[83]:


daily_return.plot()


# In[84]:


cum_return=(1+daily_return).cumprod()-1


# In[85]:


cum_return.head()


# In[86]:


cum_return.plot()


# In[87]:


daily_return.mean()


# In[88]:


sharpe_ratio=daily_return.mean()/daily_return.std()


# In[89]:


sharpe_ratio


# In[90]:


annual_sharpe_ratio=(252**0.5)*sharpe_ratio


# In[91]:


annual_sharpe_ratio


# In[92]:


max_drawdown=(df.max()-df.min())/df.max()


# In[93]:


max_drawdown


# In[ ]:




