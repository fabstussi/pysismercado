class Clientes:

    def __init__(self, id, cpf, nome, telefone, sexo, ano_nasc, visivel=1):
        self.id = id
        self.cpf = cpf
        self.nome = nome
        self.telefone = telefone
        self.sexo = sexo
        self.ano_nasc = ano_nasc
        self.visivel = visivel


class Funcionarios(Clientes):

    def __init__(self, id, cpf, nome, telefone, sexo, ano_nasc, cargo,
                 visivel=1):
        super().__init__(id, cpf, nome, telefone, sexo, ano_nasc, visivel)
        self.cargo = cargo
