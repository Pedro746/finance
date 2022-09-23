import streamlit as st
import time
import Controllers.FinalidadeController as FinalidadeController
import models.Finalidade as finalidade

def Finalidade():
    st.title('Cadastro Finalidade')

    with st.form(key="inclucde_finalidade", clear_on_submit=True):
        
        input_finalidade = st.text_input(label="Nome finalidade")
       

        input_submit = st.form_submit_button("Cadastrar finalidade")

    if input_submit:
        if input_finalidade == "" or input_finalidade == " ":
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
            time.sleep(2)
            st.experimental_rerun()
        else:
            FinalidadeController.Incluir(finalidade.finalidade(0, input_finalidade))
            # st.success(f'Finalidade {input_finalidade} foi cadastrada com sucesso!', icon="✅")
            st.markdown(f"""
            <div class="alerta-success alert d-flex align-items-center" role="alert">
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-check-lg" viewBox="0 0 16 16">
            <path d="M12.736 3.97a.733.733 0 0 1 1.047 0c.286.289.29.756.01 1.05L7.88 12.01a.733.733 0 0 1-1.065.02L3.217 8.384a.757.757 0 0 1 0-1.06.733.733 0 0 1 1.047 0l3.052 3.093 5.4-6.425a.247.247 0 0 1 .02-.022Z"/>
            </svg>
            <div>
            &nbsp Finalidade {input_finalidade} foi cadastrada com sucesso!
            </div>
            </div>
            """, unsafe_allow_html=True)
            time.sleep(2)
            st.experimental_rerun()
    
    

