import streamlit as st

# Esconde menu, rodapé e cabeçalho
hide_streamlit_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# Exemplo simples de chat
st.title("ChatVision")
user_input = st.text_input("Você:", "")
if user_input:
    st.write("Resposta da IA: Aqui vai a resposta gerada.")
