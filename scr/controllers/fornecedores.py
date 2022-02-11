from scr.models.fornecedores import Fornecedores
from scr.dals.fornecedores import FornecedoresDal
from re import fullmatch
from util.PyNumBR import ler_inteiro
import util.PyUtilTerminal as put


class FornecedoresController:

    @staticmethod
    def valida_entrada_dados(cnpj: str, nome: str, telefone: str,
                             categoria: str) -> bool:
        if not fullmatch(r'[0-9]{2}[\.]?[0-9]{3}[\.]?[0-9]{3}[/]?[0-9]{4}[-]?[0-9]{2}',
                         cnpj) and not fullmatch(r'[0-9]{11}', cnpj):
            return False
        cnpj = cnpj.replace('.', '').replace('/', '').replace('-', '')
        if not cnpj.isdigit():
            return False
        if len(cnpj) != 14:
            return False
        for i in range(2):
            peso = 6 + i
            soma = 0
            for n in cnpj[:12 + i]:
                peso -= 1
                soma += int(n) * peso
                if peso == 2:
                    peso = 10
            digito = (11 - soma % 11 if soma % 11 > 1 else 0)
            if digito != int(cnpj[12 + i]):
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
        if categoria == '' or len(categoria) <= 3:
            return False
        return True

    @classmethod
    def buscar(cls, id=None, nome=None, invisiveis=False) -> list:
        fornecedores = FornecedoresDal()
        if id is not None:
            listas = list(filter(lambda fornecedor: fornecedor.id == id,
                                 fornecedores.listar()))
        elif nome is not None:
            listas = list(filter(lambda fornecedor: fornecedor.nome == nome,
                                 fornecedores.listar()))
        else:
            listas = fornecedores.listar()
        if not invisiveis:
            listas = list(filter(lambda x: x.visivel == 1, listas))
        return listas

    @classmethod
    def cadastrar(cls, cnpj, nome, telefone, categoria, visivel=1) -> str:
        if not cls.valida_entrada_dados(cnpj, nome, telefone, categoria):
            return 'Dados inválidos'
        id = FornecedoresDal.gera_id()
        fornecedor = Fornecedores(
            id, cnpj, nome, telefone, categoria, visivel)
        if len(cls.buscar(nome=nome)) > 0:
            return 'fornecedor já cadastrado'
        elif FornecedoresDal.salvar(fornecedor, 'a'):
            return f'fornecedor {nome} cadastrado com sucesso!'
        else:
            return 'Erro não foi possível realizar o cadastro'

    @classmethod
    def alterar(cls, id: int, novo_cnpj: str, novo_nome: str,
                novo_telefone: str, nova_categoria: str, visivel=1, tudo=False
                ) -> str:
        if not cls.valida_entrada_dados(novo_cnpj, novo_nome, novo_telefone,
                                        nova_categoria):
            return 'Dados inválidos'
        fornecedor = cls.buscar(nome=novo_nome, invisiveis=tudo)
        if len(fornecedor) > 0 and fornecedor[0].id != id:
            return f'{novo_nome} já cadastrado no ID: {fornecedor[0].id}'
        fornecedor = cls.buscar(id=id, invisiveis=tudo)
        if len(fornecedor) == 0:
            return 'Fornecedor não encontrado'
        fornecedor[0].cnpj = novo_cnpj
        fornecedor[0].nome = novo_nome
        fornecedor[0].telefone = novo_telefone
        fornecedor[0].categoria = nova_categoria
        fornecedor[0].visivel = visivel
        for i, func in enumerate(cls.buscar(invisiveis=True)):
            modo = 'w' if i == 0 else 'a'
            if fornecedor[0].id != func.id:
                FornecedoresDal.salvar(func, modo)
            else:
                if input(f'Confirme a alteração do fornecedor {func.nome} ' +
                         '(s/n): ')[0].lower() == 's':
                    FornecedoresDal.salvar(fornecedor[0], modo)
                    retorno = f'fornecedor {novo_nome} alterado com sucesso!'
                else:
                    FornecedoresDal.salvar(func, modo)
                    retorno = 'Operação cancelada'
        return retorno

    @classmethod
    def excluir(cls, id: int) -> str:
        fornecedor = cls.buscar(id=id)
        if len(fornecedor) == 0:
            return 'Fornecedor não encontrado'
        return cls.alterar(id, fornecedor[0].cnpj, fornecedor[0].nome,
                           fornecedor[0].telefone, fornecedor[0].categoria,
                           visivel=0)

    @classmethod
    def recuperar_apagadas(cls) -> str:
        fornecedores = cls.buscar(invisiveis=True)
        fornecedores = list(filter(lambda c: c.visivel == 0, fornecedores))
        lista_ids = [c.id for c in fornecedores]
        if len(fornecedores) == 0:
            return 'Não há fornecedors excluídos'
        while True:
            put.titulo('fornecedors excluídos:')
            for fornecedor in fornecedores:
                print(f'ID: {fornecedor.id} - fornecedor: {fornecedor.nome}'
                      )
            put.desenha_linha('=', 30)
            id = ler_inteiro('Digite o ID do fornecedor a ser restaurado: ')
            if id in lista_ids:
                break
            else:
                print('Opção inválida\n================')
        fornecedor = cls.buscar(id=id, invisiveis=True)
        return cls.alterar(id, fornecedor[0].cnpj, fornecedor[0].nome,
                           fornecedor[0].telefone, fornecedor[0].categoria,
                           visivel=1, tudo=True)
