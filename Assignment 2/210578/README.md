# Mathematical-Trading-Strategies
Description - 
In Task 1, first I downloaded the historical data from finance and then found the correlation between NSE and Nasdaq by the .corr() function. For Task 2, I found the sum for the whole time period where NSE leads Nasdaq and vice-versa. I found that changes in Nasdaq generally occur prior to the changes in NSE, so Nasdaq leads NSE. In Task 3, we had to code the Keltner Channel, Bollinger bands and MACD indicators. For this, we needed to calculate the simple moving average and exponential moving average over different time periods (20 days for Keltner Channel and Bollinger bands, 12 and 26 for MACD indicator). Using these three strategies signals are developed and reported. In Task 4, the sharpe ratio, sortino ratio , maximum drawdown, and cumulative returns are calculated. In Task 5, for optimization, all the possible window sizes are checked and the best one is returned. Using these optimized values, favourable trades percentage are calculated.




||MACD|Bollinger Bands|Keltner Channels|
|:-:|:---:|:--------------:|:-----------------:|
|Cumulative Return|15.06725766327907 %|25.046411223769834 %|11.489076030873765 %|
|Sharpe Ratio|0.16675361734907584|0.3240500514250054|0.5456285477502468|
|Maximum drawdown|-31.758770836202398 %|-28.300449051562993 %|-14.252696626295021 %|




