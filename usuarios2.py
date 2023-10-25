#usuarios2

# usuarios_nltk_vader

import streamlit as st
import torch
from transformers import BertTokenizer, BertForSequenceClassification
from torch.nn.functional import softmax

import pandas as pd

import nltk
nltk.download('punkt')
nltk.download('vader_lexicon')
nltk.download('subjectivity')

from nltk.classify import NaiveBayesClassifier
from nltk.corpus import subjectivity
from nltk.sentiment import SentimentAnalyzer
from nltk.sentiment.util import *

from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk import tokenize

# neg: Siendo 0 cuando no es negativo y 1 cuando es completamente negativo
# neu: El cual será 0 cuando no es neutral y 1 cuando es completamente neutral
# pos: Que será 0 cuando no es positivo y 1 cuando es completamente positivo
# compound: Será -1 cuando el comentario sea completamente negativo, 0 cuando sea completamente neutro y 1 cuando sea totalmente positivo.
# Ejemplo usando compound: 
# para valores mayor a 10% (0.1) se puede considerar positivo,
# para valores menor a 10% (-0.1) se puede considerar negativo,
# para valores mayor a negativo y menor a positivo se puede considerar neutro,
def analisis_sentimento(text:str,positivo:int,negativo:int):
    lines_list = tokenize.sent_tokenize(text)
    sentimiento = 0
    Compuesto = 0
    #lines_list.extend(lines_list)
    for sentence in lines_list:
        sid = SentimentIntensityAnalyzer()
        ss = sid.polarity_scores(sentence)
        Compuesto += ss['compound']
    if Compuesto/len(lines_list) >= (positivo/100):
        sentimiento = 1
    elif Compuesto/len(lines_list) <= -(negativo/100):
        sentimiento = -1
    return sentimiento

def app():
    # Cargar y mostrar la imagen
    st.title('Opciones para usuarios')
    st.header('Proyecto Yelp & Google Maps')
    st.subheader('Machine Learning - NLTK Vader')
    st.subheader('Demo de Análisis de Sentimientos - Review')
    
    # Interfaz de usuario
    user_input = st.text_area('Ingrese un comentario en inglés:')
    if st.button('Analizar'):
        with st.spinner('Analizando...'):
            sentimiento_es = lambda x : "positivo" if (x == 1) else ("Negativo" if (x == -1) else "Neutro")
            prediction = sentimiento_es(analisis_sentimento(user_input,10,10))
            st.markdown(f'El sentimiento del comentario es **{prediction}**.')
