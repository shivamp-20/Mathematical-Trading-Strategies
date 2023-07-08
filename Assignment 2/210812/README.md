Mathematical Trading Strategies

Assignment 2

Description: Upon analyzing the correlation and lead-lag relationship between NASDAQ and NIFTY50, we concluded that NIFTY50 is a leading indicator. Hence we performed indicator coding on the NIFTY50 stocks and developed trading strategy separately for each of the following: Keltner Channel, Bollinger Bands, and MACD indicator. Then, we optimized the parameter of each method.

For Keltner Channel, we optimized *lookback period*, *ATR period* and *multiplier*.

For Bollinger Bands, we optimized *moving average window* and the width of band(*num of std deviation*).

For MACD indicator, we optimized *upper*, *lower* and *signal window* to get the best output.

The next step is to apply the strategy with optimized parameters to NASDAQ prices. The following results were obtained:


||MACD|Bollinger Bands|Keltner Channels|
| :-: | :-: | :-: | :-: |
|Cumulative returns|2\.22|1\.91|3\.18|
|Sharpe Ratio|0\.21|0\.16|0\.27|
|Max Drawdown|-58.66%|-66.54%|-60.32%|


