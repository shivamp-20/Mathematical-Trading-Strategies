import yfinance as yf
import matplotlib.pyplot as plt

data = yf.download('AAPL',start='2022-01-01',end='2023-06-04')

closing_prices = data['Close'].values.tolist()


ema_values1 = []
ema_values2 = []
signal=[]

window1 = 12# Number of days for EMA calculation
window2 = 26
window3 = 9
smoothing = 2  # Smoothing factor
ema_yesterday = closing_prices[0]  # Initialize EMA with the first closing price
for price in closing_prices:
        ema_today = (price * smoothing/(1 + window1)) + (ema_yesterday * (1 - (smoothing)/(1+window1)))
        ema_values1.append(ema_today)
        ema_yesterday = ema_today
ema_yesterday = closing_prices[0]  # Initialize EMA with the first closing price
for price in closing_prices:
        ema_today = (price * smoothing/(1 + window2)) + (ema_yesterday * (1 - (smoothing)/(1+window2)))
        ema_values2.append(ema_today)
        ema_yesterday = ema_today
macd=[]
prices=[]
for i in range(len(ema_values1)):
    macd.append(ema_values1[i]-ema_values2[i])
    prices.append(closing_prices[i])
ema_yesterday = macd[0]  # Initialize EMA with the first closing price
for price in macd:
        ema_today = (price * smoothing/(1 + window3)) + (ema_yesterday * (1 - (smoothing)/(1+window3)))
        signal.append(ema_today)
        ema_yesterday = ema_today
s1=[]    
for i in range(len(macd)):
    s1.append(macd[i]-signal[i])
    
# Create a figure and plot the MACD histogram
plt.figure(figsize=(12, 6))

plt.plot(data.index, macd, label='MACD Line', color='blue')
plt.plot(data.index, signal, label='Signal Line', color='orange')
plt.bar(data.index, s1, width=1, alpha=1, label='Histogram', color='gray')

plt.axhline(y=0, color='black', linestyle='--')
plt.legend()
plt.title('MACD Indicator')
plt.xlabel('Date')
plt.ylabel('MACD')

plt.show()    
# buy=[]
# sell=[]
# b=sl=0
# for i in range(len(macd)):
#     if macd[i]<signal[i] and macd[i-1]>signal[i]:
#         buy.append(prices[i])
#         sl+=1
#     elif macd[i]>signal[i] and macd[i-1]<signal[i]:
#         sell.append(prices[i])    
#         b+=1

# if sell[0] < buy[0]:
#     sell.remove(sell[0])
# if b>sl:
#     buy.remove(buy[-1])    
    
    
# returns=[]
# for i in range(len(sell)):
#     returns.append((sell[i]-buy[i]))


# sum=0

# for p in returns:
#     sum = sum+p

    

# print(closing_prices[-1]- closing_prices[0])
# # print(returns)
# print(sum)    

