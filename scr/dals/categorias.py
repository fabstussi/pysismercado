from models.categorias import Categorias
from locale import setlocale, LC_ALL


class CategoriasDal:

    @classmethod
    def listar(cls) -> list:
        try:
            with open('db/categorias.dbpy', 'r') as arquivo:
                linhas = arquivo.readlines()
            linhas = list(map(lambda linha: linha.replace('\n', ''), linhas))
            linhas = list(map(lambda linha: linha.split('|'), linhas))
            return [Categorias(int(linha[0]), linha[1], linha[2], int(linha[3])
                               ) for linha in linhas]
        except FileNotFoundError:
            return []
        except Exception as e:
            print(f'ERRO: {e}')
            return []

    @classmethod
    def salvar(cls, categoria: Categorias, modo: str) -> bool:
        try:
            with open('db/categorias.dbpy', modo) as arquivo:
                arquivo.write(
                    f'{categoria.id}|{categoria.nome}|{categoria.descricao}|' +
                    f'{categoria.visivel}\n')
            return True
        except Exception:
            return False

    @staticmethod
    def gera_id() -> int:
        try:
            with open('db/categorias.dbpy', 'r') as arquivo:
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
