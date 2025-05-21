# app.py
import streamlit as st
import openai
import requests
import json

# Configuração da API OpenAI
openai.api_key = "sk-..."  # Substitua pela sua chave GPT-3.5

# Chave ALTCHA
ALTCHA_API_KEY = "ckey_016c237681e746bad673fe063dce"
ALTCHA_SECRET = "csec_28f26de829242e5555973e48dea1a01d024bce7672f3fdd1"

# Função de verificação ALTCHA
def altcha_verify(token):
    url = "https://altcha.org/api/verify"
    headers = {"Content-Type": "application/json"}
    payload = {
        "token": token,
        "secret": ALTCHA_SECRET
    }
    try:
        response = requests.post(url, headers=headers, data=json.dumps(payload))
        return response.status_code == 200 and response.json().get("success")
    except Exception as e:
        return False

# Inicializa sessão
if "history" not in st.session_state:
    st.session_state.history = []

if "language" not in st.session_state:
    st.session_state.language = "pt"

# Sidebar
with st.sidebar:
    st.markdown("## Menu")
    idioma = st.selectbox("Idioma", ["pt", "en"], index=0)
    st.session_state.language = idioma
    st.markdown("---")
    st.markdown("### Histórico")
    for i, item in enumerate(st.session_state.history[::-1]):
        st.markdown(f"{len(st.session_state.history)-i}. {item[:30]}...")

# Título
st.markdown("<h1 style='text-align: center;'>ChatVision GPT-3.5</h1>", unsafe_allow_html=True)

# Input do usuário
with st.form("chat_form"):
    user_input = st.text_input("Digite sua pergunta:", "", key="user_input")
    token = st.text_input("Token ALTCHA:", "", type="password")
    submit = st.form_submit_button("Enviar")

# Processamento
if submit and user_input:
    if not altcha_verify(token):
        st.error("Verificação ALTCHA falhou. Tente novamente.")
    else:
        st.session_state.history.append(user_input)
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "Responda no idioma especificado pelo usuário."},
                    {"role": "user", "content": user_input}
                ]
            )
            output = response.choices[0].message.content
            st.markdown(f"**Resposta:** {output}")
            st.session_state.user_input = ""
        except Exception as e:
            st.error(f"Erro ao chamar a API: {e}")
                               
