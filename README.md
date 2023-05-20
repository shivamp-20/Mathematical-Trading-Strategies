# Mathematical-Trading-Strategies
Official repo for submission of assignments in Mathematical Trading Strategies
import yfinance as yf
import numpy as np
import matplotlib.pyplot as plt


def calculate_maximum_drawdown(ticker_symbol):
    # Download the historical data
    data = yf.download(ticker_symbol, start="2010-01-01", end="2023-05-01")  # Replace with desired start and end dates
    # Calculate the cumulative returns
    data['Cumulative Return'] = (data['Close'] / data['Close'].cummax()) - 1
    # Calculate the maximum drawdown
    max_drawdown = np.min(data['Cumulative Return'])
    return max_drawdown
ticker_symbol = "FSPSX"  # Replace with the desired stock ticker symbol
max_drawdown = calculate_maximum_drawdown(ticker_symbol)
print("Maximum Drawdown:", max_drawdown)




def calculate_cumulative_return(ticker_symbol):
    # Download the historical data
    data = yf.download(ticker_symbol, start="2010-01-01", end="2023-05-01")  # Replace with desired start and end dates
    # Calculate the cumulative return
    data['Cumulative Return'] = (data['Close'] / data['Close'].iloc[0]) - 1
    # Plot the cumulative return
    plt.figure(figsize=(10, 6))
    plt.plot(data.index, data['Cumulative Return'])
    plt.title('Cumulative Return for {}'.format(ticker_symbol))
    plt.xlabel('Date')
    plt.ylabel('Cumulative Return')
    plt.grid(True)
    plt.show()
    return data['Cumulative Return']
ticker_symbol = "EMQQ"  # Replace with the desired stock ticker symbol
cumulative_return = calculate_cumulative_return(ticker_symbol)
print(cumulative_return)




def calculate_sharpe_ratio(ticker_symbol):
    # Download the historical data
    data = yf.download(ticker_symbol, start="2010-01-01", end="2023-05-01")  # Replace with desired start and end dates
    # Calculate the daily returns
    data['Daily Return'] = data['Close'].pct_change()
    # Calculate the annualized average return and standard deviation
    avg_return = data['Daily Return'].mean()
    std_dev = data['Daily Return'].std()
    # Calculate the annualized Sharpe Ratio
    sharpe_ratio = (avg_return / std_dev) * np.sqrt(252)
    return sharpe_ratio
ticker_symbol = "IXUS"  # Replace with the desired stock ticker symbol
sharpe_ratio = calculate_sharpe_ratio(ticker_symbol)
print("Sharpe Ratio:", sharpe_ratio)



def calculate_sortino_ratio(ticker_symbol, risk_free_rate):
    # Download the historical data
    data = yf.download(ticker_symbol, start="2010-01-01", end="2023-05-01")  # Replace with desired start and end dates
    # Calculate the daily returns
    data['Daily Return'] = data['Close'].pct_change()
    # Calculate the downside standard deviation
    downside_returns = data['Daily Return'].copy()
    downside_returns[downside_returns > 0] = 0
    downside_std_dev = np.sqrt((downside_returns ** 2).mean())
    # Calculate the average return and risk-free rate
    avg_return = data['Daily Return'].mean()
    risk_free_rate_daily = risk_free_rate / 252  # Assuming 252 trading days in a year
    # Calculate the Sortino Ratio
    sortino_ratio = (avg_return - risk_free_rate_daily) / downside_std_dev
    return sortino_ratio
ticker_symbol = "RUT"  # Replace with the desired stock ticker symbol
risk_free_rate = 0.02  # Replace with the desired risk-free rate
sortino_ratio = calculate_sortino_ratio(ticker_symbol, risk_free_rate)
print("Sortino Ratio:", sortino_ratio)




def calculate_daily_returns(ticker_symbol):
    # Download the historical data
    data = yf.download(ticker_symbol, start="2010-01-01", end="2023-05-01")  # Replace with desired start and end dates
    # Calculate the daily returns
    data['Daily Return'] = data['Close'].pct_change()
    return data['Daily Return']
ticker_symbol = "EMQQ"  # Replace with the desired stock ticker symbol
daily_returns = calculate_daily_returns(ticker_symbol)
print(daily_returns)
