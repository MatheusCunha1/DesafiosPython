import os


def limpar_tela():
    os.system('cls')


lista = []
while True:
    print(
        '''
    |===========================|
    |    Carrinho de Compras    |
    |===========================|
    | [1] Adicionar produto     |   
    | [2] Remover produto       |
    | [3] Listar a compra       |
    |===========================|
    '''
    )
    try:
        opcao = int(input('Informe uma opção: '))
    except ValueError:
        limpar_tela()
        print("\x1b[31mPor favor, insira um número válido.\x1b[0m")
        continue
    if opcao == 1:
        item = input('Informe um item: ')
        lista.append(item)
        input('Pressione Enter para continuar...')
    elif opcao == 2:
        print("Itens na lista:")
        indices = range(len(lista))
        for indice in indices:
            print(indice, lista[indice])
        print('-------------------')
        try:
            indice = int(input('Informe o número do item a ser removido: '))
            lista.pop(indice)
        except ValueError:
            print("\x1b[31mPor favor, insira um número válido.\x1b[0m")
        continue
    else:
        print("Itens na lista:")
        indices = range(len(lista))
        for indice in indices:
            print(indice, lista[indice])
