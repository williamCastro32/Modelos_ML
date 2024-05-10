# Clasificador de imágenes de gatos y perros utilizando K-Nearest Neighbors (KNN)

Este proyecto consiste en crear un clasificador de imágenes de gatos y perros utilizando el algoritmo K-Nearest Neighbors (KNN) en Python. El proceso incluye el preprocesamiento de imágenes, entrenamiento del modelo con KNN y evaluación del modelo.

## Proceso
Recolección de datos: Se utilizó un conjunto de imágenes de gatos y perros para entrenar y probar el modelo.
Preprocesamiento de imágenes: Las imágenes se convirtieron a escala de grises, se redimensionaron a 32x32 píxeles y se aplanaron para poder ser utilizadas por el algoritmo KNN.
Entrenamiento del modelo: Se utilizó la implementación de KNN de OpenCV (cv2.ml.KNearest_create()) para entrenar el modelo con las imágenes de entrenamiento.
Evaluación del modelo: Se probó el modelo con diferentes valores de k (número de vecinos) para encontrar el mejor valor que maximizara la precisión. Se obtuvo una precisión máxima del 92.5% con k=1.
Guardado del modelo: El modelo entrenado se guardó en un archivo knn_cats_and_dogs.yml para su uso futuro.

## Resultados
El modelo logró una precisión del 92.5% utilizando k=1, lo que indica que es capaz de distinguir con alta precisión entre imágenes de gatos y perros.

Este proyecto forma parte del curso de Ingeniería de IA de IBM y fue desarrollado en colaboración con IBM Cognitive Class.

# Instrucciones de uso
Clonar el repositorio.
Instalar las dependencias con pip install -r requirements.txt.
Ejecutar streamlit run app.py para iniciar la aplicación web.
Subir una imagen de un gato o un perro para obtener la predicción del modelo.

<div style="display: flex; align-items: center;">
  <a href="https://www.linkedin.com/public-profile/settings?trk=d_flagship3_profile_self_view_public_profile.com/" style="margin-right: 10px;">
    <img src="https://github.com/williamCastro32/Modelos_ML/blob/main/imagenes/in_logo.png" alt="LinkedIn" width="42" height="42">
  </a>
  <a href="mailto:willcr32@gmail.com" style="margin-right: 10px;">
    <img src="https://github.com/williamCastro32/Modelos_ML/blob/main/imagenes/gmail_logo.png" alt="Gmail" width="42" height="42">
  </a>
</div>