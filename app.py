from msilib.schema import Icon
import streamlit as st
from streamlit_option_menu import option_menu
import Pages.Depesas.cadastroDespesa as cadastroDespesa
import Pages.Dashboard.dashboard as dashboard
import Pages.Banco.banco as banco
import Pages.Finalidade.finalidade as finalidade




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
        options=["Dashboard", "Cadastrar Despesa", "Cadastrar Banco", "Cadastrar Finalidade"],
        icons=["bar-chart", "plus", "bank", "pencil"],
        menu_icon="grid",
        default_index=0,
        # orientation="horizontal",       
    )
    

# TELA DASHBOARD
if selected == "Dashboard":
    dashboard.Dashboard()


# TELA CADASTRO DE DESPESA
if selected == "Cadastrar Despesa":
    cadastroDespesa.CadastroDespesa()
   

# TELA DE CADASTRO DE BANCO
if selected == "Cadastrar Banco":
    banco.Banco()


# TELA DE CADASTRO DE FINALIDADE
if selected == "Cadastrar Finalidade":
    finalidade.Finalidade()



st.markdown("""
<div class="alert alert-primary" role="alert">
  A simple primary alert—check it out!
</div>
""", unsafe_allow_html=True)

















# if input_submit:
#     if input_banco == "" or input_valor == "" or input_finalidade == "" or input_descricao == "":
#         st.error('Preencha todos os campos', icon="🚨")
#     else:

        

    
