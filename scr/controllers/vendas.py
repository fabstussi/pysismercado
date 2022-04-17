from itertools import count
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
                if data_i <= venda_data <= data_f:
                    listas.append(venda)
        else:
            listas = vendas.listar()
        if not invisiveis:
            listas = list(filter(lambda x: x.visivel == 1, listas))
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

    @classmethod
    def gerar_relatorio(
        cls,
        quantidade: int,
        parametro: str,
    ) -> list:
        listar = []
        if parametro == 'cliente':
            arruma_cliente = []
            vendas = cls.buscar()
            for venda in vendas:
                compras_clientes = {'Cliente': venda.cliente, 'Compras': []}
                lista = venda.compra.replace("['", '').replace("']", '')
                lista = lista.split("', '")
                for linha in lista:
                    compras = []
                    linha = linha.split(';')
                    linha.pop()
                    itens = list(map(lambda x: x.split(':')[1], linha))
                    produto = itens[1]
                    quantidades = int(itens[2])
                    compras.append(produto)
                    compras.append(quantidades)
                    compras_clientes['Compras'].append(compras)
                arruma_cliente.append(compras_clientes)
            conta_cliente = []
            lista_compras = []
            itens_compra = []
            for cliente in arruma_cliente:
                for v in cliente['Cliente']:
                    if v not in conta_cliente:
                        conta_cliente.append(v)
                        conta_cliente.append(1)
                    else:
                        conta_cliente[conta_cliente.index(v) + 1] += 1
                # for k, v in cliente.items():
                #     if k == 'Cliente':
                #         if v not in conta_cliente:
                #             conta_cliente.append(v)
                #             conta_cliente.append(1)
                #         else:
                #             conta_cliente[conta_cliente.index(v) + 1] += 1
            print(conta_cliente)
        elif parametro == 'produto':
            vendas = cls.buscar()
            for venda in vendas:
                produtos_quantidade = {}
                lista = venda.compra.replace("['", '').replace("']", '')
                lista = lista.split("', '")
                for linha in lista:
                    linha = linha.split(';')
                    linha.pop()
                    itens = list(map(lambda x: x.split(':')[1], linha))
                    produto = itens[1]
                    quantidades = int(itens[2])
                    produtos_quantidade[produto] = quantidades
                listar.append(produtos_quantidade)
            soma_produtos = []
            for item in listar:
                for key, value in item.items():
                    if key not in soma_produtos:
                        soma_produtos.append(key)
                        soma_produtos.append(value)
                    else:
                        soma_produtos[soma_produtos.index(key) + 1] += value
            for i in range(0, len(soma_produtos), 2):
                listar.append(
                    f'Produto: {soma_produtos[i]} - Quantidade: ' +
                    f'{soma_produtos[i + 1]}'
                )
        return listar
