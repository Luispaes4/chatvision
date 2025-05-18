import streamlit as st
import google.generativeai as genai

# Esconde menu, rodapé e cabeçalho
hide_streamlit_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# Chave da API Gemini
genai.configure(api_key="AIzaSyDbDd4xX4_be2mHEd27p1HLwSG0g8nde40")

# Inicializa o modelo Gemini 1.5 Pro
try:
    model = genai.GenerativeModel(model_name="models/gemini-1.5-pro-latest")
except Exception as e:
    st.error(f"Erro ao configurar o modelo: {e}")

st.title("ChatVision")

# Campo de texto com desaparecimento da pergunta
prompt = st.text_input("Digite sua pergunta:", key="input")

if prompt:
    with st.spinner("Pensando..."):
        try:
            response = model.generate_content(prompt)
            st.session_state.input = ""  # Limpa o campo após enviar
            st.markdown(f"**Resposta:** {response.text}")
        except Exception as e:
            st.error(f"Erro ao chamar API: {e}")
            
