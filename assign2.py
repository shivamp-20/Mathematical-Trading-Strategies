import pandas as pd
import yfinance as yf
import numpy as np
from skopt import BayesSearchCV

nasdaq_data=yf.download(tickers="^IXIC", start="2010-01-01", end="2023-05-01", interval="1d")
nifty_data=yf.download(tickers="^NSEI", start="2010-01-01", end="2023-05-01", interval="1d")

nas=nasdaq_data['Close']
nif=nifty_data['Close']

corr_coefficient = nas.corr(nif)

print(corr_coefficient)

#0.9513

#Direction: Positively Correlated, so vary directly with each other
#Strength: 0.9513 magnitude indicates very strong correlation between the two as the ratio is very close to 1.

df=pd.DataFrame()

df['nas_close'] = nasdaq_data['Close']
df['nif_close'] = nifty_data['Close']

lags = range(-10, 11)  
correlations = []

for lag in lags:
    df['nif_lag'] = df['nif_close'].shift(lag)
    correlation = df['nas_close'].corr(df['nif_lag'])
    correlations.append(correlation)

best_lag = lags[np.argmax(correlations)]
best_correlation = correlations[np.argmax(correlations)]

print(best_lag)
print(best_correlation)

#best_lag=-10
#correlation at best lag=0.952459

#Since the best lag is -10. The parameter to optimize must be NASDAQ index.
#Using this, we can predict the prices for the Nifty index at a ten day difference and accordingly make our prediction strategy.

train_start = 0
train_end = int(len(nasdaq_data) * 0.7)
eval_start = train_end + 1

def calculate_keltner_channel(data, atr_period, ma_period, multiplier):
    data['ATR'] = data['High'].rolling(atr_period).max() - data['Low'].rolling(atr_period).min()
    data['Centerline'] = data['Close'].rolling(ma_period).mean()
    data['Upper_Band'] = data['Centerline'] + (data['ATR'] * multiplier)
    data['Lower_Band'] = data['Centerline'] - (data['ATR'] * multiplier)
    return data

def calculate_bollinger_bands(data, ma_period, std_multiplier):
    data['Centerline'] = data['Close'].rolling(ma_period).mean()
    data['Standard_Deviation'] = data['Close'].rolling(ma_period).std()
    data['Upper_Band'] = data['Centerline'] + (data['Standard_Deviation'] * std_multiplier)
    data['Lower_Band'] = data['Centerline'] - (data['Standard_Deviation'] * std_multiplier)
    return data

def calculate_macd(data, short_ma_period, long_ma_period, signal_ma_period):
    data['MACD_Line'] = data['Close'].ewm(span=short_ma_period).mean() - data['Close'].ewm(span=long_ma_period).mean()
    data['Signal_Line'] = data['MACD_Line'].ewm(span=signal_ma_period).mean()
    data['MACD_Histogram'] = data['MACD_Line'] - data['Signal_Line']
    return data

def optimization_objective(params):
    # Apply the parameters to NASDAQ data
    nasdaq_keltner_data = calculate_keltner_channel(nasdaq_data, params['atr_period'], params['ma_period'], params['multiplier'])
    nasdaq_bollinger_data = calculate_bollinger_bands(nasdaq_data, params['ma_period'], params['std_multiplier'])
    nasdaq_macd_data = calculate_macd(nasdaq_data, params['short_ma_period'], params['long_ma_period'], params['signal_ma_period'])

    lagged_nasdaq_data = nasdaq_data['Close'].shift(10)
    
    lagged_nasdaq_keltner_data = nasdaq_keltner_data.shift(10)
    lagged_nasdaq_bollinger_data = nasdaq_bollinger_data.shift(10)
    lagged_nasdaq_macd_data = nasdaq_macd_data.shift(10)
    
    correlation = np.corrcoef(lagged_nasdaq_data[train_start:train_end], nifty_data['Close'][train_start:train_end])[0, 1]
    
    keltner_corr = np.corrcoef(lagged_nasdaq_keltner_data[train_start:train_end], nifty_keltner_data['Close'][train_start:train_end])[0, 1]
    bollinger_corr = np.corrcoef(lagged_nasdaq_bollinger_data[train_start:train_end], nifty_bollinger_data['Close'][train_start:train_end])[0, 1]
    macd_corr = np.corrcoef(lagged_nasdaq_macd_data[train_start:train_end], nifty_macd_data['MACD'][train_start:train_end])[0, 1]
    
    weighted_corr = (keltner_corr + bollinger_corr + macd_corr) / 3
    print(correlation)

    return -weighted_corr

param_space = {
    'atr_period': (10, 14, 20),
    'ma_period': (20, 30, 40),
    'multiplier': (1.5, 2.0, 2.5),
    'std_multiplier': (1.5, 2.0, 2.5),
    'short_ma_period': (10, 12, 14),
    'long_ma_period': (20, 26, 30),
    'signal_ma_period': (9, 12, 15)
}

# Step 4: Perform parameter optimization using scikit-optimize
opt = BayesSearchCV(optimization_objective, param_space, n_iter=50, cv=3)
opt.fit(nasdaq_data[train_start:train_end], nifty_data['Close'][train_start:train_end])

# Get the best parameters
best_params = opt.best_params_

# Step 5: Apply optimized parameters to Nifty data and generate signals
nifty_keltner_data = calculate_keltner_channel(nifty_data, best_params['atr_period'], best_params['ma_period'], best_params['multiplier'])
nifty_bollinger_data = calculate_bollinger_bands(nifty_data, best_params['ma_period'], best_params['std_multiplier'])
nifty_macd_data = calculate_macd(nifty_data, best_params['short_ma_period'], best_params['long_ma_period'], best_params['signal_ma_period'])

def generate_signals(data, keltner_data, bollinger_data, macd_data):
    signals = pd.DataFrame(index=data.index)
    
    signals['Keltner_Up'] = np.where(data['Close'] > keltner_data['UpperBand'], 1, 0)
    signals['Keltner_Down'] = np.where(data['Close'] < keltner_data['LowerBand'], -1, 0)
    
    signals['Bollinger_Up'] = np.where(data['Close'] > bollinger_data['UpperBand'], 1, 0)
    signals['Bollinger_Down'] = np.where(data['Close'] < bollinger_data['LowerBand'], -1, 0)
    
    signals['MACD'] = np.where(macd_data['MACD'] > macd_data['Signal'], 1, 0)
    signals['MACD_Signal'] = np.where(macd_data['MACD'] < macd_data['Signal'], -1, 0)
    
    signals['Kelt_Signal'] = signals['Keltner_Up'] + signals['Keltner_Down'] 
    signals['Bollinger_Signal']= signals['Bollinger_Up'] + signals['Bollinger_Down']  
    signals['MACD_Signal']= signals['MACD_Up'] + signals['MACD_Down']  
    
    return signals

def backtest_signals(data, signals):
    # Combine the signals with the price data
    combined_data = pd.concat([data, signals], axis=1)
    
    # Initialize variables
    position_1 = 0
    entry_price_1 = 0
    exit_price_1 = 0
    num_trades_1 = 0
    max_drawdown_1 = 0
    cum_returns_1 = [0]
    returns_1 = []

    for i in range(len(combined_data)):
        if position_1 == 0:
            if combined_data['Kelt_Signal'].iloc[i] > 0:
                position_1 = 1
                entry_price_1 = combined_data['Close'].iloc[i]
        elif position_1 == 1:
            if combined_data['Kelt_Signal'].iloc[i] < 0:
                position_1 = 0
                exit_price_1 = combined_data['Close'].iloc[i]
                profit_1 = exit_price_1 - entry_price_1
                total_profit_1 += profit_1
                num_trades_1 += 1

            returns_1.append(profit_1 / entry_price_1)
                
            # Update max drawdown
            drawdown_1 = (exit_price_1 - np.max(combined_data['Close'][i-num_trades_1+1:i+1])) / np.max(combined_data['Close'][i-num_trades_1+1:i+1])
            max_drawdown_1 = min(max_drawdown_1, drawdown_1)
                
            # Calculate cumulative returns
            cum_returns_1.append((1 + sum(returns_1)) * cum_returns_1[-1])
    
    # Calculate Sortino ratio
    returns_1 = np.array(returns_1)
    risk_free_rate_1 = 0.3  # Change this to the appropriate risk-free rate
    annualized_return_1 = np.mean(returns_1) * len(data) / len(combined_data)
    downside_returns_1 = returns_1[returns_1 < risk_free_rate_1]
    downside_std_1 = np.std(downside_returns_1)
    sortino_ratio_1 = (annualized_return_1 - risk_free_rate_1) / downside_std_1 if downside_std_1 != 0 else np.nan
        

    # Initialize variables
    position_2 = 0
    entry_price_2 = 0
    exit_price_2 = 0
    num_trades_2 = 0
    max_drawdown_2 = 0
    cum_returns_2 = [0]
    returns_2 = []
    
    for j in range(len(combined_data)):
        if position_2 == 0:
            if combined_data['Bollinger_Signal'].iloc[j] > 0:
                position_2 = 1
                entry_price_2 = combined_data['Close'].iloc[j]
        elif position_2 == 1:
            if combined_data['Bollinger_Signal'].iloc[j] < 0:
                position_2 = 0
                exit_price_2 = combined_data['Close'].iloc[j]
                profit_2 = exit_price_2 - entry_price_2
                total_profit_2 += profit_2
                num_trades_2 += 1

                returns_2.append(profit_2 / entry_price_2)
                
                # Update max drawdown
                drawdown_2 = (exit_price_2 - np.max(combined_data['Close'][i-num_trades_2+1:i+1])) / np.max(combined_data['Close'][i-num_trades_2+1:i+1])
                max_drawdown_2 = min(max_drawdown_2, drawdown_2)
                
                # Calculate cumulative returns
                cum_returns_2.append((1 + sum(returns_2)) * cum_returns_2[-1])
    
    # Calculate Sortino ratio
    returns_2 = np.array(returns_2)
    risk_free_rate_2 = 0.3  # Change this to the appropriate risk-free rate
    annualized_return_2 = np.mean(returns_2) * len(data) / len(combined_data)
    downside_returns_2 = returns_2[returns_2 < risk_free_rate_2]
    downside_std_2 = np.std(downside_returns_2)
    sortino_ratio_2 = (annualized_return_2 - risk_free_rate_2) / downside_std_2 if downside_std_2 != 0 else np.nan
    

    # Initialize variables
    position_3 = 0
    entry_price_3 = 0
    exit_price_3 = 0
    num_trades_3 = 0
    max_drawdown_3 = 0
    cum_returns_3 = [0]
    returns_3 = []
    
    for k in range(len(combined_data)):
        if position_3 == 0:
            if combined_data['MACD_Signal'].iloc[k] > 0:
                position_3 = 1
                entry_price_3 = combined_data['Close'].iloc[k]
        elif position_3 == 1:
            if combined_data['MACD_Signal'].iloc[k] < 0:
                position_3 = 0
                exit_price_3 = combined_data['Close'].iloc[k]
                profit_3 = exit_price_3 - entry_price_3
                total_profit_3 += profit_3
                num_trades_3 += 1

                returns_3.append(profit_3 / entry_price_3)
                
                # Update max drawdown
                drawdown_3 = (exit_price_3 - np.max(combined_data['Close'][i-num_trades_3+1:i+1])) / np.max(combined_data['Close'][i-num_trades_3+1:i+1])
                max_drawdown_3 = min(max_drawdown_3, drawdown_3)
                
                # Calculate cumulative returns
                cum_returns_3.append((1 + sum(returns_3)) * cum_returns_3[-1])
    
    # Calculate Sortino ratio
    returns_3 = np.array(returns_3)
    risk_free_rate_3 = 0.3  # Change this to the appropriate risk-free rate
    annualized_return_3 = np.mean(returns_3) * len(data) / len(combined_data)
    downside_returns_3 = returns_3[returns_3 < risk_free_rate_3]
    downside_std_3 = np.std(downside_returns_3)
    sortino_ratio_3 = (annualized_return_3 - risk_free_rate_3) / downside_std_3 if downside_std_3 != 0 else np.nan
    
    
    performance_metrics = {
        'Total Profit Kelt': total_profit_1,
        'Number of Trades Kelt': num_trades_1,
        'Total Profit Bollinger': total_profit_2,
        'Number of Trades Bollinger': num_trades_2,
        'Total Profit MACD': total_profit_3,
        'Number of Trades MACD': num_trades_3,
    }
    
    return performance_metrics


nifty_signals = generate_signals(nifty_data, nifty_keltner_data, nifty_bollinger_data, nifty_macd_data)

performance_metrics = backtest_signals(nifty_data, nifty_signals)

print('Best Parameters:', best_params)
print('Performance Metrics:', performance_metrics)









