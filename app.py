import streamlit as st
import openai

# Configurar chave da API OpenAI
openai.api_key = "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"

# Esconde menu, rodapé e cabeçalho
hide_streamlit_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# Interface do chat
st.title("ChatVision (GPT-4)")

user_input = st.text_input("Digite sua pergunta:")
if user_input:
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "user", "content": user_input}
            ]
        )
        st.markdown(f"**Resposta:** {response.choices[0].message.content}")
    except Exception as e:
        st.error(f"Erro ao chamar API: {e}")
        
