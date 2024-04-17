# Proyecto de Análisis de Precios de Vivienda

Este proyecto tiene como objetivo analizar y predecir los precios de las viviendas utilizando técnicas de ciencia de datos y aprendizaje automático. El conjunto de datos utilizado contiene información sobre transacciones inmobiliarias, características de las viviendas y ubicaciones geográficas.

## Contenido del Repositorio

Reg_mul.ipynb: Jupyter Notebook que contiene el código principal del proyecto.
Real_estate.csv: Conjunto de datos utilizado en el análisis.
Requerimientos
Python 3
Jupyter Notebook
Librerías: pandas, numpy, matplotlib, scikit-learn
Instalación
Clona el repositorio: git clone https://github.com/williamCastro32/Reg_Mul_analisis-precios-vivienda.git
Instala las dependencias: pip install -r requirements.txt


## Resultado del Proyecto
Después de realizar un análisis exhaustivo de los datos y entrenar varios modelos de regresión lineal, se encontró que la variable "distance_to_nearest_MRT_station" es la mejor predictor del precio de las viviendas en el área estudiada. Esta variable tiene un coeficiente de determinación (R2) de 0.8220677171860902, lo que significa que alrededor del 82.21% de la variabilidad en el precio de las viviendas puede ser explicada por la distancia a la estación de MRT más cercana.

Este hallazgo es consistente con la intuición, ya que la proximidad a servicios de transporte público suele ser un factor importante en la determinación de los precios de las viviendas. El modelo de regresión lineal desarrollado utilizando esta variable como predictor principal puede ser útil para estimar los precios de las viviendas en el área de estudio.

## El proyecto utiliza las siguientes bibliotecas de Python:

pandas
numpy
matplotlib
seaborn
scikit-learn


## Uso

Clonar este repositorio:
git clone https://github.com/tu_usuario/proyecto-analisis-precios-vivienda.git
Instalar las dependencias:
pip install -r requirements.txt
Explorar los Jupyter Notebooks para ver el análisis exploratorio de datos, la creación de modelos y la evaluación de los resultados.









