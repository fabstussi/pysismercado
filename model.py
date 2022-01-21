class Categorias:
    def __init__(self, id, nome, descricao):
        self.id = id
        self.nome = nome
        self.descricao = descricao


class Fornecerdores:
    def __init__(self, id, cnpj, nome, telefone, categoria):
        self.id = id
        self.cnpj = cnpj
        self.nome = nome
        self.telefone = telefone
        self.categoria = categoria


class Produtos:
    def __init__(self, id, categoria, fornecedor, nome, quantidade, custo,
                 preco, descricao):
        self.id = id
        self.categoria = categoria
        self.fornecedor = fornecedor
        self.nome = nome
        self.quantidade = quantidade
        self.custo = custo
        self.preco = preco
        self.descricao = descricao


class Clientes:
    def __init__(self, id, cpf, nome, telefone, sexo, ano_nasc):
        self.id = id
        self.cpf = cpf
        self.nome = nome
        self.telefone = telefone
        self.sexo = sexo
        self.ano_nasc = ano_nasc


class Cargos:
    def __init__(self, id, nome, descricao):
        self.id = id
        self.nome = nome
        self.descricao = descricao


class Vendedores(Clientes):
    def __init__(self, id, cpf, nome, telefone, sexo, ano_nasc, cargo):
        super().__init__(id, cpf, nome, telefone, sexo, ano_nasc)
        self.cargo = cargo


class Vendas:
    def __init__(self, cupom, vendedor, data, cliente, quantidade, produto,
                 preco, valor):
        self.cupom = cupom
        self.vendedor = vendedor
        self.data = data
        self.cliente = cliente
        self.quantidade = quantidade
        self.produto = produto
        self.preco = preco
        self.valor = valor
