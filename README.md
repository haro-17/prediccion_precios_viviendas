
***Informe de Predicción de Precios de Viviendas en Ámsterdam***

# Introducción

Este informe describe el proceso de predicción de precios de viviendas en Ámsterdam utilizando técnicas de Machine Learning. El objetivo principal del análisis es identificar el mejor modelo para estimar los precios de las propiedades en la ciudad, comparando varios enfoques y evaluando su desempeño.

# Descripción de los Datos

El conjunto de datos utilizado contiene información sobre diversas propiedades en Ámsterdam. Las características incluyen el tamaño de la vivienda, la ubicación, el número de habitaciones y otras variables que pueden influir en el precio de mercado. Se realizó un análisis exploratorio para entender mejor las distribuciones de las variables y su relación con el precio de la vivienda.

# Preprocesamiento y Análisis Exploratorio

El preprocesamiento de los datos consistió en las siguientes tareas:

1. Limpieza de datos: Se eliminaron valores nulos y duplicados para garantizar la calidad del conjunto de datos.

2. Codificación de variables categóricas: Las variables categóricas fueron transformadas en variables numéricas mediante técnicas de
  codificación.

3. Normalización y escalado de variables numéricas: Las variables numéricas fueron normalizadas para garantizar que todas las         
  características tuvieran un impacto similar en los modelos.

4. Análisis exploratorio: Se realizaron análisis para identificar correlaciones entre las variables y detectar patrones que pudieran 
influir en los precios.

# Modelado y Evaluación

Se entrenaron y evaluaron los siguientes modelos para la predicción de los precios de viviendas:

* Regresión Lineal
* Support Vector Machine (SVM)
* Random Forest
* XGBoost
* Red Neuronal
  
Cada uno de estos modelos fue evaluado utilizando métricas de rendimiento como el RMSE (Root Mean Squared Error) y el R², con el fin de seleccionar el modelo con mejor desempeño predictivo.

# Resultados y Conclusiones

El análisis de los resultados indicó que el modelo Random Forest fue el que ofreció el mejor rendimiento, con el menor error y la mayor capacidad predictiva. Además, se encontró que variables como la ubicación y el tamaño de la vivienda son los factores más influyentes en la estimación del precio final.

# Hallazgos Clave

* Ubicación: Las viviendas situadas en áreas céntricas tienen un impacto considerable en el precio, a menudo superando la influencia del tamaño de la propiedad.
  
* Precios en barrios específicos: Algunos barrios con alta demanda, debido a su proximidad a áreas comerciales y turísticas, presentan precios más elevados.
  
* Desempeño de modelos: Los modelos no lineales, como XGBoost y Random Forest, demostraron ser más efectivos que los modelos lineales (como la regresión) para la predicción de precios.
  
* Normalización de datos: La normalización de las variables mejoró el desempeño de modelos como SVM y redes neuronales, que requieren datos escalados para optimizar su rendimiento.
  
# Mejoras y Trabajo Futuro

Para seguir mejorando la precisión de los modelos y ampliar su aplicabilidad, se proponen las siguientes acciones:

* Optimización de hiperparámetros: Ajustar los hiperparámetros de los modelos para obtener una mayor precisión en las predicciones.
  
* Ampliación del conjunto de datos: Incluir variables adicionales como tasas de interés hipotecarias, indicadores económicos y otros factores macroeconómicos que puedan influir en los precios de las viviendas.
  
* Técnicas de Feature Engineering: Crear nuevas variables derivadas de las existentes para mejorar la capacidad predictiva de los modelos.
  
* Implementación en tiempo real: Desarrollar un sistema que permita realizar predicciones de precios en tiempo real con datos actualizados constantemente.
  
Estas acciones contribuirán a mejorar la precisión, utilidad y escalabilidad del modelo de predicción de precios de viviendas en Ámsterdam.

📌 ***Modelo seleccionado: Random Forest, con el mejor rendimiento (R² = 0.86).***

# Archivos del Proyecto

* Main.py: Código principal para entrenar y hacer predicciones.

* feature_names.pkl: Modelo Random Forest entrenado.

* random_forest_model.pkl: Escalador para normalizar características.

* Prediccion_Precios_Viviendas_Amsterdam.csv: Datos utilizados.

* requirements.txt: Dependencias e instaladores para el modelo en Streamlit.

* scaler.pkl: Escalador para normalizar características.

*streamlit_app.py: Código que genera la interfaz en Streamlit.

# Proyecto Visual

# Ejecutar Streamlit en un servidor local a través de un túnel HTTPS seguro:

1. Instalar Streamlit y ngrok:

2. Escribir el archivo app.py: Crea un archivo app.py con el código Streamlit que ya habías desarrollado.

3. Ejecutar Streamlit: Usa ngrok para crear un túnel HTTP a tu servidor local (Streamlit). Luego ejecuta Streamlit de forma que se pueda acceder al servidor a través de una URL pública.

# Desplegar en Streamlit Cloud:

1. Crear una cuenta en Streamlit Cloud: Dirígete a Streamlit Cloud y crea una cuenta si aún no tienes una.

2. Subir tu proyecto a GitHub: Si no tienes un repositorio en GitHub, crea uno. Sube todos tus archivos: app.py, el modelo (random_forest_model.pkl), el escalador (scaler.pkl) y cualquier otro archivo necesario como feature_names.pkl.

3. Conectar tu repositorio de GitHub con Streamlit Cloud: En la página de Streamlit Cloud, haz clic en "New app" y selecciona tu repositorio de GitHub. Streamlit automáticamente detectará que tienes un archivo app.py y lo ejecutará.

4. Instalación de librerías y dependencias: Crea el archivo requirements.txt con todas las librerías y sus versiones que necesitará tu proyecto en la plataforma Streamlit Cloud. La plataforma te indicará qué librerías deben instalarse o actualizarse en los logs (Manage app).

5. Desplegar la aplicación: ¡Listo! Tu aplicación estará accesible desde una URL pública proporcionada por Streamlit Cloud.

# Conclusiones

✅ Random Forest es el mejor modelo para predecir precios de viviendas en Ámsterdam.

✅ Se optimizaron los hiperparámetros para mejorar la precisión.

✅ El modelo puede ser implementado para hacer predicciones en tiempo real.

Autor: Diego Haro, haro-17

Fecha de creación: marzo, 2025

🔗 Código creado en Google Colab https://colab.research.google.com/drive/1N016w0UeHpmBa2JIIioN51pVv_XMVUrw?usp=sharing

🔗 Repositorio en GitHub https://github.com/haro-17/prediccion_precios_viviendas

🔗 Interfaz gráfica creada en Streamlit Cloud https://prediccionpreciosviviendas-crvktucdavahwkykxmxjer.streamlit.app/

