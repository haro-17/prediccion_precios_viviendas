import streamlit as st
import joblib
import numpy as np

# Cargar el modelo
modelo = joblib.load("modelo_precio_viviendas.pkl")

# Estilos CSS para personalización
st.markdown("""
    <style>
        .main { background-color: #f5f5f5; }
        h1 { color: #FF5733; text-align: center; }
        .stButton>button { background-color: #FF5733; color: white; }
    </style>
""", unsafe_allow_html=True)

# Título y descripción
st.title("🏠 Predicción de Precios de Viviendas en Ámsterdam")
st.markdown("### Ingrese las características de la vivienda para obtener una estimación del precio")

# Imagen decorativa
st.image("house.jpg", use_column_width=True)

# Organización en dos columnas
col1, col2 = st.columns(2)

with col1:
    area = st.slider("📏 Área (m²)", min_value=10, max_value=500, value=50, step=1)
    room = st.slider("🛏 Habitaciones", min_value=1, max_value=10, value=2, step=1)

with col2:
    lon = st.number_input("📍 Longitud", min_value=-180.0, max_value=180.0, step=0.01)
    lat = st.number_input("📍 Latitud", min_value=-90.0, max_value=90.0, step=0.01)

# Botón de predicción
if st.button("💰 Calcular Precio"):
    entrada = np.array([[area, room, lon, lat]])
    precio_estimado = modelo.predict(entrada)[0]
    st.success(f"Precio estimado: €{precio_estimado:,.2f}")
