from datetime import datetime
from utils.database import db

class Tarefa(db.Model):
    """
    Modelo de dados para uma tarefa no banco de dados.
    """

    __tablename__ = 'tarefas'

    # Definição das colunas
    id = db.Column(db.Integer, primary_key=True)
    descricao = db.Column(db.String(255), nullable=False)
    concluida = db.Column(db.Boolean, default=False)
    data_criacao = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<Tarefa {self.id}: {self.descricao}>'

    def to_dict(self):
        """
        Converte o objeto Tarefa em um dicionário para fácil manipulação.
        """
        return {
            'id': self.id,
            'descricao': self.descricao,
            'concluida': self.concluida,
            'data_criacao': self.data_criacao.isoformat()
        }

