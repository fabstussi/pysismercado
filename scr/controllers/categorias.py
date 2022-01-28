from models.categorias import Categorias
from dals.categorias import CategoriasDal


class CategoriasController:

    @staticmethod
    def valida_entrada_dados(nome: str, descricao: str) -> bool:
        if (nome == '' or len(nome) <= 3) or \
                (descricao == '' or len(descricao) <= 10):
            return False
        return True

    @staticmethod
    def esconde_invisiveis(categorias: list) -> list:
        return list(filter(lambda c: c.visivel == 1, categorias))

    @classmethod
    def buscar(cls, id=None, nome=None, invisiveis=False) -> list:
        categorias = CategoriasDal()
        if id is not None:
            listas = list(filter(lambda categoria: categoria.id == id,
                                 categorias.listar()))
        elif nome is not None:
            listas = list(filter(lambda categoria: categoria.nome == nome,
                                 categorias.listar()))
        else:
            listas = categorias.listar()
        if not invisiveis:
            listas = cls.esconde_invisiveis(listas)
        return listas

    @classmethod
    def cadastrar(cls, nome, descricao, visivel=1) -> str:
        if not cls.valida_entrada_dados(nome, descricao):
            return 'Dados inválidos'
        id = CategoriasDal.gera_id()
        categoria = Categorias(id, nome, descricao, visivel)
        if len(cls.buscar(nome=nome)) > 0:
            return 'Categoria já cadastrada'
        elif CategoriasDal.salvar(categoria, 'a'):
            return f'Categoria {nome} cadastrada com sucesso!'
        else:
            return 'Erro não foi possível realizar o cadastro'

    @classmethod
    def alterar(cls, id: int, novo_nome: str, nova_descricao: str, visivel=1,
                tudo=False) -> str:
        if not cls.valida_entrada_dados(novo_nome, nova_descricao):
            return 'Dados inválidos'
        categoria = cls.buscar(nome=novo_nome, invisiveis=tudo)
        if len(categoria) > 0 and categoria[0].id != id:
            return f'{novo_nome} já cadastrada no ID: {categoria[0].id}'
        categoria = cls.buscar(id=id, invisiveis=tudo)
        if len(categoria) == 0:
            return 'Categoria não encontrada'
        categoria[0].nome = novo_nome if novo_nome != categoria[0].nome else \
            categoria[0].nome
        categoria[0].descricao = nova_descricao if nova_descricao != \
            categoria[0].descricao else categoria[0].descricao
        categoria[0].visivel = visivel
        for i, cat in enumerate(cls.buscar(invisiveis=True)):
            modo = 'w' if i == 0 else 'a'
            if categoria[0].id != cat.id:
                CategoriasDal.salvar(cat, modo)
            else:
                if input(f'Confirme a alteração da categoria {cat.nome} ' +
                         '(s/n): ')[0].lower() == 's':
                    CategoriasDal.salvar(categoria[0], modo)
                    retorno = f'Categoria {novo_nome} alterada com sucesso!'
                else:
                    CategoriasDal.salvar(cat, modo)
                    retorno = 'Operação cancelada'
        return retorno

    @classmethod
    def excluir(cls, id: int) -> str:
        categoria = cls.buscar(id=id)
        if len(categoria) == 0:
            return 'Categoria não encontrada'
        return cls.alterar(id, categoria[0].nome, categoria[0].descricao, 0)

    @classmethod
    def desapagar(cls) -> str:
        categorias = cls.buscar(invisiveis=True)
        categorias = list(filter(lambda c: c.visivel == 0, categorias))
        lista_ids = [c.id for c in categorias]
        if len(categorias) == 0:
            return 'Não há categorias excluídas'
        while True:
            print('Categorias excluídas:')
            for categoria in categorias:
                print(f'ID: {categoria.id} - Categoria: {categoria.nome}')
            id = int(input('Digite o ID da categoria que deseja restaurar: '))
            if id in lista_ids:
                break
            else:
                print('Opção inválida\n================')
        categoria = cls.buscar(id=id, invisiveis=True)
        return cls.alterar(id, categoria[0].nome,
                           categoria[0].descricao, 1, tudo=True)


if __name__ == '__main__':
    pass
