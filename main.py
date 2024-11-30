from flask import Flask
from src.adapters.external_services.evolution.webhook_controller import webhook_controller

app = Flask(__name__)

# Registra o blueprint para adicionar as rotas do webhook_controller
app.register_blueprint(webhook_controller)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)