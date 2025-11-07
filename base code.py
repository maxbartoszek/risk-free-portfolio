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
df = pd.read_csv('Tickers.csv')
ticker_lst = list(df)

# Get the daily data over chosen timeframe
start_date = 
end_date = 

daily_data = yf.download(
    tickers=ticker_lst,
    start=start_date
    end=end_date)

# Apply the filter for > 5000 volume


# Get current prices, market cap, and sectors


# Calculate daily returns, standard deviation, beta


# Rank the ticker list by volatility, filter for lowest


# Check for the constraints we’re given and choose the 20-25 ‘best’ stocks


# Give everything equal weights


# Calculate the shares needed and transaction costs


# Verify that we meet all the constraints (one small cap, no more than 40% in one sector, etc.)


# Load final portfolio