import streamlit as st

def main():
    st.title("Formulário de Transferência de Estoque")

    # Campos do formulário
    material = st.text_input("Material:")
    descricao = st.text_area("Descrição:")
    quantidade = st.number_input("Quantidade:", min_value=1, step=1)
    estoque_origem = st.selectbox("Estoque Origem:", ["Estoque 1", "Estoque 2", "Estoque 3"])
    estoque_destino = st.selectbox("Estoque Destino:", ["Estoque 1", "Estoque 2", "Estoque 3"])

    # Botão para submeter o formulário
    if st.button("Enviar"):
        # Lógica para processar os dados do formulário
        processar_formulario(material, descricao, quantidade, estoque_origem, estoque_destino)

def processar_formulario(material, descricao, quantidade, estoque_origem, estoque_destino):
    # Aqui você pode adicionar a lógica para processar os dados do formulário, por exemplo, salvar em um banco de dados.
    st.success("Formulário enviado com sucesso!")
    st.write("Material:", material)
    st.write("Descrição:", descricao)
    st.write("Quantidade:", quantidade)
    st.write("Estoque Origem:", estoque_origem)
    st.write("Estoque Destino:", estoque_destino)

if __name__ == "__main__":
    main()
