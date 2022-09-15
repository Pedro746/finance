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
            # st.info('Preencha todos os campos', icon="ℹ️")
            st.markdown("""
            <div class="alerta-info alert d-flex align-items-center" role="alert">
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-exclamation-triangle" viewBox="0 0 16 16">
            <path d="M7.938 2.016A.13.13 0 0 1 8.002 2a.13.13 0 0 1 .063.016.146.146 0 0 1 .054.057l6.857 11.667c.036.06.035.124.002.183a.163.163 0 0 1-.054.06.116.116 0 0 1-.066.017H1.146a.115.115 0 0 1-.066-.017.163.163 0 0 1-.054-.06.176.176 0 0 1 .002-.183L7.884 2.073a.147.147 0 0 1 .054-.057zm1.044-.45a1.13 1.13 0 0 0-1.96 0L.165 13.233c-.457.778.091 1.767.98 1.767h13.713c.889 0 1.438-.99.98-1.767L8.982 1.566z"/>
            <path d="M7.002 12a1 1 0 1 1 2 0 1 1 0 0 1-2 0zM7.1 5.995a.905.905 0 1 1 1.8 0l-.35 3.507a.552.552 0 0 1-1.1 0L7.1 5.995z"/>
            </svg>
            <div>
            &nbsp Preencha todos os campos!
            </div>
            </div>
            """, unsafe_allow_html=True)
        else:
            BancoController.Incluir(banco.banco(0, input_banco))
            # st.success(f'Banco {input_banco} foi cadastrado com sucesso!', icon="✅")
            st.markdown(f"""
            <div class="alerta-success alert d-flex align-items-center" role="alert">
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-check-lg" viewBox="0 0 16 16">
            <path d="M12.736 3.97a.733.733 0 0 1 1.047 0c.286.289.29.756.01 1.05L7.88 12.01a.733.733 0 0 1-1.065.02L3.217 8.384a.757.757 0 0 1 0-1.06.733.733 0 0 1 1.047 0l3.052 3.093 5.4-6.425a.247.247 0 0 1 .02-.022Z"/>
            </svg>
            <div>
            &nbsp Banco {input_banco} foi cadastrado com sucesso!
            </div>
            </div>
            """, unsafe_allow_html=True)
    
     
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
            # st.success(f'Banco {item.banco} deletado com sucesso', icon="✅") 
            st.markdown(f"""
            <div class="alerta-success alert d-flex align-items-center" role="alert">
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-check-lg" viewBox="0 0 16 16">
            <path d="M12.736 3.97a.733.733 0 0 1 1.047 0c.286.289.29.756.01 1.05L7.88 12.01a.733.733 0 0 1-1.065.02L3.217 8.384a.757.757 0 0 1 0-1.06.733.733 0 0 1 1.047 0l3.052 3.093 5.4-6.425a.247.247 0 0 1 .02-.022Z"/>
            </svg>
            <div>
            &nbsp Banco <strong><u>{item.banco}</u></strong> deletado com sucesso!
            </div>
            </div>
            """, unsafe_allow_html=True)
