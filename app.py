import streamlit as st
import pandas as pd
import plotly.express as px

car_data = pd.read_csv('vehicles_us.csv') #leo los datos
st.header("Aplicacion para estudiar datos?")

hist_button = st.checkbox('Construir un histograma')
scat_button = st.checkbox("Construir un gráfico de dispersión")

#hist_button = st.button('Construir histograma')

if hist_button: #al hacer clic en el botón
    #escribir un mensaje
    st.write("Creación de un histograma para el conjunto de datos de anuncion de venta de automóviles")

    #crear un histograma
    fig = px.histogram(car_data, x="odometer")

    #mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

#scat_button = st.button('Construir gráfico de dispersión')

if scat_button: #al hacer clic en el botón
    #escribir mensaje
    st.write("Creación de un gráfico de dispersion para el conjunto de datos de anuncions de venta de automóviles")

    #crear el gráfico de dispersion
    fig =px.scatter(car_data, x="odometer", y="price")

    #mostrar un gráfico plotly interactivo
    st.plotly_chart(fig, use_container_width=True)