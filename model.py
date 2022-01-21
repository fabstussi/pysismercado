class Categorias:
    def __init__(self, id, nome, descricao):
        self.id = id
        self.nome = nome
        self.descricao = descricao

    def __str__(self):
        return f'{self.nome}'



