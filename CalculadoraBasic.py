import os
os.system('cls')

while True:
    print('=============================')
    print('=        CALCULADORA        =')
    print('=============================')
    n1 = input('Informe o primeiro número: ')
    n2 = input('Informe o segundo número: ')
    print('=============================')
    print('Opções:')
    print('      (+)-> Soma             ')
    print('      (-)-> Subtraão         ')
    print('      (*)-> Multuiplicação   ')
    print('      (/)-> Divisão          ')
    print('=============================')
    op = input('Informe a opçao desejada: ')

    num_validos = None

    try:
        n1_float = float(n1)
        n2_float = float(n2)
        num_validos = True

    except:
        num_validos = None
        os.system('cls')
        print('Erro')

    if num_validos is None:
        os.system('cls')
        print('Números não são válidos ')
        continue

    operadores_permitidos = '+-*/'

    if op not in operadores_permitidos or len(op) != 1:
        os.system('cls')
        print('Operador não permitido')
        continue

    if op == '+':
        res = n1_float + n2_float
        print(f'Soma:{res}')
    elif op == '-':
        res = n1_float - n2_float
        print(f'Subtração:{res}')
    elif op == '*':
        res = n1_float * n2_float
        print(f'Multiplicação:{res}')
    else:
        res = n1_float / n2_float
        print(f'Divisão:{res}')

    sair = input('Quer sair ?: [s]im / [n]ão ').lower().startswith('s')

    os.system('cls')

    if sair is True:
        break
