import React from 'react';
import ListaTarefas from './components/ListaTarefas';
import AdicionarTarefa from './components/AdicionarTarefa';
//import './App.css'; quando fizer css

const App = () => {
  console.log('App: Renderizando componentes');

  return (
    <div className="App">
      <header className="App-header">
        <h1>Gerenciador de Tarefas</h1>
      </header>
      <AdicionarTarefa />
      <ListaTarefas />
    </div>
  );
}

export default App;
