# Mathematical Trading Strategies

This repository contains the implementation of various mathematical and technical analysis strategies applied to financial markets. The project includes data analysis, indicator calculation, and the development of a trading strategy using a combination of technical indicators and chart patterns.

## Project Overview

The objective of this project is to explore and analyze different international indices and equities using various mathematical and technical analysis tools. The project is divided into several sections, each focusing on a specific aspect of trading strategy development and evaluation.

### Key Components

1. **Data Collection and Preprocessing:**
   - Collected daily data for 5 international indices and 5 equities from Yahoo Finance, starting from January 1, 2010.
   - Computed Daily Returns, Cumulative Returns, Maximum Drawdowns, Sharpe Ratio, and Sortino Ratio for each index and equity.

2. **Moving Averages Analysis:**
   - Implemented Simple Moving Average (SMA) and Exponential Moving Average (EMA).
   - Explored the advantages of EMA over SMA.
   - Analyzed the crossover of moving averages with different intervals to identify market trends.

3. **Correlation and Lead-Lag Relationship Analysis:**
   - Analyzed the NASDAQ and NSE indices to identify their correlation and potential lead-lag relationships.
   - Developed and optimized Keltner Channel, Bollinger Bands, and MACD indicators on one index, and used these indicators to generate trading signals on the other index.

4. **Chart Patterns Analysis:**
   - Identified and analyzed the following chart patterns:
     - Ascending Triangle
     - Descending Triangle
     - Bear Flag
     - Bull Flag
     - Cup and Handle
     - Inverse Cup and Handle
     - Head and Shoulders
     - Inverse Head and Shoulders
     - Rounding Top
     - Rounding Bottom

5. **Final Trading Strategy:**
   - Designed and implemented a trading strategy by combining a technical indicator with a chart pattern or candlestick pattern.
   - Optimized the strategy based on Cumulative Returns, Maximum Drawdown, and Sharpe Ratio.
   - Tested the strategy on a 10-year period using Indian equity data.
   - Documented the approach, including the rationale for indicator and pattern selection, limitations, and potential enhancements.


