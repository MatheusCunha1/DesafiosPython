def verifica_Par_Impar(x):
    if x % 2 == 0:
        return print('Par')
    else:
        return print('Ímpar')


while True:
    x = int(input('Informe um valor: '))
    resultado = verifica_Par_Impar(x)
