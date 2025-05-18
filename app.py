import streamlit as st
import google.generativeai as genai

# Configure sua API KEY
genai.configure(api_key="AIzaSyDbDd4xX4_be2mHEd27p1HLwSG0g8nde40")

# Inicializa o modelo Gemini-Pro
model = genai.GenerativeModel('models/gemini-pro')

# Configuração da página
st.set_page_config(page_title="ChatVision", layout="centered")

# Esconde menu, rodapé e cabeçalho
hide_streamlit_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

st.title("ChatVision")

# Campo de entrada
user_input = st.text_input("Você:", placeholder="Digite sua pergunta e pressione Enter")

# Quando o usuário envia uma pergunta
if user_input:
    with st.spinner("Pensando..."):
        try:
            response = model.generate_content(user_input)
            st.write("Resposta da IA:", response.text)
        except Exception as e:
            st.error(f"Erro ao chamar API: {e}")
            
