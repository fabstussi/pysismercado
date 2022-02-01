from models.fornecedores import Fornecerdores


class FornecedoresDal:

    @classmethod
    def listar(cls) -> list:
        try:
            with open('pydb/fornecedores.txt', 'r') as arquivo:
                linhas = arquivo.readlines()
            linhas = list(map(lambda linha: linha.replace('\n', ''), linhas))
            linhas = list(map(lambda linha: linha.split('|'), linhas))
            return [Fornecerdores(int(linha[0]), linha[1], linha[2], linha[3],
                                  linha[4], int(linha[5])
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
