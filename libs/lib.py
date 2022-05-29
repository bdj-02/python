import datetime as dt
import numpy as np
import pandas as pd
import yfinance as yf
tickers = ['AAPL','MSFT','BNP.PA']

def get_date(name_entreprise,start_date, end_date):
    #start_date = dt.datetime(2012,6,8)
    #end_date = dt.datetime(2022,5,11)
    ticket = yf.download(name_entreprise, dt.datetime(start_date,6,8), dt.datetime(end_date,5,11))
    data =  ticket.sort_values("Date", ascending=False)
    #data = data.set_index('Date')
    data.reset_index(inplace = True)
    return data



