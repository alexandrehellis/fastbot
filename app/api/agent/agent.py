from flask import Blueprint, request, jsonify
from src.adapters.database.models.agent import Agent
from src.domain.use_cases.create_agent import CreateAgent
from src.domain.use_cases.update_agent import UpdateAgent
from src.domain.interfaces.database.agent_repository import AgentRepositoryInterface

# Definindo o Blueprint
agents_bp = Blueprint('agents', __name__, url_prefix='/agents')

# Criando o repositório e casos de uso
agent_repository = AgentRepositoryInterface()
create_agent_use_case = CreateAgent(agent_repository)
update_agent_use_case = UpdateAgent(agent_repository)

# Endpoint para criar um agente
@agents_bp.route('/', methods=['POST'])
def create_agent():
    try:
        data = request.get_json()
        name = data['name']
        description = data['description']
        objective = data['objective']
        
        # Chama o caso de uso para criar o agente
        agent = create_agent_use_case.execute(name, description, objective)
        
        return jsonify({
            'message': 'Agente criado com sucesso',
            'agent': agent.to_dict()
        }), 201
    except Exception as e:
        return jsonify({'message': str(e)}), 400
