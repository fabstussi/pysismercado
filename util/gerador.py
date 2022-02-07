from random import randint
from re import fullmatch


def gerar_cpf(mascara=False) -> str:
    cpf = ''.join([str(randint(0, 9)) for i in range(9)])
    for i in range(2):
        peso = 10 + i
        soma = (sum([int(n) * (peso - cpf.index(n)) for n in cpf[:9 + i]]) * 10
                ) % 11
        cpf += '0' if soma == 10 else str(soma)
    if mascara:
        return f'{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}'
    return cpf


def gerar_cnpj(mascara=False) -> str:
    cnpj = ''.join([str(randint(0, 9)) for i in range(8)])
    cnpj += '0001'
    soma = 0
    for i in range(2):
        peso = 6 + i
        for n in cnpj:
            peso -= 1
            soma += int(n) * peso
            if peso == 2:
                peso = 10
        digito = (11 - soma % 11 if soma % 11 > 1 else 0)
        cnpj += str(digito)
        soma = 0
    if mascara:
        return f'{cnpj[:2]}.{cnpj[2:5]}.{cnpj[5:8]}/{cnpj[8:12]}-{cnpj[12:]}'
    return cnpj


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
    for i in range(2):
        peso = 10 + i
        soma = (sum([int(n) * (peso - cpf.index(n))for n in cpf[:9 + i]]) * 10
                ) % 11
        soma = 0 if soma == 10 else soma
        if soma != int(cpf[9 + i]):
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


def validar_cnpj(cnpj: str) -> bool:
    if not fullmatch(r'[0-9]{2}[\.]?[0-9]{3}[\.]?[0-9]{3}[/]?[0-9]{4}[-]?[0-9]{2}',
                     cnpj) and not fullmatch(r'[0-9]{11}', cnpj):
        return False
    cnpj = cnpj.replace('.', '').replace('/', '').replace('-', '')
    if not cnpj.isdigit():
        return False
    if len(cnpj) != 14:
        return False
    soma = 0
    for i in range(2):
        peso = 6 + i
        for n in cnpj[:12 + i]:
            peso -= 1
            soma += int(n) * peso
            if peso == 2:
                peso = 10
        digito = (11 - soma % 11 if soma % 11 > 1 else 0)
        if digito != int(cnpj[12 + i]):
            return False
        soma = 0
    return True
