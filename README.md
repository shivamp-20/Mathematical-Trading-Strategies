# Mathematical-Trading-Strategies
Official repo for submission of assignments in Mathematical Trading Strategies


import yfinance as yf
import pandas as pd
import numpy as np
resultData = yf.download(tickers = "^IXIC", start = '2010-03-01', end = '2022-03-01')
resultData.to_csv("^IXIC.csv")


resultData = yf.download(tickers = "NSE" , start = '2010-03-01', end = '2022-03-01')
resultData.to_csv("NSE.csv")

df_stock1 = pd.read_csv('^IXIC.csv')  
df_stock2 = pd.read_csv('NSE.csv') 
closing_prices_stock1 = df_stock1['Close']
closing_prices_stock2 = df_stock2['Close']
correlation_coefficient = closing_prices_stock1.corr(closing_prices_stock2)
print("Correlation Coefficient:", correlation_coefficient)

cross_corr = np.correlate(closing_prices_stock1, closing_prices_stock2 , mode='full')
print("cross_corr:", cross_corr)

import matplotlib.pyplot as plt
lags = np.arange(-len(closing_prices_stock1) + 1, len(closing_prices_stock2))
plt.figure(figsize=(10, 5))
plt.stem(lags, cross_corr)
 
 
 @Explanation
# keltner channe.length equalo 3 makes the three lines close and main line close to NSE.multiplier equal to 1 and atr length 6 will make channel lines super impose to Nse indice line.

# Bolenger bands: length equal to 4 .standard derivative to 1 and offstr equal to 0.

# MACD: length equal to 5 makes all three lines close together . signal smoothing equal to 3 makes graph almost super impose.
#NSE should be used for parameter optimisation.

