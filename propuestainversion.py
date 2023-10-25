#filtros

import pandas as pd
import streamlit as st
import streamlit.components.v1 as components
from pandas.api.types import (
    is_categorical_dtype,
    is_datetime64_any_dtype,
    is_numeric_dtype,
    is_object_dtype,
)

# st.title("Auto Filter Dataframes in Streamlit")
# st.write(
#     """Luis A, Ramirez G.
#     """
# )

def filter_dataframe(df: pd.DataFrame) -> pd.DataFrame:
    """
    Adds a UI on top of a dataframe to let viewers filter columns

    Args:
        df (pd.DataFrame): Original dataframe

    Returns:
        pd.DataFrame: Filtered dataframe
    """
    modify = st.checkbox("Add filters")

    if not modify:
        return df 

    # df = df.copy()

    modification_container = st.container()

    with modification_container:
        to_filter_columns = st.multiselect("Filter dataframe on", df.columns)
        for column in to_filter_columns:
            left, right = st.columns((1, 20))
            left.write("↳")
            # Treat columns with < 10 unique values as categorical
            if is_categorical_dtype(df[column]) or df[column].nunique() < 10:
                user_cat_input = right.multiselect(
                    f"Values for {column}",
                    df[column].unique(),
                    default=list(df[column].unique()),
                )
                df = df[df[column].isin(user_cat_input)]
            elif is_numeric_dtype(df[column]):
                _min = float(df[column].min())
                _max = float(df[column].max())
                step = (_max - _min) / 100
                user_num_input = right.slider(
                    f"Values for {column}",
                    _min,
                    _max,
                    (_min, _max),
                    step=step,
                )
                df = df[df[column].between(*user_num_input)]
            elif is_datetime64_any_dtype(df[column]):
                user_date_input = right.date_input(
                    f"Values for {column}",
                    value=(
                        df[column].min(),
                        df[column].max(),
                    ),
                )
                if len(user_date_input) == 2:
                    user_date_input = tuple(map(pd.to_datetime, user_date_input))
                    start_date, end_date = user_date_input
                    df = df.loc[df[column].between(start_date, end_date)]
            else:
                user_text_input = right.text_input(
                    f"Substring or regex in {column}",
                )
                if user_text_input:
                    df = df[df[column].str.contains(user_text_input)]

    return df

def app():
    # Cargar y mostrar la imagen
    st.title('Propuesta de Inversión')
    st.header('Proyecto Yelp & Google Maps')
    st.subheader('Propuestas de Inversiones')
    st.subheader('Filtros')
    data_url = "./Datasets_ML_NuevosDatasetsML_Consolidado_Businees_Review_Tip_inversion.parquet"

    df = pd.read_parquet(data_url)
# ['Total_CincoEstrellas', 'review_count', 'T_S_P_Review', 'T_S_P_Tip', 'Total_useful', 
# 'Total_funny', 'Total_cool']

    ### Defiiendo Columnas de Inversion
    Columnas_inversion = ['name', 'city', 'state', 
                    'stars', 'review_count', 'Categorias', 'SubCategorias',
                    'Total_Estrellas', 'Total_CincoEstrellas' , 
                    'T_S_P_Review',
                    'Total_useful', 'Total_funny', 'Total_cool', 
                    'T_S_P_Tip',
                    'latitude', 'longitude','address']

    ### Creando DataSets de Inversión
    df_inversion = df[Columnas_inversion]

    st.dataframe(filter_dataframe(df_inversion))