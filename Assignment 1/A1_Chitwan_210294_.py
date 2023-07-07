#!/usr/bin/env python
# coding: utf-8

# In[2]:


import yfinance as yf 
import pandas as pd
import datetime as dt
import matplotlib.pyplot as plt
import numpy as np


# In[3]:


start=dt.datetime(2010,1,1)
end=dt.datetime(2023,5,1)
tickers=['KO','AMZN','FL','GOOGL','NFLX','^GSPC','^GDAXI','^IXIC','^FTSE','^VIX']
data=yf.download(tickers,start,end)
df=data['Adj Close']
df.head()


# In[4]:


daily_return=df/df.shift(1)-1


# In[5]:


daily_return.head()


# In[6]:


daily_return.plot()


# In[7]:


cum_return=(1+daily_return).cumprod()-1


# In[8]:


cum_return.head()


# In[9]:


cum_return.plot()


# In[10]:


daily_return.mean()


# In[11]:


sharpe_ratio=daily_return.mean()/daily_return.std()


# In[12]:


sharpe_ratio


# In[13]:


annual_sharpe_ratio=(252**0.5)*sharpe_ratio


# In[14]:


annual_sharpe_ratio


# In[15]:


neg_daily_return=daily_return[daily_return<0]


# In[16]:


neg_daily_return.head()


# In[17]:


sortino_ratio=daily_return.mean()/neg_daily_return.std()


# In[18]:


sortino_ratio


# In[19]:


annual_sortino_ratio=(252**0.5)*sortino_ratio


# In[20]:


annual_sortino_ratio


# In[21]:


max_drawdown=(df.max()-df.min())/df.max()


# In[22]:


max_drawdown


# In[ ]:





# In[ ]:





# In[ ]:




