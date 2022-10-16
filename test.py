import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
import datetime
from datetime import date

from IPython.core.display_functions import display
from IPython.display import Markdown

# install the matplotlib utilities for the visualization, and visual analysis, of financial data
# see: https://github.com/matplotlib/mplfinance
import mplfinance as mpf

# install the Yahoo! Finance market data downloader
# see: https://github.com/ranaroussi/yfinance
import yfinance as yf
now = datetime.datetime.now()

# obtain the Bitcoin ticker in USD
bitCoinUSD = yf.Ticker("BTC-USD")
# save the historical market data to a pandas dataframe
bitCoinUSD_values = bitCoinUSD.history(start="2022-01-01")

display(Markdown('### Plot from 1 January 2022 up to ' + now.strftime('%d %B %Y')))
display(Markdown(""))

# now plot. For plotting styles see: https://github.com/matplotlib/mplfinance/blob/master/examples/styles.ipynb
mpf.plot(bitCoinUSD_values,type='candle',volume=False,figratio=(5,1),style='yahoo', title='Bitcoin (in USD) From: 1 January 2022 to ' + now.strftime('%d %B %Y'));