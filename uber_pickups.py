import streamlit as st
import pandas as pd

def main():
    st.title("Formulário de Transferência de Estoque")

    # Divide a tela em duas colunas
    col1, col2 = st.columns(2)

    # Campos do formulário na primeira coluna
    with col1:
        material = st.text_input("Material:")
        descricao = st.text_area("Descrição:")
        quantidade = st.number_input("Quantidade:", min_value=1, step=1)

    # Campos do formulário na segunda coluna
    with col2:
        estoque_origem = st.selectbox("Estoque Origem:", ["Estoque 1", "Estoque 2", "Estoque 3"])
        estoque_destino = st.selectbox("Estoque Destino:", ["Estoque 1", "Estoque 2", "Estoque 3"])

    # Botão para submeter o formulário
    if st.button("Enviar"):
        # Adiciona os dados do formulário à tabela
        adicionar_na_tabela(material, descricao, quantidade, estoque_origem, estoque_destino)

def adicionar_na_tabela(material, descricao, quantidade, estoque_origem, estoque_destino):
    # Tenta carregar a tabela existente
    try:
        tabela = pd.read_csv("dados.csv")
    except FileNotFoundError:
        tabela = pd.DataFrame(columns=["Material", "Descrição", "Quantidade", "Estoque Origem", "Estoque Destino"])

    # Adiciona os novos dados à tabela
    nova_linha = pd.DataFrame([[material, descricao, quantidade, estoque_origem, estoque_destino]],
                              columns=["Material", "Descrição", "Quantidade", "Estoque Origem", "Estoque Destino"])
    tabela = pd.concat([tabela, nova_linha], ignore_index=True)

    # Salva a tabela atualizada
    tabela.to_csv("dados.csv", index=False)

    st.success("Dados adicionados à tabela com sucesso!")

if __name__ == "__main__":
    main()
