import yfinance as yf
import numpy as np
import pandas as pd
import math

symbols = ['^IXIC', '^NSEI']

data = yf.download(symbols, start='2015-01-01', end='2023-06-01')['Adj Close']


data.dropna(inplace=True)

closing_data1 = data['^IXIC'].tolist()
closing_data2 = data['^NSEI'].tolist()


return1 =[]
return2 =[]
for i in range(len(closing_data1)-1):
    return1.append(closing_data1[i+1]/closing_data1[i] - 1)
for i in range(len(closing_data2)-1):
    return2.append(closing_data2[i+1]/closing_data2[i] - 1)


print(len(return1))
print(len(return2))


mean_returns1 = np.mean(return1)
mean_returns2 = np.mean(return2)

sum1 = sum(return1)
sum2 = sum(return2)

ts =0
for i in range(len(return2)):
    ts = ts + return1[i]*return2[i]
    
numretor = len(return2)*ts - sum1*sum2

tx =ty =0
x =y=0

for i in range(len(return2)):
    tx = tx + return1[i]*return1[i]
    ty = ty + return2[i]*return2[i]
    x = x + return1[i]
    y = y + return2[i]
   
d1 =  len(return2)*tx - x*x      
d2 = len(return2)*ty - y*y

denominator = math.sqrt(d1*d2)

coeff = numretor/denominator
print(f"{coeff:.2f}")

