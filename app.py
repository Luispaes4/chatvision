import streamlit as st
import google.generativeai as genai

# Configure a chave de API
genai.configure(api_key="AIzaSyDbDd4xX4_be2mHEd27p1HLwSG0g8nde40")

# Ocultar cabeçalho, rodapé e menu
st.markdown("""
    <style>
    #MainMenu, footer, header {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

st.title("ChatVision")

# Inicializar chat com o modelo Gemini-Pro
try:
    model = genai.GenerativeModel("gemini-pro")
    chat = model.start_chat()
except Exception as e:
    st.error(f"Erro ao iniciar modelo: {e}")
    st.stop()

# Entrada do usuário
if "history" not in st.session_state:
    st.session_state.history = []

user_input = st.chat_input("Digite sua pergunta")

if user_input:
    st.session_state.history.append({"role": "user", "text": user_input})
    try:
        response = chat.send_message(user_input)
        st.session_state.history.append({"role": "ai", "text": response.text})
    except Exception as e:
        st.error(f"Erro ao chamar API: {e}")

# Exibir histórico
for msg in st.session_state.history:
    with st.chat_message(msg["role"]):
        st.markdown(msg["text"])
