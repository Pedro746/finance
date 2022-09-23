import streamlit as st
from time import time
import time
import Controllers.DespesaController as DespesaController
import Controllers.FinalidadeController as FinalidadeController
import Controllers.BancoController as BancoController
import Pages.Depesas.cadastroDespesa as FormDespesa


fin = []
for item in FinalidadeController.showAll():
    fin.append(item.finalidade)


bco = []
for item in BancoController.showAll():
    bco.append(item.banco)

def Lista():
    params = st.experimental_get_query_params()
    if params.get("id") == None:
        with st.container():
            st.subheader('Listagem de todas as despesas cadastradas')
            if st.button("Recarregar página"):
                st.experimental_rerun()
            st.write('***')

            colms = st.columns((1, 3, 2, 2, 2, 2, 2, 2))
            campos = ['N°', 'Banco', 'Valor', 'Finalidade', 'Data', 'Descrição', 'Editar', 'Excluir']

            for col, campo_nome in zip(colms, campos):
                    col.write(campo_nome)
            
            for item in DespesaController.showAll():
                    col1, col2, col3, col4, col5, col6, col7, col8 = st.columns((1, 3, 2, 2, 2, 2, 2, 2))
                    col1.write(item.id)
                    col2.write(item.banco)
                    col3.write(f'R$ {item.valor}')
                    col4.write(item.finalidade)
                    col5.write(item.data)
                    col6.write(item.descricao)
                    delete = col7.empty()
                    on_click_deletar = delete.button('Deletar', 'btnDeletar' + str(item.id))
                    alterar = col8.empty()
                    on_click_alterar = alterar.button('Alterar', 'btnAlterar'  + str(item.id))


                    if on_click_deletar:
                            DespesaController.Deletar(item.id)
                            delete.button('Deletado', 'btnDeletado' + str(item.id))
                            # st.success(f'Despesa deletada com sucesso', icon="✅")
                            st.markdown(f"""
                            <div class="alerta-success alert d-flex align-items-center" role="alert">
                            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-check-lg" viewBox="0 0 16 16">
                            <path d="M12.736 3.97a.733.733 0 0 1 1.047 0c.286.289.29.756.01 1.05L7.88 12.01a.733.733 0 0 1-1.065.02L3.217 8.384a.757.757 0 0 1 0-1.06.733.733 0 0 1 1.047 0l3.052 3.093 5.4-6.425a.247.247 0 0 1 .02-.022Z"/>
                            </svg>
                            <div>
                            &nbsp Despesa <strong><u>{item.descricao}</u></strong> deletada com sucesso!
                            </div>
                            </div>
                            """, unsafe_allow_html=True)
                            time.sleep(2)
                            st.experimental_rerun()
                            
                    
                    if on_click_alterar:

                        st.experimental_set_query_params(
                            id = [item.id]
                        )
                        st.experimental_rerun()
                       

    else:
        FormDespesa.CadastroDespesa()
        



                    

                    
                

                
