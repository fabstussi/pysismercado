# Projeto: Utilidades para tela do terminal
# Data: 01/08/2021
# License: GNU GENERAL PUBLIC LICENSE - Version 3, 29 June 2007
# Fabiano Stussi Pereira® - © 2021

from os import system as ossy
from platform import system as plsy


def limpa_tela():
    '''
    Limpa a tela do terminal.
    '''
    ossy('cls' if plsy() == 'Windows' else 'clear')


def desenha_linha(simbolo: str, tamanho=10):
    '''
    Desenha uma linha com o simbolo passado como parâmetro.
    simbolo: simbolo a ser usado para desenhar a linha.
    tamanho: tamanho da linha a ser desenhada.
    '''
    print(simbolo * tamanho)


def titulo(texto: str, simbulo='*'):
    '''
    Exibe um título com o texto passado como parâmetro.
    texto: texto a ser exibido.
    simbulo: simbolo a ser usado para desenhar o título.
    '''
    texto = f'** {texto} **'
    desenha_linha(f'{simbulo}', len(texto))
    print(texto)
    desenha_linha(f'{simbulo}', len(texto))


def titulo_ml(titulos: list, alinhamento='e'):
    '''
    Desenha uma caixa e coloca o título dentro.
    titulos: lista com os títulos a serem exibidos.
    alinhamento: alinhamento do título ('e' para esquerdo
                                        'c' para centralizado).
    '''
    maior_texto = max(map(lambda item: len(item), titulos))
    desenha_linha('=', maior_texto + 4)
    for texto in titulos:
        if alinhamento == 'c':
            print(f'| {texto: ^{maior_texto}} |')
        else:
            print(f'| {texto: <{maior_texto}} |')
    desenha_linha('=', maior_texto + 4)


def cria_menu(menu: list):
    ''''
    Desenha uma caixa e coloca o menu dentro.
    Lista as opções do menu.
    menu: lista com as opções do menu.
    '''
    maior_texto = max(map(lambda item: len(item), menu))
    desenha_linha('=', maior_texto + 9)
    for i, item in enumerate(menu):
        print(f'| {i + 1:>2} - {item: <{maior_texto}} |')
    desenha_linha('=', maior_texto + 9)


if __name__ == '__main__':
    pass
