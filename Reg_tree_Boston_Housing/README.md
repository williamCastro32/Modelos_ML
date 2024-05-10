# Predicción de Precios de Viviendas en Boston

Este proyecto tiene como objetivo predecir el precio medio de las casas en diferentes áreas de Boston utilizando técnicas de machine learning.

## Descripción
Utilizamos el conjunto de datos Boston Housing Prices, que contiene información sobre diversas características de las viviendas en Boston, como la tasa de criminalidad, la proporción de zonas residenciales, la cantidad de habitaciones por vivienda, entre otras.

## Proceso y Resultados
Exploración de Datos: Se identificó la necesidad de manejar datos faltantes y se descubrió una distribución normal en la variable objetivo (precio de las viviendas).
Preprocesamiento de Datos: Se realizaron las transformaciones necesarias, como el manejo de datos faltantes y la normalización de variables.
Modelado: Utilizamos árboles de regresión y realizamos una búsqueda de hiperparámetros utilizando grid search. Los mejores hiperparámetros encontrados fueron: {'criterion': 'poisson'}. El modelo final tuvo un Error Cuadrático Medio (MSE) de 12.337 y un coeficiente de determinación (R^2) de 0.872.

## Uso
Abre el archivo Reg_tree_Boston_house_price.ipynb.ipynb en Jupyter Notebook.
Ejecuta las celdas para cargar los datos, entrenar el modelo y realizar predicciones.
Analiza los resultados obtenidos y la precisión del modelo.

## Contacto

<div style="display: flex; align-items: center;">
  <a href="https://www.linkedin.com/public-profile/settings?trk=d_flagship3_profile_self_view_public_profile.com/" style="margin-right: 10px;">
    <img src="https://github.com/williamCastro32/Modelos_ML/blob/main/imagenes/in_logo.png" alt="LinkedIn" width="42" height="42">
  </a>
  <a href="mailto:willcr32@gmail.com" style="margin-right: 10px;">
    <img src="https://github.com/williamCastro32/Modelos_ML/blob/main/imagenes/gmail_logo.png" alt="Gmail" width="42" height="42">
  </a>
</div>




