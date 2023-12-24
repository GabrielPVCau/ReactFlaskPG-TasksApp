import axios from 'axios';

const BASE_URL = 'http://localhost:5000/api'; 

const tarefaApi = axios.create({
    baseURL: BASE_URL
});

tarefaApi.interceptors.request.use(request => {
    console.log('Iniciando Requisição:', request);
    return request;
});

tarefaApi.interceptors.response.use(response => {
    console.log('Resposta Recebida:', response);
    return response;
}, error => {
    console.log('Erro na Resposta:', error);
    return Promise.reject(error);
});

export default tarefaApi;
