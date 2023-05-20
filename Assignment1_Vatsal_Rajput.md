
                Cummulative_Return  Sharpe_Ratio  Sortino_Ratio  Volatility  \
    Index_Name                                                                
    ^IXIC                97.407003      3.602616       4.496551   87.179630   
    ^DJI                134.244311      6.744809       7.540420  199.061889   
    ^FTSE                44.022203      1.183475       1.336582   64.209148   
    ^CNXIT              -48.851843     -2.020890      -2.334935  192.332909   
    ^GSPC               122.783298      0.909631       1.017054   24.459565   
    
                Max_drawdown  
    Index_Name                
    ^IXIC         -27.065751  
    ^DJI          -22.509980  
    ^FTSE         -36.626609  
    ^CNXIT        -69.680236  
    ^GSPC         -23.091192  



```python

import pandas as pd
import yfinance as yf
import pandas as pd
import numpy as np
import math

tickers = ["AAPL", "GOOGL", "MSFT", "AMZN", "TSLA"]


returns=[]
n_returns=[]
Equity_Name=[]
Cummulative_Return=[]
Sharpe_Ratio=[]
Sortino_Ratio=[]
Volatility=[]
Max_drawdown=[]

for j in range(5):
    capital=[]
    data = yf.download(tickers[j], start="2010-01-01", end="2023-05-01")
    capital.append(data.Open.iloc[0])
    total_profit = 0
    for i in range(len(data)):
        profit_of_day = (data.Close.iloc[i] - data.Open.iloc[i]) * (capital[i] / data.Open.iloc[i])
        capital.append(profit_of_day+capital[i])
        returns.append(profit_of_day)
        if profit_of_day<0:
            n_returns.append(profit_of_day)
    #Cummulative_Return
    cumulative_return = ((capital[-1] - data.Open.iloc[0]) / data.Open.iloc[0]) * 100
    Cummulative_Return.append(cumulative_return)
    
    #Sharpe_Ratio
    sharpe_ratio=(capital[-1]-106.5/100*data.Open.iloc[0])/((np.std(returns))*math.sqrt(252))
    Sharpe_Ratio.append(sharpe_ratio)
    
    #Sortino_Ratio
    sortino_ratio=(capital[-1]-106.5/100*data.Open.iloc[0])/((np.std(n_returns))*math.sqrt(252))
    Sortino_Ratio.append(sortino_ratio)
    
    #Volatility
    volatility=np.std(data.Close-data.Open)*math.sqrt(252)
    Volatility.append(volatility)
    
    #MAX_DRAWDOWN
    trough=[]
    trough_position=[]
    peak=[]
    peak_position=[]
    max_drop=0
    for t in range(len(capital)-2):
        if capital[t+1]>capital[t] and capital[t+1]>capital[t+2]:
            peak.append(capital[t+1])
            peak_position.append(t+1)
        if capital[t+1]<capital[t] and capital[t+1]<capital[t+2]:
            trough.append(capital[t+1])
            trough_position.append(t+1)
    for z in range(len(peak)):
        for i in range(len(trough)):
            if trough_position[i]>peak_position[z]:
                if peak[z]-trough[i]>max_drop:
                    max_drop=peak[z]-trough[i]
                    max_drop_peak=peak[z]
    max_drawdown=-(max_drop/max_drop_peak)*100
    Max_drawdown.append(max_drawdown)
    Equity_Name.append(tickers[j])
    

data_table = {
    "Equity_Name": Equity_Name,
    "Cummulative_Return": Cummulative_Return,
    "Sharpe_Ratio": Sharpe_Ratio,
    "Sortino_Ratio": Sortino_Ratio,
    "Volatility": Volatility,
    "Max_drawdown": Max_drawdown
}

df = pd.DataFrame(data_table)
df = df.set_index('Equity_Name')
print(df)

            
        
    
```


```python

```


```python

```


```python

```


```python

```


```python

```


```python

```


```python

```


```python

```


```python

```


```python

```


```python

```


```python

```


```python
     
            
```


```python

```


```python

```
