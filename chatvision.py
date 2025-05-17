import openai
import streamlit as st

openai.api_key = st.secrets["openai"]["api_key"]

st.set_page_config(page_title="ChatVision", page_icon="💡")
st.title("ChatVision")
st.markdown("Conversando com a IA GPT-3.5 da OpenAI")

if "messages" not in st.session_state:
    st.session_state["messages"] = [
        {"role": "system", "content": "Você é um assistente chamado ChatVision, sempre útil, amigável e direto."}
    ]

for msg in st.session_state.messages[1:]:
    st.chat_message(msg["role"]).markdown(msg["content"])

prompt = st.chat_input("Digite sua mensagem")
if prompt:
    st.chat_message("user").markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=st.session_state.messages
    )

    reply = response.choices[0].message["content"]
    st.chat_message("assistant").markdown(reply)
    st.session_state.messages.append({"role": "assistant", "content": reply})
  
