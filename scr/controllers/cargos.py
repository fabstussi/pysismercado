from models.cargos import Cargos
from dals.cargos import CargosDal
from util.PyNumBR import ler_inteiro
import util.PyUtilTerminal as put


class CargosController:

    @staticmethod
    def valida_entrada_dados(nome: str, privilegio: str) -> bool:
        if (nome == '' or len(nome) <= 3) or \
                (privilegio == '' or len(privilegio) <= 10):
            return False
        return True

    @classmethod
    def buscar(cls, id=None, nome=None, invisiveis=False) -> list:
        cargos = CargosDal()
        if id is not None:
            listas = list(filter(lambda cargo: cargo.id == id,
                                 cargos.listar()))
        elif nome is not None:
            listas = list(filter(lambda cargo: cargo.nome == nome,
                                 cargos.listar()))
        else:
            listas = cargos.listar()
        if not invisiveis:
            listas = list(filter(lambda x: x.visivel == 1, listas))
        return listas

    @classmethod
    def autorizacao(cls, id: int, privilegio_necessario: str) -> bool:
        cargo = cls.buscar(id=id)
        return cargo[0].privilegio == privilegio_necessario

    @classmethod
    def cadastrar(cls, nome, privilegio, visivel=1) -> str:
        if not cls.valida_entrada_dados(nome, privilegio):
            return 'Dados inválidos'
        id = CargosDal.gera_id()
        cargo = Cargos(id, nome, privilegio, visivel)
        if len(cls.buscar(nome=nome)) > 0:
            return 'cargo já cadastrado'
        elif CargosDal.salvar(cargo, 'a'):
            return f'cargo {nome} cadastrado com sucesso!'
        else:
            return 'Erro não foi possível realizar o cadastro'

    @classmethod
    def alterar(cls, id: int, novo_nome: str, novo_privilegio: str, visivel=1,
                tudo=False) -> str:
        if not cls.valida_entrada_dados(novo_nome, novo_privilegio):
            return 'Dados inválidos'
        cargo = cls.buscar(nome=novo_nome, invisiveis=tudo)
        if len(cargo) > 0 and cargo[0].id != id:
            return f'{novo_nome} já cadastrado no ID: {cargo[0].id}'
        cargo = cls.buscar(id=id, invisiveis=tudo)
        if len(cargo) == 0:
            return 'cargo não encontrado'
        cargo[0].nome = novo_nome
        cargo[0].privilegio = novo_privilegio
        cargo[0].visivel = visivel
        for i, cat in enumerate(cls.buscar(invisiveis=True)):
            modo = 'w' if i == 0 else 'a'
            if cargo[0].id != cat.id:
                CargosDal.salvar(cat, modo)
            else:
                if input(f'Confirme a alteração do cargo {cat.nome} ' +
                         '(s/n): ')[0].lower() == 's':
                    CargosDal.salvar(cargo[0], modo)
                    retorno = f'cargo {novo_nome} alterado com sucesso!'
                else:
                    CargosDal.salvar(cat, modo)
                    retorno = 'Operação cancelada'
        return retorno

    @classmethod
    def excluir(cls, id: int) -> str:
        cargo = cls.buscar(id=id)
        if len(cargo) == 0:
            return 'cargo não encontrado'
        return cls.alterar(id, cargo[0].nome, cargo[0].privilegio, 0)

    @classmethod
    def recuperar_apagados(cls) -> str:
        cargos = cls.buscar(invisiveis=True)
        cargos = list(filter(lambda c: c.visivel == 0, cargos))
        lista_ids = [c.id for c in cargos]
        if len(cargos) == 0:
            return 'Não há cargos excluídos'
        while True:
            put.titulo('cargos excluídos:')
            for cargo in cargos:
                print(f'ID: {cargo.id} - cargo: {cargo.nome}')
            put.desenha_linha('=', 30)
            id = ler_inteiro('Digite o ID da cargo a ser restaurado: ')
            if id in lista_ids:
                break
            else:
                print('Opção inválida\n================')
        cargo = cls.buscar(id=id, invisiveis=True)
        return cls.alterar(id, cargo[0].nome,
                           cargo[0].privilegio, 1, tudo=True)
