import streamlit as st
import pandas as pd
import plotly.express as px

# Leer el conjunto de datos
car_data = pd.read_csv('vehicles_us.csv')

# Encabezado de la aplicación
st.header('Análisis exploratorio de datos - Vehículos')

# Crear un botón
hist_button = st.button('Construir histograma')
# Generar el histograma al hacer clic
if hist_button:
    st.write(
        'Creación de un histograma para el conjunto de datos de anuncios de venta de coches')

    # Crear el histograma
    fig = px.histogram(car_data, x="odometer")

    # Mostrar el gráfico
    st.plotly_chart(fig, use_container_width=True)

# Crear otro botón
scatter_button = st.button('Construir gráfico de dispersión')
# Generar el gráfico de dispersión al hacer clic
if scatter_button:
    st.write(
        'Creación de un gráfico de dispersión para las columnas odómetro y precio')

    # Crear el gráfico de dispersión
    fig = px.scatter(car_data, x="odometer", y="price")

    # Mostrar el gráfico
    st.plotly_chart(fig, use_container_width=True)
