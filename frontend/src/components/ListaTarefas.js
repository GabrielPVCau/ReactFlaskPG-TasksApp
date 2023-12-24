import React, { useState, useEffect } from 'react';
import tarefaApi from '../api/tarefaApi';

const ListaTarefas = () => {
    const [tarefas, setTarefas] = useState([]);

    useEffect(() => {
        const fetchTarefas = async () => {
            try {
                console.log('Buscando tarefas...');
                const response = await tarefaApi.get('/tarefas');
                setTarefas(response.data);
                console.log('Tarefas carregadas:', response.data);
            } catch (error) {
                console.error('Erro ao buscar tarefas:', error);
            }
        };

        fetchTarefas();
    }, []);

    return (
        <div>
            <h2>Lista de Tarefas</h2>
            <ul>
                {tarefas.map(tarefa => (
                    <li key={tarefa.id}>
                        {tarefa.descricao} - {tarefa.concluida ? 'Concluída' : 'Pendente'}
                    </li>
                ))}
            </ul>
        </div>
    );
};

export default ListaTarefas;
