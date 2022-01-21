from datetime import datetime, timedelta
from model import Categorias, Fornecerdores, Produtos, Clientes, Cargos, Vendedores, Vendas


class CategoriasDao:

    @classmethod
    def listar(cls) -> list:
        try:
            with open('categorias.txt', 'r') as arquivo:
                linhas = arquivo.readlines()
            linhas = list(map(lambda linha: linha.replace('\n', ''), linhas))
            linhas = list(map(lambda linha: linha.split('|'), linhas))
            return [Categorias(linha[0],
                               linha[1],
                               linha[2]) for linha in linhas]
        except FileNotFoundError:
            return []
        except Exception as e:
            return [-1, 'ERRO', str(e)]

    @classmethod
    def salvar(cls, categoria: Categorias, modo: str) -> bool:
        try:
            with open('categorias.txt', modo) as arquivo:
                arquivo.write(
                    f'{categoria.id}|' +
                    f'{categoria.nome}|' +
                    f'{categoria.descricao}\n')
            return True
        except Exception:
            return False

    @staticmethod
    def gera_id() -> int:
        try:
            with open('categorias.txt', 'r') as arquivo:
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


class FornecedoresDao:

    @classmethod
    def listar(cls) -> list:
        try:
            with open('fornecedores.txt', 'r') as arquivo:
                linhas = arquivo.readlines()
            linhas = list(map(lambda linha: linha.replace('\n', ''), linhas))
            linhas = list(map(lambda linha: linha.split('|'), linhas))
            return [Fornecerdores(linha[0],
                                  linha[1],
                                  linha[2],
                                  linha[3],
                                  linha[5]) for linha in linhas]
        except FileNotFoundError:
            return []
        except Exception as e:
            return [-1, 'ERRO', str(e)]

    @classmethod
    def salvar(cls, fornecedor: Fornecerdores, modo: str) -> bool:
        try:
            with open('fornecedores.txt', modo) as arquivo:
                arquivo.write(
                    f'{fornecedor.id}|' +
                    f'{fornecedor.cnpj}|' +
                    f'{fornecedor.nome}|' +
                    f'{fornecedor.telefone}|' +
                    f'{fornecedor.categoria}\n')
            return True
        except Exception:
            return False

    @staticmethod
    def gera_id() -> int:
        try:
            with open('fornecedores.txt', 'r') as arquivo:
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


class ProdutosDao:

    @classmethod
    def listar(cls) -> list:
        try:
            with open('produtos.txt', 'r') as arquivo:
                linhas = arquivo.readlines()
            linhas = list(map(lambda linha: linha.replace('\n', ''), linhas))
            linhas = list(map(lambda linha: linha.split('|'), linhas))
            return [Produtos(linha[0],
                             linha[1],
                             linha[2],
                             linha[3],
                             linha[4],
                             linha[5],
                             linha[6],
                             linha[7],) for linha in linhas]
        except FileNotFoundError:
            return []
        except Exception as e:
            return [-1, 'ERRO', str(e)]

    @classmethod
    def salvar(cls, produto: Produtos, modo: str) -> bool:
        try:
            with open('produtos.txt', modo) as arquivo:
                arquivo.write(
                    f'{produto.id}|' +
                    f'{produto.categoria}|' +
                    f'{produto.fornecedor}|' +
                    f'{produto.nome}|' +
                    f'{produto.quantidade}|' +
                    f'{produto.custo}|' +
                    f'{produto.preco}|' +
                    f'{produto.descricao}\n')
            return True
        except Exception:
            return False

    @staticmethod
    def gera_id() -> int:
        try:
            with open('produtos.txt', 'r') as arquivo:
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


class ClientesDao:

    @classmethod
    def listar(cls) -> list:
        try:
            with open('clientes.txt', 'r') as arquivo:
                linhas = arquivo.readlines()
            linhas = list(map(lambda linha: linha.replace('\n', ''), linhas))
            linhas = list(map(lambda linha: linha.split('|'), linhas))
            return [Clientes(linha[0],
                             linha[1],
                             linha[2],
                             linha[3],
                             linha[4],
                             linha[5]) for linha in linhas]
        except FileNotFoundError:
            return []
        except Exception as e:
            return [-1, 'ERRO', str(e)]

    @classmethod
    def salvar(cls, cliente: Clientes, modo: str) -> bool:
        try:
            with open('clientes.txt', modo) as arquivo:
                arquivo.write(
                    f'{cliente.id}|' +
                    f'{cliente.cpf}|' +
                    f'{cliente.nome}|' +
                    f'{cliente.telefone}|' +
                    f'{cliente.sexo}|' +
                    f'{cliente.ano_nasc}\n')
            return True
        except Exception:
            return False

    @staticmethod
    def gera_id() -> int:
        try:
            with open('clientes.txt', 'r') as arquivo:
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
    # from time import sleep
    pass
