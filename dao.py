from model import Categorias, Fornecerdores, Produtos, Clientes, Cargos, Funcionarios, Vendas


class CategoriasDao:

    @classmethod
    def listar(cls) -> list:
        try:
            with open('pydb/categorias.txt', 'r') as arquivo:
                linhas = arquivo.readlines()
            linhas = list(map(lambda linha: linha.replace('\n', ''), linhas))
            linhas = list(map(lambda linha: linha.split('|'), linhas))
            return [Categorias(linha[0], linha[1], linha[2], bool(linha[3]))
                    for linha in linhas]
        except FileNotFoundError:
            return []
        except Exception as e:
            print(f'ERRO: {e}')
            return []

    @classmethod
    def salvar(cls, categoria: Categorias, modo: str) -> bool:
        try:
            with open('pydb/categorias.txt', modo) as arquivo:
                arquivo.write(
                    f'{categoria.id}|{categoria.nome}|{categoria.descricao}|' +
                    f'{categoria.visivel}\n')
            return True
        except Exception:
            return False

    @staticmethod
    def gera_id() -> int:
        try:
            with open('pydb/categorias.txt', 'r') as arquivo:
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
            with open('pydb/fornecedores.txt', 'r') as arquivo:
                linhas = arquivo.readlines()
            linhas = list(map(lambda linha: linha.replace('\n', ''), linhas))
            linhas = list(map(lambda linha: linha.split('|'), linhas))
            return [Fornecerdores(linha[0], linha[1], linha[2], linha[3],
                                  linha[4], bool(linha[5])
                                  ) for linha in linhas]
        except FileNotFoundError:
            return []
        except Exception as e:
            print(f'ERRO: {e}')
            return []

    @classmethod
    def salvar(cls, fornecedor: Fornecerdores, modo: str) -> bool:
        try:
            with open('pydb/fornecedores.txt', modo) as arquivo:
                arquivo.write(
                    f'{fornecedor.id}|{fornecedor.cnpj}|{fornecedor.nome}|' +
                    f'{fornecedor.telefone}|{fornecedor.categoria}|' +
                    f'{fornecedor.visivel}\n')
            return True
        except Exception:
            return False

    @staticmethod
    def gera_id() -> int:
        try:
            with open('pydb/fornecedores.txt', 'r') as arquivo:
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
            with open('pydb/produtos.txt', 'r') as arquivo:
                linhas = arquivo.readlines()
            linhas = list(map(lambda linha: linha.replace('\n', ''), linhas))
            linhas = list(map(lambda linha: linha.split('|'), linhas))
            return [Produtos(linha[0], linha[1], linha[2], linha[3], linha[4],
                             linha[5], linha[6], linha[7], bool(linha[8])
                             ) for linha in linhas]
        except FileNotFoundError:
            return []
        except Exception as e:
            print(f'ERRO: {e}')
            return []

    @classmethod
    def salvar(cls, produto: Produtos, modo: str) -> bool:
        try:
            with open('pydb/produtos.txt', modo) as arquivo:
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
            with open('pydb/produtos.txt', 'r') as arquivo:
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
            with open('pydb/clientes.txt', 'r') as arquivo:
                linhas = arquivo.readlines()
            linhas = list(map(lambda linha: linha.replace('\n', ''), linhas))
            linhas = list(map(lambda linha: linha.split('|'), linhas))
            return [Clientes(linha[0], linha[1], linha[2], linha[3], linha[4],
                             linha[5], bool(linha[6])) for linha in linhas]
        except FileNotFoundError:
            return []
        except Exception as e:
            print(f'ERRO: {e}')
            return []

    @classmethod
    def salvar(cls, cliente: Clientes, modo: str) -> bool:
        try:
            with open('pydb/clientes.txt', modo) as arquivo:
                arquivo.write(
                    f'{cliente.id}|{cliente.cpf}|{cliente.nome}|' +
                    f'{cliente.telefone}|{cliente.sexo}|{cliente.ano_nasc}|' +
                    f'{cliente.visivel}\n')
            return True
        except Exception:
            return False

    @staticmethod
    def gera_id() -> int:
        try:
            with open('pydb/clientes.txt', 'r') as arquivo:
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


class CargosDao:

    @classmethod
    def listar(cls) -> list:
        try:
            with open('pydb/cargos.txt', 'r') as arquivo:
                linhas = arquivo.readlines()
            linhas = list(map(lambda linha: linha.replace('\n', ''), linhas))
            linhas = list(map(lambda linha: linha.split('|'), linhas))
            return [Cargos(linha[0], linha[1], linha[2], bool(linha[4])
                           ) for linha in linhas]
        except FileNotFoundError:
            return []
        except Exception as e:
            print(f'ERRO: {e}')
            return []

    @classmethod
    def salvar(cls, cargo: Cargos, modo: str) -> bool:
        try:
            with open('pydb/cargos.txt', modo) as arquivo:
                arquivo.write(f'{cargo.id}|{cargo.nome}|{cargo.descricao}|' +
                              f'{cargo.visivel}\n')
            return True
        except Exception:
            return False

    @staticmethod
    def gera_id() -> int:
        try:
            with open('pydb/cargos.txt', 'r') as arquivo:
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


class FuncionariosDao:

    @classmethod
    def listar(cls) -> list:
        try:
            with open('pydb/funcionarios.txt', 'r') as arquivo:
                linhas = arquivo.readlines()
            linhas = list(map(lambda linha: linha.replace('\n', ''), linhas))
            linhas = list(map(lambda linha: linha.split('|'), linhas))
            return [Funcionarios(linha[0], linha[1], linha[2], linha[3],
                                 linha[4], linha[5], linha[6], bool(linha[7])
                                 ) for linha in linhas]
        except FileNotFoundError:
            return []
        except Exception as e:
            print(f'ERRO: {e}')
            return []

    @classmethod
    def salvar(cls, funcionario: Funcionarios, modo: str) -> bool:
        try:
            with open('pydb/funcionarios.txt', modo) as arquivo:
                arquivo.write(
                    f'{funcionario.id}|{funcionario.cpf}|{funcionario.nome}|' +
                    f'{funcionario.telefone}|{funcionario.sexo}|' +
                    f'{funcionario.ano_nasc}|{funcionario.cargo}|' +
                    f'{funcionario.visivel}\n')
            return True
        except Exception:
            return False

    @staticmethod
    def gera_id() -> int:
        try:
            with open('pydb/funcionarios.txt', 'r') as arquivo:
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


class VendasDao:

    @classmethod
    def listar(cls) -> list:
        try:
            with open('pydb/vendas.txt', 'r') as arquivo:
                linhas = arquivo.readlines()
            linhas = list(map(lambda linha: linha.replace('\n', ''), linhas))
            linhas = list(map(lambda linha: linha.split('|'), linhas))
            return [Vendas(linha[0], linha[1], linha[2], linha[3], linha[4],
                           linha[5], bool(linha[6])) for linha in linhas]
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
