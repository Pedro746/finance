import streamlit as st
import Controllers.FinalidadeController as FinalidadeController
import models.Finalidade as finalidade

def Finalidade():
    st.title('Cadastro Finalidade')

    with st.form(key="inclucde_finalidade", clear_on_submit=True):
        
        input_finalidade = st.text_input(label="Nome finalidade")
       

        input_submit = st.form_submit_button("Cadastrar finalidade")

    if input_submit:
        if input_finalidade == "" or input_finalidade == " ":
            st.info('Preencha todos os campos', icon="ℹ️")
        else:
            FinalidadeController.Incluir(finalidade.finalidade(0, input_finalidade))
            st.success(f'Finalidade {input_finalidade} foi cadastrada com sucesso!', icon="✅")
    
     
    colms = st.columns((1, 3, 3, 3))
    campos = ['N°', 'Finalidade','Editar', 'Excluir']

    for col, campo_nome in zip(colms, campos):
        col.write(campo_nome)
    
    for item in FinalidadeController.showAll():
        col1, col2, col3, col4 = st.columns((1, 3, 3, 3))

        col1.write(item.id)
        col2.write(item.finalidade)
        delete = col3.empty()
        on_click_deletar = delete.button('Deletar', 'btnDeletar' + str(item.id))
        alterar = col4.empty()
        on_click_alterar = alterar.button('Alterar', 'btnAlterar'  + str(item.id))

        if on_click_deletar:
            FinalidadeController.Deletar(item.id)
            delete.button('Deletado', 'btnDeletado' + str(item.id))
            st.success(f'Finalidade deletada com sucesso', icon="✅")
    

