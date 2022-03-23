from models.cargos import Cargos
from dals.cargos import CargosDal
from util.PyNumBR import ler_inteiro
import util.PyUtilTerminal as put


class CargosController:

    @staticmethod
    def valida_entrada_dados(nome: str) -> bool:
        if (nome == '' or len(nome) <= 3):
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
    def autorizacao(cls, cargo_fun: str, privilegio_necessario: int) -> bool:
        cargo = cls.buscar(nome=cargo_fun)
        return cargo[0].privilegio <= privilegio_necessario

    @classmethod
    def cadastrar(cls, nome, privilegio, visivel=1) -> tuple:
        if not cls.valida_entrada_dados(nome):
            return -1, 'Dados inválidos'
        id = CargosDal.gera_id()
        cargo = Cargos(id, nome, privilegio, visivel)
        if len(cls.buscar(nome=nome)) > 0:
            return 1, 'Cargo já cadastrado'
        elif CargosDal.salvar(cargo, 'a'):
            return 0, f'Cargo {nome} cadastrado com sucesso'
        else:
            return -2, 'Não foi possível cadastrar o cargo'

    @classmethod
    def alterar(cls, id: int, novo_nome: str, novo_privilegio: str, visivel=1,
                tudo=False) -> tuple:
        if not cls.valida_entrada_dados(novo_nome):
            return -1, 'Dados inválidos'
        cargo = cls.buscar(nome=novo_nome, invisiveis=tudo)
        if len(cargo) > 0 and cargo[0].id != id:
            return 1, f'{novo_nome} já cadastrado no ID: {cargo[0].id}'
        cargo = cls.buscar(id=id, invisiveis=tudo)
        if len(cargo) == 0:
            return -1, 'cargo não encontrado'
        cargo[0].nome = novo_nome
        cargo[0].privilegio = novo_privilegio
        cargo[0].visivel = visivel
        for i, car in enumerate(cls.buscar(invisiveis=True)):
            modo = 'w' if i == 0 else 'a'
            if cargo[0].id != car.id:
                CargosDal.salvar(car, modo)
            else:
                if input(f'Confirme a alteração do cargo {car.nome} ' +
                         '(s/n): ')[0].lower() == 's':
                    CargosDal.salvar(cargo[0], modo)
                    retorno = (0, f'cargo {novo_nome} alterado com sucesso!')
                else:
                    CargosDal.salvar(car, modo)
                    retorno = (0, 'Operação cancelada')
        return retorno

    @classmethod
    def excluir(cls, id: int) -> tuple:
        cargo = cls.buscar(id=id)
        if len(cargo) == 0:
            return -1, 'cargo não encontrado'
        return cls.alterar(id, cargo[0].nome, cargo[0].privilegio, 0)

    @classmethod
    def recuperar_apagados(cls) -> tuple:
        cargos = cls.buscar(invisiveis=True)
        cargos = list(filter(lambda c: c.visivel == 0, cargos))
        lista_ids = [c.id for c in cargos]
        if len(cargos) == 0:
            return -1, 'Não há cargos excluídos'
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
