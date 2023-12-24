from flask_sqlalchemy import SQLAlchemy

# Instância do SQLAlchemy
db = SQLAlchemy()

def init_app(app):
    """
    Inicializa o banco de dados com a aplicação Flask.
    """
    print("Iniciando a configuração do banco de dados...")
    db.init_app(app)
    print("Banco de dados configurado e associado à aplicação Flask.")
