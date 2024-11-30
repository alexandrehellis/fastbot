from dotenv import load_dotenv
import os
from openai import OpenAI

client = OpenAI()

load_dotenv(dotenv_path='config/.env')

class OpenaiClient:
    def __init__(self):
        self.apiKey = os.getenv("OPENAI_API_KEY")

    def chat(self, message):
    # Chamar a API da OpenAI
        print(message)
        try:
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",  # ou outro modelo que você desejar
                messages=[
                    {"role": "user", "content": message}
                ]
            )
            
            bot_response = response.choices[0].message.content
            print(bot_response)
            
            return bot_response
        
        except Exception as e:
            print(f"Erro ao chamar a API da OpenAI: {str(e)}")
            return ({'status': 'error', 'message': 'Erro ao chamar a API da OpenAI'}), 500