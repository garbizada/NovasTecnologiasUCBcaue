const express = require('express');
const { adicionarProduto, listarProdutos, removerProduto, editarProduto } = require('./util/estoque');

const app = express();
const port = 3000;

// Rotas
app.get('/adicionar/:id/:nome/:qtd', (req, res) => {
    res.send(adicionarProduto(req.params.id, req.params.nome, req.params.qtd));
});

app.get('/listar', (req, res) => {
    res.json(listarProdutos());
});

app.get('/remover/:id', (req, res) => {
    res.send(removerProduto(req.params.id));
});

app.get('/editar/:id/:qtd', (req, res) => {
    res.send(editarProduto(req.params.id, req.params.qtd));
});

// Inicia o servidor
app.listen(port, () => {
    console.log(`Servidor rodando em http://localhost:${port}`);
});