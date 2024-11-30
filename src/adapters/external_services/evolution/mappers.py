

def map_to_evolution_format(data, message):
    # Converte dados do domínio para o formato esperado pela API Evolution
    return { 
        "text" : message,  #data["content"],
        "number" : data['data']['key']['remoteJid'],
        "instance": data['instance']
     }


def map_from_evolution_response(response):
    # Converte a resposta da API Evolution para o formato do domínio
    return {
        "message_id" : response["id"],
        "status" : response["status"]
    }