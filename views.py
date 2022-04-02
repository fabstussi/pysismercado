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
    'Entradas de produtos',
    'Mudanças de valores',
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


def view_menu_administrativo() -> None:
    while True:
        TITULO_PRINCIPAL[5] = 'MENU: Principal -> Administrativo'
        cabecalho()
        put.cria_menu(MENU_ADMINISTRATIVO)
        opcao = pnb.ler_inteiro('Escolha uma opção: ')
        if opcao == 1:
            view_menu_gerenciamento()
        elif opcao == 2:
            view_menu_estoque()
        elif opcao == 3:
            pass
        elif opcao == 4:
            break


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
            viwe_menu_gerenciar_fornecedores()
        elif opcao == 5:
            view_menu_gerenciar_funcionarios()
        elif opcao == 6:
            view_menu_gerenciar_produtos()
        elif opcao == 7:
            break


def view_menu_gerenciar_cargos() -> None:
    while True:
        TITULO_PRINCIPAL[5] = 'MENU: Principal -> Administrativo -> ' + \
            'Gerenciar -> Cargos'
        leg_permissoes = {
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
                        f'Privilégio: {leg_permissoes[cargo[0].privilegio]}'
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
                        f'Privilégio: {leg_permissoes[cargo[0].privilegio]}'
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
                            f'Privilégio: {leg_permissoes[cargo.privilegio]}'
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
                    f'Permissão: {leg_permissoes[cargo[0].privilegio]}'
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


def view_menu_gerenciar_categorias() -> None:
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


def view_menu_gerenciar_clientes() -> None:
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
                    'Exibir todos',
                    'Voltar'
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
                idade = int(pnb.pega_data()[6:]) - cliente[0].ano_nasc
                put.titulo_ml(
                    [
                        f'ID: {cliente[0].id}',
                        f'Nome: {cliente[0].nome}',
                        f'CPF: {cliente[0].cpf}',
                        f'Telefone: {cliente[0].telefone}',
                        f'Sexo: {cliente[0].sexo}',
                        f'Idade: {idade} anos'
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
                idade = int(pnb.pega_data()[6:]) - cliente[0].ano_nasc
                put.titulo_ml(
                    [
                        f'ID: {cliente[0].id}',
                        f'Nome: {cliente[0].nome}',
                        f'CPF: {cliente[0].cpf}',
                        f'Telefone: {cliente[0].telefone}',
                        f'Sexo: {cliente[0].sexo}',
                        f'Idade: {idade} anos'
                    ]
                )
                if input('Deseja consultar outro cliente? (S/N) ').upper(
                ) == 'S':
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
                    idade = int(pnb.pega_data()[6:]) - cliente.ano_nasc
                    put.titulo_ml(
                        [
                            f'ID: {cliente.id}',
                            f'Nome: {cliente.nome}',
                            f'CPF: {cliente.cpf}',
                            f'Telefone: {cliente.telefone}',
                            f'Sexo: {cliente.sexo}',
                            f'Idade: {idade} anos'
                        ]
                    )
                input('Pressione ENTER para continuar...')
            elif opc == 4:
                break
        elif opcao == 3:
            TITULO_PRINCIPAL[5] = 'Alterar dados de um cliente'
            cabecalho()
            id_cliente = pnb.ler_inteiro('ID do cliente: ')
            cliente = CLIENTES.buscar(id=id_cliente)
            if len(cliente) == 0:
                put.titulo('ID não encontrado!')
                input('Pressione ENTER para continuar...')
                continue
            idade = int(pnb.pega_data()[6:]) - cliente[0].ano_nasc
            put.titulo_ml(
                [
                    f'ID: {cliente[0].id}',
                    f'CPF: {cliente[0].cpf}',
                    f'Nome: {cliente[0].nome}',
                    f'Telefone: {cliente[0].telefone}',
                    f'Sexo: {cliente[0].sexo}',
                    f'Idade: {idade} anos'
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


def viwe_menu_gerenciar_fornecedores() -> None:
    while True:
        TITULO_PRINCIPAL[5] = 'MENU: Principal -> Administrativo -> ' + \
            'Gerenciar -> Fornecedores'
        cabecalho()
        put.cria_menu(MENU_GERENCIAR_FORNECEDORES)
        opcao = pnb.ler_inteiro('O que deseja fazer: ')
        if opcao == 1:
            TITULO_PRINCIPAL[5] = 'Cadastrar fornecedor'
            cabecalho()
            cnpj = gera.gerar_cnpj(mascara=True)
            print(f'CNPJ: {cnpj}')
            nome = input('Nome: ').upper()
            telefone = gera.gerar_telefone(ddd=True)
            print(f'Telefone: {telefone}')
            while True:
                categorias = [f'ID: {categoria.id} - {categoria.nome}'
                              for categoria in CATEGORIAS.buscar()]
                put.titulo_ml(categorias)
                id_categoria = pnb.ler_inteiro('ID da categoria: ')
                if len(CATEGORIAS.buscar(id=id_categoria)) == 0:
                    put.titulo('ID não encontrado!')
                    input('Pressione ENTER para continuar...')
                    continue
                categoria = CATEGORIAS.buscar(id=id_categoria)[0].nome
                break
            resposta = FORNECEDORES.cadastrar(
                cnpj, nome, telefone, categoria
            )
            put.titulo(resposta[1])
            if resposta[0] != 0:
                if input('Deseja tentar novamente? (S/N) ').upper() == 'S':
                    continue
                else:
                    break
            input('Pressione ENTER para continuar...')
        elif opcao == 2:
            TITULO_PRINCIPAL[5] = 'Consultar fornecedor'
            cabecalho()
            put.cria_menu(
                [
                    'ID',
                    'Nome',
                    'Exibir todos',
                    'Voltar'
                ]
            )
            opc = pnb.ler_inteiro('O que deseja consultar? ')
            if opc == 1:
                TITULO_PRINCIPAL[5] = 'Consultar fornecedor por ID'
                cabecalho()
                id_fornecedor = pnb.ler_inteiro('ID do fornecedor: ')
                fornecedor = FORNECEDORES.buscar(id=id_fornecedor)
                if len(fornecedor) == 0:
                    put.titulo('ID não encontrado!')
                    input('Pressione ENTER para continuar...')
                    continue
                put.titulo_ml(
                    [
                        f'ID: {fornecedor[0].id}',
                        f'CNPJ: {fornecedor[0].cnpj}',
                        f'Nome: {fornecedor[0].nome}',
                        f'Telefone: {fornecedor[0].telefone}',
                        f'Categoria: {fornecedor[0].categoria}'
                    ]
                )
                input('Pressione ENTER para continuar...')
            elif opc == 2:
                TITULO_PRINCIPAL[5] = 'Consultar fornecedor por nome'
                cabecalho()
                nome = input('Nome: ').upper()
                fornecedor = FORNECEDORES.buscar(nome=nome)
                if len(fornecedor) == 0:
                    put.titulo('Nome não encontrado!')
                    input('Pressione ENTER para continuar...')
                    continue
                put.titulo_ml(
                    [
                        f'ID: {fornecedor[0].id}',
                        f'CNPJ: {fornecedor[0].cnpj}',
                        f'Nome: {fornecedor[0].nome}',
                        f'Telefone: {fornecedor[0].telefone}',
                        f'Categoria: {fornecedor[0].categoria}'
                    ]
                )
                input('Pressione ENTER para continuar...')
            elif opc == 3:
                TITULO_PRINCIPAL[5] = 'Exibindo todos os fornecedores'
                cabecalho()
                fornecedores = FORNECEDORES.buscar()
                if len(fornecedores) == 0:
                    put.titulo('Não há fornecedores cadastrados!')
                    input('Pressione ENTER para continuar...')
                    continue
                for fornecedor in fornecedores:
                    put.titulo_ml(
                        [
                            f'ID: {fornecedor.id}',
                            f'CNPJ: {fornecedor.cnpj}',
                            f'Nome: {fornecedor.nome}',
                            f'Telefone: {fornecedor.telefone}',
                            f'Categoria: {fornecedor.categoria}'
                        ]
                    )
                input('Pressione ENTER para continuar...')
            elif opc == 4:
                break
        elif opcao == 3:
            TITULO_PRINCIPAL[5] = 'Alterar fornecedor'
            cabecalho()
            id_fornecedor = pnb.ler_inteiro('ID do fornecedor: ')
            fornecedor = FORNECEDORES.buscar(id=id_fornecedor)
            if len(fornecedor) == 0:
                put.titulo('ID não encontrado!')
                input('Pressione ENTER para continuar...')
                continue
            put.titulo_ml(
                [
                    f'ID: {fornecedor[0].id}',
                    f'CNPJ: {fornecedor[0].cnpj}',
                    f'Nome: {fornecedor[0].nome}',
                    f'Telefone: {fornecedor[0].telefone}',
                    f'Categoria: {fornecedor[0].categoria}'
                ]
            )
            put.cria_menu(
                [
                    'Nome',
                    'Telefone',
                    'Categoria',
                    'Voltar'
                ]
            )
            opc = pnb.ler_inteiro('O que deseja alterar? ')
            nome = input('Nome: ').upper() if opc == 1 else fornecedor[0].nome
            telefone = gera.gerar_telefone(ddd=True) if opc == 2 else \
                fornecedor[0].telefone
            if opc == 3:
                while True:
                    categorias = [f'ID: {categoria.id} - {categoria.nome}'
                                  for categoria in CATEGORIAS.buscar()]
                    put.titulo_ml(categorias)
                    id_categoria = pnb.ler_inteiro('ID da categoria: ')
                    if len(CATEGORIAS.buscar(id=id_categoria)) == 0:
                        put.titulo('ID não encontrado!')
                        input('Pressione ENTER para continuar...')
                        cabecalho()
                        continue
                    categoria = CATEGORIAS.buscar(id=id_categoria)[0].nome
                    break
            else:
                categoria = fornecedor[0].categoria
            resposta = FORNECEDORES.alterar(
                id_fornecedor, fornecedor[0].cnpj, nome, telefone, categoria
            )
            put.titulo(resposta[1])
            if resposta[0] != 0:
                if input('Deseja tentar novamente? (S/N) ').upper() == 'S':
                    continue
                else:
                    break
            input('Pressione ENTER para continuar...')
            if opc == 4:
                break
        elif opcao == 4:
            TITULO_PRINCIPAL[5] = 'Excluir fornecedor'
            cabecalho()
            id_fornecedor = pnb.ler_inteiro('ID do fornecedor: ')
            fornecedor = FORNECEDORES.buscar(id=id_fornecedor)
            if len(fornecedor) == 0:
                put.titulo('ID não encontrado!')
                input('Pressione ENTER para continuar...')
                continue
            put.titulo_ml(
                [
                    f'ID: {fornecedor[0].id}',
                    f'CNPJ: {fornecedor[0].cnpj}',
                    f'Nome: {fornecedor[0].nome}',
                    f'Telefone: {fornecedor[0].telefone}',
                    f'Categoria: {fornecedor[0].categoria}'
                ]
            )
            resposta = FORNECEDORES.excluir(id_fornecedor)
            put.titulo(resposta[1])
            if resposta[0] != 0:
                if input('Deseja tentar novamente? (S/N) ').upper() == 'S':
                    continue
                else:
                    break
            input('Pressione ENTER para continuar...')
        elif opcao == 5:
            TITULO_PRINCIPAL[5] = 'Recuperar excluido'
            cabecalho()
            resposta = FORNECEDORES.recuperar_apagadas()
            put.titulo(resposta[1])
            if resposta[0] != 0:
                if input('Deseja tentar novamente? (S/N) ').upper() == 'S':
                    continue
                else:
                    break
            input('Pressione ENTER para continuar...')
        elif opcao == 6:
            break


def view_menu_gerenciar_funcionarios():
    while True:
        TITULO_PRINCIPAL[5] = 'MENU: Principal -> Administrativo -> ' + \
            'Gerenciar -> Funcionários'
        cabecalho()
        put.cria_menu(MENU_GERENCIAR_FUNCIONARIOS)
        opcao = pnb.ler_inteiro('O que deseja fazer: ')
        if opcao == 1:
            TITULO_PRINCIPAL[5] = 'Cadastrar novo funcionário'
            cabecalho()
            cpf = gera.gerar_cpf()
            nome = input('Nome: ').upper()
            telefone = gera.gerar_telefone(ddd=True)
            sexo = input('Sexo: ')[0].upper()
            ano = pnb.ler_inteiro('Ano de nascimento: ')
            while True:
                cargos = [f'ID: {cargo.id} - {cargo.nome}'
                          for cargo in CARGOS.buscar()]
                put.titulo_ml(cargos)
                id_cargo = pnb.ler_inteiro('ID do cargo: ')
                if len(CARGOS.buscar(id=id_cargo)) == 0:
                    put.titulo('ID não encontrado!')
                    input('Pressione ENTER para continuar...')
                    continue
                cargo = CARGOS.buscar(id=id_cargo)[0].nome
                break
            resposta = FUNCIONARIOS.cadastrar(cpf, nome, telefone, sexo, ano,
                                              cargo)
            put.titulo(resposta[1])
            if resposta[0] != 0:
                if input('Deseja tentar novamente? (S/N) ').upper() == 'S':
                    continue
                else:
                    break
            input('Pressione ENTER para continuar...')
        elif opcao == 2:
            TITULO_PRINCIPAL[5] = 'Consultar funcionário'
            cabecalho()
            put.cria_menu(
                [
                    'ID',
                    'Nome',
                    'Exibir todos',
                    'Voltar'
                ]
            )
            opc = pnb.ler_inteiro('O que deseja consultar? ')
            if opc == 1:
                TITULO_PRINCIPAL[5] = 'Consultar funcionário por ID'
                cabecalho()
                id_funcionario = pnb.ler_inteiro('ID do funcionário: ')
                funcionario = FUNCIONARIOS.buscar(id=id_funcionario)
                if len(funcionario) == 0:
                    put.titulo('ID não encontrado!')
                    input('Pressione ENTER para continuar...')
                    continue
                idade = int(pnb.pega_data()[6:]) - funcionario[0].ano_nasc
                put.titulo_ml(
                    [
                        f'ID: {funcionario[0].id}',
                        f'CPF: {funcionario[0].cpf}',
                        f'Nome: {funcionario[0].nome}',
                        f'Telefone: {funcionario[0].telefone}',
                        f'Sexo: {funcionario[0].sexo}',
                        f'Idade: {idade} anos',
                        f'Cargo: {funcionario[0].cargo}'
                    ]
                )
                input('Pressione ENTER para continuar...')
            elif opc == 2:
                TITULO_PRINCIPAL[5] = 'Consultar funcionário por nome'
                cabecalho()
                nome = input('Nome: ').upper()
                funcionario = FUNCIONARIOS.buscar(nome=nome)
                if len(funcionario) == 0:
                    put.titulo('Nome não encontrado!')
                    input('Pressione ENTER para continuar...')
                    continue
                idade = int(pnb.pega_data()[6:]) - funcionario[0].ano_nasc
                put.titulo_ml(
                    [
                        f'ID: {funcionario[0].id}',
                        f'CPF: {funcionario[0].cpf}',
                        f'Nome: {funcionario[0].nome}',
                        f'Telefone: {funcionario[0].telefone}',
                        f'Sexo: {funcionario[0].sexo}',
                        f'Idade: {idade} anos',
                        f'Cargo: {funcionario[0].cargo}'
                    ]
                )
                input('Pressione ENTER para continuar...')
            elif opc == 3:
                TITULO_PRINCIPAL[5] = 'Consultar todos os funcionários'
                cabecalho()
                funcionarios = FUNCIONARIOS.buscar()
                if len(funcionarios) == 0:
                    put.titulo('Nenhum funcionário cadastrado!')
                    input('Pressione ENTER para continuar...')
                    continue
                for funcionario in funcionarios:
                    idade = int(pnb.pega_data()[6:]) - funcionario.ano_nasc
                    put.titulo_ml(
                        [
                            f'ID: {funcionario.id}',
                            f'CPF: {funcionario.cpf}',
                            f'Nome: {funcionario.nome}',
                            f'Telefone: {funcionario.telefone}',
                            f'Sexo: {funcionario.sexo}',
                            f'Idade: {idade} anos',
                            f'Cargo: {funcionario.cargo}'
                        ]
                    )
                input('Pressione ENTER para continuar...')
            elif opc == 4:
                break
        elif opcao == 3:
            TITULO_PRINCIPAL[5] = 'Alterar dados do funcionário'
            cabecalho()
            id_funcionario = pnb.ler_inteiro('ID do funcionário: ')
            funcionario = FUNCIONARIOS.buscar(id=id_funcionario)
            if len(funcionario) == 0:
                put.titulo('ID não encontrado!')
                input('Pressione ENTER para continuar...')
                continue
            idade = int(pnb.pega_data()[6:]) - funcionario[0].ano_nasc
            put.titulo_ml(
                [
                    f'ID: {funcionario[0].id}',
                    f'CPF: {funcionario[0].cpf}',
                    f'Nome: {funcionario[0].nome}',
                    f'Telefone: {funcionario[0].telefone}',
                    f'Sexo: {funcionario[0].sexo}',
                    f'Idade: {idade} anos',
                    f'Cargo: {funcionario[0].cargo}'
                ]
            )
            put.cria_menu(
                [
                    'Nome',
                    'Telefone',
                    'Sexo',
                    'Ano de nascimento',
                    'Cargo'
                ]
            )
            opc = pnb.ler_inteiro('O que deseja alterar? ')
            nome = input('Nome: ').upper(
            ) if opc == 1 else funcionario[0].nome
            telefone = input('Telefone: ').upper(
            ) if opc == 2 else funcionario[0].telefone
            sexo = input('Sexo: ')[0].upper(
            ) if opc == 3 else funcionario[0].sexo
            ano = pnb.ler_inteiro(
                'Ano de nascimento: '
            ) if opc == 4 else funcionario[0].ano_nasc
            cargo = funcionario[0].cargo
            if opc == 5:
                while True:
                    cargos = [f'ID: {cargo.id} - Nome: {cargo.nome}'
                              for cargo in CARGOS.buscar()]
                    put.cria_menu(cargos)
                    id_cargo = pnb.ler_inteiro('ID do cargo: ')
                    if len(CARGOS.buscar(id=id_cargo)) == 0:
                        put.titulo('ID não encontrado!')
                        cabecalho()
                        continue
                    cargo = CARGOS.buscar(id=id_cargo)[0].nome
                    break
            resposta = FUNCIONARIOS.alterar(
                id_funcionario,
                funcionario[0].cpf,
                nome,
                telefone,
                sexo,
                ano,
                cargo
            )
            put.titulo(resposta[1])
            if resposta[0] != 0:
                if input('Deseja tentar novamente? [S/N]: ').upper() == 'S':
                    continue
                else:
                    break
            input('Pressione ENTER para continuar...')
        elif opcao == 4:
            TITULO_PRINCIPAL[5] = 'Excluir funcionário'
            cabecalho()
            id_funcionario = pnb.ler_inteiro('ID do funcionário: ')
            funcionario = FUNCIONARIOS.buscar(id=id_funcionario)
            if len(funcionario) == 0:
                put.titulo('ID não encontrado!')
                input('Pressione ENTER para continuar...')
                continue
            idade = int(pnb.pega_data()[6:]) - funcionario[0].ano_nasc
            put.titulo_ml(
                [
                    f'ID: {funcionario[0].id}',
                    f'CPF: {funcionario[0].cpf}',
                    f'Nome: {funcionario[0].nome}',
                    f'Telefone: {funcionario[0].telefone}',
                    f'Sexo: {funcionario[0].sexo}',
                    f'Idade: {idade} anos',
                    f'Cargo: {funcionario[0].cargo}'
                ]
            )
            resposta = FUNCIONARIOS.excluir(id_funcionario)
            put.titulo(resposta[1])
            if resposta[0] != 0:
                if input('Deseja tentar novamente? [S/N]: ').upper() == 'S':
                    continue
                else:
                    break
            input('Pressione ENTER para continuar...')
        elif opcao == 5:
            TITULO_PRINCIPAL[5] = 'Recuperar excluidos'
            cabecalho()
            resposta = FUNCIONARIOS.recuperar_apagadas()
            put.titulo(resposta[1])
            if resposta[0] != 0:
                if input('Deseja tentar novamente? [S/N]: ').upper() == 'S':
                    continue
                else:
                    break
            input('Pressione ENTER para continuar...')
        elif opcao == 6:
            break


def view_menu_gerenciar_produtos():
    while True:
        TITULO_PRINCIPAL[5] = 'MENU: Principal -> Administrativo -> ' + \
            'Gerenciar -> Produtos'
        cabecalho()
        put.cria_menu(MENU_GERENCIAR_PRODUTOS)
        opcao = pnb.ler_inteiro('O que deseja fazer? ')
        if opcao == 1:
            TITULO_PRINCIPAL[5] = 'Cadastrar novo produto'
            cabecalho()
            while True:
                categorias = [f'ID: {categoria.id} - Nome: {categoria.nome}'
                              for categoria in CATEGORIAS.buscar()]
                put.titulo_ml(categorias)
                id_categoria = pnb.ler_inteiro('ID da categoria: ')
                if len(CATEGORIAS.buscar(id=id_categoria)) == 0:
                    put.titulo('ID não encontrado!')
                    cabecalho()
                    continue
                categoria = CATEGORIAS.buscar(id=id_categoria)[0].nome
                break
            while True:
                fornecedores = []
                for fornecedor in FORNECEDORES.buscar():
                    if fornecedor.categoria == categoria:
                        fornecedores.append(
                            f'ID: {fornecedor.id} - Nome: {fornecedor.nome}'
                        )
                put.titulo_ml(fornecedores)
                id_fornecedor = pnb.ler_inteiro('ID do fornecedor: ')
                if len(FORNECEDORES.buscar(id=id_fornecedor)) == 0:
                    put.titulo('ID não encontrado!')
                    cabecalho()
                    continue
                fornecedor = FORNECEDORES.buscar(id=id_fornecedor)[0].nome
                break
            nome = input('Nome: ').upper()
            quantidade = pnb.ler_inteiro('Quantidade: ')
            preco = pnb.ler_real('Preço: R$ ')
            descricao = input('Descrição: ').upper()
            resposta = PRODUTOS.cadastrar(
                categoria,
                fornecedor,
                nome,
                quantidade,
                preco,
                descricao
            )
            put.titulo(resposta[1])
            if resposta[0] != 0:
                if input('Deseja tentar novamente? [S/N]: ').upper() == 'S':
                    continue
                else:
                    break
            input('Pressione ENTER para continuar...')
        elif opcao == 2:
            TITULO_PRINCIPAL[5] = 'Consultar produtos cadastrados'
            cabecalho()
            put.cria_menu(
                [
                    'ID',
                    'Nome',
                    'Exibir todos',
                    'Voltar'
                ]
            )
            opc = pnb.ler_inteiro('O que deseja consultar? ')
            if opc == 1:
                TITULO_PRINCIPAL[5] = 'Consultar produtos por ID'
                cabecalho()
                id_produto = pnb.ler_inteiro('ID do produto: ')
                produto = PRODUTOS.buscar(id=id_produto)
                if len(produto) == 0:
                    put.titulo('ID não encontrado!')
                    input('Pressione ENTER para continuar...')
                    continue
                put.titulo_ml(
                    [
                        f'ID: {produto[0].id}',
                        f'Categoria: {produto[0].categoria}',
                        f'Fornecedor: {produto[0].fornecedor}',
                        f'Nome: {produto[0].nome}',
                        f'Quantidade: {produto[0].quantidade}',
                        f'Preço: {pnb.mostra_BLR(produto[0].preco)}',
                        f'Descrição: {produto[0].descricao}'
                    ]
                )
                input('Pressione ENTER para continuar...')
            elif opc == 2:
                TITULO_PRINCIPAL[5] = 'Cunsultar produtos por nome'
                cabecalho()
                nome = input('Nome do produto: ').upper()
                produtos = PRODUTOS.buscar(nome=nome)
                if len(produtos) == 0:
                    put.titulo('Nome não encontrado!')
                    input('Pressione ENTER para continuar...')
                    continue
                put.titulo_ml(
                    [
                        f'ID: {produto[0].id}',
                        f'Categoria: {produto[0].categoria}',
                        f'Fornecedor: {produto[0].fornecedor}',
                        f'Nome: {produto[0].nome}',
                        f'Quantidade: {produto[0].quantidade}',
                        f'Preço: {pnb.mostra_BLR(produto[0].preco)}',
                        f'Descrição: {produto[0].descricao}'
                    ]
                )
                input('Pressione ENTER para continuar...')
            elif opc == 3:
                TITULO_PRINCIPAL[5] = 'Consultar todos os produtos'
                cabecalho()
                produtos = PRODUTOS.buscar()
                if len(produtos) == 0:
                    put.titulo('Nenhum produto cadastrado!')
                    input('Pressione ENTER para continuar...')
                    continue
                for produto in produtos:
                    put.titulo_ml(
                        [
                            f'ID: {produto.id}',
                            f'Categoria: {produto.categoria}',
                            f'Fornecedor: {produto.fornecedor}',
                            f'Nome: {produto.nome}',
                            f'Quantidade: {produto.quantidade}',
                            f'Preço: {pnb.mostra_BLR(produto.preco)}',
                            f'Descrição: {produto.descricao}'
                        ]
                    )
                input('Pressione ENTER para continuar...')
        elif opcao == 3:
            TITULO_PRINCIPAL[5] = 'Alterar produtos cadastrados'
            cabecalho()
            id_produto = pnb.ler_inteiro('ID do produto: ')
            produto = PRODUTOS.buscar(id=id_produto)
            if len(produto) == 0:
                put.titulo('ID não encontrado!')
                input('Pressione ENTER para continuar...')
                continue
            put.titulo_ml(
                [
                    f'ID: {produto[0].id}',
                    f'Categoria: {produto[0].categoria}',
                    f'Fornecedor: {produto[0].fornecedor}',
                    f'Nome: {produto[0].nome}',
                    f'Quantidade: {produto[0].quantidade}',
                    f'Preço: {pnb.mostra_BLR(produto[0].preco)}',
                    f'Descrição: {produto[0].descricao}'
                ]
            )
            put.cria_menu(
                [
                    'Alterar categoria',
                    'Alterar fornecedor',
                    'Alterar nome',
                    'Alterar quantidade',
                    'Alterar preço',
                    'Alterar descrição',
                    'Voltar'
                ]
            )
            opc = pnb.ler_inteiro('O que deseja alterar? ')
            categoria = produto[0].categoria
            fornecedor = produto[0].fornecedor
            if opc == 1:
                while True:
                    categorias = [
                        f'ID: {categoria.id} - Nome: {categoria.nome}'
                        for categoria in CATEGORIAS.buscar()
                    ]
                    put.titulo_ml(categorias)
                    id_categoria = pnb.ler_inteiro('ID da categoria: ')
                    if len(CATEGORIAS.buscar(id=id_categoria)) == 0:
                        put.titulo('ID não encontrado!')
                        input('Pressione ENTER para continuar...')
                        continue
                    categoria = CATEGORIAS.buscar(id=id_categoria)[0].nome
                    break
            elif opc == 2:
                while True:
                    fornecedores = [
                        f'ID: {fornecedor.id} - Nome: {fornecedor.nome}'
                        for fornecedor in FORNECEDORES.buscar()
                    ]
                    put.titulo_ml(fornecedores)
                    id_fornecedor = pnb.ler_inteiro('ID do fornecedor: ')
                    if len(FORNECEDORES.buscar(id=id_fornecedor)) == 0:
                        put.titulo('ID não encontrado!')
                        input('Pressione ENTER para continuar...')
                        continue
                    fornecedor = FORNECEDORES.buscar(id=id_fornecedor)[0].nome
                    break
            nome = input('Nome do produto: ').upper(
            ) if opc == 3 else produto[0].nome
            quantidade = pnb.ler_inteiro(
                'Quantidade: '
            ) if opc == 4 else produto[0].quantidade
            preco = pnb.ler_real(
                'Preço: R$ '
            ) if opc == 5 else produto[0].preco
            descricao = input('Descrição: ').upper(
            ) if opc == 6 else produto[0].descricao
            resposta = PRODUTOS.alterar(
                id_produto,
                categoria,
                fornecedor,
                nome,
                quantidade,
                preco,
                descricao
            )
            put.titulo(resposta[1])
            if resposta[0] != 0:
                if input('Deseja tentar novamente? [S/N]: ').upper() == 'S':
                    continue
                else:
                    break
            input('Pressione ENTER para continuar...')
        elif opcao == 4:
            TITULO_PRINCIPAL[5] = 'Excluir produtos cadastrados'
            cabecalho()
            id_produto = pnb.ler_inteiro('ID do produto: ')
            produto = PRODUTOS.buscar(id=id_produto)
            if len(produto) == 0:
                put.titulo('ID não encontrado!')
                input('Pressione ENTER para continuar...')
                continue
            put.titulo_ml(
                [
                    f'ID: {produto[0].id}',
                    f'Categoria: {produto[0].categoria}',
                    f'Fornecedor: {produto[0].fornecedor}',
                    f'Nome: {produto[0].nome}',
                    f'Quantidade: {produto[0].quantidade}',
                    f'Preço: {pnb.mostra_BLR(produto[0].preco)}',
                    f'Descrição: {produto[0].descricao}'
                ]
            )
            resposta = PRODUTOS.excluir(id_produto)
            put.titulo(resposta[1])
            if resposta[0] != 0:
                if input('Deseja tentar novamente? [S/N]: ').upper() == 'S':
                    continue
                else:
                    break
            input('Pressione ENTER para continuar...')
        elif opcao == 5:
            TITULO_PRINCIPAL[5] = 'Recuperar excluidos'
            cabecalho()
            resposta = PRODUTOS.recuperar_apagadas()
            put.titulo(resposta[1])
            if resposta[0] != 0:
                if input('Deseja tentar novamente? [S/N]: ').upper() == 'S':
                    continue
                else:
                    break
            input('Pressione ENTER para continuar...')
        elif opcao == 6:
            break


def view_menu_estoque() -> None:
    while True:
        TITULO_PRINCIPAL[5] = 'MENU: Principal -> Administrativo -> Estoque'
        cabecalho()
        put.cria_menu(MENU_ESTOQUE)
        opcao = pnb.ler_inteiro('O que deseja fazer? ')
        if opcao == 1:
            lista_id = []
            lista_quantidade = []
            TITULO_PRINCIPAL[5] = 'Entrada de produto no estoque'
            while True:
                cabecalho()
                id_produto = pnb.ler_inteiro('ID do produto: ')
                produto = PRODUTOS.buscar(id=id_produto)
                if len(produto) == 0:
                    put.titulo('ID não encontrado!')
                    input('Pressione ENTER para continuar...')
                    continue
                put.titulo_ml(
                    [
                        f'ID: {produto[0].id}',
                        f'Categoria: {produto[0].categoria}',
                        f'Fornecedor: {produto[0].fornecedor}',
                        f'Nome: {produto[0].nome}',
                        f'Quantidade: {produto[0].quantidade}',
                        f'Preço: {pnb.mostra_BLR(produto[0].preco)}',
                        f'Descrição: {produto[0].descricao}'
                    ]
                )
                quantidade = pnb.ler_inteiro('Quantidade a ser adicionada: ')
                lista_id.append(id_produto)
                lista_quantidade.append(quantidade)
                if input('Deseja adicionar mais algum produto? [S/N]: ').upper(
                ) == 'S':
                    continue
                else:
                    put.titulo_ml(
                        PRODUTOS.altera_estoque(lista_id, lista_quantidade)
                    )
                    input('Pressione ENTER para continuar...')
                    break
        elif opcao == 2:
            while True:
                TITULO_PRINCIPAL[5] = 'Alterar o preco de um produto'
                cabecalho()
                id_produto = pnb.ler_inteiro('ID do produto: ')
                produto = PRODUTOS.buscar(id=id_produto)
                if len(produto) == 0:
                    put.titulo('ID não encontrado!')
                    input('Pressione ENTER para continuar...')
                    continue
                put.titulo_ml(
                    [
                        f'ID: {produto[0].id}',
                        f'Categoria: {produto[0].categoria}',
                        f'Fornecedor: {produto[0].fornecedor}',
                        f'Nome: {produto[0].nome}',
                        f'Quantidade: {produto[0].quantidade}',
                        f'Preço: {pnb.mostra_BLR(produto[0].preco)}',
                        f'Descrição: {produto[0].descricao}'
                    ]
                )
                preco = pnb.ler_real('Novo preço: R$ ')
                PRODUTOS.altera_preco(id_produto, preco)
                break
        elif opcao == 3:
            break


def view_menu_vendas() -> None:
    TITULO_PRINCIPAL[5] = 'MENU: VENDAS'
    while True:
        cabecalho()
        cliente = input('Nome do cliente: ').upper()
        if CLIENTES.buscar(nome=cliente) == []:
            put.titulo('Cliente não encontrado!')
            input('Pressione ENTER para continuar...')
            continue
        compras = []
        total_compra = 0
        while True:
            id_produto = pnb.ler_inteiro('ID do produto:')
            if PRODUTOS.buscar(id=id_produto) == []:
                put.titulo('ID não encontrado!')
                input('Pressione ENTER para continuar...')
                continue
            quantidade = pnb.ler_inteiro('Quantidade: ')
            produto = PRODUTOS.buscar(id=id_produto)[0]
            if produto.quantidade < quantidade:
                put.titulo('Quantidade indisponível!')
                input('Pressione ENTER para continuar...')
                continue
            sub_total = quantidade * produto.preco
            total_compra += sub_total
            compra = f'ID:{produto.id};'
            compra += f'Produto:{produto.nome};'
            compra += f'Quantidade:{quantidade};'
            compra += f'Preço:{pnb.mostra_BLR(produto.preco)};'
            compra += f'Subtotal:{pnb.mostra_BLR(sub_total)};'
            compras.append(compra)
            if input('Adicionar mais algum produto? [S/N]: ')[0].upper(
            ) == 'S':
                continue
            break
        resposta = VENDAS.cadastrar(
            funcionario_atual.nome,
            cliente,
            compras,
            total_compra
        )
        if resposta[0] == -1:
            put.titulo('Erro ao cadastrar a venda!')
            input('Pressione ENTER para continuar...')
            continue
        saida = VENDAS.cria_cupom(
            resposta[0],
            CLIENTES.buscar(nome=cliente)[0].telefone
        )
        PRODUTOS.altera_estoque(saida[1], saida[2])
        put.titulo_ml(saida[0])
        input('Pressione ENTER para continuar...')
        break


def view_menu_consultas() -> None:
    vendas = VENDAS.buscar()
    for venda in vendas:
        cupom = [
            f'Cupom: {venda.cupom} {" " * 75} Data: {venda.data}',
            f'Funcionário: {venda.funcionario}',
            f'Cliente: {venda.cliente} - Telefone: ' +
            f'{CLIENTES.buscar(nome=venda.cliente)[0].telefone}',
            '',
        ]
        lista = venda.compra.replace("['", '').replace("']", '')
        lista = lista.split("', '")
        cupom.append(
            f'{"ID":<5}{"Produto":<50}{"Quantidade":<12}{"Preço":<15}' +
            f'{"Subtotal":<15}'
        )
        for linha in lista:
            linha = linha.split(';')
            linha.pop()
            itens = list(map(lambda x: x.split(':')[1], linha))
            cupom.append(
                f'{itens[0]:<5}{itens[1]:<50}{itens[2]:<12}{itens[3]:<15}' +
                f'{itens[4]:<15}'
            )
        cupom.append('')
        cupom.append(f'Total: {pnb.mostra_BLR(venda.valor):}')
        put.titulo_ml(cupom)
        # for i, itens in enumerate(linha):
        #     itens = itens.split(':')
        #     print(itens[1], end=' | ')
        #     if i > 0 and i % 4 == 0:
        #         print()


def view_menu_operacional() -> None:
    while True:
        TITULO_PRINCIPAL[5] = 'MENU: Principal -> Operacional'
        cabecalho()
        put.cria_menu(MENU_OPERACIONAL)
        opcao = pnb.ler_inteiro('Escolha uma opção: ')
        if opcao == 1:
            view_menu_vendas()
        elif opcao == 2:
            view_menu_consultas()
            input('Pressione ENTER para continuar...')
        elif opcao == 3:
            break
        else:
            put.titulo('Opção inválida!')
            input('Pressione ENTER para continuar...')


if not criar_usuario_inicial():
    print('Erro inesperado no sistema, por favor, tente novamente.')
    exit(1)

funcionario_atual = login()

while True:
    TITULO_PRINCIPAL[4] = f'Usurário: {funcionario_atual.nome}'
    TITULO_PRINCIPAL[5] = 'MENU: Principal'
    cabecalho()
    put.cria_menu(MENU_PRINCIPAL)
    opcao = pnb.ler_inteiro('Escolha uma opção: ')
    if opcao == 1:
        if CARGOS.autorizacao(funcionario_atual.cargo, 1):
            view_menu_administrativo()
        else:
            put.titulo('Você não tem autorização para acessar esse menu!')
            input('tecle enter para continuar...')
    if opcao == 2:
        view_menu_operacional()
    if opcao == 3:
        funcionario_atual = login()
    if opcao == 4:
        if input('Deseja realmente sair? (s/n) ').upper() == 'S':
            break

put.titulo('Execução finalizada')
