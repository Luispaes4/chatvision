import streamlit as st
import google.generativeai as genai

# Configura a chave da API
genai.configure(api_key="AIzaSyB5gvHKwrUX1XXNxZ2CfOAI-NE1UPX3CB8")

# Esconde menu, rodapé e cabeçalho
hide_streamlit_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# Interface do chat
st.title("ChatVision")

user_input = st.text_input("Digite sua pergunta:")
if user_input:
    try:
        model = genai.GenerativeModel("gemini-1.5-pro")
        response = model.generate_content(user_input)
        st.markdown(f"**Resposta:** {response.text}")
    except Exception as e:
        st.error(f"Erro ao chamar API: {e}")
