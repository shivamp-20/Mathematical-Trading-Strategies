Mathematical Trading Strategies

Name- Vatsaankit Mudgal
Roll No- 221178


Assignment 2

Description: Firstly I have used a combined strategy that produces buy and sell signals using all the 3 indicators in a combined manner. It is a more complex strategy. Later I have created a strategy that gives the returns for individual indicators.

Also according to the correlation factor calculated for different lag periods, the best factor came out to be when the lag period was 19 days. Also I have arrived to the conclusion that NSEI is lagging IXIC.

However I have explained the methodology and the code very elaborately in the code itself, I will just describe the strategy I have used.

 conditions = [
    (dfx['MACD_Signal'] == 1) & (dfx['BB_Signal'] == 1),

    (dfx['MACD_Signal'] == -1) & (dfx['BB_Signal'] == -1),

    (dfx['MACD_Signal'] == 1) & (dfx['KC_Signal'] == 1),

    (dfx['MACD_Signal'] == -1) & (dfx['KC_Signal'] == 1),

    (dfx['MACD_Signal'] == 1) & (dfx['KC_Signal'] == -1),

    (dfx['MACD_Signal'] == -1) & (dfx['KC_Signal'] == -1),

    (dfx['MACD_Signal'] == -1) & (dfx['BB_Signal'] == 1),

    (dfx['MACD_Signal'] == 1) & (dfx['BB_Signal'] == -1)
    ]

Here dfx is the dataframe in which I have stored various datas. This table basically generates the signals that are being used to place trades. The trade signals that this table produces are respectively:

choices = [1, -1, 1, -1, -1, -1,0,0]
dfx['Signal'] = np.select(conditions, choices, default=0)

This is how I have created a column for the signals.

BB stands for Bollinger bands and KC stands for Keltner Channel.
For this strategy, I get the following results on NIFTY 50 and NASDAQ COMPOSITE:

                             NIFTY 50

Cumulative Return = 546.3653328473898%

Sharpe Ratio =   0.17217826651888024

Max Drawdown = -50.29137285386618%

                         
                 NASDAQ COMPOSITE

Cumulative Return = 1160.5465495866472% 

Sharpe Ratio = 0.18646734980776278

Max Drawdown = -23.68515666096469%


Later I have calculated these metrics with individual indicators being used. For them I have used simple strategy.

MACD- go Long if MACD>SIGNAL and Short if MACD<SIGNAL 

Bollinger Bands- go Long is price close below lower band and go short if it closes above the upper band

Keltner Channels- go Long if the close price above the upper band and go short if the close price below the lower band



					MACD			Bollinger Bands		Keltner Channels
	Cumulative returns	889.6391354%			847.34390214497%	996.663904702996%

	Sharpe Ratio		0.0636393673			0.1479694528441		0.17302710730651424

	Max Drawdown		-74.9445741%	-		-14.21487426039%	-19.536823009716908%

These metrics are for the NASDAQ Composite.
