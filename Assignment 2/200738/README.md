Mathematical Trading Strategies

Assignment 2

Description: 

For Keltner Channels </br>
Strategy -  </br>
if close < lower_band and next_day_close > close: buy signal  
if close > upper_band and next_day_close < close: sell signal

For Bollinger Bands </br>
Strategy - </br>
if prev_day_close> lower_band and close < lower_band: buy signal  
if prev_day_close < upper_band and close > upper_band: sell signal

For MACD
Strategy - </br>
if macd > signal_line: buy signal  
if macd < signal_line: sell signal

|  | MACD | Bollinger Bands| Keltner Channels | 
|--|---------|---------|---------|
|Cumulative returns| 86.848| 61.525| 114.993 | 
|Sharpe Ratio|  0.187 | 0.358 | 0.785 | 
|Max Drawdown| -5.654 | -16.072 | -15.784 | 
