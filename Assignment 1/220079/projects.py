import yfinance as yf
import math
import statistics as stats


start_date = '2010-01-01'
end_date = '2023-05-1'
tickerIN = {'DJI', 'HSI', 'DJT', 'SPX','DAX'}
tickerEQ = {'TSLA', 'META', 'GOOGL', 'AAPL','NVDA'}



def getData(name, ticker, start_date, end_date):
    (name, ["Net CR", "Avg CR", "Net Return",
                         "Daily Vol", "Annual Vol" , "Overall Vol",
                         "Max DD", "Max DD2",
                         "Sharpe Ratio", "An. Sh.R.", "OverAll Sh.R.",
                         "Sortino Ratio", "An. Sort.R.", "OverAll Sort.R."])
    for t in ticker :
        data = yf.download(t, start_date, end_date)
    
        close_Data = data["Close"]
        open_Data = data["Open"]
        high = data["High"]
        low = data["Low"]
        maxPrice = max(high)
        minPrice = min(low)
        maxDDDaily = min((low-high)/high)
        dailtPL = data["Close"]-data["Open"]

        dailyCumRet = dailtPL/open_Data

        netPandL = 0
        size = 0
        for x in dailtPL :
            netPandL = netPandL + x
            size = size+1

        dailyVol = stats.stdev(dailyCumRet)
        dailyRetMean = stats.mean(dailtPL)
        dailyRetSd = stats.stdev(dailtPL)
        sharpeRatio = dailyRetMean/dailyRetSd
        
        onlyLoss = []
        for x in dailtPL :
            if x < 0 :
                onlyLoss.append(x)

        sortinoR = dailyRetMean/stats.stdev(onlyLoss)

        print(
        t, [
        " {:.2f} % ".format(((close_Data[size-1]-open_Data[0])/open_Data[0])*100), 
        " {:.3f} % ".format(stats.mean(dailyCumRet)*100), 
        " $ {:.2f} ".format(netPandL), 
        " {:.2f} % ".format(dailyVol*100),
        " {:.2f} % ".format(dailyVol*100*math.sqrt(252)),
        " {:.2f} % ".format(dailyVol*100*math.sqrt(size)),
        " {:.2f} % ".format((maxDDDaily)*100),
        " {:.2f} % ".format(((minPrice-maxPrice)/maxPrice)*100),
        " {:.2f} ".format((sharpeRatio)),
        " {:.2f} ".format((sharpeRatio)*math.sqrt(252)),
        " {:.2f} ".format((sharpeRatio)*math.sqrt(size)),
        " {:.2f} ".format((sortinoR)),
        " {:.2f} ".format((sortinoR)*math.sqrt(252)),
        " {:.2f} ".format((sortinoR)*math.sqrt(size))])
    
   


getData("Indices-->", tickerIN, start_date, end_date)
getData("Equities-->", tickerEQ, start_date, end_date)