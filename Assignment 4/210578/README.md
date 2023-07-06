Mathematical Trading Strategies <br />

Assignment 4 <br /> <br />

Technical Indicator used is “MACD”(Moving Average Convergence Divergence) and I have used the ”Bull Flag”  chart pattern. The Indian Equity used is MRF. For MACD signal generation, the exponential moving average of span 12 and 26 is calculated. For coding the bull flag pattern, I have calculated the moving average with a window = 5 days. Then High(-5) is compared with High and Low(-5) is compared with Low. Whenever a pattern is followed the flag is made 1, else kept 0. Now for the generation of buying and selling signals, if both are true, then buying signal is generated and when both false, then selling signal is generated. The buying and selling signals are plotted. Cumulative return, maximum drawdown and sharpe ratio are calculated using definition. <br /> <br />

Cumulative return = 8.080627619448503 <br />
Maximum Drawdown = -35.72847048029707 <br />
Sharpe Ratio = 0.7630508771342167 <br />
