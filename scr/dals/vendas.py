# -*- coding: utf-8 -*-
from models.vendas import Vendas
from util.PyNumBR import pega_data, pega_hora


class VendasDal:

    @classmethod
    def listar(cls) -> list:
        try:
            with open('db/vendas.dbpy', 'r', encoding='utf-8') as arquivo:
                linhas = arquivo.readlines()
            linhas = list(map(lambda linha: linha.replace('\n', ''), linhas))
            linhas = list(map(lambda linha: linha.split('|'), linhas))
            return [Vendas(linha[0], linha[1], linha[2], linha[3], linha[4],
                           float(linha[5]), int(linha[6])) for linha in linhas]
        except FileNotFoundError:
            return []
        except Exception as e:
            print(f'ERRO: {e}')
            return []

    @classmethod
    def salvar(cls, venda: Vendas, modo: str) -> bool:
        try:
            with open('db/vendas.dbpy', modo, encoding='utf-8') as arquivo:
                arquivo.write(
                    f'{venda.cupom}|{venda.funcionario}|{venda.data}|' +
                    f'{venda.cliente}|{venda.compra}|{venda.valor}|' +
                    f'{venda.visivel}\n')
            return True
        except Exception:
            return False

    @staticmethod
    def gera_cupom() -> str:
        data = pega_data().strip('/')
        hora = pega_hora().strip(':')
        return f'{data[2]}{data[1]}{data[0]}{hora[0]}{hora[1]}'
