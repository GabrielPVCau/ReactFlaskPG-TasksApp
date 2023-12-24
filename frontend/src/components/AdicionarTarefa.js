import React, { useState } from 'react';
import tarefaApi from '../api/tarefaApi';

const AdicionarTarefa = () => {
    const [descricao, setDescricao] = useState('');

    const handleSubmit = async (event) => {
        event.preventDefault();
        if (!descricao) return;

        try {
            console.log('Adicionando tarefa:', descricao);
            const response = await tarefaApi.post('/tarefas', { descricao });
            console.log('Tarefa adicionada:', response.data);
        } catch (error) {
            console.error('Erro ao adicionar tarefa:', error);
        }
    };

    return (
        <div>
            <h2>Adicionar Tarefa</h2>
            <form onSubmit={handleSubmit}>
                <input
                    type="text"
                    value={descricao}
                    onChange={(e) => setDescricao(e.target.value)}
                />
                <button type="submit">Adicionar</button>
            </form>
        </div>
    );
};

export default AdicionarTarefa;
