Mathematical Trading Strategies

Assignment 2

Description: I did the tasks stepwise by taking the historical data for NASDAQ and NSE indices and then calculating the correlation coefficient between their common data. Then an analysis of their lead-lag relationship was established. NASDAQ was found to be the index which can be used to optimize the parameters of the indicators for signal generation. Then, 3 indicators namely were coded using TA-lib in python. They were iterated over a range of parameters and optimized parameters were calculated using brute-force grid search for them. These parameters were then used to calculate the metrics of Assignment-1 for the indicators. Then the index NSE was chosen for Signal Generation analysis using the optimized parameters from the analysis on NASDAQ. 


||MACD|Bollinger Bands|Keltner Channels|
| :-: | :-: | :-: | :-: |
|Cumulative returns|4\.73585828374554|4\.73585828374554|4\.73585828374554|
|Sharpe Ratio|-0.10422264951165501|-0.19336397178882714|-0.22638524681201094|
|Max Drawdown|0\.4501579818218941|0\.4501579818218941|0\.4501579818218941|
