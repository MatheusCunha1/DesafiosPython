palavra_secreta = 'computador'
letras_acertadas = ''
numero_tentativas = 0
while True:
    letra_digitada = input('Digite uma letra: ')
    numero_tentativas += 1

    if len(letra_digitada) > 1:
        print('Digite apenas uma letra.')
        continue  # Ele printa o alerta e retorna para o ínicio do While

    if letra_digitada in palavra_secreta:
        letras_acertadas += f'{letra_digitada}'

    palavra_formada = ''
    for letras_secreta in palavra_secreta:
        if letras_secreta in letras_acertadas:
            palavra_formada += letras_secreta

        else:
            palavra_formada += '*'

    print('Palavra_formada:', palavra_formada)

    if palavra_formada == palavra_secreta:
        print('VOCÊ GANHOU!! PARABÉNS')
        print(palavra_formada)
        print('Número de Tentativas: ', numero_tentativas)

        palavra_secreta = 'computador'
        letras_acertadas = ''
        numero_tentativas = 0
