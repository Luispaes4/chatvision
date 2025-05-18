import streamlit as st
import google.generativeai as genai

# Esconde menu, rodapé e cabeçalho
st.markdown("""
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .block-container {padding-top: 2rem;}
    </style>
""", unsafe_allow_html=True)

# Configura a API do Gemini
genai.configure(api_key="AIzaSyDbDd4xX4_be2mHEd27p1HLwSG0g8nde40")

model = genai.GenerativeModel(model_name="models/gemini-pro")

st.title("ChatVision")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

prompt = st.chat_input("Digite sua pergunta...")

if prompt:
    st.session_state.chat_history.append(("Você", prompt))
    try:
        response = model.generate_content(prompt)
        st.session_state.chat_history.append(("IA", response.text))
    except Exception as e:
        st.session_state.chat_history.append(("Erro", f"Erro ao chamar API: {e}"))

for role, message in st.session_state.chat_history:
    with st.chat_message("user" if role == "Você" else "assistant"):
        st.markdown(message)
        
