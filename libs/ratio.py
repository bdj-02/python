import datetime as dt
import numpy as np
import pandas as pd
import yfinance as yf
tickers = ['AAPL','MSFT','BNP.PA']

# Calcul du Ratio de Sharpe 

def sharpe_ratio(return_series, N, rf):
    mean = return_series.mean() * N - rf
    sigma = return_series.std() * np.sqrt(N)
    return mean / sigma
 
# Calcul du Ratio de Sortino
# Ce ratio ne prend en compte les variables nuisibles contrairement au ratio de sharpe qii prend en comptr tous les observations
def sortino_ratio(series, N,rf):
    mean = series.mean() * N -rf
    std_neg = series[series<0].std()*np.sqrt(N)
    return mean/std_neg   

# Calcul du Ratio de Sortino
# Ce ratio ne prend en compte les variables nuisibles contrairement au ratio de sharpe qii prend en comptr tous les observations
# on créé une fonction permettant le calcul de ce ratio 
#on fait appelle à cette fonction dans notre programme 

#sortinos = df.apply(sortino_ratio, args=(N,rf,), axis=0 )
#sortinos.plot.bar()
#plt.ylabel('Sortino Ratio')
#st.sidebar.checkbox(sortinos)
# Calcul du Ratio de Calmar
###
def max_drawdown(return_series):
    comp_ret = (return_series+1).cumprod()
    peak = comp_ret.expanding(min_periods=1).max()
    dd = (comp_ret/peak)-1
    return dd.min()
# Création de la focntion 