from turtle import clear
import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf

#  Création et importation de données
apple =  yf.Ticker('AAPL')
datadf = apple.history(period='max', start='2020-1-1', end='2021-1-1' )

#test Moyenne 
dataFrame = pd.DataFrame(data=datadf, columns=['Close'])
dataFrame
#calcul de la moyenne 
cal_moy = dataFrame.mean()
cal_moy


#Avec matplotlib, créer une figure et la stocker dans la variable fig1
#fig1 =data['Close'].plot()
#plt.show(fig1)  
#Avec la fonction scatter dessiner un nuage de point
#plt.scatter(x, y, c = 'blue')

# Afficher les résusltats des calculs sur streamlit
#vec la fonction st.pyplot afficher la figure

#input qui permet d'écrire 
st.write("Bonjour mon projet Python")

name = st.text_input("comment tu t'appelles ?")
if name: 
    st.write("bonjour " + name)
