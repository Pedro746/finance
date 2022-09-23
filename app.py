import streamlit as st
from streamlit_option_menu import option_menu
import Pages.Depesas.cadastroDespesa as cadastroDespesa
import Pages.Dashboard.dashboard as dashboard
import Pages.Banco.banco as banco
import Pages.Finalidade.finalidade as finalidade
import Pages.Depesas.listagemDespesas as listagemDespesas
import Pages.Banco.listagemBanco as listaBanco
import Pages.Finalidade.listagemFinalidade as listagemFinalidade




st.set_page_config(page_title="Finance", initial_sidebar_state = 'auto', page_icon ="https://i.pinimg.com/564x/20/ca/38/20ca382f89cb50818ff2b7a82485ce36.jpg")

with open('style.css') as css:
    st.markdown(f'<style>{css.read()}</style>', unsafe_allow_html=True)

st.markdown("""
            <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.1/dist/css/bootstrap.min.css" rel="stylesheet">
            <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.1/dist/js/bootstrap.bundle.min.js"></script>
            """, unsafe_allow_html=True)

# SIDE BAR
with st.sidebar:
    selected = option_menu(
        menu_title="Menu",
        options=["Dashboard", "Cadastrar Despesa", "Lista Despesas", "Cadastrar Banco", "Lista Bancos", "Cadastrar Finalidade", "Lista Finalidades"],
        icons=["bar-chart", "plus", "eye", "bank", "eye", "pencil", "eye"],
        menu_icon="grid",
        default_index=0,
        # orientation="horizontal",       
    )
    

# TELA DASHBOARD
if selected == "Dashboard":
    st.experimental_set_query_params()
    dashboard.Dashboard()


# TELA CADASTRO DE DESPESA
if selected == "Cadastrar Despesa":
    st.experimental_set_query_params()
    cadastroDespesa.CadastroDespesa()

# TELA LISTAGEM DE DESPESA
if selected == "Lista Despesas":
    # st.experimental_set_query_params()
    listagemDespesas.Lista()
    
   

# TELA DE CADASTRO DE BANCO
if selected == "Cadastrar Banco":
    st.experimental_set_query_params()
    banco.Banco()

# TELA DE LISTAGEM DE BANCO
if selected == "Lista Bancos":
    st.experimental_set_query_params()
    listaBanco.listagemBanco()


# TELA DE CADASTRO DE FINALIDADE
if selected == "Cadastrar Finalidade":
    st.experimental_set_query_params()
    finalidade.Finalidade()

# TELA DE CADASTRO DE FINALIDADE
if selected == "Lista Finalidades":
    st.experimental_set_query_params()
    listagemFinalidade.ListaFinalidade()


















# if input_submit:
#     if input_banco == "" or input_valor == "" or input_finalidade == "" or input_descricao == "":
#         st.error('Preencha todos os campos', icon="🚨")
#     else:

        

    
