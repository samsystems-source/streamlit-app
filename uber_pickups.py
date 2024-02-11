import streamlit as st
import pandas as pd

def main():
    st.title("Sistema de Gestão de Estoque")

    # Adiciona um menu na barra lateral
    menu = st.topbar.radio("Menu", ["Cadastro", "Pedidos de Materiais", "Programação de Obras", "Relatório", "Sair"])

    # Verifica a opção selecionada no menu e chama a função correspondente
    if menu == "Cadastro":
        cadastrar_material()
    elif menu == "Pedidos de Materiais":
        fazer_pedido()
    elif menu == "Programação de Obras":
        programar_obras()
    elif menu == "Relatório":
        mostrar_relatorio()

def cadastrar_material():
    st.header("Cadastro de Material")
    # Coloque aqui o código para cadastrar materiais

def fazer_pedido():
    st.header("Pedidos de Materiais")
    # Coloque aqui o código para fazer pedidos de materiais

def programar_obras():
    st.header("Programação de Obras")
    # Coloque aqui o código para programar obras

def mostrar_relatorio():
    st.header("Relatório")
    # Coloque aqui o código para gerar relatórios

if __name__ == "__main__":
    main()
