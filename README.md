
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


## Contribuição


## Licença



