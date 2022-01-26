class Categorias:

    def __init__(self, id, nome, descricao, visivel=True):
        self.id = id
        self.nome = nome
        self.descricao = descricao
        self.visivel = visivel


class Fornecerdores:

    def __init__(self, id, cnpj, nome, telefone, categoria, visivel=True):
        self.id = id
        self.cnpj = cnpj
        self.nome = nome
        self.telefone = telefone
        self.categoria = categoria
        self.visivel = visivel


class Produtos:

    def __init__(self, id, categoria, fornecedor, nome, quantidade, custo,
                 preco, descricao, visivel=True):
        self.id = id
        self.categoria = categoria
        self.fornecedor = fornecedor
        self.nome = nome
        self.quantidade = quantidade
        self.custo = custo
        self.preco = preco
        self.descricao = descricao
        self.visivel = visivel


class Clientes:

    def __init__(self, id, cpf, nome, telefone, sexo, ano_nasc, visivel=True):
        self.id = id
        self.cpf = cpf
        self.nome = nome
        self.telefone = telefone
        self.sexo = sexo
        self.ano_nasc = ano_nasc
        self.visivel = visivel


class Cargos:

    def __init__(self, id, nome, descricao, visivel=True):
        self.id = id
        self.nome = nome
        self.descricao = descricao
        self.visivel = visivel


class Funcionarios(Clientes):

    def __init__(self, id, cpf, nome, telefone, sexo, ano_nasc, cargo,
                 visivel=True):
        super().__init__(id, cpf, nome, telefone, sexo, ano_nasc, visivel)
        self.cargo = cargo


class Vendas:

    def __init__(self, cupom, funcionario, data, cliente, compra, valor,
                 visivel=True):
        self.cupom = cupom
        self.funcionario = funcionario
        self.data = data
        self.cliente = cliente
        self.compra = compra
        self.valor = valor
        self.visivel = visivel
