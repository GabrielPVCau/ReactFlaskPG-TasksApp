import os
from dotenv import load_dotenv

# Carregar variáveis de ambiente do arquivo .env
load_dotenv()

class Config:
    """Configurações da aplicação Flask."""

    # URI do banco de dados (exemplo: 'postgresql://user:password@localhost/dbname')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI')

    # Desabilita a modificação de rastreamento do SQLAlchemy (para melhor desempenho)
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Chave secreta para sessões e tokens, etc.
    SECRET_KEY = os.getenv('SECRET_KEY')

    # Método para inicializar app com esta configuração, se necessário
    @staticmethod
    def init_app(app):
        pass

