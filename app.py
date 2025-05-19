import streamlit as st
import google.generativeai as genai

# Sua chave da API Gemini
API_KEY = "AIzaSyDMVC671ENiVJUFkp0Qd8FSUfI4I_ZInSA"

genai.configure(api_key=API_KEY)

# Inicializa o modelo Gemini Pro
model = genai.GenerativeModel("gemini-1.5-pro")

# Esconde elementos visuais do Streamlit
hide_streamlit_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .block-container {padding-top: 2rem;}
    </style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# Título do app
st.title("ChatVision")

# Entrada do usuário
user_input = st.text_input("Digite sua pergunta:", "")

if user_input:
    with st.spinner("Pensando..."):
        try:
            response = model.generate_content(user_input)
            resposta = response.text
            st.markdown(f"**Resposta:** {resposta}")
        except Exception as e:
            st.error(f"Erro ao chamar API: {e}")
              
