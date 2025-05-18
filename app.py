import streamlit as st
import google.generativeai as genai

# Configura sua API KEY
genai.configure(api_key="SUA_API_KEY")

# Inicializa o modelo Gemini 1.5 Pro
model = genai.GenerativeModel("models/gemini-1.5-pro-001")

# Configuração da página
st.set_page_config(page_title="ChatVision", layout="centered")

# Esconde menu, rodapé e cabeçalho
st.markdown("""
    <style>
    #MainMenu, footer, header {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

st.title("ChatVision")

# Entrada do usuário
user_input = st.text_input("Você:", placeholder="Digite sua pergunta e pressione Enter")

# Gera resposta
if user_input:
    with st.spinner("Pensando..."):
        try:
            response = model.generate_content(user_input)
            st.write("Resposta da IA:", response.text)
        except Exception as e:
            st.error(f"Erro ao chamar API: {e}")
            
