import util.gerador as gera
import util.PyNumBR as pnb
import util.PyUtilTerminal as put
from scr.controllers.cargos import CargosController
from scr.controllers.categorias import CategoriasController
from scr.controllers.clientes import ClientesController
from scr.controllers.fornecedores import FornecedoresController
from scr.controllers.funcionarios import FuncionariosController
from scr.controllers.produtos import ProdutosController
from scr.controllers.vendas import VendasController


CARGOS = CargosController()
CATEGORIAS = CategoriasController()
CLIENTES = ClientesController()
FORNECEDORES = FornecedoresController()
FUNCIONARIOS = FuncionariosController()
PRODUTOS = ProdutosController()
VENDAS = VendasController()
TITULO_PRINCIPAL = [
    ' ',
    'Sistema de Mercadinhos',
    'v. 1.0',
    ' '
]
MENU_PRINCIPAL = [
    'Administrativo',
    'Operacional',
    'Logout',
    'Sair'
]
MENU_ADMINISTRATIVO = [
    'Gerenciamento',
    'Estoque',
    'Relatórios',
    'Retornar'
]
MENU_OPERACIONAL = [
    'Vendas',
    'Clientes',
    'Consultas',
    'Retornar'
]
MENU_GERENCIAMENTO = [
    'Cargos',
    'Categorias',
    'Clientes',
    'Fornecedores',
    'Funcionários',
    'Produtos',
    'Retornar'
]
MENU_ESTOQUE = [
    'Entradas',
    'Mudanças',
    'Exclusões',
    'Recuperar excluídos',
    'Retornar'
]
MENU_RELATORIOS = [
    'Clientes',
    'Total de produtos vendidos por data',
    'Total geral de produtos vendidos',
    'Retornar'
]
MENU_GERENCIAR_CARGOS = [
    'Incluir novo cargo',
    'Consultar cadastro',
    'Alterar cargo',
    'Excluir cargo',
    'Retornar'
]


