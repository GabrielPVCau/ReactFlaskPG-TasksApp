import React from 'react';
import ReactDOM from 'react-dom';
import App from './App';
//import './index.css'; // qnd tiver css

console.log('Iniciando a renderização do React...');

ReactDOM.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
  document.getElementById('root')
);

console.log('Aplicação React renderizada com sucesso.');
