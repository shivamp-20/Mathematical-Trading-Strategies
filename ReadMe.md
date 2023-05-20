```python
import numpy as np
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
import math
```


```python
stocks = ["MSFT", "TGT", "AAPL", "EA", "ADBE"]
indices = ["^GSPC", "^IXIC", "^DJI", "^FTSE", "^XAX"]
```


```python
answers = []
for s in stocks:
    data = yf.download(s, start="2010-01-01", end="2023-05-01")
    i = 0
    arr = np.empty(len(data))
    capital = np.empty(len(data) + 1)
    j = 0
    capital[0] = data.Open.iloc[0]
    for index, row in data.iterrows():
        arr[i] = (row['Close'] - row['Open'])
        capital[j+1] = capital[j] * (1 + (arr[i])/row['Open'])
        i = i + 1
        j = j + 1
    cum_return = (capital[-1] - capital[0])*100/capital[0]
    # print(s)
    # print('Cumulative Return =', cum_return)
    answers.append(cum_return)
    std = np.std(arr)
#     print('Volatility =', std)
    answers.append(std)
    
    rfr = 5.25
    sharpe_ratio = (cum_return - rfr)/(std*math.sqrt(252)) 
#     print('Sharpe Ratio =', sharpe_ratio)
    answers.append(sharpe_ratio)
    
    neg_retn = []
    for q in range(len(arr)):
        if(arr[q] < 0):
            neg_retn.append(arr[q])
    neg_retn = np.array(neg_retn)
    std_neg = np.std(neg_retn)
    sortino_ratio = (cum_return - rfr)/(std_neg*math.sqrt(252))
#     print('Sortino Ratio =', sortino_ratio)
    answers.append(sortino_ratio)
    
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
    answers.append(max_drawdown)
    
answers = np.array(answers)
answers = answers.reshape(5,5).transpose()
hello = pd.DataFrame(answers, index = ['Cumulative Return', 'Volatility', 'Sharpe Ratio', 'Sortiono Ratio', 'Max Drawdown'], columns = ["MSFT", "TGT", "AAPL", "EA", "ADBE"])



answers1 = []
for s in indices:
    data = yf.download(s, start="2010-01-01", end="2023-05-01")
    i = 0
    arr = np.empty(len(data))
    capital = np.empty(len(data) + 1)
    j = 0
    capital[0] = data.Open.iloc[0]
    for index, row in data.iterrows():
        arr[i] = (row['Close'] - row['Open'])
        capital[j+1] = capital[j] * (1 + (arr[i])/row['Open'])
        i = i + 1
        j = j + 1
    cum_return = (capital[-1] - capital[0])*100/capital[0]
    # print(s)
    # print('Cumulative Return =', cum_return)
    answers1.append(cum_return)
    std = np.std(arr)
#     print('Volatility =', std)
    answers1.append(std)
    
    rfr = 5.25
    sharpe_ratio = (cum_return - rfr)/(std*math.sqrt(252))
#     print('Sharpe Ratio =', sharpe_ratio)
    answers1.append(sharpe_ratio)
    
    
    neg_retn = []
    for q in range(len(arr)):
        if(arr[q] < 0):
            neg_retn.append(arr[q])
    neg_retn = np.array(neg_retn)
    std_neg = np.std(neg_retn)
    sortino_ratio = (cum_return  - rfr)/(std_neg*math.sqrt(252))
#     print('Sortino Ratio =', sortino_ratio)
    answers1.append(sortino_ratio)
    
    
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
    answers1.append(max_drawdown)
    
    
answers1 = np.array(answers1)
answers1 = answers1.reshape(5,5).transpose()
hello1 = pd.DataFrame(answers1, index = ['Cumulative Return', 'Volatility', 'Sharpe Ratio', 'Sortiono Ratio', 'Max Drawdown'], columns = ["GSPC", "IXIC", "DJI", "FTSE", "XAX"])

print(hello)
print(hello1)

```

    [*********************100%***********************]  1 of 1 completed
    [*********************100%***********************]  1 of 1 completed
    [*********************100%***********************]  1 of 1 completed
    [*********************100%***********************]  1 of 1 completed
    [*********************100%***********************]  1 of 1 completed
    [*********************100%***********************]  1 of 1 completed
    [*********************100%***********************]  1 of 1 completed
    [*********************100%***********************]  1 of 1 completed
    [*********************100%***********************]  1 of 1 completed
    [*********************100%***********************]  1 of 1 completed
                             MSFT        TGT        AAPL          EA        ADBE
    Cumulative Return  228.280964  68.078329  146.724243  206.149195  369.516156
    Volatility           2.016294   1.591547    1.163274    1.352761    4.482462
    Sharpe Ratio         6.968045   2.486771    7.661171    9.355282    5.119198
    Sortiono Ratio       8.041341   3.007014    8.963635   12.016439    5.635403
    Max Drawdown       -28.768526 -38.054645  -60.345205  -51.277461  -48.807281
                             GSPC       IXIC         DJI       FTSE        XAX
    Cumulative Return  122.783298  97.407003  134.244311  44.022203  51.222650
    Volatility          24.459565  87.179630  199.061889  64.209148  31.269332
    Sharpe Ratio         0.302700   0.066591    0.040821   0.038038   0.092615
    Sortiono Ratio       0.358189   0.075134    0.049353   0.049260   0.115111
    Max Drawdown       -23.091192 -27.065751  -22.509980 -36.626609 -49.378347
    


```python

```
