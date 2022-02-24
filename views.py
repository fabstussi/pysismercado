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


def configuracoes_iniciais():
    print('Aguarde verificando configurações...')
    existem_cargos = CARGOS.buscar()
    if len(existem_cargos) == 0:
        resposta = CARGOS.cadastrar('Administrador', 'Admin')
    existem_funcionarios = FUNCIONARIOS.buscar()
    if len(existem_funcionarios) == 0:
        print('Base de dados de funcionários vazia!')
        print('Necessário cadastrar funcionários para continuar!')
        put.titulo('Cadastro de funcionários')
        cpf = gera.gerar_cpf()
        nome = input('Nome: ').capitalize()
        telefone = gera.gerar_telefone(celular=True)
        sexo = input('Sexo: ')[0].capitalize()
        ano = pnb.ler_inteiro('Ano de nascimento: ')
        cargo = CARGOS.buscar(1)
        cargo = cargo[0].nome
        resposta = FUNCIONARIOS.cadastrar(cpf, nome, telefone, sexo, ano, cargo
                                          )
        print(resposta)
        input('Pressione ENTER para continuar...')
        if resposta == 'Erro não foi possível realizar o cadastro':
            return False
    return True


if not configuracoes_iniciais():
    print('Não foi possível realizar a configuração inicial!')
    print('Tentar novamente!')
    exit()

put.limpa_tela()

put.titulo_ml(TITULO_PRINCIPAL, 'c')
