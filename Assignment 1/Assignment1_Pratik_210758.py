#!/usr/bin/env python
# coding: utf-8

# In[2]:


import yfinance as yf 
import pandas as pd
import datetime as dt
import matplotlib.pyplot as plt
import numpy as np


# In[28]:


start=dt.datetime(2010,1,1)
end=dt.datetime(2023,5,1)
tickers=['AAPL','AMZN','MSFT','GOOGL','NFLX','^GSPC','^DJI','^IXIC','^NYA','^RUT']
data=yf.download(tickers,start,end)
df=data['Adj Close']
df.head()


# In[29]:


daily_return=df/df.shift(1)-1


# In[30]:


daily_return.head()


# In[31]:


daily_return.plot()


# In[32]:


cum_return=(1+daily_return).cumprod()-1


# In[33]:


cum_return.head()


# In[34]:


cum_return.plot()


# In[35]:


daily_return.mean()


# In[36]:


sharpe_ratio=daily_return.mean()/daily_return.std()


# In[37]:


sharpe_ratio


# In[38]:


annual_sharpe_ratio=(252**0.5)*sharpe_ratio


# In[39]:


annual_sharpe_ratio


# In[40]:


neg_daily_return=daily_return[daily_return<0]


# In[41]:


neg_daily_return.head()


# In[42]:


sortino_ratio=daily_return.mean()/neg_daily_return.std()


# In[43]:


sortino_ratio


# In[44]:


annual_sortino_ratio=(252**0.5)*sortino_ratio


# In[45]:


annual_sortino_ratio


# In[46]:


max_drawdown=(df.max()-df.min())/df.max()


# In[47]:


max_drawdown


# In[ ]:




