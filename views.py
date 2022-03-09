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
    ' ',
    'Usuário: ',
    'Menu: '
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
    'Recuperar excluídos',
    'Retornar'
]
MENU_GERENCIAR_CATEGORIAS = [
    'Cadastrar nova categoria',
    'Consultar categorias cadastradas',
    'Alterar categoria',
    'Excluir categoria',
    'Recuperar excluídos',
    'Retornar'
]
MENU_GERENCIAR_CLIENTES = [
    'Cadastrar novo cliente',
    'Consultar clientes cadastrados',
    'Alterar dados de clientes',
    'Excluir cliente',
    'Recuperar excluídos',
    'Retornar'
]
MENU_GERENCIAR_FORNECEDORES = [
    'Cadastrar novo fornecedor',
    'Consultar fornecedores cadastrados',
    'Alterar dados de fornecedores',
    'Excluir fornecedor',
    'Recuperar excluídos',
    'Retornar'
]
MENU_GERENCIAR_FUNCIONARIOS = [
    'Cadastrar novo funcionário',
    'Consultar dados dos funcionários',
    'Alterar dados de funcionários',
    'Excluir funcionário',
    'Recuperar excluídos',
    'Retornar'
]
MENU_GERENCIAR_PRODUTOS = [
    'Cadastrar novo produto',
    'Consultar produtos cadastrados',
    'Alterar dados de produtos',
    'Excluir produto',
    'Recuperar excluídos',
    'Retornar'
]


def cabecalho() -> None:
    put.limpa_tela()
    put.titulo_ml(TITULO_PRINCIPAL, 'c')


def criar_usuario_inicial() -> bool:
    import os
    TITULO_PRINCIPAL[5] = 'Criar usuário inicial'
    cabecalho()
    local_arquivos = os.path.dirname(os.path.abspath(__file__))
    arquivo_cargos = f'{local_arquivos}/db/cargos.dbpy'
    arquivo_funcionarios = f'{local_arquivos}/db/funcionarios.dbpy'
    if not os.path.exists(arquivo_cargos):
        resposta = CARGOS.cadastrar('Administrador', 0)
        put.titulo(resposta[1])
        if resposta[0] == -2:
            exit(1)
        elif resposta[0] != 0:
            return False
    if not os.path.exists(arquivo_funcionarios):
        put.titulo('Cadastro do Administrador do Sistema')
        cpf = gera.gerar_cpf(mascara=True)
        nome = input('Nome: ').upper()
        telefone = gera.gerar_telefone(celular=True, mascara=True)
        sexo = input('Sexo: ')[0].upper()
        nasc = pnb.ler_inteiro('Ano de nascimento: ')
        cargo = CARGOS.buscar(id=1)[0].nome
        resposta = FUNCIONARIOS.cadastrar(
            cpf,
            nome,
            telefone,
            sexo,
            nasc,
            cargo
        )
        put.titulo(resposta[1])
        if resposta[0] == -2:
            exit(1)
        elif resposta[0] != 0:
            return False
        else:
            put.titulo_ml(
                [
                    'Usuário administrador configurado com sucesso!',
                    'Utilize o "ID 1" para entrar no sistema.'
                ],
                'e'
            )
    return True


def login():
    TITULO_PRINCIPAL[5] = 'Login'
    cabecalho()
    put.titulo('Identifique-se com o número de identificação')
    id = pnb.ler_inteiro('ID: ')
    if len(FUNCIONARIOS.buscar(id=id)) == 0:
        put.titulo('ID não encontrado!')
        input('Pressione ENTER para continuar...')
        return login()
    else:
        return FUNCIONARIOS.buscar(id=id)[0]


def view_menu_administrativo(id_funcionario: int) -> None:
    if CARGOS.autorizacao(id_funcionario, 0) or \
            CARGOS.autorizacao(id_funcionario, 1):
        while True:
            TITULO_PRINCIPAL[5] = 'MENU: Principal -> Administrativo'
            cabecalho()
            put.cria_menu(MENU_ADMINISTRATIVO)
            opcao = pnb.ler_inteiro('Escolha uma opção: ')
            if opcao == 1:
                view_menu_gerenciamento()
            elif opcao == 1:
                pass
            elif opcao == 1:
                pass
            elif opcao == 4:
                break
    else:
        put.titulo('Acesso negado, privilégio insuficiente!')


def view_menu_gerenciamento() -> None:
    while True:
        TITULO_PRINCIPAL[5] = 'MENU: Principal -> Administrativo -> ' + \
            'Gerenciamento'
        cabecalho()
        put.cria_menu(MENU_GERENCIAMENTO)
        opcao = pnb.ler_inteiro('Escolha uma opção: ')
        if opcao == 1:
            view_menu_gerenciar_cargos()
        elif opcao == 2:
            view_menu_gerenciar_categorias()
        elif opcao == 3:
            view_menu_gerenciar_clientes()
        elif opcao == 4:
            pass
        elif opcao == 5:
            pass
        elif opcao == 6:
            pass
        elif opcao == 7:
            break


def view_menu_gerenciar_cargos() -> None:
    while True:
        TITULO_PRINCIPAL[5] = 'MENU: Principal -> Administrativo -> ' + \
            'Gerenciar -> Cargos'
        legenda_permissoes = {
            0: 'Administrador',
            1: 'Gerente',
            2: 'Vendedor'
        }
        cabecalho()
        put.cria_menu(MENU_GERENCIAR_CARGOS)
        opcao = pnb.ler_inteiro('Escolha uma opção: ')
        if opcao == 1:
            TITULO_PRINCIPAL[5] = 'Cadastrar novo cargo'
            cabecalho()
            nome = input('Nome: ').capitalize()
            put.cria_menu(
                [
                    'Administrador',
                    'Gerente',
                    'Vendedor'
                ]
            )
            privilegio = pnb.ler_inteiro('Escolha uma opção: ') - 1
            resposta = CARGOS.cadastrar(nome, privilegio)
            put.titulo(resposta[1])
            if resposta[0] != 0:
                if input('Deseja tentar novamente? (S/N) ').upper() == 'S':
                    continue
                else:
                    break
            input('Pressione ENTER para continuar...')
        elif opcao == 2:
            TITULO_PRINCIPAL[5] = 'Consultar por...'
            cabecalho()
            put.cria_menu(
                [
                    'ID',
                    'Nome',
                    'Exibir todos',
                    'Voltar'
                ]
            )
            opcao = pnb.ler_inteiro('Escolha uma opção: ')
            if opcao == 1:
                TITULO_PRINCIPAL[5] = 'Consultar por ID'
                cabecalho()
                id_cargo = pnb.ler_inteiro('ID: ')
                cargo = CARGOS.buscar(id=id_cargo)
                if len(cargo) == 0:
                    put.titulo('ID não encontrado!')
                    input('Pressione ENTER para continuar...')
                    continue
                put.titulo_ml(
                    [
                        f'ID: {cargo[0].id}',
                        f'Nome: {cargo[0].nome}',
                        f'Privilégio: {legenda_permissoes[cargo[0].privilegio]}'
                    ]
                )
                input('Pressione ENTER para continuar...')
            elif opcao == 2:
                TITULO_PRINCIPAL[5] = 'Consultar por nome'
                cabecalho()
                nome = input('Nome: ').capitalize()
                cargo = CARGOS.buscar(nome=nome)
                if len(cargo) == 0:
                    put.titulo('Nome não encontrado!')
                    input('Pressione ENTER para continuar...')
                    continue
                put.titulo_ml(
                    [
                        f'ID: {cargo[0].id}',
                        f'Nome: {cargo[0].nome}',
                        f'Privilégio: {legenda_permissoes[cargo[0].privilegio]}'
                    ]
                )
                input('Pressione ENTER para continuar...')
            elif opcao == 3:
                TITULO_PRINCIPAL[5] = 'Consultar todos'
                cabecalho()
                if len(CARGOS.buscar()) == 0:
                    put.titulo('Nenhum cargo cadastrado!')
                    input('Pressione ENTER para continuar...')
                    continue
                for cargo in CARGOS.buscar():
                    put.titulo_ml(
                        [
                            f'ID: {cargo.id}',
                            f'Nome: {cargo.nome}',
                            f'Privilégio: {legenda_permissoes[cargo.privilegio]}'
                        ]
                    )
                input('Pressione ENTER para continuar...')
            elif opcao == 4:
                break
        elif opcao == 3:
            TITULO_PRINCIPAL[5] = 'Alterações de dados'
            cabecalho()
            id_cargo = pnb.ler_inteiro('ID: ')
            cargo = CARGOS.buscar(id=id_cargo)
            if len(cargo) == 0:
                put.titulo('ID não encontrado!')
                input('Pressione ENTER para continuar...')
                continue
            put.cria_menu(
                [
                    'Nome',
                    'Privilegio'
                ]
            )
            opc = pnb.ler_inteiro('O que deseja alterar?: ')
            if opc == 1:
                nome = input('Novo nome: ').capitalize()
                resposta = CARGOS.alterar(id_cargo, nome, cargo[0].privilegio)
            elif opc == 2:
                put.cria_menu(
                    [
                        'Administrador',
                        'Gerente',
                        'Vendedor'
                    ]
                )
                privilegio = pnb.ler_inteiro('Novo privilegio: ') - 1
                resposta = CARGOS.alterar(id_cargo, cargo[0].nome, privilegio)
            put.titulo(resposta[1])
            if resposta[0] != 0:
                if input('Deseja tentar novamente? (S/N) ').upper() == 'S':
                    continue
                else:
                    break
            input('Pressione ENTER para continuar...')
        elif opcao == 4:
            TITULO_PRINCIPAL[5] = 'Exclusão de cargo'
            cabecalho()
            id_cargo = pnb.ler_inteiro('ID: ')
            cargo = CARGOS.buscar(id=id_cargo)
            if len(cargo) == 0:
                put.titulo('ID não encontrado!')
                input('Pressione ENTER para continuar...')
                continue
            put.titulo_ml(
                [
                    f'ID: {cargo[0].id}',
                    f'Nome: {cargo[0].nome}',
                    f'Permissão: {legenda_permissoes[cargo[0].privilegio]}'
                ]
            )
            if input('Confirma a exclusão do cargo? (S/N) ').upper() == 'S':
                resposta = CARGOS.excluir(id_cargo)
                put.titulo(resposta[1])
                if resposta[0] != 0:
                    if input('Deseja tentar novamente? (S/N) ').upper() == 'S':
                        continue
                    else:
                        break
                put.titulo('Exclusão realizada com sucesso!')
            input('Pressione ENTER para continuar...')
        elif opcao == 5:
            resposta = CARGOS.recuperar_apagados()
            put.titulo(resposta[1])
            if resposta[0] != 0:
                if input('Deseja tentar novamente? (S/N) ').upper() == 'S':
                    continue
                else:
                    break
            input('Pressione ENTER para continuar...')
        elif opcao == 6:
            break


def view_menu_gerenciar_categorias():
    while True:
        TITULO_PRINCIPAL[5] = 'MENU: Principal -> Administrativo -> ' + \
            'Gerenciar -> Categorias'
        cabecalho()
        put.cria_menu(MENU_GERENCIAR_CATEGORIAS)
        opcao = pnb.ler_inteiro('O que deseja fazer?: ')
        if opcao == 1:
            TITULO_PRINCIPAL[5] = 'Cadastrar nova categoria'
            cabecalho()
            nome = input('Nome: ').upper()
            descricao = input('Descrição: ').upper()
            resposta = CATEGORIAS.cadastrar(nome, descricao)
            put.titulo(resposta[1])
            if resposta[0] != 0:
                if input('Deseja tentar novamente? (S/N) ').upper() == 'S':
                    continue
                else:
                    break
            input('Pressione ENTER para continuar...')
        elif opcao == 2:
            TITULO_PRINCIPAL[5] = 'Consultar por...'
            cabecalho()
            put.cria_menu(
                [
                    'ID',
                    'Nome',
                    'Exibir todos',
                    'Voltar'
                ]
            )
            opc = pnb.ler_inteiro('Escolha o tipo de consulta: ')
            if opc == 1:
                TITULO_PRINCIPAL[5] = 'Consultar por ID'
                cabecalho()
                id_categoria = pnb.ler_inteiro('ID: ')
                categoria = CATEGORIAS.buscar(id=id_categoria)
                if len(categoria) == 0:
                    put.titulo('ID não encontrado!')
                    input('Pressione ENTER para continuar...')
                    continue
                put.titulo_ml(
                    [
                        f'ID: {categoria[0].id}',
                        f'Nome: {categoria[0].nome}',
                        f'Descrição: {categoria[0].descricao}'
                    ]
                )
                input('Pressione ENTER para continuar...')
            elif opc == 2:
                TITULO_PRINCIPAL[5] = 'Consultar por nome'
                cabecalho()
                nome = input('Nome: ').upper()
                categoria = CATEGORIAS.buscar(nome=nome)
                if len(categoria) == 0:
                    put.titulo('Nome não encontrado!')
                    input('Pressione ENTER para continuar...')
                    continue
                put.titulo_ml(
                    [
                        f'ID: {categoria[0].id}',
                        f'Nome: {categoria[0].nome}',
                        f'Descrição: {categoria[0].descricao}'
                    ]
                )
                input('Pressione ENTER para continuar...')
            elif opc == 3:
                TITULO_PRINCIPAL[5] = 'Exibe todas as categorias'
                cabecalho()
                categorias = CATEGORIAS.buscar()
                if len(categorias) == 0:
                    put.titulo('Nenhuma categoria cadastrada!')
                    input('Pressione ENTER para continuar...')
                    continue
                for categoria in categorias:
                    put.titulo_ml(
                        [
                            f'ID: {categoria.id}',
                            f'Nome: {categoria.nome}',
                            f'Descrição: {categoria.descricao}'
                        ]
                    )
                input('Pressione ENTER para continuar...')
            elif opc == 4:
                break
        elif opcao == 3:
            TITULO_PRINCIPAL[5] = 'Alterar categoria'
            cabecalho()
            id_categoria = pnb.ler_inteiro('ID: ')
            categoria = CATEGORIAS.buscar(id=id_categoria)
            if len(categoria) == 0:
                put.titulo('ID não encontrado!')
                input('Pressione ENTER para continuar...')
                continue
            put.titulo_ml(
                [
                    f'ID: {categoria[0].id}',
                    f'Nome: {categoria[0].nome}',
                    f'Descrição: {categoria[0].descricao}'
                ]
            )
            put.cria_menu(
                [
                    'Nome',
                    'Descrição'
                ]
            )
            opc = pnb.ler_inteiro('O que deseja alterar?: ')
            TITULO_PRINCIPAL[5] = 'Alterar nome' if opc == 1 \
                else 'Alterar descrição'
            nome = input('Nome: ').upper(
            ) if opc == 1 else categoria[0].nome
            descricao = input('Descrição: ').upper(
            ) if opc == 2 else categoria[0].descricao
            resposta = CATEGORIAS.alterar(id_categoria, nome, descricao)
            put.titulo(resposta[1])
            if resposta[0] != 0:
                if input('Deseja tentar novamente? (S/N) ').upper() == 'S':
                    continue
                else:
                    break
            input('Pressione ENTER para continuar...')
        elif opcao == 4:
            TITULO_PRINCIPAL[5] = 'Excluir categoria'
            cabecalho()
            id_categoria = pnb.ler_inteiro('ID: ')
            categoria = CATEGORIAS.buscar(id=id_categoria)
            if len(categoria) == 0:
                put.titulo('ID não encontrado!')
                input('Pressione ENTER para continuar...')
                continue
            put.titulo_ml(
                [
                    f'ID: {categoria[0].id}',
                    f'Nome: {categoria[0].nome}',
                    f'Descrição: {categoria[0].descricao}'
                ]
            )
            resposta = CATEGORIAS.excluir(id_categoria)
            put.titulo(resposta[1])
            if resposta[0] != 0:
                if input('Deseja tentar novamente? (S/N) ').upper() == 'S':
                    continue
                else:
                    break
            input('Pressione ENTER para continuar...')
        elif opcao == 5:
            TITULO_PRINCIPAL[5] = 'Recupara excluído'
            cabecalho()
            resposta = CATEGORIAS.recuperar_apagadas()
            put.titulo(resposta[1])
            if resposta[0] != 0:
                if input('Deseja tentar novamente? (S/N) ').upper() == 'S':
                    continue
                else:
                    break
            input('Pressione ENTER para continuar...')
        elif opcao == 6:
            break


def view_menu_gerenciar_clientes():
    while True:
        TITULO_PRINCIPAL[5] = 'MENU: Principal -> Administrativo -> ' + \
            'Gerenciar -> Clientes'
        cabecalho()
        put.cria_menu(MENU_GERENCIAR_CLIENTES)
        opcao = pnb.ler_inteiro('O que deseja fazer?: ')
        if opcao == 1:
            TITULO_PRINCIPAL[5] = 'Cadastrar novo cliente'
            cabecalho()
            cpf = gera.gerar_cpf()
            nome = input('Nome: ').upper()
            telefone = gera.gerar_telefone(ddd=True, celular=True)
            sexo = input('Sexo: ')[0].upper()
            ano = pnb.ler_inteiro('Ano de nascimento: ')
            resposta = CLIENTES.cadastrar(cpf, nome, telefone, sexo, ano)
            put.titulo(resposta[1])
            if resposta[0] != 0:
                if input('Deseja tentar novamente? (S/N) ').upper() == 'S':
                    continue
                else:
                    break
            input('Pressione ENTER para continuar...')
        elif opcao == 2:
            TITULO_PRINCIPAL[5] = 'Consultar clientes cadastrados'
            cabecalho()
            put.cria_menu(
                [
                    'ID',
                    'Nome',
                    'Exibir todos'
                ]
            )
            opc = pnb.ler_inteiro('Qual a consulta: ')
            if opc == 1:
                TITULO_PRINCIPAL[5] = 'Consultar cliente por ID'
                cabecalho()
                id_cliente = pnb.ler_inteiro('ID: ')
                cliente = CLIENTES.buscar(id=id_cliente)
                if len(cliente) == 0:
                    put.titulo('ID não encontrado!')
                    input('Pressione ENTER para continuar...')
                    continue
                put.titulo_ml(
                    [
                        f'ID: {cliente[0].id}',
                        f'Nome: {cliente[0].nome}',
                        f'CPF: {cliente[0].cpf}',
                        f'Telefone: {cliente[0].telefone}',
                        f'Sexo: {cliente[0].sexo}',
                        f'Idade: {int(pnb.pega_data()[6:]) - cliente[0].ano_nasc} anos'
                    ]
                )
                input('Pressione ENTER para continuar...')
            elif opc == 2:
                TITULO_PRINCIPAL[5] = 'Consultar cliente por nome'
                cabecalho()
                nome = input('Nome: ').upper()
                cliente = CLIENTES.buscar(nome=nome)
                if len(cliente) == 0:
                    put.titulo('Nome não encontrado!')
                    input('Pressione ENTER para continuar...')
                    continue
                put.titulo_ml(
                    [
                        f'ID: {cliente[0].id}',
                        f'Nome: {cliente[0].nome}',
                        f'CPF: {cliente[0].cpf}',
                        f'Telefone: {cliente[0].telefone}',
                        f'Sexo: {cliente[0].sexo}',
                        f'Idade: {int(pnb.pega_data()[6:]) - cliente[0].ano_nasc} anos'
                    ]
                )
                if input('Deseja consultar outro cliente? (S/N) ').upper() == 'S':
                    continue
                else:
                    break
            elif opc == 3:
                TITULO_PRINCIPAL[5] = 'Exibir todos os clientes'
                cabecalho()
                clientes = CLIENTES.buscar()
                if len(clientes) == 0:
                    put.titulo('Não há clientes cadastrados!')
                    input('Pressione ENTER para continuar...')
                    continue
                for cliente in clientes:
                    put.titulo_ml(
                        [
                            f'ID: {cliente.id}',
                            f'Nome: {cliente.nome}',
                            f'CPF: {cliente.cpf}',
                            f'Telefone: {cliente.telefone}',
                            f'Sexo: {cliente.sexo}',
                            f'Idade: {int(pnb.pega_data()[6:]) - cliente.ano_nasc} anos'
                        ]
                    )
                input('Pressione ENTER para continuar...')
        elif opcao == 3:
            TITULO_PRINCIPAL[5] = 'Alterar dados de um cliente'
            cabecalho()
            id_cliente = pnb.ler_inteiro('ID do cliente: ')
            cliente = CLIENTES.buscar(id=id_cliente)
            if len(cliente) == 0:
                put.titulo('ID não encontrado!')
                input('Pressione ENTER para continuar...')
                continue
            put.titulo_ml(
                [
                    f'ID: {cliente[0].id}',
                    f'CPF: {cliente[0].cpf}',
                    f'Nome: {cliente[0].nome}',
                    f'Telefone: {cliente[0].telefone}',
                    f'Sexo: {cliente[0].sexo}',
                    f'Idade: {int(pnb.pega_data()[6:]) - cliente[0].ano_nasc} anos'
                ]
            )
            put.cria_menu(
                [
                    'Nome',
                    'Telefone',
                    'Sexo',
                    'Ano de nascimento',
                ]
            )
            opc = pnb.ler_inteiro('O que deseja alterar? ')
            nome = input('Nome: ').upper(
            ) if opc == 1 else cliente[0].nome
            telefone = input('Telefone: ') if opc == 2 else cliente[0].telefone
            sexo = input('Sexo: ')[0].upper() if opc == 3 else cliente[0].sexo
            ano = pnb.ler_inteiro(
                'Ano de nascimento: ') if opc == 4 else cliente[0].ano_nasc
            resposta = CLIENTES.alterar(
                id_cliente,
                cliente[0].cpf,
                nome,
                telefone,
                sexo,
                ano
            )
            put.titulo(resposta[1])
            if resposta[0] != 0:
                if input('Deseja tentar novamente? (S/N) ').upper() == 'S':
                    continue
                else:
                    break
            input('Pressione ENTER para continuar...')
        elif opcao == 4:
            TITULO_PRINCIPAL[5] = 'Excluir cliente'
            cabecalho()
            id_cliente = pnb.ler_inteiro('ID do cliente: ')
            cliente = CLIENTES.buscar(id=id_cliente)
            if len(cliente) == 0:
                put.titulo('ID não encontrado!')
                input('Pressione ENTER para continuar...')
                continue
            put.titulo_ml(
                [
                    f'ID: {cliente[0].id}',
                    f'CPF: {cliente[0].cpf}',
                    f'Nome: {cliente[0].nome}',
                    f'Telefone: {cliente[0].telefone}',
                    f'Sexo: {cliente[0].sexo}',
                    f'Idade: {int(pnb.pega_data()[6:]) - cliente[0].ano_nasc}'
                ]
            )
            resposta = CLIENTES.excluir(id_cliente)
            put.titulo(resposta[1])
            if resposta[0] != 0:
                if input('Deseja tentar novamente? (S/N) ').upper() == 'S':
                    continue
                else:
                    break
            input('Pressione ENTER para continuar...')
        elif opcao == 5:
            TITULO_PRINCIPAL[5] = 'Recuperar excluidos'
            cabecalho()
            resposta = CLIENTES.recuperar_apagadas()
            put.titulo(resposta[1])
            if resposta[0] != 0:
                if input('Deseja tentar novamente? (S/N) ').upper() == 'S':
                    continue
                else:
                    break
            input('Pressione ENTER para continuar...')
        elif opcao == 6:
            break


def view_menu_operacional() -> None:
    while True:
        TITULO_PRINCIPAL[5] = 'MENU: Principal -> Operacional'
        cabecalho()
        put.cria_menu(MENU_OPERACIONAL)
        opcao = pnb.ler_inteiro('Escolha uma opção: ')
        if opcao == 1:
            pass
        if opcao == 2:
            pass
        if opcao == 3:
            pass
        if opcao == 4:
            break


if not criar_usuario_inicial():
    print('Erro inesperado no sistema, por favor, tente novamente.')
    exit(1)

funcionario_atual = login()

TITULO_PRINCIPAL[4] = f'Usurário: {funcionario_atual.nome}'

while True:
    TITULO_PRINCIPAL[5] = 'MENU: Principal'
    cabecalho()
    put.cria_menu(MENU_PRINCIPAL)
    opcao = pnb.ler_inteiro('Escolha uma opção: ')
    if opcao == 1:
        view_menu_administrativo(funcionario_atual.id)
    if opcao == 2:
        view_menu_operacional()
    if opcao == 3:
        funcionario_atual = login()
    if opcao == 4:
        if input('Deseja realmente sair? (s/n) ').upper() == 'S':
            break

put.titulo('Execução finalizada')
