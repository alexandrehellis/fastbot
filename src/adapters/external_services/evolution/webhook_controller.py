from flask import Blueprint, request, jsonify
from app.aplication.use_cases.procees_webhook_data import ProcessWebhookData
from adapters.external_services.evolution.client import EvolutionApiClient
from adapters.external_services.openai.client import OpenaiClient

webhook_controller = Blueprint('webhook_controller', __name__)

@webhook_controller.route("/chatbot/webhook/messages-upsert", methods=['POST'])
def webhook():
    data = request.get_json()
    print(data)
    try: 
        evolution_client = EvolutionApiClient()
        openai_client = OpenaiClient()
        process_webhook = ProcessWebhookData(evolution_client, openai_client)
        response = process_webhook.execute(data)
        
        return {"status" : "success", "response" : response}
    except Exception as e:
        print(e)
        return jsonify({"status": "error", "details": str(e)}), 500
