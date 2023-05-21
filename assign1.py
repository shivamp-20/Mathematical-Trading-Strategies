import yfinance as yf
import pandas as pd
import numpy as np
import math

equities=["TSLA","ABT","ADBE","IBM","MSFT"]
indices=["^GSPC","^BSESN","^DJI","^RUT","^FTSE"]

for t in range(5):
    data=yf.download(tickers=equities[t], start="2010-01-01", end="2023-05-01", interval="1d")
    df=pd.DataFrame()
    df=data

    #CUMMULATIVE RETURNS PERCENTAGE
    df_cr=df[['Adj Close']]
    cumm_ret_per=((df_cr.iloc[-1]-df_cr.iloc[0])/df_cr.iloc[0])*100
    print(cumm_ret_per)

    #max_drawdowns
    peak = df.expanding(min_periods=1)["Close"].max()
    max_drawdown = (data["Close"]-peak)/peak
    max_draw_down=max_drawdown.min()
    print(max_draw_down)

    #Calculating daily returns
    Daily_return=df["Close"].pct_change().dropna()

    #sharpe_ratio
    #Treasury rate of USA on 1 May 2023 was 4.86%.
    risk_free_return = 0.04
    excess_return = Daily_return - risk_free_return
    sharpe_ratio = np.mean(excess_return)/np.std(excess_return)
    print(sharpe_ratio)

    #Volatility
    volatility=np.std(Daily_return)*(math.sqrt(252))
    print(volatility)

    #downside deviations
    down_dev_crit=Daily_return[Daily_return<0]
    sq=np.square(down_dev_crit)
    down_dev=(math.sqrt(np.sum(sq)/len(Daily_return)))*100
    print(down_dev)

    #sortino
    sortino=np.mean(excess_return)/down_dev
    print(sortino)

    t=t+1

for i in range(5):
    data=yf.download(tickers=indices[i], start="2010-01-01", end="2023-05-01", interval="1d")
    df=pd.DataFrame()
    df=data

    #CUMMULATIVE RETURNS PERCENTAGE
    df_cr=df[['Adj Close']]
    cumm_ret_per=((df_cr.iloc[-1]-df_cr.iloc[0])/df_cr.iloc[0])*100
    print(cumm_ret_per)

    #max_drawdowns
    peak = df.expanding(min_periods=1)["Close"].max()
    max_drawdown = (data["Close"]-peak)/peak
    max_draw_down=max_drawdown.min()
    print(max_draw_down)

    #Calculating daily returns
    Daily_return=df["Close"].pct_change().dropna()

    #sharpe_ratio
    #Treasury rate of USA on 1 May 2023 was 4.86%.
    risk_free_return = 0.04
    excess_return = Daily_return - risk_free_return
    sharpe_ratio = np.mean(excess_return)/np.std(excess_return)
    print(sharpe_ratio)

    #Volatility
    volatility=np.std(Daily_return)*(math.sqrt(252))
    print(volatility)

    #downside deviations
    down_dev_crit=Daily_return[Daily_return<0]
    sq=np.square(down_dev_crit)
    down_dev=(math.sqrt(np.sum(sq)/len(Daily_return)))*100
    print(down_dev)

    #sortino
    sortino=np.mean(excess_return)/down_dev
    print(sortino)

    i=i+1