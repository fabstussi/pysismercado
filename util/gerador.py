from random import randint
from re import fullmatch


def gerar_cpf(mascara=False) -> str:
    cpf = ''.join([str(randint(0, 9)) for i in range(9)])
    soma = (sum([int(cpf[10 - i]) * (i) for i in range(10, 1, - 1)]) * 10) % 11
    if soma == 10:
        soma = 0
    cpf += str(soma)
    soma = (sum([int(cpf[11 - i]) * (i)
            for i in range(11, 1, -1)]) * 10) % 11
    if soma == 10:
        soma = 0
    cpf += str(soma)
    if mascara:
        return f'{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}'
    return cpf


def gerar_telefone(celular=False, ddd=False, mascara=False) -> str:
    telefone = ''.join([str(randint(0, 9)) for i in range(8)])
    if celular:
        telefone = '9' + telefone
    if ddd:
        telefone = f'{str(randint(11, 99))}{telefone}'
    if mascara:
        if len(telefone) == 8:
            telefone = f'{telefone[:4]}-{telefone[4:]}'
        elif len(telefone) == 9:
            telefone = f'{telefone[:5]}-{telefone[5:]}'
        elif len(telefone) == 10:
            telefone = f'({telefone[:2]}) {telefone[2:6]}-{telefone[6:]}'
        elif len(telefone) == 11:
            telefone = f'({telefone[:2]}) {telefone[2:7]}-{telefone[7:]}'
    return telefone


def validar_cpf(cpf: str) -> bool:
    if not fullmatch(r'[0-9]{3}[\.]?[0-9]{3}[\.]?[0-9]{3}[-]?[0-9]{2}', cpf) \
            and not fullmatch(r'[0-9]{11}', cpf):
        return False
    cpf = cpf.replace('.', '').replace('-', '')
    if not cpf.isdigit():
        return False
    soma = (sum([int(cpf[10 - i]) * (i)
                 for i in range(10, 1, -1)]) * 10) % 11
    if soma == 10:
        soma = 0
    if soma == int(cpf[9]):
        soma = (sum([int(cpf[11 - i]) * (i)
                for i in range(11, 1, -1)]) * 10) % 11
        if soma == 10:
            soma = 0
        if soma != int(cpf[10]):
            return False
    else:
        return False
    return True


def validar_telefone(telefone: str) -> bool:
    telefone = telefone.replace('(', '')\
        .replace(')', '').replace('-', '').replace(' ', '')
    if len(telefone) < 8 or len(telefone) > 11:
        return False
    if len(telefone) == 8:
        if not telefone.isdigit():
            return False
    elif len(telefone) == 9:
        if not telefone.isdigit():
            return False
        if telefone[0] != '9':
            return False
    elif len(telefone) == 10:
        if not telefone.isdigit():
            return False
        if telefone[0] == '0':
            return False
    elif len(telefone) == 11:
        if not telefone.isdigit():
            return False
        if telefone[2] != '9' or telefone[0] == '0':
            return False
    return True
