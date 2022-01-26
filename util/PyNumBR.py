# Projeto: Utilidades para tela do terminal
# Data: 01/08/2021
# License: GNU GENERAL PUBLIC LICENSE - Version 3, 29 June 2007
# Fabiano Stussi Pereira® - © 2021

from datetime import datetime
import locale


locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')


def ler_inteiro(msg: str,
                msg_erro='[Erro de tipo] É esperado um número inteiro,' +
                'tente novamente') -> int:
    '''
    Possibilita a certeza da entrada ser um inteiro.
    msg: mensagem a ser exibida quando for solicitado um número.
    msg_erro: mensagem opcional a ser exibida quando ocorrer um erro de tipo.
    return: número inteiro lido.
    '''
    while True:
        try:
            inteiro = int(input(msg))
        except ValueError:
            print(msg_erro)
            continue
        return inteiro


def ler_real(msg: str,
             msg_erro='[Erro de tipo] É esperado um número real,' +
             'tente novamente') -> float:
    '''
    Possibilita a certeza da entrada ser um número Real.
    msg: mensagem a ser exibida quando for solicitado um número.
    msg_erro: mensagem opcional a ser exibida quando ocorrer um erro de tipo.
    return: número real lido.
    '''
    while True:
        numero = input(msg).replace(',', '.')
        try:
            real = float(numero)
        except ValueError:
            print(msg_erro)
            continue
        return real


def mostra_real(num_float: float) -> str:
    '''
    Usado para exiber um número real com virgula no lugar do ponto.
    num_float: número real a ser exibido.
    return: string com o número real formatado.
    '''
    return locale.format_string('%.2f', num_float, grouping=True)


def pega_data() -> str:
    '''
    return: string com a data atual no formato dd/mm/aaaa.
    '''
    return datetime.now().strftime('%d/%m/%Y')


def pega_hora() -> str:
    '''
    return: string com a hora atual no formato hh:mm:ss.
    '''
    return datetime.now().strftime('%H:%M:%S')


if __name__ == '__main__':
    pass
