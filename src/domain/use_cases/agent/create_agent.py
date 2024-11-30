from src.services.agent_service import AgentService

class CreateDynamicAgentUseCase:
    """Caso de uso para criar um agente dinâmico com base na entrada fornecida."""

    def __init__(self):
        self.agent_service = AgentService()

    def execute(self, role, backstory, goal):
        # Configura e cria o agente com o serviço
        agent = self.agent_service.create_agent(role, backstory, goal)
        result = agent.run(f"Processar e transcrever o conteúdo fornecido: {input_data}")

        return {"message": "Agente processado com sucesso", "result": result}

    def detect_input_type(self, input_data):
        if input_data.startswith("http"):  # Verifica se é uma URL
            return "web"
        elif input_data.lower().endswith((".mp3", ".wav")):  # Áudio
            return "audio"
        elif input_data.lower().endswith((".png", ".jpg", ".jpeg")):  # Imagem
            return "image"
        else:
            raise ValueError("Tipo de entrada não suportado.")