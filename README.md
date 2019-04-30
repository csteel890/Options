# Options
#Options project


Derivatives script utilising OOP in Python. 

The rationale behind the script Option_delta.py is to demonstrate under which conditions delta hedging a written option may be a viable solution. 

An example output of the script is:


dV = [c(t + dt) - c(t)] - deltaC[S(t + dt) - S(t)] 
 
              Option_Price        dV
Stock_Price                        
80               0.149788  4.416661
90               1.029372  1.270922
95               2.103008  0.331897
99               3.394782  0.013542
100              3.783772  0.000000
101              4.199913  0.013609
105              6.136671  0.340237
110              9.147661  1.338566
120             16.792490  4.958073


From when the option is sold, each row of the first column indicates a next possible stock price of the underlying stock at which point in time the portfolio (consisting of the option itself and the underlying stock) would next be re-balanced. As can be seen, the change in the value of the portfolio can only be considered negligible when the change in the price of the underlying changes by a small amount.

The output seems to be consistent with theory - the first derivative of the price of the call option w.r.t. the stock assumes a linear relationship which is actually only true for small price movements of the stock as the true relationship is non-linear.
