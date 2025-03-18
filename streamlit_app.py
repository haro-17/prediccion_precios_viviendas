import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Cargar los archivos .pkl
try:
    model = joblib.load("random_forest_model.pkl")
    scaler = joblib.load("scaler.pkl")
    feature_names = joblib.load("feature_names.pkl")
except Exception as e:
    st.error(f"Error al cargar los archivos: {e}")
    st.stop()  # Detiene la ejecución del código

# Ahora, puedes usar estos archivos cargados en tu aplicación
st.write("Modelo y archivos cargados correctamente.")

# Configurar la interfaz de usuario
st.title("Predicción de Precios de Viviendas en Ámsterdam 🏠")

st.markdown("Ingrese las características de la vivienda para obtener una estimación del precio.")

# Crear campos de entrada para cada característica
input_data = {}
for feature in feature_names:
    input_data[feature] = st.number_input(f"{feature}", min_value=0.0, format="%.2f")

# Botón para hacer la predicción
if st.button("Predecir Precio"):
    # Convertir la entrada en DataFrame
    input_df = pd.DataFrame([input_data])
    
    # Normalizar los datos con el mismo escalador usado en el entrenamiento
    input_scaled = scaler.transform(input_df)
    
    # Hacer la predicción
    prediction = model.predict(input_scaled)[0]
    
    # Mostrar el resultado
    st.success(f"💰 Precio estimado: €{prediction:,.2f}")

# Agregar un pie de página
st.markdown("---")
st.markdown("📌 Proyecto de predicción de precios con Machine Learning")
