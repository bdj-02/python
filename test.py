from turtle import clear
import streamlit as st
import numpy as np
import pandas as pd
import yfinance as yf
import plotly.express as px


# Confirguration de la page : titre et mise en page 
st.set_page_config(page_title="Python Dashboard", page_icon="📊", layout="wide")
st.title("📊 Python Dashboard")


# Create data
liste = ['AAPL','MSFT','BNP.PA']
test_données = []
for i in range(len(liste)):
    data = yf.Ticker(f'{liste[i]}')
    test_données.append(data.history(period='max'))

# voir les données financières Apple
if st.checkbox('Voir les données financieres'):
    st.write(test_données[0])
    #creation d'une fonction dataset qui peremet de recuperer chaques données de chasue entreprise
def cours_action(test_données):
# Affichage des cours des actions 
    test_données = actions[0]
    data_test_données = test_données.sort_values("Date", ascending=False)
    data_fliter_test_données = data_test_données.filter(['Close'])
    chartdata_test_données = data_fliter_test_données.head(150)
    fig_test_données = px.line(
        chartdata_test_données,
        x=chartdata_test_données.index,
        y="Close",
        orientation="h",
        title="<b>Prix de fermeture de l'action </b>",
        color_discrete_sequence=["green"] * len(chartdata_test_données),
        template="plotly_white",
    )
    fig_test_données.update_layout(
        plot_bgcolor="rgba(0,0,0,0)",
        xaxis=(dict(showgrid=False))
    )

    all_data_test_données = data_test_données.groupby(by=["Date"]).sum()[["Volume"]].tail(20)
    fig_hourly_test_données = px.bar(
        all_data_test_données,
        x=all_data_test_données.index,
        y="Volume",
        title="<b>Volume de l'action Apple par jour </b>",
        color_discrete_sequence=["red"] * len(all_data_test_données),
        template="plotly_white",
    )
    fig_hourly_test_données.update_layout(
        xaxis=dict(tickmode="linear"),
        plot_bgcolor="rgba(0,0,0,0)",
        yaxis=(dict(showgrid=False)),
    )    
    left_column, right_column = st.columns(2)
    left_column.plotly_chart(fig_test_données, use_container_width=True)
    right_column.plotly_chart(fig_hourly_test_données, use_container_width=True)
    return test_données
