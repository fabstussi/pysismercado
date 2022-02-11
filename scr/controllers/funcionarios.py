from models.pessoas import Funcionarios
from dals.funcionarios import FuncionariosDal
from re import fullmatch
from datetime import datetime
from util.PyNumBR import ler_inteiro
import util.PyUtilTerminal as put


class FuncionariosController:

    @staticmethod
    def valida_entrada_dados(cpf: str, nome: str, telefone: str, sexo: str,
                             nasc: int, cargo: str) -> bool:
        if not fullmatch(r'[0-9]{3}[\.]?[0-9]{3}[\.]?[0-9]{3}[-]?[0-9]{2}',
                         cpf) and not fullmatch(r'[0-9]{11}', cpf):
            return False
        cpf = cpf.replace('.', '').replace('-', '')
        if not cpf.isdigit():
            return False
        soma = (sum([int(cpf[10 - i]) * (i)
                    for i in range(10, 1, -1)]) * 10) % 11
        if soma == 10:
            soma = 0
        if soma == int(cpf[9]):
            soma = (sum([int(cpf[11 - i]) * (i)
                    for i in range(11, 1, -1)]) * 10) % 11
            if soma == 10:
                soma = 0
            if soma != int(cpf[10]):
                return False
        else:
            return False
        if nome == '' or len(nome) <= 3:
            return False
        telefone = telefone.replace('(', '')\
            .replace(')', '').replace('-', '').replace(' ', '')
        if len(telefone) < 8 or len(telefone) > 11:
            return False
        if len(telefone) == 8:
            if not telefone.isdigit():
                return False
        elif len(telefone) == 9:
            if not telefone.isdigit():
                return False
            if telefone[0] != '9':
                return False
        elif len(telefone) == 10:
            if not telefone.isdigit():
                return False
            if telefone[0] == '0':
                return False
        elif len(telefone) == 11:
            if not telefone.isdigit():
                return False
            if telefone[2] != '9' or telefone[0] == '0':
                return False
        if sexo not in 'MF':
            return False
        if int(nasc) < datetime.now().year - 120 \
                or int(nasc) > datetime.now().year - 18:
            return False
        if cargo == '' or len(cargo) <= 3:
            return False
        return True

    @classmethod
    def buscar(cls, id=None, nome=None, invisiveis=False) -> list:
        funcionarios = FuncionariosDal()
        if id is not None:
            listas = list(filter(lambda funcionario: funcionario.id == id,
                                 funcionarios.listar()))
        elif nome is not None:
            listas = list(filter(lambda funcionario: funcionario.nome == nome,
                                 funcionarios.listar()))
        else:
            listas = funcionarios.listar()
        if not invisiveis:
            listas = list(filter(lambda x: x.visivel == 1, listas))
        return listas

    @classmethod
    def cadastrar(cls, cpf, nome, telefone, sexo, nasc, cargo, visivel=1
                  ) -> str:
        if not cls.valida_entrada_dados(cpf, nome, telefone, sexo, nasc, cargo
                                        ):
            return 'Dados inválidos'
        id = FuncionariosDal.gera_id()
        funcionario = Funcionarios(
            id, cpf, nome, telefone, sexo, nasc, cargo, visivel)
        if len(cls.buscar(nome=nome)) > 0:
            return 'funcionário já cadastrado'
        elif FuncionariosDal.salvar(funcionario, 'a'):
            return f'funcionário {nome} cadastrado com sucesso!'
        else:
            return 'Erro não foi possível realizar o cadastro'

    @classmethod
    def alterar(cls, id: int, novo_cpf: str, novo_nome: str,
                novo_telefone: str, novo_sexo: str, novo_nasc: int,
                novo_cargo: str, visivel=1, tudo=False) -> str:
        if not cls.valida_entrada_dados(novo_cpf, novo_nome, novo_telefone,
                                        novo_sexo, novo_nasc, novo_cargo):
            return 'Dados inválidos'
        funcionario = cls.buscar(nome=novo_nome, invisiveis=tudo)
        if len(funcionario) > 0 and funcionario[0].id != id:
            return f'{novo_nome} já cadastrado no ID: {funcionario[0].id}'
        funcionario = cls.buscar(id=id, invisiveis=tudo)
        if len(funcionario) == 0:
            return 'Funcionário não encontrado'
        funcionario[0].cpf = novo_cpf
        funcionario[0].nome = novo_nome
        funcionario[0].telefone = novo_telefone
        funcionario[0].sexo = novo_sexo
        funcionario[0].ano_nasc = novo_nasc
        funcionario[0].cargo = novo_cargo
        funcionario[0].visivel = visivel
        for i, func in enumerate(cls.buscar(invisiveis=True)):
            modo = 'w' if i == 0 else 'a'
            if funcionario[0].id != func.id:
                FuncionariosDal.salvar(func, modo)
            else:
                if input(f'Confirme a alteração do funcionário {func.nome} ' +
                         '(s/n): ')[0].lower() == 's':
                    FuncionariosDal.salvar(funcionario[0], modo)
                    retorno = f'funcionário {novo_nome} alterado com sucesso!'
                else:
                    FuncionariosDal.salvar(func, modo)
                    retorno = 'Operação cancelada'
        return retorno

    @classmethod
    def excluir(cls, id: int) -> str:
        funcionario = cls.buscar(id=id)
        if len(funcionario) == 0:
            return 'Funcionário não encontrado'
        return cls.alterar(id, funcionario[0].cpf, funcionario[0].nome,
                           funcionario[0].telefone, funcionario[0].sexo,
                           funcionario[0].ano_nasc, funcionario[0].cargo, 0)

    @classmethod
    def recuperar_apagadas(cls) -> str:
        funcionarios = cls.buscar(invisiveis=True)
        funcionarios = list(filter(lambda c: c.visivel == 0, funcionarios))
        lista_ids = [c.id for c in funcionarios]
        if len(funcionarios) == 0:
            return 'Não há funcionários excluídos'
        while True:
            put.titulo('funcionários excluídos:')
            for funcionario in funcionarios:
                print(f'ID: {funcionario.id} - funcionário: {funcionario.nome}'
                      )
            put.desenha_linha('=', 30)
            id = ler_inteiro('Digite o ID do funcionário a ser restaurado: ')
            if id in lista_ids:
                break
            else:
                print('Opção inválida\n================')
        funcionario = cls.buscar(id=id, invisiveis=True)
        return cls.alterar(id, funcionario[0].cpf, funcionario[0].nome,
                           funcionario[0].telefone, funcionario[0].sexo,
                           funcionario[0].ano_nasc, funcionario[0].cargo,
                           visivel=1, tudo=True)
