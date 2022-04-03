from models.vendas import Vendas
from dals.vendas import VendasDal
from datetime import datetime
import util.PyNumBR as pnb


class VendasController:

    @classmethod
    def buscar(cls, cupom=None, data_i=None, data_f=None, invisiveis=False
               ) -> list:
        vendas = VendasDal()
        if cupom is not None:
            listas = list(filter(lambda venda: venda.cupom == cupom,
                                 vendas.listar()))
        elif data_i is not None and data_f is None:
            listas = list(filter(lambda venda: venda.data == data_i,
                                 vendas.listar()))
        elif data_i is not None and data_f is not None:
            data_i = datetime.strptime(data_i, '%d/%m/%Y')
            data_f = datetime.strptime(data_f, '%d/%m/%Y')
            listas = []
            for venda in vendas.listar():
                venda_data = datetime.strptime(venda.data, '%d/%m/%Y')
                if data_i < venda_data < data_f:
                    listas.append(venda)
        else:
            listas = vendas.listar()
        if not invisiveis:
            listas = list(filter(lambda x: x.visivel == 1, listas))
        return listas

    @staticmethod
    def listar_compras(compra: str) -> list:
        listas = compra[1:-1].replace("'", '').split(', ')
        listas = list(map(lambda c: c.split(';'), listas))
        return listas

    @staticmethod
    def quantidade_produtos_vendidos(cupom=None, data_i=None, data_f=None
                                     ) -> list:
        itens = []
        listas = []
        vendas = VendasController()
        for venda in vendas.buscar(cupom=cupom, data_i=data_i, data_f=data_f):
            lista_compras = venda.compra[1:-1].replace("'", "").split(', ')
            lista_compras = list(
                map(lambda compra: compra.split(';'), lista_compras))
            for item_comprado in lista_compras:
                if item_comprado[0] not in itens:
                    itens.append(item_comprado[0])
                    listas.append(item_comprado[0])
                    listas.append(int(item_comprado[1]))
                else:
                    i = listas.index(item_comprado[0])
                    listas[i + 1] += int(item_comprado[1])

        return listas

    @classmethod
    def cadastrar(
            cls,
            funcionario: str,
            cliente: str,
            compra: list,
            valor: float,
            data=pnb.pega_data(),
            visivel=1) -> tuple:
        vendas = VendasDal()
        n_cupom = vendas.gera_cupom()
        venda = Vendas(n_cupom, funcionario, data, cliente, compra,
                       valor, visivel)
        if vendas.salvar(venda, 'a'):
            return n_cupom, 'Venda cadastrada com sucesso'
        else:
            return -1, 'Erro não foi possível realizar o cadastro'

    @classmethod
    def cria_cupom(cls, cupom, telefone) -> tuple:
        vendas = cls.buscar(cupom=cupom)
        id_itens = []
        quantidade_itens = []
        for venda in vendas:
            cupom = [
                f'Cupom: {venda.cupom} {" " * 75} Data: {venda.data}',
                f'Funcionário: {venda.funcionario}',
                f'Cliente: {venda.cliente} - Telefone: {telefone}',
                '',
            ]
            lista = venda.compra.replace("['", '').replace("']", '')
            lista = lista.split("', '")
            cupom.append(
                f'{"ID":<5}{"Produto":<50}{"Quantidade":<12}{"Preço":<15}' +
                f'{"Subtotal":<15}'
            )
            for linha in lista:
                linha = linha.split(';')
                linha.pop()
                itens = list(map(lambda x: x.split(':')[1], linha))
                id_itens.append(int(itens[0]))
                quantidade_itens.append(int(itens[2]) * (-1))
                cupom.append(
                    f'{itens[0]:<5}{itens[1]:<50}{itens[2]:<12}{itens[3]:<15}'
                    + f'{itens[4]:<15}'
                )
            cupom.append('')
            cupom.append(f'Total: {pnb.mostra_BLR(venda.valor):}')
        return cupom, id_itens, quantidade_itens
