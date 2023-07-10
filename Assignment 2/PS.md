Assignment 2

The objective of this assignment is to analyze the NASDAQ and NSE indices to identify their correlation and establish potential lead-lag relationships. The next step is to code Keltner Channel, Bollinger Bands, and MACD indicators, determining the optimal parameters for these indicators on one of the indices, and generating buy and sell signals on the other index. 
Note : Utilize the established relationship to determine which index should be used for parameter optimization and which one for trading purposes.

Tasks:

Correlation Analysis:
a) Collect historical data for NASDAQ and NSE indices.
b) Calculate the correlation coefficient between the two indices.
c) Analyze the strength and direction of the relationship.

Lead-Lag Relationship:
a) Identify potential lead-lag relationships between the indices.
b) Analyze data to determine consistent leading or lagging behavior.
c) Use the lead-lag relationship to determine the index to be used for parameter optimization.
d) Provide an explanation for choosing the index for parameter optimization

Indicator Coding:
a) Code Keltner Channel, Bollinger Bands, and MACD indicators.

Parameter Optimization:
a) Optimize parameters for the indicators on one index.
b) Use metrics coded in last assignment to evaluate your strategy.
c) Document the optimized parameters for future reference.

Signal Generation:
a) Apply optimized parameters to the other index.
b) Generate buy and sell signals using the indicators.
c) Record the signals, their respective dates and returns along with other metrics covered before.

Your submission should be a Jupyter notebook, where all cells have been run and contain both code and explanations. The deadline for submission is June 3(Sunday) EOD.


# Mathematical Trading Strategies - Performance Comparison

This README provides a comparison of the performance metrics for three mathematical trading strategies: MACD, Bollinger Bands, and Keltner Channels. The table below summarizes their cumulative returns, Sharpe ratios, and maximum drawdowns.

|    Strategy    | Cumulative Returns | Sharpe Ratio | Max Drawdown |
|:--------------:|:-----------------:|:------------:|:------------:|
|      MACD      |      86.848       |    0.187     |    -5.654    |
| Bollinger Bands|      61.525       |    0.358     |   -16.072    |
|Keltner Channels|      114.993      |    0.785     |   -15.784    |

## Insights

- Keltner Channels:
  - This strategy has the highest cumulative returns of 114.993, indicating that it generated the most profitable trades over the evaluated period.
  - It also exhibits the highest risk-adjusted performance, with a Sharpe ratio of 0.785, suggesting a favorable risk-to-reward tradeoff.
  - However, it experienced a maximum drawdown of -15.784, which indicates a significant decline from a previous high point to a subsequent low point.

- Bollinger Bands:
  - This strategy achieved a cumulative return of 61.525, which is lower than the other two strategies.
  - Its Sharpe ratio of 0.358 indicates a relatively better risk-adjusted performance compared to MACD but falls short of Keltner Channels.

