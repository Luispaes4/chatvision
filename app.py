import google.generativeai as genai
import streamlit as st

# Chave da API do Gemini
genai.configure(api_key="AIzaSyDMVC671ENiVJUFkp0Qd8FSUfI4I_ZInSA")

# Inicializa o modelo
model = genai.GenerativeModel("gemini-1.5-pro")

# Esconde menu, rodapé e cabeçalho do Streamlit
hide_streamlit_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .st-emotion-cache-1v0mbdj {display: none;} /* ícones extras */
    .st-emotion-cache-13ln4jf {display: none;} /* mensagens duplicadas */
    </style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# Título do app
st.title("ChatVision")

# Caixa de entrada do usuário
user_input = st.text_input("Digite sua pergunta:", "")

# Chamada da API e resposta
if user_input:
    with st.spinner("Pensando..."):
        try:
            response = model.generate_content(user_input)
            st.write("Resposta da IA:", response.text)
        except Exception as e:
            st.error(f"Erro ao chamar API: {e}")
            
