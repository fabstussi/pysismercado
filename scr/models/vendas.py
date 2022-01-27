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
