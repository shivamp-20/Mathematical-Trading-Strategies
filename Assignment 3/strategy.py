#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import yfinance as yf
import matplotlib.pyplot as plt

def breakout_strategy(ticker, start_date='2022-01-01', end_date='2022-12-31', breakout_percentage=1):
    # Download historical data
    data = yf.download(ticker, start=start_date, end=end_date)

    # Calculate High and Low Breakout Levels
    data['High_Breakout'] = data['High'].shift(1) * (1 + breakout_percentage / 100)
    data['Low_Breakout'] = data['Low'].shift(1) * (1 - breakout_percentage / 100)

    # Generate Buy and Sell signals based on Breakout
    data['Signal'] = 0
    data.loc[data['High'] > data['High_Breakout'], 'Signal'] = 1  # Buy Signal on breakout above High
    data.loc[data['Low'] < data['Low_Breakout'], 'Signal'] = -1   # Sell Signal on breakout below Low

    return data

def plot_breakout_signals(data):
    plt.figure(figsize=(12, 6))
    plt.plot(data['Close'], label='Close Price')
    plt.plot(data[data['Signal'] == 1].index, data['Close'][data['Signal'] == 1], '^', markersize=10, label='Buy Signal')
    plt.plot(data[data['Signal'] == -1].index, data['Close'][data['Signal'] == -1], 'v', markersize=10, label='Sell Signal')
    plt.title(f'Breakout Strategy for {ticker}')
    plt.legend()
    plt.show()

# Example usage
ticker = 'SUNPHARMA.NS'
breakout_data = breakout_strategy(ticker)
plot_breakout_signals(breakout_data)

