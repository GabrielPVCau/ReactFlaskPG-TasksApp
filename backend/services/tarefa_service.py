from models.tarefa_model import Tarefa
from utils.database import db

class TarefaService:

    @staticmethod
    def listar_tarefas():
        print("Serviço: Listando todas as tarefas...")
        return Tarefa.query.all()

    @staticmethod
    def adicionar_tarefa(descricao):
        print(f"Serviço: Adicionando tarefa com descrição - '{descricao}'")
        nova_tarefa = Tarefa(descricao=descricao)
        db.session.add(nova_tarefa)
        db.session.commit()
        return nova_tarefa

    @staticmethod
    def atualizar_tarefa(id_tarefa, nova_descricao):
        print(f"Serviço: Atualizando tarefa {id_tarefa} com nova descrição - '{nova_descricao}'")
        tarefa = Tarefa.query.get(id_tarefa)
        if tarefa:
            tarefa.descricao = nova_descricao
            db.session.commit()
            return tarefa
        return None

    @staticmethod
    def deletar_tarefa(id_tarefa):
        print(f"Serviço: Deletando tarefa {id_tarefa}")
        tarefa = Tarefa.query.get(id_tarefa)
        if tarefa:
            db.session.delete(tarefa)
            db.session.commit()
            return True
        return False
