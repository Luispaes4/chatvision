import requests

API_KEY = "AIzaSyDbDd4xX4_be2mHEd27p1HLwSG0g8nde40"
url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={API_KEY}"

# Função de chat com Gemini
def gemini_chat(user_input):
    payload = {
        "contents": [
            {
                "parts": [{"text": user_input}]
            }
        ]
    }

    headers = {
        "Content-Type": "application/json"
    }

    response = requests.post(url, headers=headers, json=payload)

    if response.status_code == 200:
        data = response.json()
        return data['candidates'][0]['content']['parts'][0]['text']
    else:
        return f"Erro: {response.status_code}\n{response.text}"

# Exemplo de uso
pergunta = input("Digite sua pergunta: ")
resposta = gemini_chat(pergunta)
print("\nGemini respondeu:\n", resposta)
