import litellm
from dotenv import load_dotenv
import os

# Carregar variáveis de ambiente
load_dotenv()

# Obter a chave da API OpenAI
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    print("Erro: A variável OPENAI_API_KEY não está configurada no .env.")
    exit(1)

# Inicializar a instância de OpenAIChatCompletion
openai_chat = litellm.OpenAIChatCompletion()

# Fazer uma chamada ao modelo de chat
response = openai_chat.create(
    model="gpt-3.5-turbo",  # Substitua pelo modelo desejado
    messages=[{"role": "user", "content": "Diga Olá, mundo!"}],
    api_key=api_key  # A chave API é passada diretamente no método `create()`
)

# Exibir a resposta
print(response["choices"][0]["message"]["content"])
