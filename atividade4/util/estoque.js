const estoque = {};

// Adicionar um produto
function adicionarProduto(id, nome, qtd) {
    estoque[id] = { nome, quantidade: parseInt(qtd) };
    return `Produto ${nome} adicionado com sucesso!`;
}

// Listar todos os produtos
function listarProdutos() {
    return estoque;
}

// Remover um produto
function removerProduto(id) {
    if (estoque[id]) {
        delete estoque[id];
        return `Produto removido com sucesso!`;
    }
    return `Produto não encontrado!`;
}

// Editar a quantidade de um produto
function editarProduto(id, qtd) {
    if (estoque[id]) {
        estoque[id].quantidade = parseInt(qtd);
        return `Quantidade do produto ${estoque[id].nome} atualizada para ${qtd}!`;
    }
    return `Produto não encontrado!`;
}

module.exports = { adicionarProduto, listarProdutos, removerProduto, editarProduto };