import streamlit as st
import Controllers.DespesaController as DespesaController
import Controllers.FinalidadeController as FinalidadeController
import Controllers.BancoController as BancoController
import models.Despesa as despesa


def CadastroDespesa():
    fin = []
    for item in FinalidadeController.showAll():
        fin.append(item.finalidade)


    bco = []
    for item in BancoController.showAll():
        bco.append(item.banco)


    
    with st.form(key="inclucde_despesa", clear_on_submit=True):
        input_banco = st.selectbox(label="Selecione o Banco", options=(bco))
        input_valor = st.number_input(label="Valor R$",format="%.2f")
        input_finalidade = st.selectbox(label="Selecione a finalidade", options=(fin))
        input_data = st.date_input(label="Data")
        input_descricao = st.text_area(label="Descrição da despesa")

        input_submit = st.form_submit_button("Cadastrar despesa")

    if input_submit:
        if input_descricao == "" or input_descricao == " ":
            st.info('Preencha todos os campos', icon="ℹ️")
        else:
            DespesaController.Incluir(despesa.despesa(0, input_banco, input_valor, input_finalidade, input_data, input_descricao))
            st.success(f'Despesa {input_descricao} foi cadastrada com sucesso!', icon="✅")
    
    with st.container():
        st.write('***')
        st.subheader('Listagem de todas as despesas cadastradas')

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
                        st.success(f'Despesa deletada com sucesso', icon="✅")
