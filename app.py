import streamlit as st
from google.generativeai import client

# Sua chave API do Google AI embutida
API_KEY = "AIzaSyDbDd4xX4_be2mHEd27p1HLwSG0g8nde40"
client.configure(api_key=API_KEY)

st.set_page_config(page_title="ChatVision", page_icon="🤖")

st.title("ChatVision - Chat estilo ChatGPT")

if "messages" not in st.session_state:
    st.session_state.messages = []

def enviar_pergunta(pergunta):
    if not pergunta.strip():
        return None
    st.session_state.messages.append({"role": "user", "content": pergunta})

    # Chamada à API do Google Generative AI
    try:
        response = client.chat.completions.create(
            model="chat-bison-001",
            messages=[{"role": "user", "content": pergunta}],
        )
        resposta = response.choices[0].message.content
    except Exception as e:
        resposta = f"Erro ao chamar API: {e}"

    st.session_state.messages.append({"role": "assistant", "content": resposta})

# Campo de input aparece só se não tiver pergunta recente não respondida
if "input_visible" not in st.session_state:
    st.session_state.input_visible = True

if st.session_state.input_visible:
    pergunta = st.text_input("Digite sua pergunta:", key="input_pergunta")
    botao = st.button("Enviar")

    if botao and pergunta:
        enviar_pergunta(pergunta)
        st.session_state.input_visible = False  # Esconde o input depois de enviar

# Mostrar histórico das mensagens tipo chat
for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.markdown(f"**Você:** {msg['content']}")
    else:
        st.markdown(f"**ChatVision:** {msg['content']}")

# Botão para reiniciar conversa e mostrar o input de novo
if not st.session_state.input_visible:
    if st.button("Nova pergunta"):
        st.session_state.input_visible = True
        st.experimental_rerun()
        
