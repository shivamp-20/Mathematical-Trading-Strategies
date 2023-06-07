Mathematical Trading Strategies

Assignment 2

Correlation Analysis:
 NASDAQ and NSE indices show a strong positive correlation of around 0.95 in the given time period.

 Lead-Lag Relationship:
  Correlation coefficient of NASDAQ[i] and NSE[i+x], 20 > x > 0 is greater than that for x = 0. While its less when x<0. Thus, NASDAQ leads NSE consistently.
  NASDAQ-NSE have a leading-lagging relation.
  Since, the price movement is more likely to be reflected in NASDAQ first, it should be chosen for parameter optimisation.

Parameter Optimisation:
 These parameters were optimised on NASDAQ and not directly by generating signals on NASDAQ and trading on NSE which would have given better results. In some cases the cumulative returns were maximum for very low spans in EMA or ATR. I rejected those and took a span of atleast 10. I used brute force to iterate over all cases.

 MACD:- 10, 29, 7
 Bollinger:- 15, 2.5
 Keltner:- 16, 10, 3


||MACD|Bollinger Bands|Keltner Channels|
| :-: | :-: | :-: | :-: |
|Cumulative returns(in %)|502.34198663119525%|132.39877302964214%|226.81547906442194%|
|Sharpe Ratio|5.386132245689329|13.832240778710622|8.089629465833603|
|Max Drawdown|-0.10020381789538857|-0.03308659010084436|-0.09051421231600798|


