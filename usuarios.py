# usuarios

import streamlit as st
import torch
from transformers import BertTokenizer, BertForSequenceClassification
from torch.nn.functional import softmax

# Cargar el modelo y el tokenizador
tokenizer = BertTokenizer.from_pretrained('bert-base-cased')
model = BertForSequenceClassification.from_pretrained('bert-base-cased')

# Definir la función para la clasificación de sentimiento
def classifySentiment(review_text):
    # Tokenizar el texto
    inputs = tokenizer(review_text, return_tensors="pt", padding=True, truncation=True)

    # Realizar la clasificación de sentimientos
    with torch.no_grad():
        outputs = model(**inputs)
        logits = outputs.logits

    # Calcular las probabilidades de clase
    probs = softmax(logits, dim=1)
    label = torch.argmax(probs, dim=1)

    # Decodificar la etiqueta
    class_names = ["Negativo", "Positivo"]
    sentiment = class_names[label]    
    return sentiment

def app():
    # Cargar y mostrar la imagen
    st.title('Opciones para usuarios')
    st.header('Proyecto Yelp & Google Maps')
    st.subheader('Machine Learning - BERT')
    st.subheader('Demo de Análisis de Sentimientos - Review')
    
    # Interfaz de usuario
    user_input = st.text_area('Ingrese un comentario en inglés:')
    if st.button('Analizar'):
        with st.spinner('Analizando...'):
            prediction = classifySentiment(user_input)
            st.markdown(f'El sentimiento del comentario es **{prediction}**.')

