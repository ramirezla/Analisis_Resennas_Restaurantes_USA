# inicio

import streamlit as st

def app():
    # Título de la aplicación
    st.title('Inicio')
    st.title("Demo de Machine Learning")    
    st.header('Proyecto Yelp & Google Maps')

    # Cargar la imagen desde el archivo "mapa.png"
    imagen = "src/mapa.png"

    # URL que deseas enlazar
    url = "https://jl3.ntx360.net/MapaML_Grupo07_01.html"

    # Mostrar la imagen en el centro de la página
    st.image(imagen, use_column_width=True)
    # st.markdown("[MAPA]({url})")
    st.markdown("<div style='text-align: center;'><a href='{}' target='_blank'>MAPA</a></div>".format(url), unsafe_allow_html=True)


