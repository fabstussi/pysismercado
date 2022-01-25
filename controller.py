from locale import setlocale, LC_ALL
from datetime import datetime, timedelta
from dao import CategoriasDao, FornecedoresDao, ProdutosDao, ClientesDao, CargosDao, VendedoresDao, VendasDao
from model import Categorias, Fornecerdores, Produtos, Clientes, Cargos, Vendedores, Vendas


setlocale(LC_ALL, 'pt_BR.UTF-8')
MASCARA_DATA = '%d/%m/%Y'
MASCARA_DATA_HORA = '%d/%m/%Y %H:%M:%S'
FUSO = timedelta(hours=-3)


class CatagoriasController:

    @classmethod
    def buscar(cls, id=None, nome=None) -> list:
        categorias = CategoriasDao()
        if id is not None:
            listas = list(filter(lambda x: int(x.id)
                          == id, categorias.listar()))
            if len(listas) > 0:
                return listas
            else:
                return []
        elif nome is not None:
            listas = list(filter(lambda x: x.nome == nome, categorias.listar()
                                 ))
            if len(listas) > 0:
                return listas
            else:
                return []
        else:
            return categorias.listar()

    @classmethod
    def cadastrar(cls, nome: str, descricao: str) -> bool:
        categorias = CategoriasDao()
        listas = cls.buscar(nome=nome)
        if len(listas) > 0:
            return False
        else:
            id = categorias.gera_id()
            if id == -1:
                return False
            resposta = categorias.salvar(Categorias(id, nome,
                                         descricao), 'a')
            return resposta

    @classmethod
    def editar(cls, id: int, novo_nome: str, descricao: str) -> bool:
        categorias = CategoriasDao()
        listas = cls.buscar(id=id)
        if len(listas) > 0:
            listas = cls.buscar()
            for i, categoria in enumerate(listas):
                modo = 'w' if i == 0 else 'a'
                if categoria.id != id:
                    categorias.salvar(categoria, modo)
                else:
                    categorias.salvar(Categorias(id, novo_nome,
                                                 descricao), modo)
            return True
        else:
            return False

    @classmethod
    def excluir(cls, id: int) -> bool:
        categorias = CategoriasDao()
        listas = cls.buscar(id=id)
        if len(listas) > 0:
            listas = cls.buscar()
            for i, categoria in enumerate(listas):
                modo = 'w' if i == 0 else 'a'
                if categoria.id != id:
                    categorias.salvar(categoria, modo)
            return True
        else:
            return False


class FornecedoresController:

    @classmethod
    def buscar(cls, id=None, nome=None) -> list:
        fornecedores = FornecedoresDao()
        if id is not None:
            listas = list(filter(lambda x: int(x.id) == id,
                                 fornecedores.listar()))
            if len(listas) > 0:
                return listas
            else:
                return []
        elif nome is not None:
            listas = list(filter(lambda x: x.nome ==
                          nome, fornecedores.listar()))
            if len(listas) > 0:
                return listas
            else:
                return []
        else:
            return fornecedores.listar()

    @classmethod
    def cadastrar(cls, cnpj: str, nome: str, telefone: str,
                  categoria: str) -> bool:
        fornecedores = FornecedoresDao()
        listas = cls.buscar(nome=nome)
        if len(listas) > 0:
            return False
        else:
            id = fornecedores.gera_id()
            if id == -1:
                return False
            resposta = fornecedores.salvar(Fornecerdores(id, cnpj, nome,
                                                         telefone, categoria),
                                           'a')
            return resposta

    @classmethod
    def editar(cls, id: int, novo_cnpj: str, novo_nome: str,
               novo_telefone: str, nova_categoria: str) -> bool:
        fornecedores = FornecedoresDao()
        listas = cls.buscar(id=id)
        if len(listas) > 0:
            listas = cls.buscar()
            for i, fornecedor in enumerate(listas):
                modo = 'w' if i == 0 else 'a'
                if fornecedor.id != id:
                    fornecedores.salvar(fornecedor, modo)
                else:
                    fornecedores.salvar(Fornecerdores(id, novo_cnpj,
                                                      novo_nome, novo_telefone,
                                                      nova_categoria), modo)
            return True
        else:
            return False

    @classmethod
    def excluir(cls, id: int) -> bool:
        fornecedores = FornecedoresDao()
        listas = cls.buscar(id=id)
        if len(listas) > 0:
            listas = cls.buscar()
            for i, fornecedor in enumerate(listas):
                modo = 'w' if i == 0 else 'a'
                if fornecedor.id != id:
                    fornecedores.salvar(fornecedor, modo)
            return True
        else:
            return False


class ProdutosController:

    @classmethod
    def buscar(cls, id=None, nome=None) -> list:
        produtos = ProdutosDao()
        if id is not None:
            listas = list(filter(lambda x: int(x.id) == id,
                                 produtos.listar()))
            if len(listas) > 0:
                return listas
            else:
                return []
        elif nome is not None:
            listas = list(filter(lambda x: x.nome ==
                          nome, produtos.listar()))
            if len(listas) > 0:
                return listas
            else:
                return []
        else:
            return produtos.listar()

    @classmethod
    def cadastrar(cls, nome: str, descricao: str,
                  categoria: str, fornecedor: str, quantidade: int,
                  preco: float) -> bool:
        produtos = ProdutosDao()
        listas = cls.buscar(nome=nome)
        if len(listas) > 0:
            return False
        else:
            id = produtos.gera_id()
            if id == -1:
                return False
            resposta = produtos.salvar(Produtos(id, nome, descricao,
                                                categoria, fornecedor,
                                                quantidade, preco), 'a')
            return resposta

    @classmethod
    def editar(cls, id: int, novo_nome: str, descricao: str,
               nova_categoria: str, novo_fornecedor: str, nova_quantidade: int,
               novo_preco: float) -> bool:
        produtos = ProdutosDao()
        listas = cls.buscar(id=id)
        if len(listas) > 0:
            listas = cls.buscar()
            for i, produto in enumerate(listas):
                modo = 'w' if i == 0 else 'a'
                if produto.id != id:
                    produtos.salvar(produto, modo)
                else:
                    produtos.salvar(Produtos(id, novo_nome, descricao,
                                             nova_categoria, novo_fornecedor,
                                             nova_quantidade, novo_preco), modo)
            return True
        else:
            return False

    @classmethod
    def excluir(cls, id: int) -> bool:
        produtos = ProdutosDao()
        listas = cls.buscar(id=id)
        if len(listas) > 0:
            listas = cls.buscar()
            for i, produto in enumerate(listas):
                modo = 'w' if i == 0 else 'a'
                if produto.id != id:
                    produtos.salvar(produto, modo)


if __name__ == '__main__':
    pass
