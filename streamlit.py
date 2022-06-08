# PROJET PYTHON 
from tarfile import LENGTH_LINK
from turtle import clear
from PIL import Image
from pyrsistent import b
from libs.lib import get_date
from libs.ratio import sharpe_ratio
from libs.ratio import sortino_ratio
from libs.ratio import max_drawdown
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
# Create data
start = dt.datetime(2013, 1, 1)
end = dt.datetime(2022, 1, 1)

tickers = ['AAPL','MSFT','BNP.PA']
actions =[]
data = web.DataReader(tickers,
                        'yahoo', start, end)['Adj Close']

st.write(data)

cols = st.columns(2)

# Creation du grphique

fig4 = px.line(data, y=tickers,) 
cols[0].plotly_chart(fig4, use_container_width=True)

# Ccalcule de la moyenne et ajout d'une colonne Portefeuille pour mieux voir l'évoulution des cours d'action en fonction du portefeuille
df = data.pct_change().dropna()
df['Portefeuiile'] = df.mean(axis=1) # 20% apple, ... , 20% Bnp Paris_bas
df_1  = (df + 1).cumprod()

# Affichage des données
st.write(df_1)
# Affichage du graphique associé
cols = st.columns(2)
fig5 = px.line(df_1, y=tickers.append(['Portefeuiile']))
cols[0].plotly_chart(fig5, use_container_width=True)

#################################### Calcul Ratio de sharpe ######################################################"
# On fait appelle à la fonction permettant de calculer le ratio de sharpes

N = 255 
rf = 0.01 
sharpes = df_1.apply(sharpe_ratio, args=(N,rf),axis=0)

Ratio_1 = st.sidebar.checkbox('voir le Ratio de Sharpes ')
if Ratio_1:
    st.write(sharpes) 
    st.text('le ratio de sharpes des 3 entreprises, ' ) 
    st.bar_chart(sharpes)  

#################################### Calcul Ratio de Sortino ######################################################"
# Calcul du Ratio de Sortino
# Ce ratio ne prend en compte les variables nuisibles contrairement au ratio de sharpe qii prend en comptr tous les observations
# on créé une fonction permettant le calcul de ce ratio 
#on fait appelle à cette fonction dans notre programme 
    
N = 255 #255 trading days in a year
rf = 0.01 #1% risk free rate

sortinos = df.apply(sortino_ratio, args=(N,rf,),axis=0)

Ratio_2 = st.sidebar.checkbox('voir le Ratio de Sortinos ')
if Ratio_2:
    st.write(sortinos) 
    st.text('le ratio de sortinos des 3 entreprises, ' ) 
    st.bar_chart(sortinos)

############### Calcule ratio de calmar ########################

max_drawdowns = df.apply(max_drawdown,axis=0)
if st.checkbox('La perte successive'):
    st.write('max_drawdowns')
    st.write(max_drawdowns)
    st.write('la perte maximale: permet de déterminer la perte successive maximale ')
    st.write('cet indicateur permet également de savoir si notre système est rentable ou pas.')
    st.write('permet d’obtenir une synthèse de votre performance et de la qualité de votre stratégie en bourse')
    st.bar_chart(max_drawdowns)
# Ratio Calmar : donne le ratio entre le Risque/Rendement
calmars = df.mean()*255/abs(max_drawdowns)

Ratio_3 = st.sidebar.checkbox('voir le Ratio du Rapport Calmaire ')
if Ratio_3:
    st.write(' Ratio de Calmar permet de calculer le ratio entre le Rsique et le Rendement ')
    st.write(calmars) 
    st.write(' il semble que Microsoft soit le plus performant selon ce ratio') 
    st.bar_chart(calmars)

# Création d'un DataFrame permettant de regrouper tous les ratios calculés. 

if st.checkbox('Création d un DataFrame permettant de regrouper tous les ratios calculés'):
    st.write('Regroupement des données calculées séparement') 

btstats = pd.DataFrame()
btstats['sortino'] = sortinos
btstats['sharpe'] = sharpes
btstats['maxdd'] = max_drawdowns
btstats['calmar'] = calmars

Ratio_4 = st.sidebar.checkbox('Traçage de la trame de données sous forme de table')
if Ratio_4:
    st.write(btstats) 
# Creation du grphique
fig6 = plt.table(cellText=np.round(btstats.values,2), colLabels=btstats.columns,
          rowLabels=btstats.index,rowLoc='center',cellLoc='center',loc='top',
          colWidths=[0.25]*len(btstats.columns))
if st.checkbox('Constat Global'):
    st.write('Au vue de notre étude, Microsoft est la seule entreprise qui a les ratios les plus rentables, les indices les plus significatifs  ')
if st.checkbox('Fin du Projet'):
    st.balloons()
    #st.video("https://giphy.com/gifs/the-end-hcpVSCSwDcKju", format="vide/mp4")