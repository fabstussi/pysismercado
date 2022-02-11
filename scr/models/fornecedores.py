class Fornecedores:

    def __init__(self, id, cnpj, nome, telefone, categoria, visivel=1):
        self.id = id
        self.cnpj = cnpj
        self.nome = nome
        self.telefone = telefone
        self.categoria = categoria
        self.visivel = visivel
