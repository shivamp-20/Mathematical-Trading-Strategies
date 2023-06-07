# Mathematical Trading Strategies

Assignment 2

Description: First, I downloaded the historical data of ^IXIC and ^NSEI indices and did some preprocessing of data. Then, I found the lead-lag relationship between the two indices and observed that NSEI index was leading behind IXIC index using the correlation between the two.
 I used IXIC index to optimize the parameters and then used them for NSEI index. After optimizing the parameters for the indicators, I generated buy and sell signals using all 3 indicators. Finally, I calculated cumulative returns, Sharpe ratio and Max Drawdown for NSEI index using the Keltner channel strategy, Bollinger bands strategy and MACD.

|
 | MACD | Bollinger Bands | Keltner Channels |
| --- | --- | --- | --- |
| Cumulative returns | 15.067 % | 25.046 % | 14.034 % |
| Sharpe Ratio | 0.1858 | 0.2045 | 0.4359 |
| Max Drawdown | -31.411 % | -31.185% | -17.672 % |