from models.pessoas import Funcionarios


class FuncionariosDal:

    @classmethod
    def listar(cls) -> list:
        try:
            with open('db/funcionarios.dbpy', 'r') as arquivo:
                linhas = arquivo.readlines()
            linhas = list(map(lambda linha: linha.replace('\n', ''), linhas))
            linhas = list(map(lambda linha: linha.split('|'), linhas))
            return [Funcionarios(int(linha[0]), linha[1], linha[2], linha[3],
                                 linha[4], linha[5], linha[6], int(linha[7])
                                 ) for linha in linhas]
        except FileNotFoundError:
            return []
        except Exception as e:
            print(f'ERRO: {e}')
            return []

    @classmethod
    def salvar(cls, funcionario: Funcionarios, modo: str) -> bool:
        try:
            with open('db/funcionarios.dbpy', modo) as arquivo:
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
            with open('db/funcionarios.dbpy', 'r') as arquivo:
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
