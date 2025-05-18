import streamlit as st
import google.generativeai as genai

# Esconde cabeçalho, rodapé e menu
st.markdown("""
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

# Chave da API
genai.configure(api_key="AIzaSyDbDd4xX4_be2mHEd27p1HLwSG0g8nde40")

# Carrega o modelo
try:
    model = genai.GenerativeModel("models/gemini-pro")
except Exception as e:
    st.error(f"Erro ao carregar modelo: {e}")
    st.stop()

# Título do app
st.title("ChatVision")

# Input do usuário
prompt = st.text_input("Faça uma pergunta:")

# Gera resposta
if prompt:
    try:
        response = model.generate_content(prompt)
        st.markdown("**Resposta:**")
        st.write(response.text)
    except Exception as e:
        st.error(f"Erro ao chamar API: {e}")
