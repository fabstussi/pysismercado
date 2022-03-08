from models.pessoas import Clientes
from dals.clientes import ClientesDal
from re import fullmatch
from datetime import datetime
from util.PyNumBR import ler_inteiro
import util.PyUtilTerminal as put


class ClientesController:

    @staticmethod
    def valida_entrada_dados(cpf: str, nome: str, telefone: str, sexo: str,
                             nasc: int) -> bool:
        if not fullmatch(r'[0-9]{3}[\.]?[0-9]{3}[\.]?[0-9]{3}[-]?[0-9]{2}',
                         cpf) and not fullmatch(r'[0-9]{11}', cpf):
            return False
        cpf = cpf.replace('.', '').replace('-', '')
        if not cpf.isdigit():
            return False
        for i in range(2):
            peso = 10 + i
            soma = (sum([int(n) * (peso - cpf.index(n))for n in cpf[:9 + i]]) * 10
                    ) % 11
            soma = 0 if soma == 10 else soma
            if soma != int(cpf[9 + i]):
                print(f'A soma deu {soma} e o dígito {cpf[9 + i]} não confere')
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
        return True

    @classmethod
    def buscar(cls, id=None, nome=None, invisiveis=False) -> list:
        clientes = ClientesDal()
        if id is not None:
            listas = list(filter(lambda cliente: cliente.id == id,
                                 clientes.listar()))
        elif nome is not None:
            listas = list(filter(lambda cliente: cliente.nome == nome,
                                 clientes.listar()))
        else:
            listas = clientes.listar()
        if not invisiveis:
            listas = list(filter(lambda x: x.visivel == 1, listas))
        return listas

    @classmethod
    def cadastrar(cls, cpf, nome, telefone, sexo, nasc, visivel=1) -> tuple:
        if not cls.valida_entrada_dados(cpf, nome, telefone, sexo, nasc):
            return -1, 'Dados inválidos'
        id = ClientesDal.gera_id()
        cliente = Clientes(id, cpf, nome, telefone, sexo, nasc, visivel)
        if len(cls.buscar(nome=nome)) > 0:
            return 1, 'cliente já cadastrado'
        elif ClientesDal.salvar(cliente, 'a'):
            return 0, f'cliente {nome} cadastrado com sucesso!'
        else:
            return -2, 'Erro não foi possível realizar o cadastro'

    @classmethod
    def alterar(cls, id: int, novo_cpf: str, novo_nome: str,
                novo_telefone: str, novo_sexo: str, novo_nasc, visivel=1,
                tudo=False) -> tuple:
        if not cls.valida_entrada_dados(novo_cpf, novo_nome, novo_telefone,
                                        novo_sexo, novo_nasc):
            return -1, 'Dados inválidos'
        cliente = cls.buscar(nome=novo_nome, invisiveis=tudo)
        if len(cliente) > 0 and cliente[0].id != id:
            return 1, f'{novo_nome} já cadastrado no ID: {cliente[0].id}'
        cliente = cls.buscar(id=id, invisiveis=tudo)
        if len(cliente) == 0:
            return -1, 'cliente não encontrado'
        cliente[0].cpf = novo_cpf
        cliente[0].nome = novo_nome
        cliente[0].telefone = novo_telefone
        cliente[0].sexo = novo_sexo
        cliente[0].ano_nasc = novo_nasc
        cliente[0].visivel = visivel
        for i, clie in enumerate(cls.buscar(invisiveis=True)):
            modo = 'w' if i == 0 else 'a'
            if cliente[0].id != clie.id:
                ClientesDal.salvar(clie, modo)
            else:
                if input(f'Confirme a alteração do cliente {clie.nome} ' +
                         '(s/n): ')[0].lower() == 's':
                    ClientesDal.salvar(cliente[0], modo)
                    retorno = 0, f'Cliente {novo_nome} alterado com sucesso!'
                else:
                    ClientesDal.salvar(clie, modo)
                    retorno = 0, 'Operação cancelada'
        return retorno

    @classmethod
    def excluir(cls, id: int) -> tuple:
        cliente = cls.buscar(id=id)
        if len(cliente) == 0:
            return 1, 'Cliente não encontrado'
        return cls.alterar(id, cliente[0].cpf, cliente[0].nome,
                           cliente[0].telefone, cliente[0].sexo,
                           cliente[0].ano_nasc, 0)

    @classmethod
    def recuperar_apagadas(cls) -> tuple:
        Clientes = cls.buscar(invisiveis=True)
        Clientes = list(filter(lambda c: c.visivel == 0, Clientes))
        lista_ids = [c.id for c in Clientes]
        if len(Clientes) == 0:
            return 1, 'Não há Clientes excluídos'
        while True:
            put.titulo('Clientes excluídos:')
            for cliente in Clientes:
                print(f'ID: {cliente.id} - cliente: {cliente.nome}')
            put.desenha_linha('=', 30)
            id = ler_inteiro('Digite o ID do cliente a ser restaurado: ')
            if id in lista_ids:
                break
            else:
                print('Opção inválida\n================')
        cliente = cls.buscar(id=id, invisiveis=True)
        return cls.alterar(id, cliente[0].cpf, cliente[0].nome,
                           cliente[0].telefone, cliente[0].sexo,
                           cliente[0].ano_nasc, 1, tudo=True)
