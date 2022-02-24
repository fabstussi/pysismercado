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
        print('Inicie o sistema com o ID "1"')
        input('Pressione ENTER para continuar...')
        if resposta == 'Erro não foi possível realizar o cadastro':
            return False
    return True


def login_sistema():
    while True:
        put.titulo('Por favor identifique-se')
        id_funcionario = pnb.ler_inteiro('ID: ')
        if len(FUNCIONARIOS.buscar(id_funcionario)) == 0:
            put.titulo('ID inválido!')
            continue
        else:
            funcionario_atual = FUNCIONARIOS.buscar(id_funcionario)
            put.titulo('Bem vindo(a) ' + funcionario_atual[0].nome)
            input('Pressione ENTER para começar...')
            break


if not configuracoes_iniciais():
    print('Não foi possível realizar a configuração inicial!')
    print('Tentar novamente!')
    exit()

put.limpa_tela()

put.titulo_ml(TITULO_PRINCIPAL, 'c')
login_sistema()


while True:
    put.limpa_tela()
    TITULO_PRINCIPAL[3] = 'Menu Principal'
    put.titulo_ml(TITULO_PRINCIPAL, 'c')
    put.cria_menu(MENU_PRINCIPAL)
    op_menu_p = pnb.ler_inteiro('Opção: ')
    if op_menu_p == 1:
        while True:
            put.limpa_tela()
            TITULO_PRINCIPAL[3] = 'Menu Principal > Administrativo'
            put.titulo_ml(TITULO_PRINCIPAL, 'c')
            put.cria_menu(MENU_ADMINISTRATIVO)
            op_menu_p_a = pnb.ler_inteiro('Opção: ')
            if op_menu_p_a == 1:
                TITULO_PRINCIPAL[3] = 'Menu Principal > Administrativo > Gerenciamento'
                put.limpa_tela()
                put.titulo_ml(TITULO_PRINCIPAL, 'c')
                while True:
                    put.cria_menu(MENU_GERENCIAMENTO)
                    op_menu_p_a_g = pnb.ler_inteiro('Opção: ')
                    if op_menu_p_a_g == 1:
                        pass
                    if op_menu_p_a_g == 2:
                        pass
                    if op_menu_p_a_g == 3:
                        pass
                    if op_menu_p_a_g == 4:
                        pass
                    if op_menu_p_a_g == 5:
                        pass
                    if op_menu_p_a_g == 6:
                        pass
                    if op_menu_p_a_g == 7:
                        put.limpa_tela()
                        put.titulo_ml(TITULO_PRINCIPAL, 'c')
                        break
            if op_menu_p_a == 1:
                put.limpa_tela()
                put.titulo_ml(TITULO_PRINCIPAL, 'c')
            if op_menu_p_a == 1:
                put.limpa_tela()
                put.titulo_ml(TITULO_PRINCIPAL, 'c')
            if op_menu_p_a == 4:
                put.limpa_tela()
                put.titulo_ml(TITULO_PRINCIPAL, 'c')
                break
    if op_menu_p == 2:
        while True:
            put.limpa_tela()
            TITULO_PRINCIPAL[3] = 'Menu Principal > Operacional'
            put.titulo_ml(TITULO_PRINCIPAL, 'c')
            put.cria_menu(MENU_OPERACIONAL)
            op_menu_p_o = pnb.ler_inteiro('Opção: ')
            if op_menu_p_o == 1:
                put.limpa_tela()
                put.titulo_ml(TITULO_PRINCIPAL, 'c')
            if op_menu_p_o == 2:
                put.limpa_tela()
                put.titulo_ml(TITULO_PRINCIPAL, 'c')
            if op_menu_p_o == 3:
                put.limpa_tela()
                put.titulo_ml(TITULO_PRINCIPAL, 'c')
            if op_menu_p_o == 4:
                put.limpa_tela()
                put.titulo_ml(TITULO_PRINCIPAL, 'c')
                break
    if op_menu_p == 3:
        put.limpa_tela()
        put.titulo_ml(TITULO_PRINCIPAL, 'c')
        login_sistema()
    if op_menu_p == 4:
        break
put.titulo('Sistema encerrado!')
