#!/usr/bin/env python
# coding: utf-8

# In[105]:


import yfinance as yf
import pandas as pd
import numpy as np


# In[116]:


FTSE_100=yf.Ticker("^FTSE")
SP_500=yf.Ticker("^GSPC")
Nikkei225=yf.Ticker("^N225")
CAC40=yf.Ticker("^FCHI")
Dow_Jones=yf.Ticker("^DJI")

apple=yf.Ticker("AAPL")
amazon=yf.Ticker("AMZN")
johnson=yf.Ticker("JNJ")
exxon=yf.Ticker("XOM")
coca_cola=yf.Ticker("KO")
apple.info


# In[140]:


FTSE=FTSE_100.history(interval='1d',start='2010-01-01',end='2023-01-01')
SP500=SP_500.history(interval='1d',start='2010-01-01',end='2023-01-01')
Nikki225=Nikkei225.history(interval='1d',start='2010-01-01',end='2023-01-01')
CAC=CAC40.history(interval='1d',start='2010-01-01',end='2023-01-01')
DJ=Dow_Jones.history(interval='1d',start='2010-01-01',end='2023-01-01')
Apple=apple.history(interval='1d',start='2010-01-01',end='2023-01-01')
Amazon=amazon.history(interval='1d',start='2010-01-01',end='2023-01-01')
Johnson=johnson.history(interval='1d',start='2010-01-01',end='2023-01-01')
Exxon=exxon.history(interval='1d',start='2010-01-01',end='2023-01-01')
Coca_Cola=coca_cola.history(interval='1d',start='2010-01-01',end='2023-01-01')
equities=[Apple,Amazon,Johnson,Exxon,Coca_Cola]
def extent(stock):
    a=range(len(stock.Open))
    stock['extent']=a
#type(FTSE)
S_no1= range(len(FTSE.Open))
S_no2= range(len(SP500.Open))
S_no3= range(len(Nikki225.Open))
S_no4= range(len(CAC.Open))
S_no5= range(len(DJ.Open))

FTSE['extent']=S_no1
SP500['extent']=S_no2
Nikki225['extent']=S_no3
CAC['extent']=S_no4
DJ['extent']=S_no5
for x in equities:
    extent(x)

print(Apple)


# In[155]:


#daily return for equities

def daily_return(stock):
    a=stock.Close-stock.Open
    stock["Daily return"]=((a/stock.Open)*100)
    return np.std(stock["Daily return"])
    
print("Equities\n\n")
for x in equities:
    print(daily_return(x))
    


# In[156]:


#daily return(DR) I have computed the daily return and then reported the mean value
DR_FTSE=(FTSE.Close)-(FTSE.Open)
DR_SP500=(SP500.Close)-(SP500.Open)
DR_Nikki225=(Nikki225.Close)-(Nikki225.Open)
DR_CAC=(CAC.Close)-(CAC.Open)
DR_DJ=(DJ.Close)-(DJ.Open)
FTSE['Daily return']=DR_FTSE
CAC['Daily return']=DR_CAC
DJ['Daily return']=DR_DJ    
SP500['Daily return']=DR_SP500
Nikki225['Daily return']=DR_Nikki225
indices=[FTSE,CAC,DJ,SP500,Nikki225]
#indices_average=[FTSE["Daily return"].mean(),CAC["Daily return"].mean(),DJ["Daily return"].mean(),SP500["Daily return"].mean(),Nikki225["Daily return"].mean()]
print("Indices\n\n")
for x in indices:
    print(daily_return(x))
#print(FTSE["Daily return"])


# In[134]:


#cumulative return(CR)
def CR(x):
    a=x.Open[0]
    b=x.Open[-1]
    c=((b-a)/a)
    return c
print("Indices: \n")
for x in indices:
    print(CR(x))
print("\nEquities: \n")
for x in equities:
    print(CR(x))
        

    


# In[142]:


#Max Drawdowns( MD)
def MaxDrawdowns(stock):
    peak=[]
    position=[]
    difference=[]
    for x in stock.extent:
        if(x==0 or x==(len(stock.extent)-1)or x==(len(stock.extent))):
            continue
        else:
            if(stock.Close[x]>=stock.Close[x-1] and stock.Close[x]>=stock.Close[x+1]):
               peak.append(stock.Close[x])
               position.append(x)
                
    #print(position)
    i=0
    for a in position:
        if(a==position[-1]):
            break
        else:
            c=stock.Close[a]
            for b in range(position[i],position[i+1]):
                if stock.Close[b]<c:
                    c=stock.Close[b]
            i=i+1
            difference.append(stock.Close[a]-c)
    return (max(difference))

print("Indices: \n")           
for x in indices:
    print(MaxDrawdowns(x))
print("\nEquities: \n")
for x in equities:
    print(MaxDrawdowns(x))

            
        

     
        
        


# In[143]:


#Sharpe Ratio(SR)
#risk free rate has been taken as 1%
def Sharpe_Ratio(stock,rf,N):
    a=stock["Daily return"].mean()
    b=(a*N)-rf
    c=stock["Daily return"].std()
    d=c*np.sqrt(N)
    return b/d
print("Indices: \n")
for x in indices:
    print(Sharpe_Ratio(x,0.01,255))
print("\nEquities: \n")
for x in equities:
    print(Sharpe_Ratio(x,0.01,255))


# In[144]:


#The Sortino Ratio(TSR)
#risk free rate has been taken as 1%
def The_Sortino_Ratio(stock,rf,N):
    a=stock["Daily return"].mean()
    b=(a*N)-rf
    Stock=[]
    for x in stock.extent:
        if stock["Daily return"][x]<0:
            Stock.append(stock["Daily return"][x])
    c=np.std(Stock)
    d=c*np.sqrt(N)
    return b/d
print("Indices:\n")
for x in indices:
    print(The_Sortino_Ratio(x,0.01,255))
print("\nEquities:\n")
for x in equities:
    print(The_Sortino_Ratio(x,0.01,255))
    

    


# In[ ]:




