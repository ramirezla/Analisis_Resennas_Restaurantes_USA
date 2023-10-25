import inicio, usuarios, usuarios2, negocios, inversionistas, propuestainversion, acercade
import streamlit as st
from streamlit_option_menu import option_menu

# logo_url = "./src/LogoJL3.png"
# st.markdown.image(logo_url)
st.set_page_config(
        page_title="JL3",
        layout="wide",
)

class MultiApp:

    def __init__(self):
        self.apps = []

    def add_app(self, title, func):

        self.apps.append({
            "title": title,
            "function": func
        })       

    def run():
        # app = st.sidebar(
        with st.sidebar:        
            app = option_menu(
                menu_title='JL3 ',
                options=['inicio','usuarios ml 1','usuarios ml 2','negocios','inversionistas', 'propuesta inversion','acerca de'],
                icons=['house-fill','person-circle','person-circle','person-circle', 'person-circle','person-circle', 'info-circle-fill'],
                menu_icon='chat-text-fill',
                default_index=0,
                styles={
                    "container": {"padding": "5!important","background-color":'black'},
        "icon": {"color": "white", "font-size": "23px"}, 
        "nav-link": {"color":"white","font-size": "20px", "text-align": "left", "margin":"0px", "--hover-color": "blue"},
        "nav-link-selected": {"background-color": "#02ab21"},}
                
                )

        
        if app == "inicio":
            inicio.app()
        if app == "negocios":
            negocios.app()    
        if app == "usuarios ml 1":
            usuarios.app()        
        if app == "usuarios ml 2":
            usuarios2.app()        
        if app == 'inversionistas':
            inversionistas.app()
        if app == 'propuesta inversion':
            propuestainversion.app()
        if app == 'filtros':
            filtros.app()  
        if app == 'acerca de':
            acercade.app()   
             
          
             
    run()            
         