#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path
from warnings import simplefilter
import yfinance as yf


# In[38]:


data_nse=yf.download('^NSEI', start="2010-01-01", end="2023-05-31")['Adj Close']
data_nasdaq=yf.download('^IXIC', start="2010-01-01", end="2023-05-31")['Adj Close']

correlation=data_nse.corr(data_nasdaq)
print(correlation)


# In[3]:


get_ipython().system('pip install scikit-learn')


# In[39]:


combined_data=pd.concat([data_nse, data_nasdaq], axis=1)
combined_data.columns=['NSE', 'NASDAQ']
combined_data['NASDAQ_lag']=combined_data['NASDAQ'].shift(1)
print(combined_data.head())

from sklearn.linear_model import LinearRegression
X=combined_data.loc[:,['NASDAQ_lag']]
X.dropna(inplace=True)
y=combined_data.loc[:,'NSE']
y.dropna(inplace=True)
y,X=y.align(X, join='inner')
model = LinearRegression()
model.fit(X, y)
y_pred = pd.Series(model.predict(X), index=X.index)

#ax = y.plot(**plot_params)
plt.figure(figsize=(10, 6))
plt.plot(combined_data['NSE'], label='NSE')
plt.plot(y_pred, label='NSE_predicted')
plt.xlabel('Date')
plt.ylabel('Adjusted Close Price')
#plt.title('NSE vs NASDAQ')
plt.legend()
plt.grid(True)
plt.show()


# In[40]:


combined_data['NSE_lag']=combined_data['NSE'].shift(11)

from sklearn.linear_model import LinearRegression
X=combined_data.loc[:,['NSE_lag']]
X.dropna(inplace=True)
y=combined_data.loc[:,'NASDAQ']
y.dropna(inplace=True)
y,X=y.align(X, join='inner')
model = LinearRegression()
model.fit(X, y)
y_pred = pd.Series(model.predict(X), index=X.index)

plt.figure(figsize=(10, 6))
plt.plot(combined_data['NASDAQ'], label='NASDAQ')
plt.plot(y_pred, label='NASDAQ_predicted')
plt.xlabel('Date')
plt.ylabel('Adjusted Close Price')
#plt.title('NSE vs NASDAQ')
plt.legend()
plt.grid(True)
plt.show()


# In[41]:


print(combined_data['NSE'].corr(combined_data['NASDAQ_lag']))
print(combined_data['NASDAQ'].corr(combined_data['NSE_lag']))

Since there is a higher correlation between NSE and NASDAQ lag, which means NSE leads NASDAQ.
# In[2]:


get_ipython().system('pip install statsmodels')


# In[28]:


from statsmodels.tsa.stattools import grangercausalitytests


# In[29]:


data_r=pd.concat([combined_data['NSE'], combined_data['NASDAQ']], axis=1).dropna()
data_r.head()


# In[30]:


result = grangercausalitytests(data_r, maxlag=10, verbose=False)
result


# In[31]:


for lag in result.keys():
    p_value = result[lag][0]['ssr_chi2test'][1]
    if p_value < 0.05:
        print(f"Lag {lag}: NSE leads NASDAQ (p-value: {p_value})")
    else:
        print(f"Lag {lag}: NASDAQ leads NSE (p-value: {p_value})")

Using Granger causality tests we infer that NSE leads NASDAQ
# In[32]:


nasdaq_prices = combined_data['NASDAQ'].values
nse_prices = combined_data['NSE'].values


# In[33]:


cross_corr = np.correlate(nasdaq_prices, nse_prices, mode='full')


# In[34]:


lags = np.arange(-len(nasdaq_prices) + 1, len(nasdaq_prices))


# In[35]:


import matplotlib.pyplot as plt
plt.figure(figsize=(10, 5))
plt.plot(lags, cross_corr)
plt.xlabel('Lag')
plt.ylabel('Cross-correlation')
plt.title('Cross-correlation between NASDAQ and NSE')
plt.grid(True)
plt.show()

Here we observe a graph with a positive slope, positive cross-correlation values on the y-axis, and negative lags on the x-axis, it suggests that the index on the y-axis (in this case, NSE) leads the index on the x-axis (NASDAQ).
Therefore, based on the graph, we can conclude that NSE leads NASDAQ. The positive cross-correlation values further support the lead of NSE over NASDAQ. 
# In[2]:


data=yf.download('^NSEI', start="2010-01-01", end="2023-05-30")


# # Keltner Channel

# In[3]:


atr_period=16
data['TR']=data['High']-data['Low']
data['H_L']=abs(data['High']-data['Low']).shift(1)
data['H_PC']=abs(data['High']-data['Close']).shift(1)
data['L_PC']=abs(data['Low']-data['Close']).shift(1)
data['TR']=data[['H_L', 'H_PC', 'L_PC']].max(axis=1)
data['ATR']=data['TR'].rolling(window=atr_period).mean()

ema_period = 25
data['EMA'] = data['Close'].ewm(span=ema_period, adjust=False).mean()

data['KC_L']=data['EMA']-(2*data['ATR'])
data['KC_M']=data['EMA']
data['KC_U']=data['EMA']+(2*data['ATR'])

plt.figure(figsize=(25,12.5))
plt.plot(data.loc['2018-01-01':,'Close'], label='NSE Index')
plt.plot(data.loc['2018-01-01':,'KC_L'], label='KC_L')
plt.plot(data.loc['2018-01-01':,'KC_M'], label='KC_M')
plt.plot(data.loc['2018-01-01':,'KC_U'], label='KC_U')
plt.xlabel('Date')
plt.ylabel('Price')
plt.title('NSE Index with Kelter Channel')
plt.legend()
plt.grid(True)
plt.show()


# In[4]:


def implement_kc_strategy(prices, kc_upper, kc_lower):
    buy_price = []
    sell_price = []
    kc_signal = []
    signal = 0
    
    for i in range(len(prices)-1):
        if prices[i] < kc_lower[i] and prices[i+1] > prices[i]:
            if signal != 1:
                buy_price.append(prices[i])
                sell_price.append(np.nan)
                signal = 1
                kc_signal.append(signal)
            else:
                buy_price.append(np.nan)
                sell_price.append(np.nan)
                kc_signal.append(0)
        elif prices[i] > kc_upper[i] and prices[i+1] < prices[i]:
            if signal != -1:
                buy_price.append(np.nan)
                sell_price.append(prices[i])
                signal = -1
                kc_signal.append(signal)
            else:
                buy_price.append(np.nan)
                sell_price.append(np.nan)
                kc_signal.append(0)
        else:
            buy_price.append(np.nan)
            sell_price.append(np.nan)
            kc_signal.append(0)
            
    return buy_price, sell_price, kc_signal

buy_price, sell_price, kc_signal = implement_kc_strategy(data['Close'], data['KC_U'], data['KC_L'])
buy_price.append(np.nan)
sell_price.append(np.nan)
kc_signal.append(0)


# In[5]:


plt.figure(figsize=(20,8.5))
plt.plot(data['Close'], linewidth=1, label='NSE')
plt.plot(data['KC_U'], linewidth=1, color='orange', linestyle='--', label='KC UPPER 20')
plt.plot(data['KC_M'], linewidth=0.75, color='grey', label='KC MIDDLE 20')
plt.plot(data['KC_L'], linewidth=1, color='orange', linestyle='--', label='KC LOWER 20')
plt.plot(data.index, buy_price, marker = '^', color = 'green', label = 'BUY SIGNAL', markersize=7)
plt.plot(data.index, sell_price, marker = 'v', color= 'r', label = 'SELL SIGNAL', markersize=7)
plt.legend(loc = 'lower right')
plt.title('NSE KELTNER CHANNEL 20 TRADING SIGNALS')
plt.show()


# In[6]:


position = []
for i in range(len(kc_signal)):
    if kc_signal[i] > 1:
        position.append(0)
    else:
        position.append(1)
        
for i in range(len(data['Close'])):
    if kc_signal[i] == 1:
        position[i] = 1
    elif kc_signal[i] == -1:
        position[i] = 0
    else:
        position[i] = position[i-1]
        
close_price = data['Close']
kc_upper = data['KC_U']
kc_lower = data['KC_L']
kc_signal = pd.DataFrame(kc_signal).rename(columns = {0:'kc_signal'}).set_index(data.index)
position = pd.DataFrame(position).rename(columns = {0:'kc_position'}).set_index(data.index)

frames = [close_price, kc_upper, kc_lower, kc_signal, position]
strategy = pd.concat(frames, join = 'inner', axis = 1)

strategy


# In[7]:


import math
from termcolor import colored as cl

NSE_ret = pd.DataFrame(np.diff(data['Close'])).rename(columns = {0:'returns'})
kc_strategy_ret = []

for i in range(len(NSE_ret)):
    returns = NSE_ret['returns'][i]*strategy['kc_position'][i]
    kc_strategy_ret.append(returns)
    
kc_strategy_ret_df = pd.DataFrame(kc_strategy_ret).rename(columns = {0:'kc_returns'})
investment_value = 100000
number_of_stocks = math.floor(investment_value/data['Close'][0])
kc_investment_ret = []

for i in range(len(kc_strategy_ret_df['kc_returns'])):
    returns = number_of_stocks*kc_strategy_ret_df['kc_returns'][i]
    kc_investment_ret.append(returns)

kc_investment_ret_df = pd.DataFrame(kc_investment_ret).rename(columns = {0:'investment_returns'})
total_investment_ret = round(sum(kc_investment_ret_df['investment_returns']), 2)
profit_percentage = math.floor((total_investment_ret/investment_value)*100)
print(cl('Profit gained from the KC strategy by investing $100k in INTC : {}'.format(total_investment_ret), attrs = ['bold']))
print(cl('Profit percentage of the KC strategy : {}%'.format(profit_percentage), attrs = ['bold']))


# In[8]:


returns=kc_investment_ret_df['investment_returns']/1000
cum_ret_c=0
cum_returns=[]
for i in range(len(kc_investment_ret_df)):
    if (i==0): 
        cum_returns.append(returns[0])
        cum_ret_c+=returns[0]
    else: 
        cum_ret_c+=returns[i]
        cum_returns.append(cum_ret_c)
cum_returns_df=pd.DataFrame(cum_returns).rename(columns = {0:'cum_returns'})
print(cum_returns_df.iloc[-1])

volatility=returns.std()*np.sqrt(252)
print(volatility)

rolling_max=cum_returns_df.rolling(window=len(cum_returns_df), min_periods=1).max()
drawdown=(cum_returns_df/rolling_max)-1
max_drawdown=drawdown.min()
print(max_drawdown)

sharpe_ratio=(returns.mean()-(0.02/252))*np.sqrt(252)/returns.std()
print(sharpe_ratio)


# # Bollinger Bands

# In[185]:


sma_period=25
data['TP']=(data['High']+data['Low']+data['Close'])/3
data['SMA']=data['TP'].rolling(window=sma_period).mean()
data['BOL_U']=data['SMA']+(0.1*data['TP'].std())
data['BOL_L']=data['SMA']-(0.1*data['TP'].std())

plt.figure(figsize=(25, 12.5))
plt.plot(data['Close'], label='NSE Index')
plt.plot(data['SMA'], label='BOL_M')
plt.plot(data['BOL_U'], label='BOL_U')
plt.plot(data['BOL_L'], label='BOL_L')
plt.xlabel('Date')
plt.ylabel('Price')
plt.title('NSE Index with BOL')
plt.legend()
plt.grid(True)
plt.show()


# In[176]:


def implement_bb_strategy(data):
    buy_price = []
    sell_price = []
    bb_signal = []
    signal = 0
    
    for i in range(len(data)):
        if data['Close'][i-1] > data['BOL_L'][i-1] and data['Close'][i] < data['BOL_L'][i]:
            if signal != 1:
                buy_price.append(data['Close'][i])
                sell_price.append(np.nan)
                signal = 1
                bb_signal.append(signal)
            else:
                buy_price.append(np.nan)
                sell_price.append(np.nan)
                bb_signal.append(0)
        elif data['Close'][i-1] < data['BOL_U'][i-1] and data['Close'][i] > data['BOL_U'][i]:
            if signal != -1:
                buy_price.append(np.nan)
                sell_price.append(data['Close'][i])
                signal = -1
                bb_signal.append(signal)
            else:
                buy_price.append(np.nan)
                sell_price.append(np.nan)
                bb_signal.append(0)
        else:
            buy_price.append(np.nan)
            sell_price.append(np.nan)
            bb_signal.append(0)
            
    return buy_price, sell_price, bb_signal

buy_price, sell_price, bb_signal = implement_bb_strategy(data)


# In[177]:


plt.figure(figsize=(25, 12.5))
data['Close'].plot(label = 'CLOSE PRICES', alpha = 0.9)
data['BOL_L'].plot(label = 'UPPER BB', linestyle = '--', linewidth = 3, color = 'black')
data['SMA'].plot(label = 'MIDDLE BB', linestyle = '--', linewidth = 3.2, color = 'grey')
data['BOL_U'].plot(label = 'LOWER BB', linestyle = '--', linewidth = 3, color = 'black')
plt.scatter(data.index, buy_price, marker = '^', color = 'green', label = 'BUY', s = 200)
plt.scatter(data.index, sell_price, marker = 'v', color = 'red', label = 'SELL', s = 200)
plt.title('NSE BB STRATEGY TRADING SIGNALS')
plt.legend(loc = 'upper left')
plt.show()


# In[178]:


position = []
for i in range(len(bb_signal)):
    if bb_signal[i] > 1:
        position.append(0)
    else:
        position.append(1)
        
for i in range(len(data['Close'])):
    if bb_signal[i] == 1:
        position[i] = 1
    elif bb_signal[i] == -1:
        position[i] = 0
    else:
        position[i] = position[i-1]
        
upper_bb = data['BOL_U']
lower_bb = data['BOL_L']
close_price = data['Close']
bb_signal = pd.DataFrame(bb_signal).rename(columns = {0:'bb_signal'}).set_index(data.index)
position = pd.DataFrame(position).rename(columns = {0:'bb_position'}).set_index(data.index)

frames = [close_price, upper_bb, lower_bb, bb_signal, position]
strategy = pd.concat(frames, join = 'inner', axis = 1)
#strategy = strategy.reset_index().drop('date', axis = 1)

strategy


# In[179]:


NSE_ret_bb = pd.DataFrame(np.diff(data['Close'])).rename(columns = {0:'returns'})
bb_strategy_ret = []

for i in range(len(NSE_ret_bb)):
    try:
        returns = NSE_ret_bb['returns'][i]*strategy['bb_position'][i]
        bb_strategy_ret.append(returns)
    except:
        pass
    
bb_strategy_ret_df = pd.DataFrame(bb_strategy_ret).rename(columns = {0:'bb_returns'})

investment_value = 100000
number_of_stocks = math.floor(investment_value/data['Close'][-1])
bb_investment_ret = []

for i in range(len(bb_strategy_ret_df['bb_returns'])):
    returns = number_of_stocks*bb_strategy_ret_df['bb_returns'][i]
    bb_investment_ret.append(returns)

bb_investment_ret_df = pd.DataFrame(bb_investment_ret).rename(columns = {0:'investment_returns'})
total_investment_ret = round(sum(bb_investment_ret_df['investment_returns']), 2)
profit_percentage = math.floor((total_investment_ret/investment_value)*100)
print(cl('Profit gained from the BB strategy by investing $100k in TSLA : {}'.format(total_investment_ret), attrs = ['bold']))
print(cl('Profit percentage of the BB strategy : {}%'.format(profit_percentage), attrs = ['bold']))


# In[183]:


returns=bb_investment_ret_df['investment_returns']/1000
cum_ret_c=0
cum_returns=[]
for i in range(len(bb_investment_ret_df)):
    if (i==0): 
        cum_returns.append(returns[0])
        cum_ret_c+=returns[0]
    else: 
        cum_ret_c+=returns[i]
        cum_returns.append(cum_ret_c)
cum_returns_df=pd.DataFrame(cum_returns).rename(columns = {0:'cum_returns'})
print(cum_returns_df.iloc[-1])

volatility=returns.std()*np.sqrt(252)
print(volatility)

rolling_max=cum_returns_df.rolling(window=len(cum_returns_df), min_periods=1).max()
drawdown=(cum_returns_df/rolling_max)-1
max_drawdown=drawdown.min()
print(max_drawdown)

sharpe_ratio=(returns.mean()-(0.02/252))*np.sqrt(252)/returns.std()
print(sharpe_ratio)


# # MACD

# In[8]:


data['MACD']=data['Close'].ewm(span=15).mean()-data['Close'].ewm(span=50).mean()
data['Signal']=data['MACD'].ewm(span=10).mean()
data['Histogram']=data['MACD']-data['Signal']

plt.figure(figsize=(50, 25))
plt.plot(data['Close'])


plt.legend(loc = 'lower right')
plt.ylabel('Price')
plt.title('NSE')
plt.legend()
plt.grid(True)
plt.show()

plt.figure(figsize=(50, 10))
plt.plot(data['MACD'], color = 'grey', linewidth = 0.5, label = 'MACD')
plt.plot(data['Signal'], color = 'skyblue', linewidth = 0.5, label = 'SIGNAL')

for i in range(len(data['Histogram'])):
    if str(data['Histogram'][i])[0] == '-':
        plt.bar(data['Close'].index[i], data['Histogram'][i], color = '#ef5350')
    else:
        plt.bar(data['Close'].index[i], data['Histogram'][i], color = '#26a69a')

plt.legend(loc = 'lower right')
plt.ylabel('MACD indicator')
plt.title('MACD')
plt.legend()
plt.grid(True)
plt.show()


# In[9]:


def implement_macd_strategy(data):    
    buy_price = []
    sell_price = []
    macd_signal = []
    signal = 0

    for i in range(len(data)):
        if data['MACD'][i] > data['Signal'][i]:
            if signal != 1:
                buy_price.append(data['Close'][i])
                sell_price.append(np.nan)
                signal = 1
                macd_signal.append(signal)
            else:
                buy_price.append(np.nan)
                sell_price.append(np.nan)
                macd_signal.append(0)
        elif data['MACD'][i] < data['Signal'][i]:
            if signal != -1:
                buy_price.append(np.nan)
                sell_price.append(data['Close'][i])
                signal = -1
                macd_signal.append(signal)
            else:
                buy_price.append(np.nan)
                sell_price.append(np.nan)
                macd_signal.append(0)
        else:
            buy_price.append(np.nan)
            sell_price.append(np.nan)
            macd_signal.append(0)
            
    return buy_price, sell_price, macd_signal
            
buy_price, sell_price, macd_signal = implement_macd_strategy(data)


# In[10]:


plt.figure(figsize=(25, 12.5))
plt.plot(data['Close'], color = 'skyblue', linewidth = 2, label = 'NSE')
plt.plot(data.index, buy_price, marker = '^', color = 'green', markersize = 10, label = 'BUY SIGNAL', linewidth = 0)
plt.plot(data.index, sell_price, marker = 'v', color = 'r', markersize = 10, label = 'SELL SIGNAL', linewidth = 0)
#plt.legend()
plt.title('NSE BUY SELL INDICATOR')

plt.legend(loc = 'lower right')
plt.show()

plt.figure(figsize=(50, 10))
plt.plot(data['MACD'], color = 'grey', linewidth = 0.5, label = 'MACD')
plt.plot(data['Signal'], color = 'skyblue', linewidth = 0.5, label = 'SIGNAL')

for i in range(len(data['Histogram'])):
    if str(data['Histogram'][i])[0] == '-':
        plt.bar(data['Close'].index[i], data['Histogram'][i], color = '#ef5350')
    else:
        plt.bar(data['Close'].index[i], data['Histogram'][i], color = '#26a69a')
plt.title('MACD SIGNALS')        
plt.legend(loc = 'lower right')
plt.show()


# In[11]:


position = []
for i in range(len(data['Signal'])):
    if macd_signal[i] > 1:
        position.append(0)
    else:
        position.append(1)
        
for i in range(len(data['Close'])):
    if macd_signal[i] == 1:
        position[i] = 1
    elif macd_signal[i] == -1:
        position[i] = 0
    else:
        position[i] = position[i-1]
        
macd = data['MACD']
signal = data['Signal']
close_price = data['Close']
macd_signal = pd.DataFrame(macd_signal).rename(columns = {0:'macd_signal'}).set_index(data.index)
position = pd.DataFrame(position).rename(columns = {0:'macd_position'}).set_index(data.index)

frames = [close_price, macd, signal, macd_signal, position]
strategy = pd.concat(frames, join = 'inner', axis = 1)

strategy


# In[49]:


get_ipython().system('pip install termcolor')


# In[57]:


NSE_ret = pd.DataFrame(np.diff(data['Close'])).rename(columns = {0:'returns'})
macd_strategy_ret = []
for i in range(len(NSE_ret)):
    try:
        returns = NSE_ret['returns'][i]*strategy['macd_position'][i]
        macd_strategy_ret.append(returns)
    except:
        pass
    
macd_strategy_ret_df = pd.DataFrame(macd_strategy_ret).rename(columns = {0:'macd_returns'})

investment_value = 100000
number_of_stocks = math.floor(investment_value/data['Close'][0])
macd_investment_ret = []

for i in range(len(macd_strategy_ret_df['macd_returns'])):
    returns = number_of_stocks*macd_strategy_ret_df['macd_returns'][i]
    macd_investment_ret.append(returns)
   
macd_investment_ret_df = pd.DataFrame(macd_investment_ret).rename(columns = {0:'investment_returns'})
total_investment_ret = round(sum(macd_investment_ret_df['investment_returns']), 2) 
profit_percentage = math.floor((total_investment_ret/investment_value)*100)
print(cl('Profit gained from the MACD strategy by investing Rs 100k in NSE : {}'.format(total_investment_ret), attrs = ['bold']))
print(cl('Profit percentage of the MACD strategy : {}%'.format(profit_percentage), attrs = ['bold']))


# In[105]:


returns=macd_investment_ret_df['investment_returns']/1000
cum_ret_c=0
cum_returns=[]
for i in range(len(NSE_ret)):
    if (i==0): 
        cum_returns.append(returns[0])
        cum_ret_c+=returns[0]
    else: 
        cum_ret_c+=returns[i]
        cum_returns.append(cum_ret_c)
cum_returns_df=pd.DataFrame(cum_returns).rename(columns = {0:'cum_returns'})
print(cum_returns_df.iloc[-1])

volatility=returns.std()*np.sqrt(252)
print(volatility)

rolling_max=cum_returns_df.rolling(window=len(cum_returns_df), min_periods=1).max()
drawdown=(cum_returns_df/rolling_max)-1
max_drawdown=drawdown.min()
print(max_drawdown)

sharpe_ratio=(returns.mean()-(0.02/252))*np.sqrt(252)/returns.std()
print(sharpe_ratio)

