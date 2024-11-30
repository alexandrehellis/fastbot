import requests
import os
from dotenv import load_dotenv

import base64
from io import BytesIO
from PIL import Image

load_dotenv(dotenv_path='config/.env')


class EvolutionApiClient:
    def __init__(self):
        self.apiUrl = os.getenv("EVOLUTION_API_URL")
        self.apiKey = os.getenv("EVOLUTION_API_KEY")
        self.instance = os.getenv("EVOLUTION_API_INSTANCE")

    def send_message(self, data):
        print(data)
        instance = data["instance"]
        route = f"{self.apiUrl}/message/sendText/{instance}"
        headers = {
            'Content-Type': 'application/json',
            'apikey': self.apiKey
        }
        payload = {
            "number": data["number"],
            "text": data["text"]
        }
        
        response = requests.post(route, json=payload, headers=headers)
        response.raise_for_status()

        return response.json()
    
    def create_instance(self, nameInstance):
        print(nameInstance)

        route = f"{self.apiUrl}/instance/create/"
        
        headers = {
            'Content-Type': 'application/json',
            'apikey': self.apiKey
        }
        payload = {
            "instanceName": nameInstance,
            "qrcode": True,
            "integration": "WHATSAPP-BAILEYS",
            "webhookUrl": "https://new-jeans-walk.loca.lt/chatbot/webhook/",
            "webhookByEvents": True,
            "webhookBase64": True,
            "webhookEvents": [
             "MESSAGES_UPSERT"
            ]
        }
        
        response = requests.post(route, json=payload, headers=headers)
        print(response.text)

        try:
         qrcode_base64 = response.json()['qrcode']['base64']
        except KeyError:
            print("Erro ao obter QR Code da resposta.")
            return

        print(f"Base64 QR Code: {qrcode_base64[:100]}...")  # Imprime os primeiros 100 caracteres do base64 para verificação

        # Remover o prefixo "data:image/png;base64," se existir
        if qrcode_base64.startswith("data:image/png;base64,"):
            qrcode_base64 = qrcode_base64.split(",")[1]

        # Decodificar a string base64
        try:
            image_data = base64.b64decode(qrcode_base64)
        except Exception as e:
            print(f"Erro ao decodificar base64: {e}")
            return

        # Carregar a imagem usando PIL
        try:
            image = Image.open(BytesIO(image_data))
        except Exception as e:
            print(f"Erro ao abrir a imagem: {e}")
            return

        # Exibir a imagem (isso abrirá a imagem no visualizador padrão)
        image.show()

        # Salvar a imagem no disco
        try:
            image.save("/app/qrcodes/qrcode.png")
            print("QR Code salvo como 'qrcode.png'.")
        except Exception as e:
            print(f"Erro ao salvar a imagem: {e}")

            response.raise_for_status()

        
        return response.json()