from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib
import numpy as np

# Cargar los archivos guardados del modelo
model = joblib.load("random_forest_model.pkl")
scaler = joblib.load("scaler.pkl")
feature_names = joblib.load("feature_names.pkl")

# Crear la API con FastAPI
app = FastAPI()

# Crear la estructura de entrada basada en las características originales
class HouseFeatures(BaseModel):
    features: list[float]  # Lista con los valores de las características

@app.post("/predict")
def predict_price(features: HouseFeatures):
    # Verificar que el número de características sea correcto
    if len(features.features) != len(feature_names):
        raise HTTPException(status_code=400, detail=f"Se esperaban {len(feature_names)} características, pero se recibieron {len(features.features)}.")

    # Convertir a NumPy array y escalar los datos
    data = np.array([features.features])
    data_scaled = scaler.transform(data)

    # Hacer la predicción
    prediction = model.predict(data_scaled)
    return {"predicted_price": prediction[0]}

