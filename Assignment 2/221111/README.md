# Mathematical Trading Strategies

## Assignment 2

NASDAQ and NSE have a strong correlation. The strength of correlation is high and and direction is positive.
After analysis it was found that NASDAQ leads and NSE lags. 

I applied 3 strategies MACD, Bollinger Channel and Keltner Channel on NASDAQ and then optimised the parameters. Then I applied the same strategy on the NSE dataset. Following are the observations:

## On NASDAQ Dataset
||MACD|Bollinger Channel|Keltner Channel|
---|---|---|---|
Cumulative returns|251.4952727441091|427.0895761555454|281.18442795820744|
Sharpe Ratio|0.5155510302280012 |0.5185650415317772|0.46014195671344776|
Maximum Drawdown|-3.115932646988304|-2.616539175506242|-4.149814004180698|

## On NSE Dataset
||MACD|Bollinger Channel|Keltner Channel|
---|---|---|---|
Cumulative returns|361.2183794203646|126.80918261023012|83.63990114278536|
Sharpe Ratio|0.8351786392209993|0.27647067887488247|0.11860851369015452|
Maximum Drawdown|-2.7101982659154062|-2.56613638451474|-4.929056067266709|

### Optimised parameters for Keltner Channel
>window=12  
>atr_window=11  
>atr_multiplier=3
### Optimised parameters for Bollinger Bands
>window=21  
>num_std=3
### Optimised parameters for MACD
>short_window=12  
>long_window=26  
>signal_window=9
