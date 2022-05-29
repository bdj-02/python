# PROJET PYTHON 
from tarfile import LENGTH_LINK
from turtle import clear
from PIL import Image
from libs.lib import get_date
from libs.ratio import sharpe_ratio
from libs.ratio import sortino_ratio

import streamlit as st
import datetime as dt
import numpy as np
import pandas as pd
import yfinance as yf
import plotly.express as px
import time 
import plotly
from ta.trend import  macd
import matplotlib.pyplot as plt
import pandas_datareader.data as web
from ta.momentum import rsi


# Confirguration de la page : titre et mise en page 
st.set_page_config(page_title="Python Dashboard", page_icon="📊", layout="wide")
st.title("📊 Python Dashboard")

# Ajout d'une image au bord
#image = Image.open('Image.jpg')
st.image("https://www.pexiweb.be/wp-content/uploads/2020/08/Custom-Software-Development.jpg", use_column_width=True)




# Create data
liste = ['AAPL','MSFT','BNP.PA']
actions = []
for i in range(len(liste)):
    data = yf.Ticker(f'{liste[i]}')
    actions.append(data.history(period='max'))

# voir les données financières Apple
if st.checkbox('Voir les données financieres Apple'):
    st.write(actions[0])

# Affichage des cours des actions 
apple = actions[0]
data_apple = apple.sort_values("Date", ascending=False)
data_fliter_apple = data_apple.filter(['Close'])
chartdata_apple = data_fliter_apple.head(150)
fig_apple = px.line(
    chartdata_apple,
    x=chartdata_apple.index,
    y="Close",
    orientation="h",
    title="<b>Prix de fermeture de l'action </b>",
    color_discrete_sequence=["green"] * len(chartdata_apple),
    template="plotly_white",
)
fig_apple.update_layout(
    plot_bgcolor="rgba(0,0,0,0)",
    xaxis=(dict(showgrid=False))
)

all_data_apple = data_apple.groupby(by=["Date"]).sum()[["Volume"]].tail(20)
fig_hourly_apple = px.bar(
    all_data_apple,
    x=all_data_apple.index,
    y="Volume",
    title="<b>Volume de l'action Apple par jour </b>",
    color_discrete_sequence=["red"] * len(all_data_apple),
    template="plotly_white",
)
fig_hourly_apple.update_layout(
    xaxis=dict(tickmode="linear"),
    plot_bgcolor="rgba(0,0,0,0)",
    yaxis=(dict(showgrid=False)),
)    
left_column, right_column = st.columns(2)
left_column.plotly_chart(fig_apple, use_container_width=True)
right_column.plotly_chart(fig_hourly_apple, use_container_width=True)

apple["MACD"] = macd(close=apple["Close"], window_slow=26, window_fast=12, fillna=True)
apple["RSI"] = rsi(close=apple["Close"], window=14, fillna=True)
moyenne_mobile_1 = st.sidebar.checkbox('voir moyenne mobile et la RSI ')
if moyenne_mobile_1 :
    data_apple = apple.sort_values("Date", ascending=False)
    data_fliter_apple = data_apple.filter(['RSI'])
    chartdata_apple = data_fliter_apple.head(150)
    fig_1 = px.line(
        chartdata_apple,
        x=chartdata_apple.index,
        y="RSI",
        orientation="h",
        title="<b>indicateur technique : momentum RSI </b>",
        color_discrete_sequence=["blue"] * len(chartdata_apple),
        template="plotly_white",
        )
    fig_1.update_layout(
        plot_bgcolor="rgba(0,0,0,0)",
        xaxis=(dict(showgrid=False))
        )
    #fi_2
    data_fig_2 = data_apple.filter(['MACD'])
    chartdata_fig_2 = data_fig_2.head(150)
    fig_2 = px.line(
        chartdata_fig_2,
        x=chartdata_fig_2.index,
        y="MACD",
        orientation="h",
        title="<b>indicateur technique: moyenne mobile </b>",
        color_discrete_sequence=["yellow"] * len(chartdata_fig_2),
        template="plotly_white",
        )
    fig_2.update_layout(
        plot_bgcolor="rgba(0,0,0,0)",
        xaxis=(dict(showgrid=False))
        )    
    left_column, right_column = st.columns(2)
    left_column.plotly_chart(fig_1, use_container_width=True)
    right_column.plotly_chart(fig_2, use_container_width=True)

# voir les données financières Microsoft
if st.checkbox('Voir les données financieres Microsoft'):
    st.write(actions[1])

# Affichage des cours des actions 
microsoft = actions[1]
data_microsoft = microsoft.sort_values("Date", ascending=False)
data_fliter_microsoft = data_microsoft.filter(['Close'])
chartdata_microsoft = data_fliter_microsoft.head(150)
fig_microsoft = px.line(
    chartdata_microsoft,
    x=chartdata_microsoft.index,
    y="Close",
    orientation="h",
    title="<b>Prix de fermeture de l'action </b>",
    color_discrete_sequence=["blue"] * len(chartdata_microsoft),
    template="plotly_white",
)
fig_microsoft.update_layout(
    plot_bgcolor="rgba(0,0,0,0)",
    xaxis=(dict(showgrid=False))
)

all_data_microsoft = data_microsoft.groupby(by=["Date"]).sum()[["Volume"]].tail(20)
fig_hourly_microsoft = px.bar(
    all_data_microsoft,
    x=all_data_microsoft.index,
    y="Volume",
    title="<b>Volume de l'action Microsoft par jour </b>",
    color_discrete_sequence=["orange"] * len(all_data_microsoft),
    template="plotly_white",
)
fig_hourly_microsoft.update_layout(
    xaxis=dict(tickmode="linear"),
    plot_bgcolor="rgba(0,0,0,0)",
    yaxis=(dict(showgrid=False)),
)    
left_column, right_column = st.columns(2)
left_column.plotly_chart(fig_microsoft, use_container_width=True)
right_column.plotly_chart(fig_hourly_microsoft, use_container_width=True)

microsoft["MACD"] = macd(close=apple["Close"], window_slow=26, window_fast=12, fillna=True)
microsoft["RSI"] = rsi(close=apple["Close"], window=14, fillna=True)
moyenne_mobile_2 = st.sidebar.checkbox('voir moyenne mobile et la RSI de l action Microsoft')
if moyenne_mobile_2 :
    data_microsoft = microsoft.sort_values("Date", ascending=False)
    data_fliter_microsoft = data_microsoft.filter(['RSI'])
    chartdata_microsoft = data_fliter_microsoft.head(150)
    fig_1 = px.line(
        chartdata_microsoft,
        x=chartdata_microsoft.index,
        y="RSI",
        orientation="h",
        title="<b>indicateur technique : momentum RSI </b>",
        color_discrete_sequence=["green"] * len(chartdata_microsoft),
        template="plotly_white",
        )
    fig_1.update_layout(
        plot_bgcolor="rgba(0,0,0,0)",
        xaxis=(dict(showgrid=False))
        )
    #fi_2
    data_fig_2 = data_microsoft.filter(['MACD'])
    chartdata_fig_2 = data_fig_2.head(150)
    fig_2 = px.line(
        chartdata_fig_2,
        x=chartdata_fig_2.index,
        y="MACD",
        orientation="h",
        title="<b>indicateur technique: moyenne mobile </b>",
        color_discrete_sequence=["red"] * len(chartdata_fig_2),
        template="plotly_white",
        )
    fig_2.update_layout(
        plot_bgcolor="rgba(0,0,0,0)",
        xaxis=(dict(showgrid=False))
        )    
    left_column, right_column = st.columns(2)
    left_column.plotly_chart(fig_1, use_container_width=True)
    right_column.plotly_chart(fig_2, use_container_width=True)

# voir les données financières BNP ParisBas
if st.checkbox('Voir les données financieres BNP ParisBas'):
    st.write(actions[2])

# Affichage des cours des actions 
BNP_ParisBas = actions[2]
data_BNP_ParisBas = BNP_ParisBas.sort_values("Date", ascending=False)
data_fliter_BNP_ParisBas = data_BNP_ParisBas.filter(['Close'])
chartdata_BNP_ParisBas = data_fliter_BNP_ParisBas.head(150)
fig_BNP_ParisBas = px.line(
    chartdata_BNP_ParisBas,
    x=chartdata_BNP_ParisBas.index,
    y="Close",
    orientation="h",
    title="<b>Prix de fermeture de l'action BNP ParisBas </b>",
    color_discrete_sequence=["brown"] * len(chartdata_BNP_ParisBas),
    template="plotly_white",
)
fig_BNP_ParisBas.update_layout(
    plot_bgcolor="rgba(0,0,0,0)",
    xaxis=(dict(showgrid=False))
)

all_data_BNP_ParisBas = data_BNP_ParisBas.groupby(by=["Date"]).sum()[["Volume"]].tail(20)
fig_hourly_BNP_ParisBas = px.bar(
    all_data_BNP_ParisBas,
    x=all_data_BNP_ParisBas.index,
    y="Volume",
    title="<b>Volume de l'action BNP ParisBas par jour </b>",
    color_discrete_sequence=["purple"] * len(all_data_BNP_ParisBas),
    template="plotly_white",
)
fig_hourly_BNP_ParisBas.update_layout(
    xaxis=dict(tickmode="linear"),
    plot_bgcolor="rgba(0,0,0,0)",
    yaxis=(dict(showgrid=False)),
)    
left_column, right_column = st.columns(2)
left_column.plotly_chart(fig_BNP_ParisBas, use_container_width=True)
right_column.plotly_chart(fig_hourly_BNP_ParisBas, use_container_width=True)

BNP_ParisBas["MACD"] = macd(close=apple["Close"], window_slow=26, window_fast=12, fillna=True)
BNP_ParisBas["RSI"] = rsi(close=apple["Close"], window=14, fillna=True)
moyenne_mobile_3 = st.sidebar.checkbox('voir moyenne mobile et la RSI pour la société BNP ParisBas ')
if moyenne_mobile_3 :
    data_BNP_ParisBas = BNP_ParisBas.sort_values("Date", ascending=False)
    data_fliter_BNP_ParisBas = data_BNP_ParisBas.filter(['RSI'])
    chartdata_BNP_ParisBas = data_fliter_BNP_ParisBas.head(150)
    fig_1 = px.line(
        chartdata_BNP_ParisBas,
        x=chartdata_BNP_ParisBas.index,
        y="RSI",
        orientation="h",
        title="<b>indicateur technique : momentum RSI </b>",
        color_discrete_sequence=["violet"] * len(chartdata_BNP_ParisBas),
        template="plotly_white",
        )
    fig_1.update_layout(
        plot_bgcolor="rgba(0,0,0,0)",
        xaxis=(dict(showgrid=False))
        )
    #fi_2
    data_fig_2 = data_BNP_ParisBas.filter(['MACD'])
    chartdata_fig_2 = data_fig_2.head(150)
    fig_2 = px.line(
        chartdata_fig_2,
        x=chartdata_fig_2.index,
        y="MACD",
        orientation="h",
        title="<b>indicateur technique: moyenne mobile </b>",
        color_discrete_sequence=["pink"] * len(chartdata_fig_2),
        template="plotly_white",
        )
    fig_2.update_layout(
        plot_bgcolor="rgba(0,0,0,0)",
        xaxis=(dict(showgrid=False))
        )    
    left_column, right_column = st.columns(2)
    left_column.plotly_chart(fig_1, use_container_width=True)
    right_column.plotly_chart(fig_2, use_container_width=True)


# Récupération et Initialisation pour traitement des données 
### Create data
tickers = ['AAPL','MSFT','BNP.PA']

# On créé une liste contenant les données des entreprises que l'on aura choisit de faire l'étude

# on crée une fonction qui nous permet de recuperer les données que nous voulions utliser
# ici dans notre cas il s'agit des observations 'Close'
    ### la fonction utliser est celle stockée dans la library Get_date
    ### on fait appelle à la fonction pour récuperer les données 

#*********************************************************

# testing data bnp
BNP = get_date('BNP.PA',2008,2022)
Apple = get_date('AAPL',2008,2022)
microsoft = get_date('MSFT',2008,2022)

Apple['Close BNP'] = BNP['Adj Close']
Apple['Close microsoft'] = microsoft['Adj Close']

if st.checkbox('Voir données financières avant tri'):
    st.write(' Récupération des données brutes avant tri et traitements de données')
    st.write(Apple)



bnp = get_date('BNP.PA',2008,2022)
Apple = get_date('AAPL',2008,2022)
microsoft = get_date('MSFT',2008,2022)
# Affichage des données graces à une checkbox
Apple['Close BNP'] = bnp['Adj Close']
Apple['Close microsoft'] = microsoft['Adj Close']
Apple = Apple.drop(['Open','High', 'Volume', 'Low', 'Close'], axis=1)
#st.write(Apple) 

if st.sidebar.checkbox('Récupération des données des 3 entreprises entreprises pour traitement : cas général'):
    st.write(' Récupération des données brutes après tri et traitements de données')
    st.write(Apple)
#********************************************
cols = st.columns(2)

# Creation du grphique
fig4 = px.line(Apple,x="Date" ,y=['Adj Close','Close BNP','Close microsoft'],) # met le nom de la colonne date ici dans X='
cols[0].plotly_chart(fig4, use_container_width=True)

# Calcule de la moyenne 
tickers = ['AAPL','MSFT','BNP.PA']

bnp = get_date('BNP.PA',2013,2022)
apple = get_date('AAPL',2013,2022)
microsoft = get_date('MSFT',2013,2022)
apple['Close BNP'] = bnp['Adj Close']
apple['Close microsoft'] = microsoft['Adj Close']
df = apple.drop(['Open','High', 'Low', 'Volume','Close'], axis=1)
#st.write(df)

df['Moyenne'] = df.mean(axis=1) # 20% apple, ... , 20% Bnp Paris_bas
print(df)
df_1 = df.copy()

if st.checkbox('Voir données financières des 3 entreprises'):
    st.write(df_1)

#********************************************
df_1.reset_index(inplace = True)
df_1=df_1.drop(['index'],axis=1)
cols_2 = st.columns(2)

# Creation du grphique
fig5 = px.line(df_1,x="Date" ,y=['Adj Close','Close BNP','Close microsoft','Moyenne'],) # met le nom de la colonne date ici dans X='
cols_2[0].plotly_chart(fig5, use_container_width=False)

#################################### Calcul Ratio de sharpe ######################################################"
# On fait appelle à la fonction permettant de calculer le ratio de sharpes
def sharpe_ratio(return_series, N, rf):
    mean = return_series.mean() * N - rf
    sigma = return_series.std() * np.sqrt(N)
    return mean / sigma

df_2 = df.copy()
df_2 = df_2.set_index("Date")
print(df_2)


N = 255 #255 trading days in a year
rf = 0.01 #1% risk free rate
sharpes = df_2.apply(sharpe_ratio, args=(N,rf,),axis=0)

data  = {'Sharpes': [i for i in sharpes]}
sharpes = pd.DataFrame(data=data)

Ratio_1 = st.sidebar.checkbox('voir le Ratio de Sharpes ')
if Ratio_1:
    st.write(sharpes["Sharpes"])  
    st.bar_chart(sharpes)
#fig6 = px.line(sharpes,x="Date" ,y=['Adj Close','Close BNP','Close microsoft','Moyenne'],) # met le nom de la colonne date ici dans X='
#cols_2[0].plotly_chart(fig6, use_container_width=False)
