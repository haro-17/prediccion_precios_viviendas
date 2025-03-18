import streamlit as st
import pandas as pd
import numpy as np
import joblib
import matplotlib.pyplot as plt
import seaborn as sns

# Cargar los archivos .pkl
try:
    model = joblib.load("random_forest_model.pkl")
    scaler = joblib.load("scaler.pkl")
    feature_names = joblib.load("feature_names.pkl")
    data = pd.read_csv("dataset.csv")  # Agrega tu dataset de viviendas
except Exception as e:
    st.error(f"❌ Error al cargar los archivos: {e}")
    st.stop()

st.success("✅ Modelo y archivos cargados correctamente.")

# Configurar la interfaz de usuario
st.title("🏠 Predicción de Precios de Viviendas en Ámsterdam")
st.markdown("Ingrese las características de la vivienda para obtener una estimación del precio.")

# Organizar los inputs en columnas para mejor presentación
col1, col2 = st.columns(2)
input_data = {}

for i, feature in enumerate(feature_names):
    with col1 if i % 2 == 0 else col2:
        input_data[feature] = st.number_input(f"**{feature}**", min_value=0.0, format="%.2f", step=1.0)

# Botón para hacer la predicción
st.markdown("---")
if st.button("🔍 Predecir Precio"):
    input_df = pd.DataFrame([input_data])
    input_scaled = scaler.transform(input_df)
    prediction = model.predict(input_scaled)[0]
    st.markdown(f"## 💰 Precio estimado: **€{prediction:,.2f}**")

# 📊 Visualización de Datos
st.markdown("## 📈 Visualización de Datos")

# Histograma de precios
st.subheader("Distribución de Precios de Viviendas")
fig, ax = plt.subplots(figsize=(8, 4))
sns.histplot(data["price"], bins=30, kde=True, ax=ax)
ax.set_xlabel("Precio (€)")
ax.set_ylabel("Frecuencia")
st.pyplot(fig)

# Gráfico de dispersión (Área vs. Precio)
st.subheader("📏 Relación entre Área y Precio")
fig, ax = plt.subplots(figsize=(8, 4))
sns.scatterplot(x=data["area"], y=data["price"], alpha=0.6)
ax.set_xlabel("Área (m²)")
ax.set_ylabel("Precio (€)")
st.pyplot(fig)

# Mapa interactivo con ubicaciones
st.subheader("📍 Mapa de Viviendas en Ámsterdam")
st.map(data[["lat", "lon"]])

# Pie de página
st.markdown("---")
st.caption("📌 Proyecto de predicción de precios con Machine Learning")
