from adapters.external_services.evolution.client import EvolutionApiClient
from adapters.external_services.evolution.mappers import map_to_evolution_format
from adapters.external_services.openai.client import OpenaiClient

class ProcessWebhookData:
    def __init__(self, evolution_client: EvolutionApiClient, openai_client: OpenaiClient):
        self.evolution_client = evolution_client
        self.openai_client = openai_client

    def execute(self, data):
        returnOpenai = self.openai_client.chat(data['data']['message']['conversation'])
        message_data = map_to_evolution_format(data, returnOpenai)
        print(message_data)
        # self.evolution_client.create_instance("teste Katlin")
        return self.evolution_client.send_message(message_data)