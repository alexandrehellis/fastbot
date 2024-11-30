from crewai import Agent
from crewai_tools import SerperDevTool, AudioTool, ImageTool

# Ferramentas disponíveis para os agentes
ferramenta_pesquisa = SerperDevTool(api_key="SUA_API_KEY_SERPER")
ferramenta_audio = AudioTool()
ferramenta_imagem = ImageTool()

# Função para criar agentes dinamicamente
def criar_agente(role, backstory, goal, tools=None):
    return Agent(
        role=role,
        backstory=backstory,
        goal=goal,
        verbose=True,
        llm="gpt-4-mini",
        max_iter=15,
        max_rpm=30,
        memory=True,
        function_calling_llm="gpt-4",
        max_execution_time=120,  # tempo máximo em segundos
        allow_code_execution=True,
        tools=tools or []  # Lista de ferramentas para o agente
    )

# Exemplo: Criar um agente de pesquisa na web
pesquisador = criar_agente(
    role="Pesquisador",
    backstory="Você é um especialista em encontrar informações na web rapidamente.",
    goal="Coletar e analisar informações sobre tendências de mercado.",
    tools=[ferramenta_pesquisa]
)

# Exemplo: Criar um agente para lidar com áudios
audio_analista = criar_agente(
    role="Analista de Áudio",
    backstory="Você é um especialista em transcrever e interpretar áudios.",
    goal="Converter arquivos de áudio em texto e extrair insights importantes.",
    tools=[ferramenta_audio]
)

# Exemplo: Criar um agente para analisar imagens
imagem_analista = criar_agente(
    role="Analista de Imagem",
    backstory="Você é um perito em análise de imagens e extração de informações visuais.",
    goal="Analisar imagens para identificar padrões ou informações específicas.",
    tools=[ferramenta_imagem]
)

# Exemplo: Executar tarefas com os agentes
result_pesquisador = pesquisador.run("Pesquisar tendências no mercado de IA.")
result_audio = audio_analista.run("Transcrever e interpretar o áudio fornecido.")
result_imagem = imagem_analista.run("Analisar esta imagem e descrever os detalhes principais.")