## Assignment 2
This repository contains code for analyzing stock market data using Python and various libraries such as yfinance, numpy, pandas, and matplotlib.

# Description
The code performs the following tasks:

Collects historical data for NASDAQ and NSE indices using the yfinance library.
Calculates the correlation coefficient between the two indices to analyze the relationship between them.
Identifies potential lead-lag relationships between the indices and determines the lag and correlation.
Implements indicator coding for Keltner Channel, Bollinger Bands, and MACD indicators.
Optimizes the parameters for each indicator using a parameter optimization technique.
Generates buy/sell signals based on the indicators and a trading strategy.
Records the signals, dates, returns, and other metrics for analysis and visualization.
Dependencies
To run this code, the following dependencies need to be installed:

yfinance: A Python library to fetch historical market data from Yahoo Finance.
numpy: A library for numerical computing in Python.
pandas: A library for data manipulation and analysis.
matplotlib.pyplot: A plotting library for creating visualizations.

# Trading Strategy Performance Metrics

|            | MACD | Bollinger Bands | Keltner Channels |
|------------|------|----------------|------------------|
| Cumulative Returns | 0.15 | 0.10 | 0.12 |
| Sharpe Ratio       | 1.75 | 1.45 | 1.60 |
| Max Drawdown       | 0.08 | 0.05 | 0.06 |
