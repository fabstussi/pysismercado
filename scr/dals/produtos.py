from models.produtos import Produtos


class ProdutosDal:

    @classmethod
    def listar(cls) -> list:
        try:
            with open('db/produtos.dbpy', 'r') as arquivo:
                linhas = arquivo.readlines()
            linhas = list(map(lambda linha: linha.replace('\n', ''), linhas))
            linhas = list(map(lambda linha: linha.split('|'), linhas))
            return [Produtos(int(linha[0]), linha[1], linha[2], linha[3],
                             linha[4], linha[5], linha[6], linha[7],
                             int(linha[8])) for linha in linhas]
        except FileNotFoundError:
            return []
        except Exception as e:
            print(f'ERRO: {e}')
            return []

    @classmethod
    def salvar(cls, produto: Produtos, modo: str) -> bool:
        try:
            with open('db/produtos.dbpy', modo) as arquivo:
                arquivo.write(
                    f'{produto.id}|{produto.categoria}|{produto.fornecedor}' +
                    f'|{produto.nome}|{produto.quantidade}|{produto.custo}|' +
                    f'{produto.preco}|{produto.descricao}|{produto.visivel}\n')
            return True
        except Exception:
            return False

    @staticmethod
    def gera_id() -> int:
        try:
            with open('db/produtos.dbpy', 'r') as arquivo:
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
