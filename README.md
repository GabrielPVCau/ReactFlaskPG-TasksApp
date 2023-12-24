
# FlaskReactPostgres-ToDoList

## Descrição
"FlaskReactPostgres-ToDoList" é uma aplicação interativa de lista de tarefas, desenvolvida utilizando Python Flask para o backend, React para o frontend, e PostgreSQL para o banco de dados. Esta solução permite aos usuários gerenciar tarefas diárias, com funcionalidades de criar, ler, atualizar e deletar (CRUD), uma interface de usuário intuitiva e uma API robusta e escalável.

## Características
- **CRUD de Tarefas**: Usuários podem adicionar, visualizar, modificar e excluir tarefas.
- **Backend em Flask**: Uma API RESTful bem estruturada para gerenciar as operações de tarefas.
- **Frontend em React**: Uma interface de usuário interativa e responsiva.
- **Banco de Dados PostgreSQL**: Armazenamento seguro e eficiente de dados de tarefas.
- **Design Modular**: Código organizado e fácil de manter.
- **Segurança Integrada**: Medidas básicas de segurança aplicadas.

## Tecnologias Utilizadas
- Backend: Python Flask
- Frontend: React
- Banco de Dados: PostgreSQL
- Gerenciamento de Configurações: dotenv
- Controle de Versão: Git

## Estrutura do Projeto
```
projeto-to-do-list/
├── backend/
│   ├── app.py                     # Aplicação Flask e configuração da API
│   ├── config.py                  # Configurações da aplicação
│   ├── models/
│   │   └── tarefa_model.py        # Modelo do SQLAlchemy
│   ├── resources/
│   │   ├── tarefa_resource.py     # Endpoints da API
│   ├── services/
│   │   └── tarefa_service.py      # Lógica de negócios
│   ├── tests/
│   │   ├── test_config.py         # Testes de configuração
│   │   └── test_tarefa.py         # Testes de tarefas
│   └── utils/
│       └── database.py            # Configuração do banco de dados
├── frontend/
│   ├── public/                    
│   │   └── index.html             # Página HTML principal
│   ├── src/
│   │   ├── components/            
│   │   │   ├── ListaTarefas.js    # Componente de lista de tarefas
│   │   │   └── AdicionarTarefa.js # Componente para adicionar tarefas
│   │   ├── App.js                 # Componente principal React
│   │   └── api/
│   │       └── tarefaApi.js       # Interação com a API Flask
└── README.md                      # Este arquivo
```

## Instalação e Execução

Claro, aqui está a seção detalhada de **Instalação e Execução** para o seu README, considerando tanto o backend quanto o frontend do seu projeto "To Do List".

---

## Instalação e Execução

Para executar a aplicação "To Do List", você precisará instalar e configurar tanto o backend (Python/Flask) quanto o frontend (React).

### Backend (Python/Flask)

1. **Instalação das Dependências:**
   - Navegue até a pasta `backend`.
   - Instale as dependências do projeto executando o comando:
     ```bash
     pip install -r requirements.txt
     ```

2. **Configuração do Banco de Dados:**
   - Certifique-se de ter o PostgreSQL instalado e em execução.
   - Crie um banco de dados para a aplicação.
   - Configure as credenciais do banco de dados e outras configurações no arquivo `.env`, baseando-se no modelo `.env`.

3. **Execução do Servidor Flask:**
   - Inicie o servidor Flask com o comando:
     ```bash
     python app.py
     ```
   - O servidor estará rodando em `http://localhost:5000` (ou na porta configurada).

### Frontend (React)

1. **Instalação das Dependências:**
   - Navegue até a pasta `frontend`.
   - Instale as dependências do projeto executando:
     ```bash
     npm install
     ```
   - Este passo é necessário apenas na primeira execução ou quando novas dependências são adicionadas.

2. **Execução da Aplicação React:**
   - Inicie a aplicação React com o comando:
     ```bash
     npm start
     ```
   - Isso abrirá a aplicação no navegador padrão. Por padrão, a aplicação estará disponível em `http://localhost:3000`.

### Observações Adicionais:

- Certifique-se de que o backend esteja em execução para que o frontend possa interagir com a API.
- As portas padrão (`5000` para Flask e `3000` para React) podem ser alteradas conforme sua configuração ou necessidade.



## Contribuição
Sinta-se livre para contribuir com este projeto. Sugestões e pull requests são bem-vindas.



