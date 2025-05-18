import google.generativeai as genai
import streamlit as st

# Esconde menus
st.markdown("""
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

# Sua chave da API
genai.configure(api_key="AIzaSyDbDd4xX4_be2mHEd27p1HLwSG0g8nde40")

# Cria modelo chat Gemini
model = genai.GenerativeModel("gemini-pro")

st.title("ChatVision")

# Caixa de texto para o usuário
user_input = st.text_input("Digite sua pergunta:")

if user_input:
    try:
        response = model.generate_content(user_input)
        st.write("Resposta da IA:", response.text)
    except Exception as e:
        st.error(f"Erro ao chamar API: {e}")
        
