import streamlit as st
import datetime as dt
import Controllers.FinalidadeController as FinalidadeController
import Controllers.BancoController as BancoController
import plotly.express as px

bco = []
for item in BancoController.showAll():
        bco.append(item.banco)

fin = []
for item in FinalidadeController.showAll():
        fin.append(item.finalidade)

data = dt.datetime.today()

def Dashboard():

        with st.container():
                col1, col2, col3 = st.columns(3)

                with col1:
                        st.selectbox('Selecione o Banco', options=(bco))

                with col2:
                        st.date_input('Selecione a Data', data)

                with col3:
                        st.selectbox('Selecione a Finalidade', options=(fin))
        
        with st.container():
                pass

    
        
