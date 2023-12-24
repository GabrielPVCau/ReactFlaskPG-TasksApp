from flask import Flask
from config import Config
from utils.database import db, init_app
from resources.tarefa_resource import (
    listar_tarefas,
    adicionar_tarefa,
    atualizar_tarefa,
    deletar_tarefa
)

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Inicializa o banco de dados com a aplicação
    init_app(app)

    # Define as rotas para a API
    app.add_url_rule('/api/tarefas', 'listar_tarefas', listar_tarefas, methods=['GET'])
    app.add_url_rule('/api/tarefas', 'adicionar_tarefa', adicionar_tarefa, methods=['POST'])
    app.add_url_rule('/api/tarefas/<int:id_tarefa>', 'atualizar_tarefa', atualizar_tarefa, methods=['PUT'])
    app.add_url_rule('/api/tarefas/<int:id_tarefa>', 'deletar_tarefa', deletar_tarefa, methods=['DELETE'])

    print("Aplicação Flask criada e configurada.")

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
    print("Aplicação Flask em execução.")
