import streamlit as st
import time
import Controllers.FinalidadeController as FinalidadeController

def ListaFinalidade():
     with st.container():
        st.subheader('Listagem de todas as finalidades cadastradas')
        if st.button("Recarregar página"):
            st.experimental_rerun
        st.write('***')
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
                # st.success(f'Finalidade deletada com sucesso', icon="✅")
                st.markdown(f"""
                <div class="alerta-success alert d-flex align-items-center" role="alert">
                <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-check-lg" viewBox="0 0 16 16">
                <path d="M12.736 3.97a.733.733 0 0 1 1.047 0c.286.289.29.756.01 1.05L7.88 12.01a.733.733 0 0 1-1.065.02L3.217 8.384a.757.757 0 0 1 0-1.06.733.733 0 0 1 1.047 0l3.052 3.093 5.4-6.425a.247.247 0 0 1 .02-.022Z"/>
                </svg>
                <div>
                &nbsp Finalidade <strong><u>{item.finalidade}</u></strong> deletada com sucesso!
                </div>
                </div>
                """, unsafe_allow_html=True)
                time.sleep(2)
                st.experimental_rerun()
        

