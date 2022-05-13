# PROJET PYTHON 
from tarfile import LENGTH_LINK
from turtle import clear
import streamlit as st
import numpy as np
import pandas as pd
import yfinance as yf
import plotly.express as px
from ta.trend import  macd
from ta.momentum import rsi


# Confirguration de la page : titre et mise en page 
st.set_page_config(page_title="Python Dashboard", page_icon="📊", layout="wide")
st.title("📊 Python Dashboard")


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
moyenne_mobile_1 = st.sidebar.checkbox('voir moyenne mobille et la RSI ')
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
moyenne_mobile_2 = st.sidebar.checkbox('voir moyenne mobille et la RSI de l action Microsoft')
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
moyenne_mobile_3 = st.sidebar.checkbox('voir moyenne mobille et la RSI pour la société BNP ParisBas ')
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

st.write('je vous remerci de votre attention')
st.balloons()