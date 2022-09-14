import streamlit as st
import Controllers.BancoController as BancoController
import models.Banco as banco


def Banco():
    st.title('Cadastro Banco')
    st.markdown("""""", unsafe_allow_html=True)

    with st.form(key="inclucde_banco", clear_on_submit=True):
        
        input_banco = st.text_input(label="Nome Banco")
       

        input_submit = st.form_submit_button("Cadastrar Banco")

    if input_submit:
        if input_banco == "" or input_banco == " ":
            st.info('Preencha todos os campos', icon="ℹ️")
        else:
            BancoController.Incluir(banco.banco(0, input_banco))
            st.success(f'Banco {input_banco} foi cadastrado com sucesso!', icon="✅")
    
     
    colms = st.columns((1, 3, 3, 3))
    campos = ['N°', 'Banco','Editar', 'Excluir']

    for col, campo_nome in zip(colms, campos):
        col.write(campo_nome)
    
    for item in BancoController.showAll():
        col1, col2, col3, col4 = st.columns((1, 3, 3, 3))

        col1.write(item.id)
        col2.write(item.banco)
        delete = col3.empty()
        on_click_deletar = delete.button('Deletar', 'btnDeletar' + str(item.id))
        alterar = col4.empty()
        on_click_alterar = alterar.button('Alterar', 'btnAlterar'  + str(item.id))

        if on_click_deletar:
            BancoController.Deletar(item.id)
            delete.button('Deletado', 'btnDeletado' + str(item.id))
            st.success(f'Banco {item.banco} deletado com sucesso', icon="✅") 
