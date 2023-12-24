from flask import request, jsonify, abort
from services.tarefa_service import TarefaService
from models.tarefa_model import Tarefa

def listar_tarefas():
    print("Listando todas as tarefas...")
    try:
        tarefas = TarefaService.listar_tarefas()
        return jsonify([tarefa.to_dict() for tarefa in tarefas]), 200
    except Exception as e:
        print(f"Erro ao listar tarefas: {e}")
        abort(500)

def adicionar_tarefa():
    dados = request.json
    if not dados or not 'descricao' in dados:
        print("Dados inválidos recebidos para criação de tarefa.")
        abort(400)

    print(f"Adicionando tarefa: {dados['descricao']}")
    try:
        tarefa = TarefaService.adicionar_tarefa(dados['descricao'])
        return jsonify(tarefa.to_dict()), 201
    except Exception as e:
        print(f"Erro ao adicionar tarefa: {e}")
        abort(500)

def atualizar_tarefa(id_tarefa):
    dados = request.json
    if not dados or not 'descricao' in dados:
        print("Dados inválidos recebidos para atualização de tarefa.")
        abort(400)

    print(f"Atualizando tarefa {id_tarefa} com: {dados['descricao']}")
    try:
        tarefa = TarefaService.atualizar_tarefa(id_tarefa, dados['descricao'])
        if tarefa is None:
            abort(404)
        return jsonify(tarefa.to_dict()), 200
    except Exception as e:
        print(f"Erro ao atualizar tarefa {id_tarefa}: {e}")
        abort(500)

def deletar_tarefa(id_tarefa):
    print(f"Deletando tarefa {id_tarefa}...")
    try:
        sucesso = TarefaService.deletar_tarefa(id_tarefa)
        if not sucesso:
            abort(404)
        return jsonify({'mensagem': 'Tarefa deletada com sucesso!'}), 200
    except Exception as e:
        print(f"Erro ao deletar tarefa {id_tarefa}: {e}")
        abort(500)
