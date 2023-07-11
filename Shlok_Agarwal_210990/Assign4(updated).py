import pandas as pd
import talib
import yfinance as yf

initial_capital = 1000000  

data = yf.download("RELIANCE.NS", start="2013-07-06", end="2023-07-06", interval="1d")

macd, macd_signal, _ = talib.MACD(data['Close'])

bull_flag = ((data['High'] - data['Low']) > 0.2 * (data['High'].rolling(20).max() - data['Low'].rolling(20).min())) & \
            (data['Close'] > (data['Close'].rolling(20).max() - 0.5 * (data['High'].rolling(20).max() - data['Low'].rolling(20).min())))

cumulative_returns = []
max_drawdowns = []
sharpe_ratios = []
positions = []
portfolio_value = initial_capital
peak_value = initial_capital

for i in range(len(data)):
    if macd[i] > macd_signal[i]:  
        position_size = portfolio_value / data['Close'][i]

        portfolio_value -= position_size * data['Close'][i]
        positions.append(position_size)

    elif macd[i] < macd_signal[i] and bull_flag[i]:  
        sell_value = sum(positions) * data['Close'][i]
        portfolio_value += sell_value
        
        cumulative_return = (portfolio_value - initial_capital) / initial_capital
        cumulative_returns.append(cumulative_return)
        
        drawdown = (portfolio_value - peak_value) / peak_value
        max_drawdowns.append(drawdown)
        
        risk_free_rate = 0.05 
        annualized_return = cumulative_return * (252 / (i+1))  
        annualized_volatility = pd.Series(cumulative_returns[:i+1]).std() * (252 ** 0.5)
        sharpe_ratio = (annualized_return - risk_free_rate) / annualized_volatility
        sharpe_ratios.append(sharpe_ratio)

        peak_value = max(portfolio_value, peak_value)
        
        positions = []

for i in range(len(cumulative_returns)):
    print(f"Sell Signal {i+1} - Cumulative Returns: {cumulative_returns[i]}, Max Drawdown: {max_drawdowns[i]}, Sharpe Ratio: {sharpe_ratios[i]}")

net_max_drawdown = min(max_drawdowns)
net_sharpe_ratio = sharpe_ratios[-1]
net_cumulative_return = cumulative_returns[-1]

print(f"Net Maximum Drawdown: {net_max_drawdown}")
print(f"Net Sharpe Ratio: {net_sharpe_ratio}")
print(f"Net Cumulative Return: {net_cumulative_return}")
