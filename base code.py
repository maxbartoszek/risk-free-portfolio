#These are the libraries you can use.  You may add any libraries directy related to threading if this is a direction
#you wish to go (this is not from the course, so it's entirely on you if you wish to use threading).  Any
#further libraries you wish to use you must email me, james@uwaterloo.ca, for permission.

from IPython.display import display, Math, Latex

import pandas as pd
import numpy as np
import numpy_financial as npf
import yfinance as yf
import matplotlib.pyplot as plt
import random
from datetime import datetime

# Load the tickers
df = pd.read_csv('Tickers_Example.csv') # test with Tickers_Example.csv?
ticker_lst = list(df.iloc[:,0])

# Filter out tickers that don't exist; include only valid tickers

# Apply a filter to remove all stocks with volumes below 5000

# Get the daily data over chosen timeframe (2025-10-24 to 2025-10-31 for testing?)
start_date = '2025-10-24' # change to Nov 21 2025
end_date = '2025-10-31' # change to Nov 28 2025

daily_data = yf.download(
    tickers=ticker_lst,
    start=start_date,
    end=end_date)

# Get/calculate volatility (std), beta, market cap, and sectors

# Use the weighted scoring algorithm in the doc to provide a score /100 per stock

# After scoring, put all stocks in lists based on sector

# Take the top 5 from each sector (based on their score /100) and put them in a new dataframe

# Then return the top 25

# Use minimum variance portfolio optimization to determine optimal weights per stock

# Calculate the shares per stock based on weightings and transaction costs

# Determine what will actually be the transaction cost (What is lower)
# Subtract that from the amount allocated to the company, and determine new total shares

# Verify that we meet all the constraints (one small cap, no more than 40% in one sector, etc.)

# Load final portfolio
