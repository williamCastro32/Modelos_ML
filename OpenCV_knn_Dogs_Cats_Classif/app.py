import streamlit as st
import cv2
import numpy as np

# Cargar el modelo KNN previamente guardado
model = cv2.ml.KNearest_load('knn_cats_and_dogs.yml')

# Función para predecir una imagen dada
def predict_image(image):
    # Preprocesar la imagen (convertir a escala de grises, redimensionar, aplanar)
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    resized_image = cv2.resize(gray_image, (32, 32))
    flattened_image = resized_image.flatten().astype('float32')

    # Realizar la predicción utilizando el modelo KNN
    ret, result, neighbors, dist = model.findNearest(flattened_image.reshape(1, -1), k=1)

    # Convertir el resultado a una etiqueta legible
    label = 'Gato' if result == 1 else 'Perro'
    return label

# Configurar la aplicación de Streamlit
st.title('Clasificador de Gatos y Perros')
uploaded_file = st.file_uploader('Sube una imagen de un gato o un perro:', type=['png', 'jpg'])

if uploaded_file is not None:
    # Cargar la imagen y mostrarla
    image = cv2.imdecode(np.fromstring(uploaded_file.read(), np.uint8), 1)
    st.image(cv2.cvtColor(image, cv2.COLOR_BGR2RGB), caption='Imagen subida', use_column_width=True)
    
    # Realizar la predicción y mostrar el resultado
    prediction = predict_image(image)
    st.write(f'La imagen subida parece ser un/a {prediction.lower()}')
