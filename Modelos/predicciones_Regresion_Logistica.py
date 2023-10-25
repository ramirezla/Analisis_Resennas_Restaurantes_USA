import pandas as pd
import numpy as np
from datetime import datetime
import matplotlib.pyplot as plt
import seaborn as sns
import os
import io
import json
import gcsfs
import scipy.optimize as opt
from sklearn import preprocessing### Seleccionando Variables

### Cargando DataSets Consolidado para Análisis de ML: 'df_business_yelp_ML.parquet'
# Ruta completa en Cloud Storage
ruta_eda_datalike = "gs://gmy/Datasets_ML/df_ML_promedios_Final.parquet"
# Lee el archivo Parquet directamente en un DataFrame de pandas
df_ML_promedios_Final = pd.read_parquet(ruta_eda_datalike, storage_options={"project": "Proyecto Final - Henry"})




+def analisis_sentimento(text:str,positivo:int,negativo:int):
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
            prediction = sentimiento_es(analisis_sentimento(fila['text'],10,10))
            st.markdown(f'El sentimiento del comentario es **{prediction}**.')
