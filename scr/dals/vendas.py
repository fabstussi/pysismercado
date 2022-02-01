from models.vendas import Vendas


class VendasDal:

    @classmethod
    def listar(cls) -> list:
        try:
            with open('pydb/vendas.txt', 'r') as arquivo:
                linhas = arquivo.readlines()
            linhas = list(map(lambda linha: linha.replace('\n', ''), linhas))
            linhas = list(map(lambda linha: linha.split('|'), linhas))
            return [Vendas(int(linha[0]), linha[1], linha[2], linha[3],
                           linha[4], linha[5], int(linha[6])
                           ) for linha in linhas]
        except FileNotFoundError:
            return []
        except Exception as e:
            print(f'ERRO: {e}')
            return []

    @classmethod
    def salvar(cls, venda: Vendas, modo: str) -> bool:
        try:
            with open('pydb/vendas.txt', modo) as arquivo:
                arquivo.write(
                    f'{venda.cupom}|{venda.funcionario}|{venda.data}|' +
                    f'{venda.cliente}|{venda.compra}|{venda.valor}|' +
                    f'{venda.visivel}\n')
            return True
        except Exception:
            return False

    @staticmethod
    def gera_cupom() -> int:
        try:
            with open('pydb/vendas.txt', 'r') as arquivo:
                linhas = arquivo.readlines()
            ultma_linha = [linhas.strip() for linhas in linhas][-1]
            if len(ultma_linha) == 0:
                return 1
            return int(ultma_linha.split('|')[0]) + 1
        except FileNotFoundError:
            return 1
        except Exception as e:
            print(f'Erro: {e}')
            return -1


if __name__ == '__main__':
    pass
