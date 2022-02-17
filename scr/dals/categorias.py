
# -*- coding: utf-8 -*-
from models.categorias import Categorias


class CategoriasDal:

    @classmethod
    def listar(cls) -> list:
        try:
            with open('db/categorias.dbpy', 'r', encoding='utf-8') as arquivo:
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
            with open('db/categorias.dbpy', modo, encoding='utf-8') as arquivo:
                arquivo.write(
                    f'{categoria.id}|{categoria.nome}|{categoria.descricao}|' +
                    f'{categoria.visivel}\n')
            return True
        except Exception:
            return False

    @staticmethod
    def gera_id() -> int:
        try:
            with open('db/categorias.dbpy', 'r', encoding='utf-8') as arquivo:
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
