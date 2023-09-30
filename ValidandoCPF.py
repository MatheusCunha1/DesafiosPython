print(
    '''
   |==================|
   | Validando de CPF | 
   |==================|
   '''
)

while True:
    cpf_str = input('Informe seu CPF:')
    cpf_str = ''.join(filter(str.isdigit, cpf_str)).replace(
        '-', '').replace(' ', '').replace('.', '')
    if len(cpf_str) == 11 and cpf_str.isdigit():
        print('\x1b[32mVerificando CPF...\x1b[0m')
        break
    else:
        print('\x1b[31mInforme um CPF válido\x1b[0m')

# Primeiro Digito
valores = [10, 9, 8, 7, 6, 5, 4, 3, 2]
soma = 0
for i in range(9):
    digito = int(cpf_str[i])
    valor = digito * valores[i]
    soma += valor

operacao = (soma * 10) % 11
if operacao > 9:
    digito_1 = 0
else:
    digito_1 = operacao

# Segundo Digito
valores = [11, 10, 9, 8, 7, 6, 5, 4, 3, 2]
soma = 0
cpf_str_novo = cpf_str
cpf_str_novo += str(digito_1)
for i in range(10):
    digito = int(cpf_str_novo[i])
    valor = digito * valores[i]
    soma += valor

operacao = (soma * 10) % 11
if operacao > 9:
    digito_2 = 0
else:
    digito_2 = operacao

cpf_gerado_pelo_calculo = f'{cpf_str[:9]}{digito_1}{digito_2}'

if cpf_str == cpf_gerado_pelo_calculo:
    print('\x1b[32mCPF Válido\x1b[0m')
else:
    print('\x1b[31mCPF Inválido\x1b[0m')
