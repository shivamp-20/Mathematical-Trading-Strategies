import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

data = yf.download('AAPL',start='2022-01-01',end='2023-01-01')

def calculate_exponential_moving_average(closing_prices, window, smoothing):
    ema_values = []
    ema_yesterday = closing_prices[0]  # Initialize EMA with the first closing price

    for price in closing_prices:
        ema_today = (price * smoothing/(1 + window)) + (ema_yesterday * (1 - (smoothing)/(1+window)))
        ema_values.append(ema_today)
        ema_yesterday = ema_today

    return ema_values


closing_prices = data['Close'].values.tolist()
high_prices = data['High'].tolist()
low_prices = data['Low'].tolist()

data['ranges'] = data['High'] - data['Low']
# print(data['ranges'])
ranges = data['ranges'].values.tolist()

series = pd.Series(ranges)

moving_average = series.rolling(window=10).mean()

# print(moving_average)
ema_values=calculate_exponential_moving_average(closing_prices, 10, 2)

plt.figure(figsize=(10, 6))
plt.plot(data.index, closing_prices, label='Stock Price')
plt.plot(data.index, ema_values, label=f'Keltner Channel Middle Line')
plt.plot(data.index, ema_values-2*moving_average, label=f'Keltner Channel Lower Band')
plt.plot(data.index, ema_values+2*moving_average, label=f'Keltner Channel Upper Band')
plt.xlabel('Date')
plt.ylabel('Price')
plt.title(f'fac Stock Price with Exponential Moving Average (EMA)')
plt.legend()
plt.xticks(rotation=45)
plt.grid(True)
plt.show()


