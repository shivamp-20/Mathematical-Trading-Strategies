Stock Used : Asian paints (ticker: ASIANPAINT.NS)

**Description:**
The technique looks for probable buy and sell signals in the market by combining the Keltner channel bands with the hammer candlestick pattern. The Keltner Channel has been preferred over other technical indicators like Bollinger Bands because of the two main differences:

1. The Keltner Channel is smoother than Bollinger Bands
1. Keltner Channels employ an exponential moving average, whereas Bollinger Bands use a Simple moving average.

A hammer pattern often denotes a possible price direction reversal. Any time a hammer pattern appears, it shows that the price may be overbought close to the top band of the Keltner channel, indicating a potential sell opportunity. On the other hand a hammer pattern close to the lower band, suggests that the price may be oversold and points to a potential buy opportunity.

**Effectiveness and Optimisations:**
The technique uses the Keltner channel bands and the likelihood of reversal signs of the hammer candlestick pattern to identify overbought and oversold levels. The Keltner channel's lower band functions as a dynamic support level, and the upper band as a dynamic resistance level. The approach seeks to spot times when the price may revert from overbought or oversold levels by looking for hammer patterns close to these zones. This strategy can offer useful signs for seizing winning trading chances in the right market circumstances. The selection of the right thresholds for signal generation is also as important as the selection of right strategy. 

I have used the following parameters for Keltner Channel(as optimized in 2<sup>nd</sup> Assignment) and Hammer candlestick pattern:

|**Keltner Channel**|**Hammer Candlestick Pattern**|
| :- | :- |
|KC\_Lookback period: 17 days|UpperBand threshold: 2.8%|
|<p>ATR period: 10 days</p><p>Multiplier: 1.93</p>|<p>LowerBand threshold: 14%</p><p></p>|

**Results and Evaluation:**
The result of the above trading strategy can be observed from the performance metrics noted below:

|Max. Drawdown|Sharpe Ratio|Cumulative Returns|
| :-: | :-: | :-: |
|-5.478186412842345 %|1\.0437427253317282|1\.5857508631788104|

**Drawbacks and Limitations**:

1. The above strategic parameters may not work effectively for a different market sector. 
1. Not all signals result in actual reversal. The subtle breakdown points may need to be taken care of.
