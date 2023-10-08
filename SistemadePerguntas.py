perguntas = [
    {
        'Pergunta': 'Quanto é 2+2 ?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5 ?',
        'Opções': ['25', '34', '18', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2 ?',
        'Opções': ['100', '66', '12', '5'],
        'Resposta': '5',
    }
]

print('\033[0;34mSistema de Perguntas e Respostas\033[0m')

acerto = 0
erro = 0
for pergunta in perguntas:
    print(pergunta['Pergunta'])
    print('Opções:')
    i = 1
    for alternativa in pergunta['Opções']:
        print(f'{i}) {alternativa}')
        i += 1

    opcao = int(input('Digite a sua opção: ')) - 1
    correta = pergunta['Resposta']
    if pergunta['Opções'][opcao] == correta:
        print('Você Acertou!! ✅')
        acerto += 1
    else:
        print('Você Errou!!! ❌')
        erro += 1
    print('------------------')

print(f'Resultado: ✅ {acerto} ❌ {erro}')
