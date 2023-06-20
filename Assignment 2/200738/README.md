Mathematical Trading Strategies

Assignment 2

Description: 

For Keltner Channels
Strategy -  if close < lower_band and next_day_close > close: buy signal  
$~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~$ if close > upper_band and next_day_close < close: sell signal

For Bollinger Bands
Strategy - if prev_day_close> lower_band and close < lower_band: buy signal  
$~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~$ if prev_day_close < upper_band and close > upper_band: sell signal

For MACD
Strategy - if macd > signal_line: buy signal  
$~~~~~~~~~~~~~~~~~~~~~$ if macd < signal_line: sell signal

|  | MACD | Bollinger Bands| Keltner Channels | 
|--|---------|---------|---------|
|Cumulative returns| 86.848| 61.525| 114.993 | 
|Sharpe Ratio|  0.187 | 0.358 | 0.785 | 
|Max Drawdown| -5.654 | -16.072 | -15.784 | 
