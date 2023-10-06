def receber_argumentos(*args):
    print("Valores informados:")
    total = 1
    for indice in range(0, len(args)):
        valor = int(args[indice])
        print(valor)
        total *= valor
    return total


valores = input('Informe os valores separados por espaço: ').split()
resultado = receber_argumentos(*valores)
print(f"O resultado da multiplicação dos elementos é: {resultado}")
