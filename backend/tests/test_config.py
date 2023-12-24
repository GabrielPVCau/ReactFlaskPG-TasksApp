import pytest
from app import create_app
from config import Config

@pytest.fixture
def app():
    """
    Cria uma instância da aplicação para os testes.
    """
    app = create_app(Config)
    return app

def test_app_is_created(app):
    """
    Testa se a aplicação é criada corretamente.
    """
    assert app is not None

def test_config_is_loaded(app):
    """
    Testa se a configuração é carregada corretamente.
    """
    assert app.config['DEBUG'] is False
