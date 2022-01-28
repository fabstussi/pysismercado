from models.cargos import Cargos
from dals.cargos import CargosDal


class CargosController:

    @staticmethod
    def valida_entrada_dados(nome: str, descricao: str) -> bool:
        if (nome == '' or len(nome) <= 3) or \
                (descricao == '' or len(descricao) <= 10):
            return False
        return True

    @staticmethod
    def esconde_invisiveis(cargos: list) -> list:
        return list(filter(lambda c: c.visivel == 1, cargos))

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
            listas = cls.esconde_invisiveis(listas)
        return listas

    @classmethod
    def cadastrar(cls, nome, descricao, visivel=1) -> str:
        if not cls.valida_entrada_dados(nome, descricao):
            return 'Dados inválidos'
        id = CargosDal.gera_id()
        cargo = Cargos(id, nome, descricao, visivel)
        if len(cls.buscar(nome=nome)) > 0:
            return 'cargo já cadastrado'
        elif CargosDal.salvar(cargo, 'a'):
            return f'cargo {nome} cadastrado com sucesso!'
        else:
            return 'Erro não foi possível realizar o cadastro'

    @classmethod
    def alterar(cls, id: int, novo_nome: str, nova_descricao: str, visivel=1,
                tudo=False) -> str:
        if not cls.valida_entrada_dados(novo_nome, nova_descricao):
            return 'Dados inválidos'
        cargo = cls.buscar(nome=novo_nome, invisiveis=tudo)
        if len(cargo) > 0 and cargo[0].id != id:
            return f'{novo_nome} já cadastrado no ID: {cargo[0].id}'
        cargo = cls.buscar(id=id, invisiveis=tudo)
        if len(cargo) == 0:
            return 'cargo não encontrado'
        cargo[0].nome = novo_nome if novo_nome != cargo[0].nome else \
            cargo[0].nome
        cargo[0].descricao = nova_descricao if nova_descricao != \
            cargo[0].descricao else cargo[0].descricao
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
        return cls.alterar(id, cargo[0].nome, cargo[0].descricao, 0)

    @classmethod
    def recuperar_apagados(cls) -> str:
        cargos = cls.buscar(invisiveis=True)
        cargos = list(filter(lambda c: c.visivel == 0, cargos))
        lista_ids = [c.id for c in cargos]
        if len(cargos) == 0:
            return 'Não há cargos excluídos'
        while True:
            print('cargos excluídos:')
            for cargo in cargos:
                print(f'ID: {cargo.id} - cargo: {cargo.nome}')
            id = int(input('Digite o ID da cargo que deseja restaurar: '))
            if id in lista_ids:
                break
            else:
                print('Opção inválida\n================')
        cargo = cls.buscar(id=id, invisiveis=True)
        return cls.alterar(id, cargo[0].nome,
                           cargo[0].descricao, 1, tudo=True)


if __name__ == '__main__':
    pass
