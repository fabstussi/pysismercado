from models.vendas import Vendas
from util.PyNumBR import pega_data, pega_hora


class VendasDal:

    @classmethod
    def listar(cls) -> list:
        try:
            with open('db/vendas.dbpy', 'r') as arquivo:
                linhas = arquivo.readlines()
            linhas = list(map(lambda linha: linha.replace('\n', ''), linhas))
            linhas = list(map(lambda linha: linha.split('|'), linhas))
            return [Vendas(linha[0], linha[1], linha[2], linha[3],
                           float(linha[4]), float(linha[5]), int(linha[6])
                           ) for linha in linhas]
        except FileNotFoundError:
            return []
        except Exception as e:
            print(f'ERRO: {e}')
            return []

    @classmethod
    def salvar(cls, venda: Vendas, modo: str) -> bool:
        try:
            with open('db/vendas.dbpy', modo) as arquivo:
                arquivo.write(
                    f'{venda.cupom}|{venda.funcionario}|{venda.data}|' +
                    f'{venda.cliente}|{venda.compra}|{venda.valor}|' +
                    f'{venda.visivel}\n')
            return True
        except Exception:
            return False

    @classmethod
    def cria_cupom(cls, venda: Vendas) -> bool:
        pass
        # try:
        #     with open(f'cupom_{venda.cupom}.txt', 'w') as arquivo:
        #         arquivo.write(
        #             f'{venda.cupom}\n' +
        #             f'{venda.funcionario}\n' +
        #             f'{venda.data}\n' +
        #             f'{venda.cliente}\n' +
        #             f'{venda.compra}\n' +
        #             f'{venda.valor}\n' +
        #             f'{venda.visivel}\n')

    @classmethod
    def cria_relatorio(cls) -> bool:
        pass

    @staticmethod
    def gera_cupom() -> str:
        data = pega_data().strip('/')
        hora = pega_hora().strip(':')
        return f'{data[2]}{data[1]}{data[0]}{hora[2]}{hora[1]}'
