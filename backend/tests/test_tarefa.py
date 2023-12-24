import pytest
from app import create_app
from config import Config
from models.tarefa_model import Tarefa
from utils.database import db

@pytest.fixture
def app():
    """
    Cria uma instância da aplicação para os testes.
    """
    app = create_app(Config)
    with app.app_context():
        db.create_all()
    yield app
    with app.app_context():
        db.drop_all()

@pytest.fixture
def client(app):
    """
    Cria um cliente de teste para enviar requisições à aplicação.
    """
    return app.test_client()

def test_adicionar_tarefa(client):
    """
    Testa a adição de uma nova tarefa.
    """
    resposta = client.post('/api/tarefas', json={'descricao': 'Teste'})
    assert resposta.status_code == 201
    assert 'id' in resposta.json

def test_listar_tarefas(client):
    """
    Testa a listagem de tarefas.
    """
    resposta = client.get('/api/tarefas')
    assert resposta.status_code == 200
    assert isinstance(resposta.json, list)
