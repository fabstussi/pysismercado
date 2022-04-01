class Produtos:

    def __init__(
        self,
        id,
        categoria,
        fornecedor,
        nome,
        quantidade,
        preco,
        descricao,
        visivel=1
    ):
        self.id = id
        self.categoria = categoria
        self.fornecedor = fornecedor
        self.nome = nome
        self.quantidade = quantidade
        self.preco = preco
        self.descricao = descricao
        self.visivel = visivel
