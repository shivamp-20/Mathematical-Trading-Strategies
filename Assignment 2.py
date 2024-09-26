#!/usr/bin/env python
# coding: utf-8

# In[183]:


import yfinance as yf
import pandas as pd
import numpy as np
nasdaq_data = yf.download(tickers = "^IXIC", start = '2021-05-23', end = '2023-05-23')
df=nasdaq_data['Close']
print(df)
df.to_numpy()


# In[184]:


nse_data = yf.download(tickers = "^NSEI" , start = '2021-05-23', end = '2023-06-01')
dfh=nse_data['Close']
print(dfh)
dfh.to_numpy()


# In[185]:


correlation_coef = np.corrcoef(dfh,df)[0, 1]
print("Correlation Coefficient:", correlation_coef)


# In[186]:


cross_corr = np.correlate(closing_prices_stock1, closing_prices_stock2 , mode='full')
print("cross_corr:", cross_corr)


# In[187]:


import matplotlib.pyplot as plt
fig, ax = plt.subplots()

ax.plot(df,color='blue', label='index1')

ax.plot(dfh,color='green', label='index2')

ax.set_title('Comparison of Index 1 and Index 2')
ax.set_xlabel('Time')
ax.set_ylabel('Index Value')

ax.legend()

plt.show()


# In[188]:


#keltner channe.length equalo 3 makes the three lines close and main line close to NSE.multiplier equal to 1 and atr length 6 will make channel lines super impose to Nse indice line.

# Bolenger bands: length equal to 4 .standard derivative to 1 and offstr equal to 0.

# MACD: length equal to 5 makes all three lines close together . signal smoothing equal to 3 makes graph almost super impose.
#NSE should be used for parameter optimisation.


# In[189]:


def get_kc(high, low, close, kc_lookback, multiplier,atr_lookback):
    tr1 = pd.DataFrame(high - low)
    tr2 = pd.DataFrame(abs(high - close.shift()))
    tr3 = pd.DataFrame(abs(low - close.shift()))
    frames = [tr1, tr2, tr3]
    tr = pd.concat(frames, axis=1, join='inner').max(axis=1)
    atr = tr.ewm(alpha=1/atr_lookback).mean()

    kc_middle = close.ewm(kc_lookback).mean()
    kc_upper = close.ewm(kc_lookback).mean() + multiplier * atr
    kc_lower = close.ewm(kc_lookback).mean() - multiplier * atr

    return kc_middle, kc_upper, kc_lower

nasdaq_data['kc_middle'], nasdaq_data['kc_upper'], nasdaq_data['kc_lower'] = get_kc(nasdaq_data['High'], nasdaq_data['Low'], nasdaq_data['Close'], 20, 2,10)
print(nasdaq_data.tail())
kc_middle = nasdaq_data['kc_middle']
kc_upper = nasdaq_data['kc_upper']
kc_lower = nasdaq_data['kc_lower']


nasdaq_data['signal2'] = 0


nasdaq_data.loc[nasdaq_data['Close'] > kc_upper, 'signal2'] = -1  
nasdaq_data.loc[nasdaq_data['Close'] < kc_lower, 'signal2'] = 1

plt.figure(figsize=(10, 6))
plt.plot(nasdaq_data['Close'], label='Close Price')
plt.plot(nasdaq_data.loc[nasdaq_data['signal2'] == 1, 'Close'], 'go', label='Buy Signal')
plt.plot(nasdaq_data.loc[nasdaq_data['signal2'] == -1, 'Close'], 'ro', label='Sell Signal')
plt.plot(kc_middle, 'b--', label='kc Middle')
plt.plot(kc_upper, 'r--', label='kc Upper')
plt.plot(kc_lower, 'g--', label='kc Lower')
plt.xlabel('Date')
plt.ylabel('Price')
plt.title('Buy and Sell Signals using keltner channel')
plt.legend()
plt.show()


# In[199]:


window_size = 20
std_dev = 2

rolling_mean = nasdaq_data['Close'].rolling(window=window_size).mean()
rolling_std = nasdaq_data['Close'].rolling(window=window_size).std()

bb_upper = rolling_mean + (std_dev * rolling_std)
bb_lower = rolling_mean - (std_dev * rolling_std)

signals = []
for i in range(len(nasdaq_data)):
    if nasdaq_data['Close'][i] > upper_band[i]:
        signals.append(-1)  
    elif nasdaq_data['Close'][i] < lower_band[i]:
        signals.append(1)  
    else:
        signals.append(0)
plt.figure(figsize=(10, 6))
plt.plot(nasdaq_data['Close'], label='Close Price')
plt.plot(nasdaq_data.loc[nasdaq_data['signal2'] == 1, 'Close'], 'go', label='Buy Signal')
plt.plot(nasdaq_data.loc[nasdaq_data['signal2'] == -1, 'Close'], 'ro', label='Sell Signal')
plt.plot(bb_upper, 'r--', label='bb Upper')
plt.plot(bb_lower, 'g--', label='bb Lower')
plt.xlabel('Date')
plt.ylabel('Price')
plt.title('Buy and Sell Signals using bolingel bandIndicator')
plt.legend()
plt.show()


# In[200]:


nasdaq_data['Signal'] = nasdaq_data.apply(bollinger_strategy, axis=1)
nasdaq_data['Daily Returns'] = nasdaq_data['Close'].pct_change() * nasdaq_data['Signal'].shift()

nasdaq_data['Cumulative Returns'] = (1 + nasdaq_data['Daily Returns']).cumprod()


# In[ ]:




