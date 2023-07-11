# TRADING STRATEGY

### In this code, I try to implement the trading strategy for the Reliance company.

### Bull Flag pattern and MACD indicator were used to implement the trading strategy.

### In this strategy, talib generates the MACD line and MACD signal line to generate the buy and sell signals for the shares of Reliance.
### The MACD line is calculated by subtracting the 26 day (or in general 26 period) EMA (Exponentially Moving Average) from the 12 day EMA. I take time period as 1 day here. That's why I have mentioned 'day' instead of 'period' in the time limit. The MACD signal line is the EMA of the MACD line for 9 days. When the MACD signal line moves above the MACD line, a selling signal is generated, and when it moves below, a buy signal is generated.

### Next is the Bull Flag pattern, which is founnd generally in uptrending patters and is said to be good for identifying a continuation pattern as well. Bull flags that are 'tighter', are a better indicator of upgrowth as the stock price doesn't vary much on the downside. That's why Bull Flags are better to show uptrend, which will be further helpful in generating sellig signals.
### In my code, I try to implement that the Bull Flag pattern is detected when the height of the flagpole is at least 20% of the range, and the closing price is above the halfway point within the range of the 20 day rolling window.

### In the combined strategy, when the MACD line is above MACD signal line, a buy signal is generated. But, when the MACD signal line is above MACD line, as well as the Bull Flag is detected, only then a selling signal is generated. That's why I have eased up on the 20% criteria for the Bull flag pattern detection.

### The value of the parameters at the end of the 10 year period is:
- **Cummulative returns: 3.87717434**
- **Sharpe Ratio: 0.0159880**
- **Max Drawdowns: -0.13383110** 
