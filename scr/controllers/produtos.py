from models.produtos import Produtos
from dals.produtos import ProdutosDal
from util.PyNumBR import ler_inteiro
import util.PyUtilTerminal as put


class ProdutosController:

    @staticmethod
    def valida_entrada_dados(nome: str, quantidade: int, custo: float,
                             preco: float, descricao: str) -> bool:
        if nome == '' or len(nome) < 3:
            return False
        if quantidade < 1:
            return False
        if custo < 0.01:
            return False
        if preco < custo:
            return False
        if descricao == '' or len(descricao) < 3:
            return False
        return True

    @classmethod
    def buscar(cls, id=None, nome=None, invisiveis=False) -> list:
        produtos = ProdutosDal()
        if id is not None:
            listas = list(filter(lambda produto: produto.id == id,
                                 produtos.listar()))
        elif nome is not None:
            listas = list(filter(lambda produto: produto.nome == nome,
                                 produtos.listar()))
        else:
            listas = produtos.listar()
        if not invisiveis:
            listas = list(filter(lambda x: x.visivel == 1, listas))
        return listas

    @classmethod
    def cadastrar(cls, categoria, fornecedor, nome, quantidade, custo, preco,
                  descricao, visivel=1) -> tuple:
        if not cls.valida_entrada_dados(nome, quantidade, custo, preco,
                                        descricao):
            return -1, 'Dados inválidos'
        id = ProdutosDal.gera_id()
        produto = Produtos(
            id, categoria, fornecedor, nome, quantidade, custo, preco,
            descricao, visivel)
        if len(cls.buscar(nome=nome)) > 0:
            return 1, 'Produto já cadastrado'
        elif ProdutosDal.salvar(produto, 'a'):
            return 0, f'Produto {nome} cadastrado com sucesso!'
        else:
            return -2, 'Erro não foi possível realizar o cadastro'

    @classmethod
    def alterar(cls, id_prod: int, nova_cat: str, novo_fornecedor: str,
                novo_nome: str, nova_quantidade: int, novo_custo: float,
                novo_preco: float, nova_descricao: str, visivel=1, tudo=False
                ) -> tuple:
        if not cls.valida_entrada_dados(novo_nome, nova_quantidade, novo_custo,
                                        novo_preco, nova_descricao):
            return -1, 'Dados inválidos'
        produto = cls.buscar(nome=novo_nome, invisiveis=tudo)
        if len(produto) > 0 and produto[0].id != id_prod:
            return 1, f'{novo_nome} já cadastrado no ID: {produto[0].id}'
        produto = cls.buscar(id=id_prod, invisiveis=tudo)
        if len(produto) == 0:
            return -1, 'Produto não encontrado'
        produto[0].categoria = nova_cat
        produto[0].fornecedor = novo_fornecedor
        produto[0].nome = novo_nome
        produto[0].quantidade = nova_quantidade
        produto[0].custo = novo_custo
        produto[0].preco = novo_preco
        produto[0].descricao = nova_descricao
        produto[0].visivel = visivel
        for i, prod in enumerate(cls.buscar(invisiveis=True)):
            modo = 'w' if i == 0 else 'a'
            if produto[0].id != prod.id:
                ProdutosDal.salvar(prod, modo)
            else:
                if input(f'Confirme a alteração do produto {prod.nome} ' +
                         '(s/n): ')[0].lower() == 's':
                    ProdutosDal.salvar(produto[0], modo)
                    retorno = 0, f'Produto {novo_nome} alterado com sucesso!'
                else:
                    ProdutosDal.salvar(prod, modo)
                    retorno = 0, 'Operação cancelada'
        return retorno

    @classmethod
    def altera_estoque(cls, id: list, modificador: list):
        for i_id, item_id in enumerate(id):
            produto = cls.buscar(id=item_id)
            produto[0].quantidade += modificador[i_id]
            for i, prod in enumerate(cls.buscar(invisiveis=True)):
                modo = 'w' if i == 0 else 'a'
                if produto[0].id != prod.id:
                    ProdutosDal.salvar(prod, modo)
                else:
                    ProdutosDal.salvar(produto[0], modo)

    @classmethod
    def excluir(cls, id: int) -> tuple:
        produto = cls.buscar(id=id)
        if len(produto) == 0:
            return -1, 'Produto não encontrado'
        return cls.alterar(id, produto[0].nome, produto[0].quantidade,
                           produto[0].custo, produto[0].preco,
                           produto[0].descricao, visivel=0)

    @classmethod
    def recuperar_apagadas(cls) -> tuple:
        produtos = cls.buscar(invisiveis=True)
        produtos = list(filter(lambda p: p.visivel == 0, produtos))
        lista_ids = [p.id for p in produtos]
        if len(produtos) == 0:
            return -1, 'Não há produtos excluídos'
        while True:
            put.titulo('produtos excluídos:')
            for produto in produtos:
                print(f'ID: {produto.id} - produto: {produto.nome}'
                      )
            put.desenha_linha('=', 30)
            id = ler_inteiro('Digite o ID do produto a ser restaurado: ')
            if id in lista_ids:
                break
            else:
                print('Opção inválida\n================')
        produto = cls.buscar(id=id, invisiveis=True)
        return cls.alterar(id, produto[0].nome, produto[0].quantidade,
                           produto[0].custo, produto[0].preco,
                           produto[0].descricao, visivel=1, tudo=True)
